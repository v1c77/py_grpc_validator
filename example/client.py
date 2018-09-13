# -*- coding: utf-8 -*-

from __future__ import print_function

import grpc

from example import hello_bro_pb2
from example import hello_bro_pb2_grpc


def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    channel = grpc.insecure_channel('localhost:1947')
    stub = hello_bro_pb2_grpc.BroStub(channel)
    # response1 = stub.SayHello(hello_bro_pb2.HelloRequest(name='you'))
    # print("Greeter client received: " + response1.message)
    stub.SayBye(hello_bro_pb2.HelloRequest(name='vici'))
    print('never say bye.')  # server exception...


if __name__ == '__main__':
    run()
