python grpc validator
~~~~~~~~~~~~~~~~~~~~~
plugin of validate request field for python grpc server.

TODO:
    - type hint for different field type.(such as only string field can do
      a string length check.)
    - setup tool & test case & Makefile. & LICENSE & push to pypi repo
    - a cli to help protoc with `validator.proto`.
    - anymore bugs or improves?



How To
######

1. install (TODO: setup.py needed.)

.. code-block:: bash

    git clone https://github.com/v1c77/py_grpc_validator.git
    cd py_grpc_validator
    pip install --editable .


2. copy **validator.proto** to your project proto path and do protoc.

 a example on how to generate the grpc files.

.. code-block:: bash

    $ python -m grpc_tools.protoc
      --proto_path={/path/to/validator/proto} \
      --proto_path={/path/to/your/project/proto} \
      --python_out={/path/to/project/src} \
      {/path/to/validator/proto}/validator.proto

.. code-block:: bash

    $ python -m grpc_tools.protoc --proto_path=./proto \
      --proto_path={/path/to/validator/proto} \
      --proto_path={/path/to/your/project/proto} \
      --python_out={/path/to/project/src} \
      --grpc_python_out={/path/to/project/src} \
      example/proto/hello_bro.proto

3. change your service code. (just a little.)

to validate all the service handlers:

.. code-block:: python

    import six
    from grpc_validator.validator import ValidateMetaclass

    class YourService(six.with_metaclass(ValidateMetaclass,
                             YourService_pb2_grpc.YourServiceServer)):

        def behaviour1(self, request, context)
            ...


Also you can select individual service handler to do the field check:

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
TODO

.. _ecosystem: https://github.com/grpc-ecosystem/go-grpc-middleware/tree/master/validator
.. _go-proto-validator: https://github.com/mwitkow/go-proto-validators
.. _issue: https://github.com/v1c77/py_grpc_validator/issues/new
