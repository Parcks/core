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
from src.domain.post_install.plugin.plugin_downloader import PluginDownloader
from src.domain.plugin import Plugin
from src.domain.log.logger import Logger
import unittest
try:
    from unittest.mock import patch
except ImportError:
    from mock import patch

class TestPluginDownloader(unittest.TestCase):
    TEST_PLUGIN_URL = "https://raw.githubusercontent.com/Parcks/plugins/master/testPlugin.ppl"
    
    def setUp(self):
        self.plugin = Plugin("Dummy plugin", TestPluginDownloader.TEST_PLUGIN_URL)
        self.plugin_downloader = PluginDownloader(self.plugin)
        Logger.disable_all()
        
    def tearDown(self):
        Logger.enable()
        
    def test_download_from_repo_returns_dict_plugin(self):
        downloaded_json_plugin = self.plugin_downloader.download_from_repo()
        self.assertTrue(type(downloaded_json_plugin) is dict)
        
    @patch.object(PluginDownloader,  'parse')
    @patch.object(PluginDownloader,  'download_from_repo')
    def test_download_calls_download_from_repo(self,  mock,  mocked_parse):
        self.plugin_downloader.download()
        self.assertTrue(mock.call_count == 1)
        
    @patch.object(PluginDownloader,  'parse')
    @patch.object(PluginDownloader,  'download_from_repo')
    def test_download_calls_parse(self,  mock,  mocked_parse):
        self.plugin_downloader.download()
        self.assertTrue(mocked_parse.call_count == 1)
