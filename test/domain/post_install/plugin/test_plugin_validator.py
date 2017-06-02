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
from src.domain.post_install.plugin.plugin_validator import PluginValidator
from src.exceptions.malformed_plugin_error import MalformedPluginError
from src.domain.log.logger import Logger
import unittest


# the validation of the plugin format is done by src.domain.parse.plugin_parser. This code is not tested in this testcase
class TestPluginValidator(unittest.TestCase):
    def setUp(self):
        self.create_plugin_that_requires_download()
        self.create_plugin_that_requires_download_official_repo()
        self.create_plugin_no_download_required()
        self.create_invalid_plugin()
        Logger.disable_all()
        
    def tearDown(self):
        Logger.enable()
        
    def create_plugin_that_requires_download(self):
        self.plugin_download = Plugin("Dummy plugin", "http://example.com")
        
    def create_plugin_that_requires_download_official_repo(self):
        self.plugin_download_official_repo = Plugin("Dummy plugin", "https://raw.githubusercontent.com/Parcks/plugins/master/testPlugin.ppl")
        
    def create_plugin_no_download_required(self):
        dummy_shell = Shell(["pwd"])
        self.plugin_no_download = Plugin("Dummy plugin", shell=dummy_shell)
        
    def create_invalid_plugin(self):
        self.invalid_plugin = Plugin("Dummy plugin")
        
    def test_is_download_required_returns_true_if_no_shell_provided(self):
        plugin_validator = PluginValidator(self.plugin_download)
        plugin_validator.validate()
        self.assertEqual(plugin_validator.is_download_required(),  True)
        
    def test_is_download_required_returns_false_if_shell_provided(self):
        plugin_validator = PluginValidator(self.plugin_no_download)
        plugin_validator.validate()
        self.assertEqual(plugin_validator.is_download_required(),  False)
        
    def test_validate_raises_MalformedPluginError_on_invalid_plugin(self):
        plugin_validator = PluginValidator(self.invalid_plugin)
        self.assertRaises(MalformedPluginError,  plugin_validator.validate)
        
    def test_is_external_download_url_returns_true_if_non_official_url(self):
        plugin_validator = PluginValidator(self.plugin_download)
        plugin_validator.validate()
        self.assertTrue(plugin_validator.is_external_download_url())
        
    def test_is_external_download_url_retruns_true_if_official_url(self):
        plugin_validator = PluginValidator(self.plugin_download_official_repo)
        plugin_validator.validate()
        self.assertFalse(plugin_validator.is_external_download_url())
