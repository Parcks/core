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
from src.domain.parse.file_create_parser import FileCreateParser
from src.domain.log.logger import Logger
from src.exceptions.unknown_post_installation_object_error import UnknownPostInstallationObjectError
try:
    from unittest.mock import patch
except ImportError:
    from mock import patch


class TestPostInstallationParser(unittest.TestCase):
    def setUp(self):
        self.create_valid_json()
        self.create_unknown_type_json()
        self.create_file_json()
        self.create_valid_file_append_json()
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

    def create_unknown_type_json(self):
        JSON = """\
            [
        	    {
                    "type":"unknown-type"
                }
        	]
        """
        self.unknown_type_json = json.loads(JSON)

    def create_file_json(self):
        JSON = """\
            [
                {
                    "type":"file-create",
                    "name":"dummy create",
                    "destination-path":"/tmp/dummy",
                    "contents":"dummy",
                    "root":false
                }
            ]
        """
        self.file_json = json.loads(JSON)

    def create_valid_file_append_json(self):
        JSON = """\
        [
            {
                "type":"file-append",
                "name":"Dummy append",
                "destination-path":"/tmp",
                "contents":"Dummy content"
            }
        ]
        """
        self.file_append_json = json.loads(JSON)

    @patch.object(RemoteParser, 'parse')
    @patch.object(ShellParser, 'parse')
    def test_load_post_installation_object_calls_right_parser(self, mocked_shell_parser, mocked_remote_parser):
        self.parser.parse()
        self.assertEqual(1, mocked_remote_parser.call_count)
        self.assertEqual(1, mocked_shell_parser.call_count)

    @patch.object(PostInstallationParser, 'load_post_installation_object')
    def test_parse_post_installation_calls_load_post_installation_object_twice_if_two_post_installation_objects(self, mocked_parser):
        self.parser.parse()
        self.assertEqual(2, mocked_parser.call_count)
        
    def test_load_post_installation_object_raises_UnknownPostInstallationObjectError_if_unknown_type(self):
        parser = PostInstallationParser(self.unknown_type_json)
        with self.assertRaises(UnknownPostInstallationObjectError):
            parser.parse()

    @patch.object(FileCreateParser, 'parse')
    def test_load_post_installation_object_calls_parse_on_CreateFileParser_if_type_fileCreate(self, mock):
        parser = PostInstallationParser(self.file_json)
        parser.parse()
        self.assertTrue(mock.called)


    def test_load_post_installation_loads_correct_type(self):
        parser = PostInstallationParser(self.file_json)
        result = parser.parse()
        self.assertEqual("FileCreate", result[0].__class__.__name__)

    def test_load_post_installation_loads_FileAppendParser_if_type_file_append(self):
        parser = PostInstallationParser(self.file_append_json)
        result = parser.parse()
        self.assertEqual("FileAppend", result[0].__class__.__name__)
