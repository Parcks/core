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

from src.domain.model.post_install.shell import Shell
from src.domain.model.post_install.shell_command import ShellCommand

from src.domain.log.logger import Logger
from src.domain.model.post_install.remote import Remote
from src.domain.post_install.remote.remote_downloader import RemoteDownloader
from src.domain.post_install.remote.remote_installer import RemoteInstaller
from src.domain.post_install.remote.remote_runner import RemoteRunner
from src.domain.post_install.remote.remote_validator import RemoteValidator

try:
    from unittest.mock import patch
except ImportError:
    from mock import patch
import sys


class TestRemoteInstaller(unittest.TestCase):
    def setUp(self):
        self.remote_installer_with_invalid_remote = RemoteInstaller(Remote("dummy_remote"))
        self.remote_installer_with_remote_that_needs_a_download = RemoteInstaller(Remote("dummy_remote", url="https://raw.githubusercontent.com/Parcks/plugins/master/testPlugin.ppl"))
        self.remote_installer_with_remote_that_does_not_need_a_download = RemoteInstaller(Remote("dummy_remote", shell=Shell([ShellCommand("pwd")])))
        self.remote_installer_unverified_remote_source = RemoteInstaller(Remote("dummy_remote", url="http://www.example.com"))
        self.saved_out = sys.stdout
        sys.stdout = open("/dev/null", "w")
        Logger.disable_all()
        
    def tearDown(self):
        Logger.enable()
        sys.stdout = self.saved_out
        
    @patch.object(RemoteRunner, 'run')
    @patch.object(RemoteValidator, 'validate')
    def test_run_calls_validate_on_remote_validator(self,  mock,  mocked_remote_runner_run_method):
        self.remote_installer_with_remote_that_needs_a_download.run()
        self.assertTrue(mock.call_count > 0)
        
    @patch.object(RemoteDownloader, 'download')
    def test_download_remote_but_keep_local_name_keeps_original_name(self,  mock):
        mock.return_value = Remote("dummy_remote") #mock the return value
        name_before_download = self.remote_installer_with_remote_that_needs_a_download.remote.name
        self.remote_installer_with_remote_that_needs_a_download.download_remote_but_keep_local_name()
        name_after_download = self.remote_installer_with_remote_that_needs_a_download.remote.name
        self.assertEqual(name_before_download,  name_after_download)
        
    @patch.object(RemoteDownloader, 'download')
    def test_download_remote_but_keep_local_name_updates_remote_runner(self,  mock):
        mock.return_value = Remote("dummy_remote") #mock the return value of the download method
        remote_runner_before_download = self.remote_installer_with_remote_that_needs_a_download.remote_runner
        self.remote_installer_with_remote_that_needs_a_download.download_remote_but_keep_local_name()
        self.assertNotEqual(remote_runner_before_download, self.remote_installer_with_remote_that_needs_a_download.remote_runner)

    @patch.object(RemoteValidator, 'is_download_required')
    def test_download_if_necessary_calls_is_download_required_on_validator(self, mock):
        self.remote_installer_with_remote_that_needs_a_download.download_if_necessary()
        self.assertEqual(1, mock.call_count)

    @patch.object(RemoteInstaller, 'ask_confirmation')
    @patch.object(RemoteValidator, 'is_external_download_url')
    def test_verify_url_calls_is_external_download_url_on_remote_validator_url_if_download_required(self, mock, mocked_input):
        self.remote_installer_unverified_remote_source.verify_url()
        self.assertEqual(1, mock.call_count)