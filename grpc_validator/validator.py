# -*- coding: utf-8 -*-
from functools import wraps, partial
import logging

from grpc_validator.validator_pb2 import FieldValidator, field

ERROR_DETAIL = '12312'

logger = logging.getLogger(__name__)


def terminate(context, detail):
    """abort to serve this request and throw grpc error"""

    # TODO(vici) get code from giagnose detail.
    context.abort(detail, detail)


def gen_field_to_check(message):

    fields_desc = message.DESCRIPTOR.fields
    for field_desc in fields_desc:
        # TODO(vici) handle default value.
        yield getattr(message, field_desc.name), field_desc


def validate_message(message):
    """do request validate with message info and request message descriptor
    what a messgae descriptor include:

      name: (str) Name of this protocol message type.
    full_name: (str) Fully-qualified name of this protocol message type,
      which will include protocol "package" name and the name of any
      enclosing types.

    containing_type: (Descriptor) Reference to the descriptor of the
      type containing us, or None if this is top-level.

    fields: (list of FieldDescriptors) Field descriptors for all
      fields in this type.
    fields_by_number: (dict int -> FieldDescriptor) Same FieldDescriptor
      objects as in |fields|, but indexed by "number" attribute in each
      FieldDescriptor.
    fields_by_name: (dict str -> FieldDescriptor) Same FieldDescriptor
      objects as in |fields|, but indexed by "name" attribute in each
      FieldDescriptor.

    nested_types: (list of Descriptors) Descriptor references
      for all protocol message types nested within this one.
    nested_types_by_name: (dict str -> Descriptor) Same Descriptor
      objects as in |nested_types|, but indexed by "name" attribute
      in each Descriptor.

    enum_types: (list of EnumDescriptors) EnumDescriptor references
      for all enums contained within this type.
    enum_types_by_name: (dict str ->EnumDescriptor) Same EnumDescriptor
      objects as in |enum_types|, but indexed by "name" attribute
      in each EnumDescriptor.
    enum_values_by_name: (dict str -> EnumValueDescriptor) Dict mapping
      from enum value name to EnumValueDescriptor for that value.

    extensions: (list of FieldDescriptor) All extensions defined directly
      within this message type (NOT within a nested type).
    extensions_by_name: (dict, string -> FieldDescriptor) Same FieldDescriptor
      objects as |extensions|, but indexed by "name" attribute of each
    FieldDescriptor.

    is_extendable:  does this type define any extension ranges?

    options: (descriptor_pb2.MessageOptions) Protocol message options or None
      to use default message options.

    file: (FileDescriptor) Reference to file descriptor.

    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    just for field & nested_field.
    return nothing or raise ValueError

    """
    try:
        list(map(validate_field, gen_field_to_check(message)))
    except Exception as e:
        print('error in validate message')
        logger.exception(e)
        pass

    return


def validate_field(value, field_desc):
    """return nothing or raise valueError"""

    # TODO(vici) handle sub message
    # if 'value是 messgae':
    #     validate_message(value)
    #     return

    # iter all field option check
    options = field_desc.GetOptions()
    validator_option = options.Extensions[field]
    if not validator_option:
        # do not check if no validator option
        return
    conditions = validator_option.ListFields()

    for condition, limit in conditions:

        worker = ProtoValidator.get_validator_by_number(condition.number)
        ok, detail = worker(value, limit)
        if not ok:
            return detail


def validator_wrap(func):

    @wraps(func)
    def wrapper(self, request, context):
        try:
            validate_message(request)
        except Exception as e:
            logger.exception(e)
            return terminate(context, ERROR_DETAIL)

        return func(self, request, context)
    return wrapper


class ValidateMetaclass(type):

    def __new__(mcs, name, bases, attrs):
        for attr in attrs:
            value = attrs[attr]
            if callable(value):
                attrs[attr] = validator_wrap(value)

        return type.__new__(mcs, name, bases, attrs)


class ProtoValidator(object):

    desc = FieldValidator.DESCRIPTOR

    @classmethod
    def get_field_validator_by_option(cls, option):
        pass

    # validate the value, func is better than magic.
    @staticmethod
    def validate_regex(value, limit):

        return True

    @staticmethod
    def validate_gt(value, limit):
        print('in gt')
        return True

    @staticmethod
    def validate_lt(value, limit):
        print('in lt')

        return True

    @staticmethod
    def validate_gte(value, limit):

        return True

    @staticmethod
    def validate_lte(value, limit):

        return True

    @staticmethod
    def validate_float_gt(value, limit):
        return True

    @staticmethod
    def validate_float_lt(value, limit):
        return True

    @staticmethod
    def validate_float_gte(value, limit):

        return True

    @staticmethod
    def validate_float_lte(value, limit):

        return True

    @staticmethod
    def validate_msg_exists(value, limit):

        return True

    @staticmethod
    def validate_human_error(value, limit):

        return True

    @staticmethod
    def validate_string_not_empty(value, limit):

        return True

    @staticmethod
    def validate_repeated_count_min(value, limit):

        return True

    @staticmethod
    def validate_repeated_count_max(value, limit):

        return True

    @staticmethod
    def validate_length_gt(value, limit):

        return True

    @staticmethod
    def validate_length_lt(value, limit):

        return True

    @staticmethod
    def validate_length_eq(value, limit):

        return True

    validator_map = {
        desc.fields_by_name['regex'].number: validate_regex,
        desc.fields_by_name['gt'].number: validate_gt,
        desc.fields_by_name['lt'].number: validate_lt,
        desc.fields_by_name['gte'].number: validate_gte,
        desc.fields_by_name['lte'].number: validate_lte,
        desc.fields_by_name['float_gt'].number: validate_float_gt,
        desc.fields_by_name['float_lt'].number: validate_float_lt,
        desc.fields_by_name['float_gte'].number: validate_float_gte,
        desc.fields_by_name['float_lte'].number: validate_float_lte,
        desc.fields_by_name['msg_exists'].number: validate_msg_exists,
        desc.fields_by_name['human_error'].number: validate_human_error,
        desc.fields_by_name['string_not_empty'].number: validate_string_not_empty,  # NOQA
        desc.fields_by_name['repeated_count_min'].number: validate_repeated_count_min,  # NOQA
        desc.fields_by_name['repeated_count_max'].number: validate_repeated_count_max,  # NOQA
        desc.fields_by_name['length_gt'].number: validate_length_gt,
        desc.fields_by_name['length_lt'].number: validate_length_lt,
        desc.fields_by_name['length_eq'].number: validate_length_eq,
    }

    @classmethod
    def get_validator_by_number(cls, option_number):
        return cls.validator_map.get(option_number)
