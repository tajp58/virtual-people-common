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

#ifndef WFA_VIRTUAL_PEOPLE_COMMON_FIELD_FILTER_TRUE_FILTER_H_
#define WFA_VIRTUAL_PEOPLE_COMMON_FIELD_FILTER_TRUE_FILTER_H_

#include "absl/status/statusor.h"
#include "google/protobuf/message.h"
#include "src/main/proto/wfa/virtual_people/common/field_filter.pb.h"
#include "wfa/virtual_people/common/field_filter/field_filter.h"

namespace wfa_virtual_people {

// The implementation of field filter when op is TRUE in @config.
class TrueFilter : public FieldFilter {
 public:
  // Always use FieldFilter::New.
  // Users should never call TrueFilter::New or any constructor directly.
  //
  // Returns error status if any of the following happens:
  //   @config.op is not TRUE.
  //   @config.name is set.
  //   @config.value is set.
  //   @config.sub_filters is not empty.
  static absl::StatusOr<std::unique_ptr<TrueFilter>> New(
      const FieldFilterProto& config);

  TrueFilter() {}

  TrueFilter(const TrueFilter&) = delete;
  TrueFilter& operator=(const TrueFilter&) = delete;

  // Always returns true.
  bool IsMatch(const google::protobuf::Message&) const override;
};

}  // namespace wfa_virtual_people

#endif  // WFA_VIRTUAL_PEOPLE_COMMON_FIELD_FILTER_TRUE_FILTER_H_
