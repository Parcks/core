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
from src.controller.startup_controller import StartupController
from src.controller.installation_controller import InstallationController
import unittest, sys, os
try:
    from unittest.mock import patch, MagicMock
except ImportError:
    from mock import patch

class TestStarupController(unittest.TestCase):
    def setUp(self):
        self.controller = StartupController("-i file.parcks".split())
        self.out = open(os.devnull, 'w')
        sys.stdout = self.out ##disable print

    def tearDown(self):
        self.out.close()

    @patch.object(StartupController, 'parse_arguments')
    @patch.object(StartupController, 'boot_install_controller')
    def test_run_calls_parse_arguments(self, mocked_parse_arguments, mocked_boot_install_controller):
        controller = StartupController("-i f.parcks".split())
        controller.run()
        self.assertTrue(mocked_parse_arguments.called)

    @patch.object(StartupController, 'parse_arguments')
    @patch.object(StartupController, 'boot_install_controller')
    def test_run_calls_boot_install_controller(self, mocked_parse_arguments, mocked_boot_install_controller):
        controller = StartupController("-i f.parcks".split())
        controller.run()
        self.assertTrue(mocked_boot_install_controller.called)

    def test_parse_arguments_returns_input_file(self):
        file = self.controller.parse_arguments()
        self.assertEqual("file.parcks", file)

    @patch.object(InstallationController, 'run')
    def test_boot_installation_controller_calls_run_from_install_controller(self, mocked_run_from_install_controller):
        self.controller.boot_install_controller("file.parcks")
        self.assertTrue(mocked_run_from_install_controller.called)