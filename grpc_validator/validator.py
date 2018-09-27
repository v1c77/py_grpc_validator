# -*- coding: utf-8 -*-
import inspect
from functools import wraps


def validator_wrap(func):

    @wraps(func)
    def wrapper(self, *args, **kwargs):
        # TODO(vici) do validate.
        pass
    return wrapper


class ValidateMetaclass(type):

    def __new__(mcs, name, bases, attrs):
        for attr in attrs:
            value = attrs[attr]
            if inspect.ismethod(attr):
                attrs[attr] = validator_wrap(value)

        return type.__new__(mcs, name, bases, attrs)


class Validator(object):


    def validate(self, request, context, handler_detail):
        pass

    def get_field_options(self, handler_detail):
        pass

    def wrapper_gen(self, handler_detail):

        # TODO(vici) field_options from pb and handler detail
        def deco(func):

            @wraps(func)
            def wrapper(*args, **kwargs):
                # TODO(vici) delete
                print('I did not do the valdator now for {}'.format(func.__name__))
                return func(*args, **kwargs)
            return wrapper
        return deco
