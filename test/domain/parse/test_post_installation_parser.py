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
from src.domain.parse.post_installation_parser import PostInstallationParser
from src.domain.parse.remote_parser import RemoteParser
from src.domain.parse.shell_parser import ShellParser
from src.domain.log.logger import Logger
try:
    from unittest.mock import patch
except ImportError:
    from mock import patch

class TestPostInstallationParser(unittest.TestCase):
    def setUp(self):
        self.create_valid_json()
        self.parser = PostInstallationParser(self.validJSON)
        Logger.disable_all()
        
    def tearDown(self):
        Logger.enable()

    def create_valid_json(self):
        JSON = """\
        [
	    {
		"type":"remote",
		"name":"composer",
		"url":"http://www.example.com"
            },
            {
                "type":"shell",
		"cmds":[
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
	]
        """
        self.validJSON = json.loads(JSON)

    @patch.object(RemoteParser, 'parse')
    @patch.object(ShellParser, 'parse')
    def test_load_post_installation_object_calls_right_parser(self, mocked_shell_parser, mocked_remote_parser):
        self.parser.parse()
        self.assertEqual(1, mocked_remote_parser.call_count)
        self.assertEqual(1, mocked_shell_parser.call_count)

    @patch.object(PostInstallationParser, 'load_post_installation_object')
    def test_parse_post_installation_calls_load_post_installation_object_twice_if_two_remotes(self, mocked_parser):
        self.parser.parse()
        self.assertEqual(2, mocked_parser.call_count)
        
