// Copyright 2022 The Cross-Media Measurement Authors
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

#ifndef SRC_MAIN_CC_WFA_VIRTUAL_PEOPLE_COMMON_INTEGRATION_TESTING_FRAMEWORK_GOLDEN_GENERATOR_H_
#define SRC_MAIN_CC_WFA_VIRTUAL_PEOPLE_COMMON_INTEGRATION_TESTING_FRAMEWORK_GOLDEN_GENERATOR_H_

#include <string>
#include <vector>

#include "wfa/virtual_people/common/config.pb.h"

namespace wfa_virtual_people {

// Generates CLI commands to generate golden files of binaries based on input
// config.
std::vector<std::string> GoldenGenerator(const IntegrationTestList& config);

}  // namespace wfa_virtual_people

#endif  // SRC_MAIN_CC_WFA_VIRTUAL_PEOPLE_COMMON_INTEGRATION_TESTING_FRAMEWORK_GOLDEN_GENERATOR_H_