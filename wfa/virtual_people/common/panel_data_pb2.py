# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: wfa/virtual_people/common/panel_data.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from wfa.virtual_people.common import demographic_pb2 as wfa_dot_virtual__people_dot_common_dot_demographic__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*wfa/virtual_people/common/panel_data.proto\x12\x12wfa_virtual_people\x1a+wfa/virtual_people/common/demographic.proto\"b\n\nPanelistId\x12\x18\n\x0bpanelist_id\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x19\n\x0chousehold_id\x18\x02 \x01(\tH\x01\x88\x01\x01\x42\x0e\n\x0c_panelist_idB\x0f\n\r_household_id\"\x90\x01\n\x08Panelist\x12\x38\n\x0bpanelist_id\x18\x01 \x01(\x0b\x32\x1e.wfa_virtual_people.PanelistIdH\x00\x88\x01\x01\x12\x31\n\x04\x64\x65mo\x18\x02 \x01(\x0b\x32\x1e.wfa_virtual_people.DemoBucketH\x01\x88\x01\x01\x42\x0e\n\x0c_panelist_idB\x07\n\x05_demo\"`\n\tPanelData\x12\x15\n\x08panel_id\x18\x01 \x01(\tH\x00\x88\x01\x01\x12/\n\tpanelists\x18\x02 \x03(\x0b\x32\x1c.wfa_virtual_people.PanelistB\x0b\n\t_panel_idB#\n\x1forg.wfanet.virtualpeople.commonP\x01\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'wfa.virtual_people.common.panel_data_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\037org.wfanet.virtualpeople.commonP\001'
  _PANELISTID._serialized_start=111
  _PANELISTID._serialized_end=209
  _PANELIST._serialized_start=212
  _PANELIST._serialized_end=356
  _PANELDATA._serialized_start=358
  _PANELDATA._serialized_end=454
# @@protoc_insertion_point(module_scope)
