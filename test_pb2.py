# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: test.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='test.proto',
  package='test',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\ntest.proto\x12\x04test\"\x18\n\x07Request\x12\r\n\x05image\x18\x01 \x01(\x0c\"\x14\n\x05Reply\x12\x0b\n\x03ret\x18\x01 \x01(\t21\n\tSpeedTest\x12$\n\x04work\x12\r.test.Request\x1a\x0b.test.Reply\"\x00\x62\x06proto3')
)




_REQUEST = _descriptor.Descriptor(
  name='Request',
  full_name='test.Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='image', full_name='test.Request.image', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
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
  serialized_start=20,
  serialized_end=44,
)


_REPLY = _descriptor.Descriptor(
  name='Reply',
  full_name='test.Reply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ret', full_name='test.Reply.ret', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=46,
  serialized_end=66,
)

DESCRIPTOR.message_types_by_name['Request'] = _REQUEST
DESCRIPTOR.message_types_by_name['Reply'] = _REPLY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Request = _reflection.GeneratedProtocolMessageType('Request', (_message.Message,), {
  'DESCRIPTOR' : _REQUEST,
  '__module__' : 'test_pb2'
  # @@protoc_insertion_point(class_scope:test.Request)
  })
_sym_db.RegisterMessage(Request)

Reply = _reflection.GeneratedProtocolMessageType('Reply', (_message.Message,), {
  'DESCRIPTOR' : _REPLY,
  '__module__' : 'test_pb2'
  # @@protoc_insertion_point(class_scope:test.Reply)
  })
_sym_db.RegisterMessage(Reply)



_SPEEDTEST = _descriptor.ServiceDescriptor(
  name='SpeedTest',
  full_name='test.SpeedTest',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=68,
  serialized_end=117,
  methods=[
  _descriptor.MethodDescriptor(
    name='work',
    full_name='test.SpeedTest.work',
    index=0,
    containing_service=None,
    input_type=_REQUEST,
    output_type=_REPLY,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_SPEEDTEST)

DESCRIPTOR.services_by_name['SpeedTest'] = _SPEEDTEST

# @@protoc_insertion_point(module_scope)