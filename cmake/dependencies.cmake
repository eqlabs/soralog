#
# Copyright Soramitsu Co., Ltd. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0
#

if (TESTING OR COVERAGE)
  add_3rdparty(GTest)
endif()

add_3rdparty(yaml-cpp)
if (NOT TARGET yaml-cpp::yaml-cpp)
    add_library(yaml-cpp::yaml-cpp ALIAS yaml-cpp)
endif()

add_3rdparty(fmt)
