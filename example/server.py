# -*- coding: utf-8 -*-
import six
import time
import logging
import sys
from concurrent import futures

import grpc
from grpc_proto_validator.validator import ValidateMetaclass

from example import hello_bro_pb2
from example import hello_bro_pb2_grpc


root = logging.getLogger()
root.setLevel(logging.DEBUG)

ch = logging.StreamHandler(sys.stdout)
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
root.addHandler(ch)

_ONE_DAY_IN_SECONDS = 60 * 60 * 24


def func_cost():
    print('c is runing.!!!')
    start = time.time()
    end = start + 10
    i = 1

    while i > 0:
        i += 1
        if time.time() > end:
            break
    print('down')


class Bro(six.with_metaclass(ValidateMetaclass,
                             hello_bro_pb2_grpc.BroServicer)):

    def SayHello(self, request, context):
        root.info('trace')

        return hello_bro_pb2.HelloReply(
            message='Hello, %s!' % request.name,
            by=request.name)

    def SayBye(self, request, context):
        return hello_bro_pb2.HelloReply(
            message='did i say bye to %s?' % request.name,
            by='bad_man')


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=65))
    hello_bro_pb2_grpc.add_BroServicer_to_server(Bro(), server)
    port = server.add_insecure_port('[::]:1947')
    print("port at {}".format(port))
    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    serve()
