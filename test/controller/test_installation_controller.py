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
import unittest
from src.controller.installation_controller import InstallationController
from src.service.install_facade import InstallFacade
try:
    from unittest.mock import patch, MagicMock
except ImportError:
    from mock import patch

class TestInstallationController(unittest.TestCase):
    def setUp(self):
        self.controller = InstallationController("file.parcks")

    @patch.object(InstallFacade, 'install')
    @patch.object(InstallFacade, 'parse_installation_file')
    def test_run_calls_parse_installation_file_on_facade(self, mocked_parse_facade_method, mocked_install_method):
        self.controller.run()
        self.assertTrue(mocked_parse_facade_method.called)

    @patch.object(InstallFacade, 'install')
    @patch.object(InstallFacade, 'parse_installation_file')
    def test_run_calls_install_on_facade(self, mocked_parse_facade_method, mocked_install_method):
        self.controller.run()
        self.assertTrue(mocked_install_method.called)