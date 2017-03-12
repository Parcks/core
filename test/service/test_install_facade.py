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
from src.service.install_facade import InstallFacade
from src.domain.parse.installation_file_parser import InstallationFileParser
from src.domain.software_catalog import SoftwareCatalog
from src.domain.package import Package
import unittest, logging
try:
    from unittest.mock import patch, MagicMock
except ImportError:
    from mock import patch

class TestInstallFacade(unittest.TestCase):
    def setUp(self):
        self.facade = InstallFacade("file.parcks")
        logging.disable(logging.CRITICAL)

    def tearDown(self):
        logging.disable(logging.NOTSET)

    @patch.object(InstallationFileParser, 'parse')
    def test_parse_installation_file_calls_installation_file_parser(self, mock):
        self.facade.parse_installation_file()
        self.assertTrue(mock.called)

    @patch.object(Package, 'install')
    def test_install_calls_software_catalog_install_once_if_only_one_package(self, mocked_software_catalog_install_method):        
        package = Package("test")
        self.facade.software_catalog = SoftwareCatalog("test", [package])
        self.facade.install()
        self.assertEqual(1, mocked_software_catalog_install_method.call_count)