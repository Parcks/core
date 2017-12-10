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

import json
import unittest

from src.domain.log.logger import Logger
from src.domain.parse.variable_parser import VariableParser
from src.exceptions.malformed_variable_error import MalformedVariableError

try:
    from unittest.mock import patch
except ImportError:
    from mock import patch


class TestVariableParser(unittest.TestCase):
    def setUp(self):
        Logger.disable_all()
        self._create_empty_json_array()
        self._create_invalid_variable_json_without_description()
        self._create_json_array_with_two_variables()
        self._create_question_variable_json()
        self._create_variable_json_with_value()
        self._create_invalid_variable_json_without_name()

    def tearDown(self):
        Logger.enable()

    def _create_empty_json_array(self):
        JSON = """\
        []
        """
        self.emptyJson = json.loads(JSON)

    def _create_json_array_with_two_variables(self):
        JSON = """\
        [
            {
                "name":"test",
                "description": "td",
                "value":0
            },
            {
                "name":"test2",
                "description": "td",
                "value":"st"
            }
        ]
        """
        self.two_json = json.loads(JSON)

    def _create_invalid_variable_json_without_name(self):
        JSON = """\
            {
                "description":"desc"
            }
        """
        self.json_without_name = json.loads(JSON)

    def _create_invalid_variable_json_without_description(self):
        JSON = """\
            {
                "name":"name"
            }
        """
        self.json_without_description = json.loads(JSON)

    def _create_question_variable_json(self):
        JSON = """\
            {
                "name":"name",
                "description":"question?",
                "default":true
            }
        """
        self.json_question_variable = json.loads(JSON)

    def _create_variable_json_with_value(self):
        JSON = """\
            {
                "name":"name",
                "description":"var",
                "value":"master"
            }
        """
        self.json_variable = json.loads(JSON)

    def test_parse_returns_empty_list_if_json_list_empty(self):
        parser = VariableParser(self.emptyJson)
        result = parser.parse()
        self.assertEqual(0, len(result))

    def test_parse_returns_list_with_two_variables_if_two_provided(self):
        parser = VariableParser(self.two_json)
        self.assertEqual(2, len(parser.parse()))

    def test_parse_variable_returns_malformed_variable_error_if_no_name_provided(self):
        parser = VariableParser("")
        with self.assertRaises(MalformedVariableError):
            parser.parse_variable(self.json_without_name)

    def test_parse_variable_returns_malformed_variable_error_if_no_description_provided(self):
        parser = VariableParser("")
        with self.assertRaises(MalformedVariableError):
            parser.parse_variable(self.json_without_description)

    def test_parse_variable_creates_question_variable_if_no_value_provided(self):
        parser = VariableParser("")
        var = parser.parse_variable(self.json_question_variable)
        self.assertTrue(var.is_question())

    def test_parse_variable_creates_variable_with_value_if_value_provided(self):
        parser = VariableParser("")
        var = parser.parse_variable(self.json_variable)
        self.assertEqual("master", var.value)

    def test_parse_variable_returns_Variable_object(self):
        parser = VariableParser("")
        var = parser.parse_variable(self.json_variable)
        self.assertEqual("Variable", var.__class__.__name__)
