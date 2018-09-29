# -*- coding: utf-8 -*-

from __future__ import print_function

import grpc

from example import hello_bro_pb2
from example import hello_bro_pb2_grpc
from google.protobuf.json_format import ParseDict


def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    channel = grpc.insecure_channel('localhost:1947')
    stub = hello_bro_pb2_grpc.BroStub(channel)
    hello_dict = {
        'name': 'vici.sigma',
        'age': 56,
        'child': {
            'name': 'v1c1',
            'weight': 66.66,
        },
        'dau': {
            'mail': '13522455567'
        }
    }
    hello_requst = ParseDict(
                hello_dict,
                hello_bro_pb2.HelloRequest(),
            )
    stub.SayHello(hello_requst)


if __name__ == '__main__':
    run()
