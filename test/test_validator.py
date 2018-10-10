# -*- coding: utf-8 -*-

from grpc_proto_validator.validator import validate_regex


def test_validate_regex():

    re = "^1(3|4|5|7|8)\\d{9}$"
    assert not validate_regex('13933312', re)
    assert validate_regex('13933312345', re)
