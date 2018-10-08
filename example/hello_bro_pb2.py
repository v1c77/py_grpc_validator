# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: hello_bro.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import grpc_proto_validator.validator_pb2 as validator__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='hello_bro.proto',
  package='hellobro',
  syntax='proto3',
  serialized_options=_b('\242\002\003HLW'),
  serialized_pb=_b('\n\x0fhello_bro.proto\x12\x08hellobro\x1a\x0fvalidator.proto\"-\n\x03\x44\x61u\x12&\n\x04mail\x18\x01 \x01(\tB\x18\x9a\x42\x15\n\x13^1(3|4|5|7|8)\\d{9}$\"\xe1\x01\n\x0cHelloRequest\x12\x13\n\x04name\x18\x01 \x01(\tB\x05\x9a\x42\x02`\x01\x12\x14\n\x03\x61ge\x18\x02 \x01(\x05\x42\x07\x9a\x42\x04\x10\x32\x18\x64\x12\x32\n\x05\x63hild\x18\x03 \x01(\x0b\x32\x1c.hellobro.HelloRequest.ChildB\x05\x9a\x42\x02P\x01\x12\x1a\n\x03\x64\x61u\x18\x04 \x01(\x0b\x32\r.hellobro.Dau\x12\x10\n\x08\x63\x61tegray\x18\x05 \x01(\t\x1a\x44\n\x05\x43hild\x12\x14\n\x04name\x18\x01 \x01(\tB\x06\x9a\x42\x03\x88\x01\x04\x12%\n\x06weight\x18\x02 \x01(\x02\x42\x15\x9a\x42\x12\x31\x33\x33\x33\x33\x33\x33N@9\x00\x00\x00\x00\x00\x00Y@\")\n\nHelloReply\x12\x0f\n\x07message\x18\x01 \x01(\t\x12\n\n\x02\x62y\x18\x02 \x01(\t2{\n\x03\x42ro\x12:\n\x08SayHello\x12\x16.hellobro.HelloRequest\x1a\x14.hellobro.HelloReply\"\x00\x12\x38\n\x06SayBye\x12\x16.hellobro.HelloRequest\x1a\x14.hellobro.HelloReply\"\x00\x42\x06\xa2\x02\x03HLWb\x06proto3')
  ,
  dependencies=[validator__pb2.DESCRIPTOR,])




_DAU = _descriptor.Descriptor(
  name='Dau',
  full_name='hellobro.Dau',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='mail', full_name='hellobro.Dau.mail', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\232B\025\n\023^1(3|4|5|7|8)\\d{9}$'), file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=46,
  serialized_end=91,
)


_HELLOREQUEST_CHILD = _descriptor.Descriptor(
  name='Child',
  full_name='hellobro.HelloRequest.Child',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='hellobro.HelloRequest.Child.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\232B\003\210\001\004'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='weight', full_name='hellobro.HelloRequest.Child.weight', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\232B\0221333333N@9\000\000\000\000\000\000Y@'), file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=251,
  serialized_end=319,
)

_HELLOREQUEST = _descriptor.Descriptor(
  name='HelloRequest',
  full_name='hellobro.HelloRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='hellobro.HelloRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\232B\002`\001'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='age', full_name='hellobro.HelloRequest.age', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\232B\004\0202\030d'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='child', full_name='hellobro.HelloRequest.child', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\232B\002P\001'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dau', full_name='hellobro.HelloRequest.dau', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='categray', full_name='hellobro.HelloRequest.categray', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_HELLOREQUEST_CHILD, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=94,
  serialized_end=319,
)


_HELLOREPLY = _descriptor.Descriptor(
  name='HelloReply',
  full_name='hellobro.HelloReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='hellobro.HelloReply.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='by', full_name='hellobro.HelloReply.by', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=321,
  serialized_end=362,
)

_HELLOREQUEST_CHILD.containing_type = _HELLOREQUEST
_HELLOREQUEST.fields_by_name['child'].message_type = _HELLOREQUEST_CHILD
_HELLOREQUEST.fields_by_name['dau'].message_type = _DAU
DESCRIPTOR.message_types_by_name['Dau'] = _DAU
DESCRIPTOR.message_types_by_name['HelloRequest'] = _HELLOREQUEST
DESCRIPTOR.message_types_by_name['HelloReply'] = _HELLOREPLY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Dau = _reflection.GeneratedProtocolMessageType('Dau', (_message.Message,), dict(
  DESCRIPTOR = _DAU,
  __module__ = 'hello_bro_pb2'
  # @@protoc_insertion_point(class_scope:hellobro.Dau)
  ))
_sym_db.RegisterMessage(Dau)

HelloRequest = _reflection.GeneratedProtocolMessageType('HelloRequest', (_message.Message,), dict(

  Child = _reflection.GeneratedProtocolMessageType('Child', (_message.Message,), dict(
    DESCRIPTOR = _HELLOREQUEST_CHILD,
    __module__ = 'hello_bro_pb2'
    # @@protoc_insertion_point(class_scope:hellobro.HelloRequest.Child)
    ))
  ,
  DESCRIPTOR = _HELLOREQUEST,
  __module__ = 'hello_bro_pb2'
  # @@protoc_insertion_point(class_scope:hellobro.HelloRequest)
  ))
_sym_db.RegisterMessage(HelloRequest)
_sym_db.RegisterMessage(HelloRequest.Child)

HelloReply = _reflection.GeneratedProtocolMessageType('HelloReply', (_message.Message,), dict(
  DESCRIPTOR = _HELLOREPLY,
  __module__ = 'hello_bro_pb2'
  # @@protoc_insertion_point(class_scope:hellobro.HelloReply)
  ))
_sym_db.RegisterMessage(HelloReply)


DESCRIPTOR._options = None
_DAU.fields_by_name['mail']._options = None
_HELLOREQUEST_CHILD.fields_by_name['name']._options = None
_HELLOREQUEST_CHILD.fields_by_name['weight']._options = None
_HELLOREQUEST.fields_by_name['name']._options = None
_HELLOREQUEST.fields_by_name['age']._options = None
_HELLOREQUEST.fields_by_name['child']._options = None

_BRO = _descriptor.ServiceDescriptor(
  name='Bro',
  full_name='hellobro.Bro',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=364,
  serialized_end=487,
  methods=[
  _descriptor.MethodDescriptor(
    name='SayHello',
    full_name='hellobro.Bro.SayHello',
    index=0,
    containing_service=None,
    input_type=_HELLOREQUEST,
    output_type=_HELLOREPLY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='SayBye',
    full_name='hellobro.Bro.SayBye',
    index=1,
    containing_service=None,
    input_type=_HELLOREQUEST,
    output_type=_HELLOREPLY,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_BRO)

DESCRIPTOR.services_by_name['Bro'] = _BRO

# @@protoc_insertion_point(module_scope)
