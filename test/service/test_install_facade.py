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
from src.domain.distro.factory.install_package_management_wrapper_factory import InstallPackageManagementWrapperFactory
from src.domain.package import Package
from src.domain.software_catalog import SoftwareCatalog
from src.domain.distro.debian.debian_install_package_management_wrapper import DebianInstallPackageManagementWrapper
from src.domain.log.logger import Logger
import unittest
try:
    from unittest.mock import patch
except ImportError:
    from mock import patch

class TestInstallFacade(unittest.TestCase):
    def setUp(self):
        self.facade = InstallFacade("file.parcks")
        self.facade.distro_name = "debian"
        self.facade.software_catalog = self.create_software_catalog()
        Logger.disable_all()

    def tearDown(self):
        Logger.enable()
        
    def create_software_catalog(self):
        catalog = SoftwareCatalog("dummy",  [Package("git")])
        return catalog

    @patch.object(InstallationFileParser, 'parse')
    def test_parse_installation_file_calls_installation_file_parser(self, mock):
        self.facade.parse_installation_file()
        self.assertTrue(mock.called)

    @patch.object(InstallPackageManagementWrapperFactory, 'create')
    def test_create_install_package_management_wrapper_calls_factory_create(self, mocked_factory_create):
        self.facade.create_install_package_management_wrapper(Package("test"))
        self.assertTrue(mocked_factory_create.called)
        
    @patch.object(DebianInstallPackageManagementWrapper,  'install')
    @patch.object(Package,  'handle_post_installation')
    def test_install_calls_handle_post_installation_on_package(self,  mock,  mocked_install_method):
        self.facade.install()
        self.assertTrue(mock.call_count >= 1)
