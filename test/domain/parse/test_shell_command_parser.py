"""
Environment Packages Installer
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

Setarit - support[at]setarit.com
"""
from __future__ import absolute_import
import unittest, json
from src.domain.parse.shell_command_parser import ShellCommandParser

class TestShellCommandParser(unittest.TestCase):
    def setUp(self):
        self.create_valid_json()
        self.create_invalid_json()

    def create_valid_json(self):
        JSON = """\
        {
            "root":true,
            "do":["whoami","ls -al"]
	}
        """
        self.valid_json = json.loads(JSON)

    def create_invalid_json(self):
        JSON = """\
        {
            "do":["whoami","ls -al"]
	}
        """
        self.invalid_json = json.loads(JSON)

    def test_parse_returns_shell_command(self):
        parser = ShellCommandParser(self.valid_json)
        shell_command = parser.parse()
        self.assertTrue(shell_command.asRoot)
        self.assertTrue(self.check_list_equal(["whoami","ls -al"], shell_command.commands))

    def test_parse_raises_key_error_if_invalid_json(self):
        parser = ShellCommandParser(self.invalid_json)
        with self.assertRaises(KeyError):
            parser.parse()

    def check_list_equal(self, listOne, listTwo):
        return len(listOne) == len(listTwo) and sorted(listOne) == sorted(listTwo)