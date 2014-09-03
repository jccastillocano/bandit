# -*- coding:utf-8 -*-
#
# Copyright 2014 Hewlett-Packard Development Company, L.P.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

"""Defines a set of tests targeting Str nodes in the AST."""

import bandit
from bandit.test_selector import *

# Str nodes are pretty simple - likely only basic string-matching tests
# will be defined here

@checks_strings
def str_hardcoded_bind_all_interfaces(context):
    if context.string_val == '0.0.0.0':
        return bandit.WARN, 'Possible binding to all interfaces'