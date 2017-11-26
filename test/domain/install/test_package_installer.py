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

import unittest

from src.domain.install.package_installer import PackageInstaller
from src.domain.log.logger import Logger
from src.domain.model.package import Package
from src.exceptions.no_alternative_package_suitable_error import NoAlternativePackageSuitableError
from src.exceptions.package_installation_failure_error import PackageInstallationFailureError

try:
    from unittest.mock import patch
except ImportError:
    from mock import patch


class TestPackageInstaller(unittest.TestCase):
    def setUp(self):
        Logger.disable_all()
        self.create_package_with_alternatives()
        self.create_installer_without_alternatives()

    def tearDown(self):
        Logger.enable()

    def create_package_with_alternatives(self):
        self.package_with_alternatives = Package("fake-name", ["alternative1", "alternative2"])

    def create_installer_without_alternatives(self):
        self.package_without_alternatives = Package("fake-name")

    @patch('src.domain.distro.debian.debian_install_package_management_wrapper.DebianInstallPackageManagementWrapper')
    @patch.object(PackageInstaller, 'install_package_with_alternatives')
    def test_install_calls_install_package_with_alternatives_if_alternatives_provided(self, mock, mocked_wrapper):
        installer_with_alternatives = PackageInstaller(self.package_with_alternatives, mocked_wrapper)
        installer_with_alternatives.install()
        self.assertTrue(mock.called)

    @patch('src.domain.distro.debian.debian_install_package_management_wrapper.DebianInstallPackageManagementWrapper')
    @patch.object(PackageInstaller, 'try_package')
    def test_install_calls_try_package_if_no_alternatives(self, mock, mocked_wrapper):
        installer_without_alternatives = PackageInstaller(self.package_without_alternatives, mocked_wrapper)
        installer_without_alternatives.install()
        self.assertTrue(mock.called)

    @patch.object(PackageInstaller, 'try_package')
    @patch('src.domain.distro.debian.debian_install_package_management_wrapper.DebianInstallPackageManagementWrapper')
    @patch.object(PackageInstaller, 'try_alternatives')
    def test_install_package_with_alternatives_calls_try_alternatives_if_default_package_installation_failed(
            self, mock, mocked_wrapper, mocked_try_package):
        mocked_try_package.side_effect = PackageInstallationFailureError(self.package_with_alternatives.name)
        installer_with_alternatives = PackageInstaller(self.package_with_alternatives, mocked_wrapper)
        installer_with_alternatives.install_package_with_alternatives()
        self.assertTrue(mock.called)

    def test_try_package_calls_set_package_name_on_wrapper(self):
        with patch('src.domain.distro.debian.debian_install_package_management_wrapper.DebianInstallPackageManagementWrapper') as mock:
            installer_without_alternatives = PackageInstaller(self.package_without_alternatives, mock)
            installer_without_alternatives.try_package()
            mock.set_package_name.assert_called_with(self.package_without_alternatives.name)

    def test_try_package_calls_install_on_wrapper(self):
        with patch('src.domain.distro.debian.debian_install_package_management_wrapper.DebianInstallPackageManagementWrapper') as mock:
            installer_without_alternatives = PackageInstaller(self.package_without_alternatives, mock)
            installer_without_alternatives.try_package()
            mock.install.assert_called_with()

    def test_try_alternative_package_calls_set_package_name_on_wrapper(self):
        with patch('src.domain.distro.debian.debian_install_package_management_wrapper.DebianInstallPackageManagementWrapper') as mock:
            installer_without_alternatives = PackageInstaller(self.package_without_alternatives, mock)
            installer_without_alternatives.try_alternative_package("alternative1")
            mock.set_package_name.assert_called_with("alternative1")

    def test_try_alternative_package_calls_set_package_name_on_wrapper_with_alternative_name(self):
        with patch('src.domain.distro.debian.debian_install_package_management_wrapper.DebianInstallPackageManagementWrapper') as mock:
            installer_without_alternatives = PackageInstaller(self.package_without_alternatives, mock)
            installer_without_alternatives.try_alternative_package("alternative1")
            mock.set_package_name.assert_called_with("alternative1")

    def test_try_alternative_package_calls_install_on_wrapper(self):
        with patch('src.domain.distro.debian.debian_install_package_management_wrapper.DebianInstallPackageManagementWrapper') as mock:
            installer_without_alternatives = PackageInstaller(self.package_without_alternatives, mock)
            installer_without_alternatives.try_alternative_package("alternative1")
            mock.install.assert_called_with()

    def test_try_alternatives_raises_NoAlternativePackageSuitableError_if_all_alternatives_failed(self):
        with patch('src.domain.distro.debian.debian_install_package_management_wrapper.DebianInstallPackageManagementWrapper') as mock:
            mock.install.side_effect = PackageInstallationFailureError("fake alternative")
            installer_with_alternatives = PackageInstaller(self.package_with_alternatives, mock)
            with self.assertRaises(NoAlternativePackageSuitableError):
                installer_with_alternatives.try_alternatives()

    @patch.object(PackageInstaller, 'try_alternative_package')
    @patch('src.domain.distro.debian.debian_install_package_management_wrapper.DebianInstallPackageManagementWrapper')
    def test_try_alternatives_stops_at_first_success(self, mocked_wrapper, mocked_try_alternative_package):
        installer_with_alternatives = PackageInstaller(self.package_with_alternatives, mocked_wrapper)
        installer_with_alternatives.try_alternatives()
        self.assertEqual(1, mocked_try_alternative_package.call_count)