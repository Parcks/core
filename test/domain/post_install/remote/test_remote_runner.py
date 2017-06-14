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
from src.domain.model.post_install.shell import Shell
from src.domain.model.post_install.shell_command import ShellCommand
from src.domain.post_install.remote.remote_downloader import RemoteDownloader
from src.domain.post_install.remote.remote_runner import RemoteRunner
from src.domain.post_install.remote.remote_validator import RemoteValidator
from src.service.post_installation_facade import PostInstallationFacade

try:
    from unittest.mock import patch
except ImportError:
    from mock import patch
import sys


class TestRemoteRunner(unittest.TestCase):
    def setUp(self):
        self.remote_runner_with_remote_verified_source = RemoteRunner(Remote("dummy_remote", url="https://raw.githubusercontent.com/Parcks/plugins/master/testPlugin.ppl"))
        self.remote_runner_unverified_remote_source = RemoteRunner(Remote("dummy_remote", url="http://www.example.com"))
        self.saved_out = sys.stdout
        sys.stdout = open("/dev/null", "w")
        Logger.disable_all()
        
    def tearDown(self):
        Logger.enable()
        sys.stdout = self.saved_out

    @patch.object(RemoteRunner, '_boot_post_installation_facade')
    @patch.object(RemoteDownloader, 'download')
    @patch.object(RemoteValidator, 'validate')
    def test_run_calls_validate_on_remote_validator(self,  mock,  mocked_remote_downloader_download, mocked_boot_facade):
        self.remote_runner_with_remote_verified_source.run()
        self.assertTrue(mock.call_count > 0)

    @patch.object(RemoteRunner, '_boot_post_installation_facade')
    @patch.object(RemoteRunner, '_download')
    def test_run_calls_download(self, mocked_download, mocked_facade):
        self.remote_runner_with_remote_verified_source.run()
        self.assertTrue(mocked_download.called)
        
    @patch.object(RemoteDownloader, 'download')
    def test_download_remote_from_repository_calls_download_on_remote_downloader(self,  mock):
        self.remote_runner_with_remote_verified_source._download_remote_from_repository()
        self.assertTrue(mock.call_count == 1)

    @patch.object(RemoteRunner, '_ask_confirmation')
    @patch.object(RemoteValidator, 'is_external_download_url')
    def test_verify_url_calls_is_external_download_url_on_remote_validator_url_if_download_required(self, mock, mocked_input):
        self.remote_runner_unverified_remote_source._verify_url()
        self.assertEqual(1, mock.call_count)

    @patch.object(RemoteRunner, '_download')
    @patch.object(RemoteRunner, '_boot_post_installation_facade')
    def test_run_calls__boot_post_installation_facade(self, mock, mock_download):
        self.remote_runner_with_remote_verified_source.run()
        self.assertTrue(mock.called)
        self.assertEqual(1, mock.call_count)
