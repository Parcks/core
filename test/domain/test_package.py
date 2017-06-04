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
from src.domain.log.logger import Logger
from src.domain.package import Package
from src.domain.plugin import Plugin
import unittest
try:
    from unittest.mock import patch
except ImportError:
    from mock import patch

class TestPackage(unittest.TestCase):
    def setUp(self):
        Logger.disable_all()
        self.create_package_with_post_install()
        self.create_package_without_post_install()

    def tearDown(self):
        Logger.enable()

    def create_package_with_post_install(self):
        self.package_with_post_install = Package("php", [Plugin("dummy"), Plugin("other dummy")])

    def create_package_without_post_install(self):
        self.package_without_post_install = Package("php")

    @patch.object(Plugin, 'install')
    def test_handle_post_installation_calls_install_on_plugin_if_plugin_provided(self, mocked_install):
        self.package_with_post_install.handle_post_installation()
        self.assertEqual(2, mocked_install.call_count)

    @patch.object(Plugin, 'install')
    def test_handle_post_installation_does_no_call_install_on_plugin_if_no_plugins_provided(self, mocked_install):
        self.package_without_post_install.handle_post_installation()
        self.assertFalse(mocked_install.called)