# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: wfa/virtual_people/common/config.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&wfa/virtual_people/common/config.proto\x12\x12wfa_virtual_people\"\x9e\x01\n\x06Golden\x12\x18\n\x0bgolden_path\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x17\n\nproto_path\x18\x02 \x01(\tH\x01\x88\x01\x01\x12\x1a\n\x12proto_dependencies\x18\x03 \x03(\t\x12\x17\n\nproto_type\x18\x04 \x01(\tH\x02\x88\x01\x01\x42\x0e\n\x0c_golden_pathB\r\n\x0b_proto_pathB\r\n\x0b_proto_type\"j\n\x0f\x42inaryParameter\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\x12/\n\x06golden\x18\x03 \x01(\x0b\x32\x1a.wfa_virtual_people.GoldenH\x00\x88\x01\x01\x42\t\n\x07_golden\"X\n\x08TestCase\x12\x0c\n\x04name\x18\x01 \x01(\t\x12>\n\x11\x62inary_parameters\x18\x02 \x03(\x0b\x32#.wfa_virtual_people.BinaryParameter\"a\n\x0fIntegrationTest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0e\n\x06\x62inary\x18\x02 \x01(\t\x12\x30\n\ntest_cases\x18\x03 \x03(\x0b\x32\x1c.wfa_virtual_people.TestCase\"I\n\x13IntegrationTestList\x12\x32\n\x05tests\x18\x01 \x03(\x0b\x32#.wfa_virtual_people.IntegrationTestb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'wfa.virtual_people.common.config_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _GOLDEN._serialized_start=63
  _GOLDEN._serialized_end=221
  _BINARYPARAMETER._serialized_start=223
  _BINARYPARAMETER._serialized_end=329
  _TESTCASE._serialized_start=331
  _TESTCASE._serialized_end=419
  _INTEGRATIONTEST._serialized_start=421
  _INTEGRATIONTEST._serialized_end=518
  _INTEGRATIONTESTLIST._serialized_start=520
  _INTEGRATIONTESTLIST._serialized_end=593
# @@protoc_insertion_point(module_scope)