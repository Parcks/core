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
from src.domain.parse.file_append_parser import FileAppendParser
from src.exceptions.malformed_file_append_error import MalformedFileAppendError


class TestFileAppendParser(unittest.TestCase):
    def setUp(self):
        self.create_valid_append_file_json()
        self.create_invalid_append_file_json()
        Logger.disable_all()

    def tearDown(self):
        Logger.enable()

    def create_invalid_append_file_json(self):
        JSON = """\
            {
                "type":"file-append",
                "destination-path":"/tmp"
            }
        """
        self.invalid_json = json.loads(JSON)

    def create_valid_append_file_json(self):
        JSON = """\
            {
                "type":"file-append",
                "name":"Dummy append",
                "destination-path":"/tmp",
                "contents":"Dummy content"
            }
        """
        self.valid_json = json.loads(JSON)

    def test_parse_returns_FileAppend(self):
        parser = FileAppendParser(self.valid_json)
        result = parser.parse()
        self.assertEqual("Dummy append", result.name)
        self.assertEqual("/tmp", result.file_path)
        self.assertEqual("Dummy content", result.contents)

    def test_load_root_returns_false_if_no_root_attribute(self):
        parser = FileAppendParser(self.valid_json)
        result = parser.parse()
        self.assertFalse(result.as_root)

    def test_load_raises_MalformedFileAppendError_if_invalid_json(self):
        parser = FileAppendParser(self.invalid_json)
        with self.assertRaises(MalformedFileAppendError):
            parser.parse()

