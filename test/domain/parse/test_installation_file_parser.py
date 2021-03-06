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
import unittest, shutil, tempfile
from os import path
from src.domain.log.logger import Logger
from src.exceptions.invalid_installation_file_extension_error import InvalidInstallationFileExtensionError
import json
from src.domain.parse.installation_file_parser import InstallationFileParser
try:
    FileNotFoundError
except NameError:
    FileNotFoundError = IOError
try:
    from unittest.mock import patch
except ImportError:
    from mock import patch

class TestInstallationFileParser(unittest.TestCase):
    def setUp(self):
        self.testDir = tempfile.mkdtemp()
        self.tempFile = self.create_test_install_file()
        self.invalidTempFile = self.create_invalid_test_install_file()
        self.invalid_extension_file = self.create_invalid_file_extension_install_file()
        Logger.disable_all()

    def tearDown(self):
        shutil.rmtree(self.testDir)
        Logger.enable()

    def create_test_install_file(self):
        jsonData = self.create_valid_json()
        tempJsonPath = path.join(self.testDir,"test.parcks")
        with open(tempJsonPath ,'w') as ofile:
            json.dump(jsonData, ofile)
        return tempJsonPath

    def create_valid_json(self):
        JSON = """\
        {
	"name":"PHP installer",
	"install": [
		{"package": "php",
		"post-installation": []
		}
            ]
        }
        """
        return json.loads(JSON)

    def create_invalid_test_install_file(self):
        JSON = """\
        {
	"name":"PHP installer"
        }
        """
        jsonData = json.loads(JSON)
        tempJsonPath = path.join(self.testDir,"invalidTest.parcks")
        with open(tempJsonPath ,'w') as ofile:
            json.dump(jsonData, ofile)
        return tempJsonPath
        
    def create_invalid_file_extension_install_file(self):
        jsonData = self.create_valid_json()
        tempJsonPath = path.join(self.testDir,"invalid_extension.json")
        with open(tempJsonPath ,'w') as ofile:
            json.dump(jsonData, ofile)
        return tempJsonPath

    def test_parse_returns_software_catalog_on_valid_installation_file(self):
        parser = InstallationFileParser(self.tempFile)
        self.assertNotEqual(None, parser.parse())

    def test_parse_raises_file_not_found_error_on_non_existing_file(self):
        parser = InstallationFileParser("fakeFile.parcks")
        with self.assertRaises(FileNotFoundError):
            parser.parse()        

    def test_parse_raises_key_error_on_invalid_install_file(self):
        parser = InstallationFileParser(self.invalidTempFile)
        with self.assertRaises(KeyError):
            parser.parse()

    def test_parse_sets_correct_software_catalog_name(self):
        parser = InstallationFileParser(self.tempFile)
        catalog = parser.parse()
        self.assertEqual("PHP installer", catalog.name)
        
    def test_validate_file_extension_raises_InvalidInstallationFileExtensionError_if_no_valid_extension(self):
        parser = InstallationFileParser(self.invalid_extension_file)
        with self.assertRaises(InvalidInstallationFileExtensionError):
            parser.validate_file_extension()
            
    @patch.object(InstallationFileParser,  'validate_file_extension')
    def test_parse_calls_validate_file_extension(self,  mock):
       parser = InstallationFileParser(self.tempFile)
       parser.parse()
       self.assertEqual(1,  mock.call_count)
        
