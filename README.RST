python grpc validator
~~~~~~~~~~~~~~~~~~~~~
validator for python grpc framework. (in draft)

grpc ecosystem_ give the definition of grpc validator:

    grpc_validator is a generic request contents validator server-side
    middleware for gRPC.


to generate proto python file:

.. code-block:: bash

    python -m grpc_tools.protoc --proto_path=./proto \
     --proto_path=./example/proto \
     --python_out=./example/ \
     --grpc_python_out=./example/ \
     example/proto/hello_bro.proto

in draft now...

any help or idea is favourably receive.


.. _ecosystem: https://github.com/grpc-ecosystem/go-grpc-middleware/tree/master/validator

