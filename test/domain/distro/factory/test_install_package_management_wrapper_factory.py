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

from src.domain.distro.factory.install_package_management_wrapper_factory import InstallPackageManagementWrapperFactory
from src.domain.log.logger import Logger
from src.exceptions.unsupported_distro_name_error import UnsupportedDistroNameError


class TestInstallPackageManagementWrapperFactory(unittest.TestCase):
    def setUp(self):
        self.factory = InstallPackageManagementWrapperFactory()
        Logger.disable_all()
        
    def tearDown(self):
        Logger.enable()
    
    def test_create_returns_correct_implementation(self):
        wrapper = self.factory.create("debian")
        self.assertEqual("DebianInstallPackageManagementWrapper", wrapper.__class__.__name__)

    def test_create_raises_exception_on_unknown_distro_name(self):
        with self.assertRaises(UnsupportedDistroNameError):
            self.factory.create("fictiveDistro")
