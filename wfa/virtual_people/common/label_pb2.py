# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: wfa/virtual_people/common/label.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from wfa.virtual_people.common import demographic_pb2 as wfa_dot_virtual__people_dot_common_dot_demographic__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%wfa/virtual_people/common/label.proto\x12\x12wfa_virtual_people\x1a+wfa/virtual_people/common/demographic.proto\"S\n\x15PersonLabelAttributes\x12\x31\n\x04\x64\x65mo\x18\x01 \x01(\x0b\x32\x1e.wfa_virtual_people.DemoBucketH\x00\x88\x01\x01\x42\x07\n\x05_demo\"|\n\x0cQuantumLabel\x12\x39\n\x06labels\x18\x01 \x03(\x0b\x32).wfa_virtual_people.PersonLabelAttributes\x12\x15\n\rprobabilities\x18\x02 \x03(\x01\x12\x11\n\x04seed\x18\x03 \x01(\tH\x00\x88\x01\x01\x42\x07\n\x05_seed\"T\n\x18IndependentQuantumLabels\x12\x38\n\x0equantum_labels\x18\x01 \x03(\x0b\x32 .wfa_virtual_people.QuantumLabel\"\xd4\x01\n\x15VirtualPersonActivity\x12\x1e\n\x11virtual_person_id\x18\x01 \x01(\x04H\x01\x88\x01\x01\x12\x39\n\rquantum_label\x18\x02 \x01(\x0b\x32 .wfa_virtual_people.QuantumLabelH\x00\x12:\n\x05label\x18\x03 \x01(\x0b\x32).wfa_virtual_people.PersonLabelAttributesH\x00\x42\x0e\n\x0cperson_labelB\x14\n\x12_virtual_person_id\"\x8a\x01\n\rLabelerOutput\x12\x39\n\x06people\x18\x01 \x03(\x0b\x32).wfa_virtual_people.VirtualPersonActivity\x12#\n\x16serialized_debug_trace\x18\x02 \x01(\tH\x00\x88\x01\x01\x42\x19\n\x17_serialized_debug_trace\"\\\n\x17LabelerResponseMetadata\x12\x1a\n\rapplied_model\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x13\n\x0bmodel_lines\x18\x02 \x03(\tB\x10\n\x0e_applied_model\"\xd9\x01\n\x11MetaLabelerOutput\x12>\n\x0elabeler_output\x18\x01 \x01(\x0b\x32!.wfa_virtual_people.LabelerOutputH\x00\x88\x01\x01\x12S\n\x19labeler_response_metadata\x18\x02 \x01(\x0b\x32+.wfa_virtual_people.LabelerResponseMetadataH\x01\x88\x01\x01\x42\x11\n\x0f_labeler_outputB\x1c\n\x1a_labeler_response_metadataB#\n\x1forg.wfanet.virtualpeople.commonP\x01\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'wfa.virtual_people.common.label_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\037org.wfanet.virtualpeople.commonP\001'
  _PERSONLABELATTRIBUTES._serialized_start=106
  _PERSONLABELATTRIBUTES._serialized_end=189
  _QUANTUMLABEL._serialized_start=191
  _QUANTUMLABEL._serialized_end=315
  _INDEPENDENTQUANTUMLABELS._serialized_start=317
  _INDEPENDENTQUANTUMLABELS._serialized_end=401
  _VIRTUALPERSONACTIVITY._serialized_start=404
  _VIRTUALPERSONACTIVITY._serialized_end=616
  _LABELEROUTPUT._serialized_start=619
  _LABELEROUTPUT._serialized_end=757
  _LABELERRESPONSEMETADATA._serialized_start=759
  _LABELERRESPONSEMETADATA._serialized_end=851
  _METALABELEROUTPUT._serialized_start=854
  _METALABELEROUTPUT._serialized_end=1071
# @@protoc_insertion_point(module_scope)
