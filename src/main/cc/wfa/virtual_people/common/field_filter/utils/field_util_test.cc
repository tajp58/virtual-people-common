// Copyright 2021 The Cross-Media Measurement Authors
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//      http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

#include "wfa/virtual_people/common/field_filter/utils/field_util.h"

#include "absl/status/status.h"
#include "gmock/gmock.h"
#include "google/protobuf/descriptor.h"
#include "google/protobuf/message.h"
#include "google/protobuf/text_format.h"
#include "gtest/gtest.h"
#include "src/main/cc/wfa/virtual_people/common/field_filter/test/test.pb.h"

namespace wfa_virtual_people {
namespace {

using ::google::protobuf::FieldDescriptor;
using ::google::protobuf::Message;
using ::wfa_virtual_people::test::TestProto;

TEST(GetFieldFromProtoTest, GetFieldAndValue) {
  TestProto test_proto_1, test_proto_2;
  ASSERT_TRUE(google::protobuf::TextFormat::ParseFromString(R"PROTO(
      a {
        b {
          int32_value: 1
          int64_value: 1
          uint32_value: 1
          uint64_value: 1
          float_value: 1.0
          double_value: 1.0
          bool_value: true
          enum_value: TEST_ENUM_1
          string_value: "string1"
        }
      }
  )PROTO", &test_proto_1));
  ASSERT_TRUE(google::protobuf::TextFormat::ParseFromString(R"PROTO(
      a {
        b {
          int32_value: 2
          int64_value: 2
          uint32_value: 2
          uint64_value: 2
          float_value: 2.0
          double_value: 2.0
          bool_value: false
          enum_value: TEST_ENUM_2
          string_value: "string2"
        }
      }
  )PROTO", &test_proto_2));
  std::vector<const google::protobuf::FieldDescriptor*> field_descriptors;
  // Test int32.
  EXPECT_TRUE(
      GetFieldFromProto(
          test_proto_1.GetDescriptor(), "a.b.int32_value", &field_descriptors
      ).ok());
  EXPECT_EQ(GetValueFromProto<int32_t>(test_proto_2, field_descriptors), 2);
  // Test int64.
  EXPECT_TRUE(
      GetFieldFromProto(
          test_proto_1.GetDescriptor(), "a.b.int64_value", &field_descriptors
      ).ok());
  EXPECT_EQ(GetValueFromProto<int64_t>(test_proto_2, field_descriptors), 2);
  // Test uint32.
  EXPECT_TRUE(
      GetFieldFromProto(
          test_proto_1.GetDescriptor(), "a.b.uint32_value", &field_descriptors
      ).ok());
  EXPECT_EQ(GetValueFromProto<uint32_t>(test_proto_2, field_descriptors), 2);
  // Test int64.
  EXPECT_TRUE(
      GetFieldFromProto(
          test_proto_1.GetDescriptor(), "a.b.uint64_value", &field_descriptors
      ).ok());
  EXPECT_EQ(GetValueFromProto<uint64_t>(test_proto_2, field_descriptors), 2);
  // Test float.
  EXPECT_TRUE(
      GetFieldFromProto(
          test_proto_1.GetDescriptor(), "a.b.float_value", &field_descriptors
      ).ok());
  EXPECT_EQ(GetValueFromProto<float>(test_proto_2, field_descriptors), 2.0);
  // Test double.
  EXPECT_TRUE(
      GetFieldFromProto(
          test_proto_1.GetDescriptor(), "a.b.double_value", &field_descriptors
      ).ok());
  EXPECT_EQ(GetValueFromProto<double>(test_proto_2, field_descriptors), 2.0);
  // Test bool.
  EXPECT_TRUE(
      GetFieldFromProto(
          test_proto_1.GetDescriptor(), "a.b.bool_value", &field_descriptors
      ).ok());
  EXPECT_FALSE(GetValueFromProto<bool>(test_proto_2, field_descriptors));
  // Test enum.
  EXPECT_TRUE(
      GetFieldFromProto(
          test_proto_1.GetDescriptor(), "a.b.enum_value", &field_descriptors
      ).ok());
  EXPECT_EQ(
      GetValueFromProto<const google::protobuf::EnumValueDescriptor*>(
          test_proto_2, field_descriptors)->number(), 2);
  // Test string.
  EXPECT_TRUE(
      GetFieldFromProto(
          test_proto_1.GetDescriptor(), "a.b.string_value", &field_descriptors
      ).ok());
  EXPECT_EQ(
      GetValueFromProto<const std::string&>(test_proto_2, field_descriptors),
      "string2");
}

TEST(GetFieldFromProtoTest, InvalidFieldName) {
  TestProto test_proto;
  ASSERT_TRUE(google::protobuf::TextFormat::ParseFromString(R"PROTO(
      a {
        b {
          int64_value: 1
        }
      }
  )PROTO", &test_proto));
  std::vector<const google::protobuf::FieldDescriptor*> field_descriptors;
  absl::Status status =
      GetFieldFromProto(test_proto.GetDescriptor(), "a.c", &field_descriptors);
  EXPECT_EQ(status.code(), absl::StatusCode::kInvalidArgument);
}

TEST(GetFieldFromProtoTest, InvalidSubmessageName) {
  TestProto test_proto;
  ASSERT_TRUE(google::protobuf::TextFormat::ParseFromString(R"PROTO(
      a {
        b {
          int64_value: 1
        }
      }
  )PROTO", &test_proto));
  std::vector<const google::protobuf::FieldDescriptor*> field_descriptors;
  absl::Status status =
      GetFieldFromProto(test_proto.GetDescriptor(), "a.b.int64_value.c",
                        &field_descriptors);
  EXPECT_EQ(status.code(), absl::StatusCode::kInvalidArgument);
}

}  // namespace
}  // namespace wfa_virtual_people
