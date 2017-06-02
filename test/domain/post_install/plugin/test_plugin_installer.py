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
from src.domain.plugin import Plugin
from src.domain.shell import Shell
from src.domain.shell_command import ShellCommand
from src.domain.post_install.plugin.plugin_validator import PluginValidator
from src.domain.post_install.plugin.plugin_installer import PluginInstaller
from src.domain.post_install.plugin.plugin_runner import PluginRunner
from src.domain.log.logger import Logger
from src.domain.post_install.plugin.plugin_downloader import PluginDownloader
import unittest
try:
    from unittest.mock import patch
except ImportError:
    from mock import patch
import sys


class TestPluginInstaller(unittest.TestCase):
    def setUp(self):
        self.plugin_installer_with_invalid_plugin = PluginInstaller(Plugin("dummy_plugin"))
        self.plugin_installer_with_plugin_that_needs_a_download = PluginInstaller(Plugin("dummy_plugin", url="https://raw.githubusercontent.com/Parcks/plugins/master/testPlugin.ppl"))
        self.plugin_installer_with_plugin_that_does_not_need_a_download = PluginInstaller(Plugin("dummy_plugin",  shell=Shell([ShellCommand("pwd")])))
        self.plugin_installer_unverified_plugin_source = PluginInstaller(Plugin("dummy_plugin", url="http://www.example.com"))
        self.saved_out = sys.stdout
        sys.stdout = open("/dev/null", "w")
        Logger.disable_all()
        
    def tearDown(self):
        Logger.enable()
        sys.stdout = self.saved_out
        
    @patch.object(PluginRunner,  'run')
    @patch.object(PluginValidator,  'validate')
    def test_run_calls_validate_on_plugin_validator(self,  mock,  mocked_plugin_runner_run_method):
        self.plugin_installer_with_plugin_that_needs_a_download.run()
        self.assertTrue(mock.call_count > 0)
        
    @patch.object(PluginDownloader,  'download')
    def test_download_plugin_but_keep_local_name_keeps_original_name(self,  mock):
        mock.return_value = Plugin("dummy_plugin") #mock the return value
        name_before_download = self.plugin_installer_with_plugin_that_needs_a_download.plugin.name
        self.plugin_installer_with_plugin_that_needs_a_download.download_plugin_but_keep_local_name()
        name_after_download = self.plugin_installer_with_plugin_that_needs_a_download.plugin.name
        self.assertEqual(name_before_download,  name_after_download)
        
    @patch.object(PluginDownloader,  'download')
    def test_download_plugin_but_keep_local_name_updates_plugin_runner(self,  mock):
        mock.return_value = Plugin("dummy_plugin") #mock the return value of the download method
        plugin_runner_before_download = self.plugin_installer_with_plugin_that_needs_a_download.plugin_runner
        self.plugin_installer_with_plugin_that_needs_a_download.download_plugin_but_keep_local_name()
        self.assertNotEqual(plugin_runner_before_download,  self.plugin_installer_with_plugin_that_needs_a_download.plugin_runner)

    @patch.object(PluginValidator, 'is_download_required')
    def test_download_if_necessary_calls_is_download_required_on_validator(self, mock):
        self.plugin_installer_with_plugin_that_needs_a_download.download_if_necessary()
        self.assertEqual(1, mock.call_count)

    @patch.object(PluginInstaller, 'ask_confirmation')
    @patch.object(PluginValidator, 'is_external_download_url')
    def test_verify_url_calls_is_external_download_url_on_plugin_validator_url_if_download_required(self, mock, mocked_input):
        self.plugin_installer_unverified_plugin_source.verify_url()
        self.assertEqual(1, mock.call_count)