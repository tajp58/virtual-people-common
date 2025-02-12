# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: wfa/virtual_people/common/event.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from wfa.virtual_people.common import demographic_pb2 as wfa_dot_virtual__people_dot_common_dot_demographic__pb2
from wfa.virtual_people.common import geo_location_pb2 as wfa_dot_virtual__people_dot_common_dot_geo__location__pb2
from wfa.virtual_people.common import label_pb2 as wfa_dot_virtual__people_dot_common_dot_label__pb2
from wfa.virtual_people.common import panel_data_pb2 as wfa_dot_virtual__people_dot_common_dot_panel__data__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%wfa/virtual_people/common/event.proto\x12\x12wfa_virtual_people\x1a+wfa/virtual_people/common/demographic.proto\x1a,wfa/virtual_people/common/geo_location.proto\x1a%wfa/virtual_people/common/label.proto\x1a*wfa/virtual_people/common/panel_data.proto\"w\n\x07\x45ventId\x12\x16\n\tpublisher\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x0f\n\x02id\x18\x02 \x01(\tH\x01\x88\x01\x01\x12\x1b\n\x0eid_fingerprint\x18\x03 \x01(\x04H\x02\x88\x01\x01\x42\x0c\n\n_publisherB\x05\n\x03_idB\x11\n\x0f_id_fingerprint\"\xb3\x02\n\x08UserInfo\x12\x14\n\x07user_id\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x1c\n\x0fprofile_version\x18\x02 \x01(\tH\x01\x88\x01\x01\x12/\n\x04\x64\x65mo\x18\x03 \x01(\x0b\x32\x1c.wfa_virtual_people.DemoInfoH\x02\x88\x01\x01\x12\x36\n\x08home_geo\x18\x04 \x01(\x0b\x32\x1f.wfa_virtual_people.GeoLocationH\x03\x88\x01\x01\x12\x1a\n\x12\x63reation_time_usec\x18\x05 \x01(\x03\x12 \n\x13user_id_fingerprint\x18\x06 \x01(\x04H\x04\x88\x01\x01\x42\n\n\x08_user_idB\x12\n\x10_profile_versionB\x07\n\x05_demoB\x0b\n\t_home_geoB\x16\n\x14_user_id_fingerprint\"G\n\x0bTrafficInfo\x12 \n\x13\x65vent_collection_id\x18\x01 \x01(\tH\x00\x88\x01\x01\x42\x16\n\x14_event_collection_id\"\xe1\x0b\n\x0bProfileInfo\x12:\n\x0f\x65mail_user_info\x18\x01 \x01(\x0b\x32\x1c.wfa_virtual_people.UserInfoH\x00\x88\x01\x01\x12:\n\x0fphone_user_info\x18\x02 \x01(\x0b\x32\x1c.wfa_virtual_people.UserInfoH\x01\x88\x01\x01\x12\x41\n\x16logged_in_id_user_info\x18\x04 \x01(\x0b\x32\x1c.wfa_virtual_people.UserInfoH\x02\x88\x01\x01\x12\x42\n\x17logged_out_id_user_info\x18\x05 \x01(\x0b\x32\x1c.wfa_virtual_people.UserInfoH\x03\x88\x01\x01\x12K\n proprietary_id_space_1_user_info\x18\x03 \x01(\x0b\x32\x1c.wfa_virtual_people.UserInfoH\x04\x88\x01\x01\x12K\n proprietary_id_space_2_user_info\x18\x06 \x01(\x0b\x32\x1c.wfa_virtual_people.UserInfoH\x05\x88\x01\x01\x12K\n proprietary_id_space_3_user_info\x18\x07 \x01(\x0b\x32\x1c.wfa_virtual_people.UserInfoH\x06\x88\x01\x01\x12K\n proprietary_id_space_4_user_info\x18\x08 \x01(\x0b\x32\x1c.wfa_virtual_people.UserInfoH\x07\x88\x01\x01\x12K\n proprietary_id_space_5_user_info\x18\t \x01(\x0b\x32\x1c.wfa_virtual_people.UserInfoH\x08\x88\x01\x01\x12K\n proprietary_id_space_6_user_info\x18\n \x01(\x0b\x32\x1c.wfa_virtual_people.UserInfoH\t\x88\x01\x01\x12K\n proprietary_id_space_7_user_info\x18\x0b \x01(\x0b\x32\x1c.wfa_virtual_people.UserInfoH\n\x88\x01\x01\x12K\n proprietary_id_space_8_user_info\x18\x0c \x01(\x0b\x32\x1c.wfa_virtual_people.UserInfoH\x0b\x88\x01\x01\x12K\n proprietary_id_space_9_user_info\x18\r \x01(\x0b\x32\x1c.wfa_virtual_people.UserInfoH\x0c\x88\x01\x01\x12L\n!proprietary_id_space_10_user_info\x18\x0e \x01(\x0b\x32\x1c.wfa_virtual_people.UserInfoH\r\x88\x01\x01\x42\x12\n\x10_email_user_infoB\x12\n\x10_phone_user_infoB\x19\n\x17_logged_in_id_user_infoB\x1a\n\x18_logged_out_id_user_infoB#\n!_proprietary_id_space_1_user_infoB#\n!_proprietary_id_space_2_user_infoB#\n!_proprietary_id_space_3_user_infoB#\n!_proprietary_id_space_4_user_infoB#\n!_proprietary_id_space_5_user_infoB#\n!_proprietary_id_space_6_user_infoB#\n!_proprietary_id_space_7_user_infoB#\n!_proprietary_id_space_8_user_infoB#\n!_proprietary_id_space_9_user_infoB$\n\"_proprietary_id_space_10_user_info\"\xa6\x03\n\x0cLabelerInput\x12\x32\n\x08\x65vent_id\x18\x01 \x01(\x0b\x32\x1b.wfa_virtual_people.EventIdH\x00\x88\x01\x01\x12\x1b\n\x0etimestamp_usec\x18\x02 \x01(\x03H\x01\x88\x01\x01\x12\x17\n\nuser_agent\x18\x03 \x01(\tH\x02\x88\x01\x01\x12\x31\n\x03geo\x18\x04 \x01(\x0b\x32\x1f.wfa_virtual_people.GeoLocationH\x03\x88\x01\x01\x12:\n\x0cprofile_info\x18\x05 \x01(\x0b\x32\x1f.wfa_virtual_people.ProfileInfoH\x04\x88\x01\x01\x12\x18\n\x0b\x64\x65vice_type\x18\x06 \x01(\tH\x05\x88\x01\x01\x12:\n\x0ctraffic_info\x18\x07 \x01(\x0b\x32\x1f.wfa_virtual_people.TrafficInfoH\x06\x88\x01\x01\x42\x0b\n\t_event_idB\x11\n\x0f_timestamp_usecB\r\n\x0b_user_agentB\x06\n\x04_geoB\x0f\n\r_profile_infoB\x0e\n\x0c_device_typeB\x0f\n\r_traffic_info\"[\n\x08LogEvent\x12=\n\rlabeler_input\x18\xe8\x07 \x01(\x0b\x32 .wfa_virtual_people.LabelerInputH\x00\x88\x01\x01\x42\x10\n\x0e_labeler_input\"\x8e\x01\n\x11\x44\x61taProviderEvent\x12\x34\n\tlog_event\x18\x01 \x01(\x0b\x32\x1c.wfa_virtual_people.LogEventH\x00\x88\x01\x01\x12\x35\n\x06labels\x18\x02 \x03(\x0b\x32%.wfa_virtual_people.MetaLabelerOutputB\x0c\n\n_log_event\"\xbd\x01\n\rResearchEvent\x12\x34\n\tlog_event\x18\x01 \x01(\x0b\x32\x1c.wfa_virtual_people.LogEventH\x00\x88\x01\x01\x12\x35\n\x06labels\x18\x02 \x03(\x0b\x32%.wfa_virtual_people.MetaLabelerOutput\x12\x31\n\npanel_data\x18\x03 \x03(\x0b\x32\x1d.wfa_virtual_people.PanelDataB\x0c\n\n_log_eventB#\n\x1forg.wfanet.virtualpeople.commonP\x01\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'wfa.virtual_people.common.event_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\037org.wfanet.virtualpeople.commonP\001'
  _EVENTID._serialized_start=235
  _EVENTID._serialized_end=354
  _USERINFO._serialized_start=357
  _USERINFO._serialized_end=664
  _TRAFFICINFO._serialized_start=666
  _TRAFFICINFO._serialized_end=737
  _PROFILEINFO._serialized_start=740
  _PROFILEINFO._serialized_end=2245
  _LABELERINPUT._serialized_start=2248
  _LABELERINPUT._serialized_end=2670
  _LOGEVENT._serialized_start=2672
  _LOGEVENT._serialized_end=2763
  _DATAPROVIDEREVENT._serialized_start=2766
  _DATAPROVIDEREVENT._serialized_end=2908
  _RESEARCHEVENT._serialized_start=2911
  _RESEARCHEVENT._serialized_end=3100
# @@protoc_insertion_point(module_scope)
