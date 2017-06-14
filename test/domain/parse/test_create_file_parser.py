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
import unittest, json
from src.domain.parse.create_file_parser import CreateFileParser
from src.exceptions.malformed_create_file_error import MalformedCreateFileError
from src.domain.log.logger import Logger

try:
    from unittest.mock import patch
except ImportError:
    from mock import patch


class TestRemoteParser(unittest.TestCase):
    def setUp(self):
        self.create_valid_create_file_json()
        self.create_invalid_create_file_json()
        Logger.disable_all()

    def tearDown(self):
        Logger.enable()

    def create_valid_create_file_json(self):
        JSON = """\
            {
		        "type":"file-create",
                "name":"dummy creator",
                "destination-path":"/tmp/xyz",
                "contents":"JValck"
            }
        """
        self.valid_create_file_JSON = json.loads(JSON)

    def create_invalid_create_file_json(self):
        JSON = """\
            {
                "type":"file-create",
                "name":"dummy creator"
            }
        """
        self.invalid_create_file_JSON = json.loads(JSON)

    def test_parse_returns_FileCreator(self):
        parser = CreateFileParser(self.valid_create_file_JSON)
        file_creator = parser.parse()
        self.assertEqual("dummy creator", file_creator.name)
        self.assertEqual("/tmp/xyz", file_creator.file_path)
        self.assertEqual("JValck", file_creator.contents)

    def test_parse_raises_malformed_remote_error_on_invalid_json(self):
        parser = CreateFileParser(self.invalid_create_file_JSON)
        with self.assertRaises(MalformedCreateFileError):
            parser.parse()

    def test_load_root_returns_false_if_no_root_attribute(self):
        parser = CreateFileParser(self.valid_create_file_JSON)
        result = parser.parse()
        self.assertFalse(result.as_root)