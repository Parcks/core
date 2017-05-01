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
from src.domain.plugin import Plugin
from src.domain.shell import Shell
from src.domain.shell_command import ShellCommand
from src.domain.post_install.plugin.plugin_validator import PluginValidator
from src.domain.post_install.plugin.plugin_installer import PluginInstaller
from src.domain.log.logger import Logger
import unittest
try:
    from unittest.mock import patch
except ImportError:
    from mock import patch

class TestPluginInstaller(unittest.TestCase):
    def setUp(self):
        self.plugin_installer_with_invalid_plugin = PluginInstaller(Plugin("dummy_plugin"))
        self.plugin_installer_with_plugin_that_needs_a_download = PluginInstaller(Plugin("dummy_plugin",  "http://www.example.com"))
        self.plugin_installer_with_plugin_that_does_not_need_a_download = PluginInstaller(Plugin("dummy_plugin",  shell=Shell([ShellCommand("pwd")])))
        Logger.disable_all()
        
    def tearDown(self):
        Logger.enable()
        
    @patch.object(PluginValidator,  'validate')
    def test_run_calls_validate_on_plugin_validator(self,  mock):
        self.plugin_installer_with_plugin_that_needs_a_download.run()
        self.assertTrue(mock.call_count > 0)
