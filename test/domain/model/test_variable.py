"""
Scriptable Packages Installer - Parcks
Copyright (C) 2017  JValck - Setarit

This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License
as published by the Free Software Foundation; either version 2
of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.

Setarit - parcks[at]setarit.com
"""
from __future__ import absolute_import

import unittest

from src.domain.log.logger import Logger
from src.domain.model.variable import Variable

try:
    from unittest.mock import patch
except ImportError:
    from mock import patch

class TestVariable(unittest.TestCase):
    def setUp(self):
        Logger.disable_all()
        self.create_variable_json()
        self.create_variable_json_as_question()

    def tearDown(self):
        Logger.enable()

    def create_variable_json(self):
        self.variable = Variable("name", "desc", 7)

    def create_variable_json_as_question(self):
        self.question_variable = Variable("name", "question")

    def test_is_question_returns_true_if_no_value_provided(self):
        self.assertTrue(self.question_variable.is_question())

    def test_is_question_returns_false_if_value_provided(self):
        self.assertFalse(self.variable.is_question())
