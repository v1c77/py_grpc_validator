# -*- coding: utf-8 -*-
import logging
from functools import wraps

import six
from grpc import StatusCode

from grpc_proto_validator.validator_pb2 import (
    FieldValidator,
    field as validator_field,
)
from grpc_proto_validator import IllegalFieldValueError

logger = logging.getLogger(__name__)


# validate the value, func is better than magic.

def validate_regex(value, limit):

    return True


def validate_gt(value, limit):
    return value > limit


def validate_lt(value, limit):
    return value < limit


def validate_gte(value, limit):
    return value >= limit


def validate_lte(value, limit):
    return value <= limit


validate_float_gt = validate_gt
validate_float_lt = validate_lt
validate_float_gte = validate_gte
validate_float_lte = validate_lte


# TODO(vici) logic....
def validate_msg_exists(value, limit):
    return True if bool(value.ByteSize()) == limit else False


def validate_string_not_empty(value, limit):
    return bool(value) == limit


def validate_repeated_count_min(value, limit):
    return len(value) >= limit


def validate_repeated_count_max(value, limit):
    return len(value) <= limit


def validate_length_gt(value, limit):
    text = six.text_type(value)
    return len(text) > limit


def validate_length_lt(value, limit):
    text = six.text_type(value)
    return len(text) < limit


def validate_length_eq(value, limit):
    text = six.text_type(value)
    return len(text) == limit


DESC = FieldValidator.DESCRIPTOR
VALIDATOR_MAP = {
    DESC.fields_by_name['regex'].number: validate_regex,
    DESC.fields_by_name['int_gt'].number: validate_gt,
    DESC.fields_by_name['int_lt'].number: validate_lt,
    DESC.fields_by_name['int_gte'].number: validate_gte,
    DESC.fields_by_name['int_lte'].number: validate_lte,
    DESC.fields_by_name['float_gt'].number: validate_float_gt,
    DESC.fields_by_name['float_lt'].number: validate_float_lt,
    DESC.fields_by_name['float_gte'].number: validate_float_gte,
    DESC.fields_by_name['float_lte'].number: validate_float_lte,
    DESC.fields_by_name['msg_exists'].number: validate_msg_exists,
    DESC.fields_by_name['string_not_empty'].number: validate_string_not_empty,  # NOQA
    DESC.fields_by_name['repeated_count_min'].number: validate_repeated_count_min,  # NOQA
    DESC.fields_by_name['repeated_count_max'].number: validate_repeated_count_max,  # NOQA
    DESC.fields_by_name['length_gt'].number: validate_length_gt,
    DESC.fields_by_name['length_lt'].number: validate_length_lt,
    DESC.fields_by_name['length_eq'].number: validate_length_eq,
}


def get_validator_by_number(option_number):
    return VALIDATOR_MAP.get(option_number)


def terminate(context, code, detail):
    """abort to serve this request and throw grpc error"""

    # TODO(vici) get code from giagnose detail.
    context.abort(code, detail)


def gen_field_to_check(message):

    fields_desc = message.DESCRIPTOR.fields
    for field_desc in fields_desc:
        # TODO(vici) handle default value.
        yield getattr(message, field_desc.name), field_desc


def validate_message(message):
    """do request validate with a inited message

    what a message descriptor structure?
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    name: (str) Name of this protocol message type.
    full_name: (str) Fully-qualified name of this protocol message type,which
      will include protocol "package" name and the name of any enclosing types.

    containing_type: (Descriptor) Reference to the descriptor of the type
      containing us, or None if this is top-level.

    fields: (list of FieldDescriptors) Field descriptors for all fields in this
      type.
    fields_by_number: (dict int -> FieldDescriptor) Same FieldDescriptor
      objects as in |fields|, but indexed by "number" attribute in each
      FieldDescriptor.
    fields_by_name: (dict str -> FieldDescriptor) Same FieldDescriptor
      objects as in |fields|, but indexed by "name" attribute in each
      FieldDescriptor.

    nested_types: (list of Descriptors) Descriptor references for all protocol
      message types nested within this one.
    nested_types_by_name: (dict str -> Descriptor) Same Descriptor objects as
      in |nested_types|, but indexed by "name" attribute in each Descriptor.

    enum_types: (list of EnumDescriptors) EnumDescriptor references
      for all enums contained within this type.
    enum_types_by_name: (dict str ->EnumDescriptor) Same EnumDescriptor
      objects as in |enum_types|, but indexed by "name" attribute in each
      EnumDescriptor.
    enum_values_by_name: (dict str -> EnumValueDescriptor) Dict mapping from
      enum value name to EnumValueDescriptor for that value.

    extensions: (list of FieldDescriptor) All extensions defined directly
      within this message type (NOT within a nested type).
    extensions_by_name: (dict, string -> FieldDescriptor) Same FieldDescriptor
      objects as |extensions|, but indexed by "name" attribute of each
    FieldDescriptor.

    is_extendable:  does this type define any extension ranges?
    options: (descriptor_pb2.MessageOptions) Protocol message options or None
      to use default message options.
    file: (FileDescriptor) Reference to file descriptor.
    -------------------------------------------------------------------------

    the validator only work on check for the value error of field &
    nested_field & field wish message_type
    return nothing or raise ValueError

    """
    for value, field_desc in gen_field_to_check(message):
        validate_field(value, field_desc)


def _get_human_error(conditions):
    human_error_number = DESC.fields_by_name['human_error'].number
    for condition, limit in conditions:
        if condition.number == human_error_number:
            return limit
    return None


def validate_field(value, field_desc):
    """return nothing or raise valueError"""

    # TODO(vici) handle sub message and nested_message
    if field_desc.message_type:
        validate_message(value)

    # iter all field option check
    options = field_desc.GetOptions()
    validator_option = options.Extensions[validator_field]  # TODO(vici) soft get?
    if not validator_option:
        # do not check if no validator option
        return
    conditions = validator_option.ListFields()

    human_error = ''
    for condition, limit in conditions:
        conditions.pop(0)
        worker = get_validator_by_number(condition.number)
        if condition.number == DESC.fields_by_name['human_error'].number:
            human_error = limit
            continue
        if not worker(value, limit):
            if human_error:
                raise IllegalFieldValueError(human_error)
            elif conditions:
                human_error = _get_human_error(conditions)
                if human_error:
                    raise IllegalFieldValueError(human_error)

            raise IllegalFieldValueError('validation error: {} with illegal '
                                         'value: {}.'
                                         .format(field_desc.full_name,
                                                 value or 'None'))


def validator_wrap(func):

    @wraps(func)
    def wrapper(self, request, context):
        try:
            validate_message(request)
        except IllegalFieldValueError as e:
            return terminate(context, StatusCode.INVALID_ARGUMENT,
                             e.message)
        except Exception as e:
            logger.exception(e)

        return func(self, request, context)
    return wrapper


class ValidateMetaclass(type):

    def __new__(mcs, name, bases, attrs):
        for attr in attrs:
            value = attrs[attr]
            if callable(value):
                attrs[attr] = validator_wrap(value)

        return type.__new__(mcs, name, bases, attrs)
