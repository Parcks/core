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

from src.domain.log.logger import Logger
from src.domain.model.post_install.remote import Remote
from src.domain.post_install.remote.remote_validator import RemoteValidator
from src.exceptions.malformed_remote_error import MalformedRemoteError


# the validation of the remote format is done by src.domain.parse.remote_parser. This code is not tested in this testcase
class TestRemoteValidator(unittest.TestCase):
    def setUp(self):
        self.create_remote_that_requires_download()
        self.create_remote_that_requires_download_official_repo()
        self.create_remote_no_download_required()
        self.create_invalid_remote()
        Logger.disable_all()
        
    def tearDown(self):
        Logger.enable()
        
    def create_remote_that_requires_download(self):
        self.remote_download = Remote("Dummy remote", "http://example.com")
        
    def create_remote_that_requires_download_official_repo(self):
        self.remote_download_official_repo = Remote("Dummy remote", "https://raw.githubusercontent.com/Parcks/plugins/master/testPlugin.ppl")
        
    def create_remote_no_download_required(self):
        dummy_shell = Shell(["pwd"])
        self.remote_no_download = Remote("Dummy remote", shell=dummy_shell)
        
    def create_invalid_remote(self):
        self.invalid_remote = Remote("Dummy remote")
        
    def test_is_download_required_returns_true_if_no_shell_provided(self):
        remote_validator = RemoteValidator(self.remote_download)
        remote_validator.validate()
        self.assertEqual(remote_validator.is_download_required(),  True)
        
    def test_is_download_required_returns_false_if_shell_provided(self):
        remote_validator = RemoteValidator(self.remote_no_download)
        remote_validator.validate()
        self.assertEqual(remote_validator.is_download_required(),  False)
        
    def test_validate_raises_MalformedPluginError_on_invalid_remote(self):
        remote_validator = RemoteValidator(self.invalid_remote)
        self.assertRaises(MalformedRemoteError, remote_validator.validate)
        
    def test_is_external_download_url_returns_true_if_non_official_url(self):
        remote_validator = RemoteValidator(self.remote_download)
        remote_validator.validate()
        self.assertTrue(remote_validator.is_external_download_url())
        
    def test_is_external_download_url_retruns_true_if_official_url(self):
        remote_validator = RemoteValidator(self.remote_download_official_repo)
        remote_validator.validate()
        self.assertFalse(remote_validator.is_external_download_url())
