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
from src.domain.distro.debian.debian_install_package_management_wrapper import DebianInstallPackageManagementWrapper
from src.domain.distro.install_package_management_wrapper import InstallPackageManagementWrapper
from src.domain.log.logger import Logger
import unittest
from src.exceptions.package_installation_failure_error import PackageInstallationFailureError
try:
    from unittest.mock import patch
except ImportError:
    from mock import patch

class TestDebianInstallPackageManagementWrapper(unittest.TestCase):
    def setUp(self):
        Logger.disable_all()
        self.wrapper = DebianInstallPackageManagementWrapper()
        self.wrapper.set_package_name("test")

    def tearDown(self):
        Logger.enable()

    @patch.object(InstallPackageManagementWrapper, 'handle_result')
    @patch('subprocess.call')    
    def test_install_calls_subprocess(self, mocked_call_method, mocked_handle_result):
        self.wrapper.install()
        self.assertTrue(mocked_call_method.called)

    def test_handle_result_raises_PackageInstallationFailureError_on_installation_failure(self):
        with self.assertRaises(PackageInstallationFailureError):
            self.wrapper.handle_result(1)

    def test_set_package_name_updates_package_name(self):
        self.wrapper.set_package_name("name")
        self.assertEqual("name", self.wrapper.package_name)