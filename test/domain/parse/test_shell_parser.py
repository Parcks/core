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
from src.domain.model.post_install.shell_command import ShellCommand
from src.domain.parse.shell_command_parser import ShellCommandParser
from src.domain.parse.shell_parser import ShellParser

try:
    from unittest.mock import patch
except ImportError:
    from mock import patch

class TestShellParser(unittest.TestCase):
    def setUp(self):
        self.create_valid_shell_json_two()
        self.create_valid_shell_json_one()
        self.create_valid_shell_json_zero()
        Logger.disable_all()
        
    def tearDown(self):
        Logger.enable()

    def create_valid_shell_json_two(self):
        JSON = """\
        {
            "name":"dummy",
            "type":"shell",
            "cmds":
                [
                    {
                "root":true,
                "do":["whoami","ls -al"]
                    },
                    {   
                "root":false,
                "do":["pwd"]
                    }
            ]
        }
        """
        self.valid_two_JSON = json.loads(JSON)

    def create_valid_shell_json_one(self):
        JSON = """\
        {
            "name":"dummy",
            "type":"shell",
            "cmds":
                [
                    {
                "root":true,
                "do":["whoami","ls -al"]
                    }
            ]
        }
        """
        self.valid_one_JSON = json.loads(JSON)

    def create_valid_shell_json_zero(self):
        JSON = """\
        {
            "name":"dummy",
            "type":"shell",
            "cmds":[]
        }
        """
        self.valid_zero_JSON = json.loads(JSON)

    @patch.object(ShellCommandParser, 'parse')
    def test_parse_calls_shell_command_parser_parse_twice_if_two_commands(self, mock):
        parser = ShellParser(self.valid_two_JSON)
        parser.parse()
        self.assertEqual(2, mock.call_count)

    @patch.object(ShellCommandParser, 'parse')
    def test_parse_calls_shell_command_parser_parse_once_if_one_commands(self, mock):
        parser = ShellParser(self.valid_one_JSON)
        parser.parse()
        self.assertEqual(1, mock.call_count)

    @patch.object(ShellCommandParser, 'parse')
    def test_parse_calls_shell_command_parser_parse_never_if_no_commands(self, mock):
        parser = ShellParser(self.valid_zero_JSON)
        parser.parse()
        self.assertEqual(0, mock.call_count)

    def test_parse_returns_shell_object(self):
        parser = ShellParser(self.valid_two_JSON)
        shell_object = parser.parse()
        self.assertEqual(2, len(shell_object.shell_commands))
        self.assertTrue(type(shell_object.shell_commands[0]) is ShellCommand)
