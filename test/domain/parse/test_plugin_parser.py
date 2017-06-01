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

Setarit - parcks[at]setarit.com
"""
from __future__ import absolute_import
import unittest,json
from src.domain.parse.plugin_parser import PluginParser
from src.exceptions.malformed_plugin_error import MalformedPluginError
from src.domain.parse.shell_parser import ShellParser
from src.domain.log.logger import Logger
try:
    from unittest.mock import patch
except ImportError:
    from mock import patch

class TestPluginParser(unittest.TestCase):
    def setUp(self):
        self.create_valid_plugin_json()
        self.create_invalid_plugin_json()
        self.create_valid_plugin_json_with_commands()
        Logger.disable_all()
        
    def tearDown(self):
        Logger.enable()

    def create_valid_plugin_json(self):
        JSON = """\
            {
		"type":"plugin",
		"name":"composer",
		"url":"http://www.example.com"
            }
        """
        self.valid_plugin_JSON = json.loads(JSON)

    def create_invalid_plugin_json(self):
        JSON = """\
            {
		"type":"plugin",
		"name":"composer"
            }
        """
        self.invalid_plugin_JSON = json.loads(JSON)

    def create_valid_plugin_json_with_commands(self):
        JSON = """\
            {
		"type":"plugin",
		"name":"composer",
		"url":"http://www.example.com",
		"cmds":[{
                        "root":true,
                        "do":["whoami","ls -al"]
		    },{
                        "root":false,
			"do":["pwd"]
                    }
		]
            }
        """
        self.valid_plugin_JSON_with_commands = json.loads(JSON)

    def test_parse_returns_plugin(self):
        parser = PluginParser(self.valid_plugin_JSON)
        plugin = parser.parse()
        self.assertEqual("composer", plugin.name)
        self.assertEqual("http://www.example.com", plugin.url)
        self.assertEqual(None, plugin.shell)

    def test_parse_raises_malformed_plugin_error_on_invalid_json(self):
        parser = PluginParser(self.invalid_plugin_JSON)
        with self.assertRaises(MalformedPluginError):
            parser.parse()

    @patch.object(ShellParser, 'parse')
    def test_load_commands_calls_shell_parser_if_commands_provided(self, mock_shell_parser):
        parser = PluginParser(self.valid_plugin_JSON_with_commands)
        parser.load_commands()
        self.assertTrue(mock_shell_parser.called)
        
