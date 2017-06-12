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

from src.domain.log.logger import Logger
from src.domain.model.post_install.post_install_runnable import PostInstallRunnable
from src.domain.model.post_install.remote import Remote

from src.service.post_installation_facade import PostInstallationFacade
import unittest
try:
    from unittest.mock import patch
except ImportError:
    from mock import patch


class TestPostInstallationFacade(unittest.TestCase):
    def setUp(self):
        self.create_facade()
        Logger.disable_all()

    def tearDown(self):
        Logger.enable()

    def create_facade(self):
        self.facade_under_test = PostInstallationFacade([
            Remote("Dummy", "http://example.com"),
            Remote("Dummy", "http://example.com")
        ])

    @patch.object(PostInstallRunnable, 'run')
    def test_handle_post_installation_calls_run_on_PostInstallRunnable(self, mock):
        self.facade_under_test.handle_post_installation()
        self.assertEqual(2, mock.call_count)