python grpc validator
~~~~~~~~~~~~~~~~~~~~~
plugin of validate request field for python grpc server.

.. image:: https://travis-ci.com/v1c77/py_grpc_validator.svg?branch=master
    :target: https://travis-ci.com/v1c77/py_grpc_validator
.. image:: https://codecov.io/gh/v1c77/py_grpc_validator/branch/master/graph/badge.svg
  :target: https://codecov.io/gh/v1c77/py_grpc_validator

TODO:
    - type hint for different field type.(such as only string field can do
      a string length check.)
    - test case & Makefile.
    - a cli to help protoc with `validator.proto`.
    - anymore bugs or improves?



How To
######

1. install

.. code-block:: bash

    pip install grpc-proto-validator

2. copy **validator.proto** to your project proto path and do protoc.(TODO a
cli help to copy or build proto.)

 The **validator.proto** is included in this package, you can find it in
 python site-packages path.


A example on how to generate the grpc files:

.. code-block:: bash

    $ python -m grpc_tools.protoc \
      --proto_path={/path/to/validator/proto} \
      --proto_path={/path/to/your/project/proto} \
      --python_out={/path/to/project/src} \
      --grpc_python_out={/path/to/project/src} \
      path/to/your.proto



3. change your service and \*_pb2 code.

To avoid protobuf import error, change one line in the generated
python file(like `hello_bro_pb2.py`).

from:

.. code-block:: python

    import validator_pb2 as validator__pb2

to:

.. code-block:: python

    import grpc_proto_validator.validator_pb2 as validator__pb2.

Then create service with validator:

.. code-block:: python

    import six
    from grpc_validator.validator import ValidateMetaclass

    class YourService(six.with_metaclass(ValidateMetaclass,
                             YourService_pb2_grpc.YourServiceServer)):

        def behaviour1(self, request, context)
            ...


Also, you can select individual service handler to do the field check:

.. code-block:: python

    from grpc_validator.validator import validator_wrap


    class YourService(YourService_pb2_grpc.YourServiceServer):

        def behaviour(self, request, context):
            """request will not be validated."""
            ...

        @validator_wrap
        def behaviour2(self, request, context):
            ...



Notice
######

Someone has used go-proto-validator_ before will notice
that I almost reuse its proto file which make it easier
to co-work with our golang service team.

But please don't mix these two proto files.
**!!!THEY ARE NOT IN COMMON USE!!!**

Any help or idea is favourably receive. Please just make a issue_.

LICENSE
=======
MIT_.

.. _ecosystem: https://github.com/grpc-ecosystem/go-grpc-middleware/tree/master/validator
.. _go-proto-validator: https://github.com/mwitkow/go-proto-validators
.. _issue: https://github.com/v1c77/py_grpc_validator/issues/new
.. _MIT: https://github.com/v1c77/py_grpc_validator/blob/master/LICENSE
