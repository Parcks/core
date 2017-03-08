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
import unittest,json
from src.domain.parse.package_parser import PackageParser

class TestPackageParser(unittest.TestCase):
    def setUp(self):
        self.create_valid_json()
        self.create_valid_multiple_json()
        self.create_valid_no_packages_json()        

    def create_valid_json(self):
        JSON = """\
        [
	    {"package": "php",
	    "post-installation": []
            }
        ]
        """
        self.validJSON = json.loads(JSON)

    def create_valid_multiple_json(self):
        JSON = """\
        [
	    {"package": "php",
	    "post-installation": []
            },
	    {"package": "git",
	    "post-installation": []
	    }
        ]        
        """
        self.validMultiplePackages = json.loads(JSON)

    def create_valid_no_packages_json(self):
        JSON = """\
        []        
        """
        self.validNoPackages = json.loads(JSON)

    def test_parse_loads_correct_packages(self):
        parser = PackageParser(self.validMultiplePackages)
        packages = parser.parse()
        self.assertEqual("php", packages[0].name)
        self.assertEqual("git", packages[1].name)

    def test_parse_returns_one_package_if_one_package_provided(self):
        parser = PackageParser(self.validJSON)
        packages = parser.parse()
        self.assertEqual(1, len(packages))

    def test_parse_returns_two_packages_if_two_packages_provided(self):
        parser = PackageParser(self.validMultiplePackages)
        packages = parser.parse()
        self.assertEqual(2, len(packages))

    def test_parse_returns_empty_list_if_no_packages_provided(self):
        parser = PackageParser(self.validNoPackages)
        packages = parser.parse()
        self.assertEqual(0, len(packages))
