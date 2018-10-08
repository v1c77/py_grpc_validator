# -*- coding: utf-8 -*-

from grpc_proto_validator.validator import (
    validate_regex,
    validate_gt,
    validate_lt,
    validate_gte,
    validate_lte,
    validate_float_gt,
    validate_float_lt,
    validate_float_gte,
    validate_float_lte,
    validate_msg_exists,
    validate_string_not_empty,
    validate_repeated_count_min,
    validate_repeated_count_max,
    validate_length_gt,
    validate_length_lt,
    validate_message,


)


def test_validate_regex():

    re = "^1(3|4|5|7|8)\\d{9}$"
    assert not validate_regex('13933312', re)
    assert validate_regex('13933312345', re)


def test_validate_gt():
    value, limit = 1, 2
    assert not validate_gt(value, limit)
