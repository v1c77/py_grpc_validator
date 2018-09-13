# -*- coding: utf-8 -*-
# Copyright (c) 2013-2018, SMARTX
# All rights reserved.

import grpc
import abc
import six


def _unary_unary_rpc_terminator(code, details):

    def terminate(ignored_request, context):
        context.abort(code, details)

    return grpc.unary_unary_rpc_method_handler(terminate)


class Validator(six.with_metaclass(abc.ABCMeta)):

    @abc.abstractmethod
    def validator(self):
        """
        interface used to
        :return:
        """
        raise NotImplementedError()


class GrpcServerValidator(grpc.ServerInterceptor, Validator):

    def validator(self):
        pass

    def intercept_service(self, continuation, handler_call_details):

        pass


class GrpcClientValidator(grpc.StreamStreamClientInterceptor,
                           grpc.StreamUnaryClientInterceptor,
                           grpc.UnaryStreamClientInterceptor,
                           grpc.UnaryUnaryClientInterceptor,
                           Validator):

    def validator(self):
        pass

    def intercept_unary_unary(self, continuation, client_call_details,
                              request):
        pass

    def intercept_unary_stream(self, continuation, client_call_details,
                               request):
        pass

    def intercept_stream_unary(self, continuation, client_call_details,
                               request_iterator):
        pass

    def intercept_stream_stream(self, continuation, client_call_details,
                                request_iterator):
        pass
