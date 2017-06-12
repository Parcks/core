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

import unittest

from src.domain.log.logger import Logger
from src.domain.model.post_install.remote import Remote
from src.domain.post_install.remote.remote_downloader import RemoteDownloader

try:
    from unittest.mock import patch
except ImportError:
    from mock import patch

class TestRemoteDownloader(unittest.TestCase):
    TEST_REMOTE_URL = "https://raw.githubusercontent.com/Parcks/plugins/master/testPlugin.ppl"
    
    def setUp(self):
        self.remote = Remote("Dummy remote", TestRemoteDownloader.TEST_REMOTE_URL)
        self.remote_downloader = RemoteDownloader(self.remote)
        Logger.disable_all()
        
    def tearDown(self):
        Logger.enable()
        
    def test_download_from_repo_returns_dict_plugin(self):
        downloaded_json_plugin = self.remote_downloader.download_from_repo()
        self.assertTrue(type(downloaded_json_plugin) is dict)
        
    @patch.object(RemoteDownloader, 'parse')
    @patch.object(RemoteDownloader, 'download_from_repo')
    def test_download_calls_download_from_repo(self,  mock,  mocked_parse):
        self.remote_downloader.download()
        self.assertTrue(mock.call_count == 1)
        
    @patch.object(RemoteDownloader, 'parse')
    @patch.object(RemoteDownloader, 'download_from_repo')
    def test_download_calls_parse(self,  mock,  mocked_parse):
        self.remote_downloader.download()
        self.assertTrue(mocked_parse.call_count == 1)
