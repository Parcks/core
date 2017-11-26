"""
Scriptable Packages Installer - Parcks
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

import json

from src.domain.log.logger import Logger
from src.domain.model.post_install.shell import Shell
from src.domain.model.post_install.shell_command import ShellCommand

from src.service.post_installation_facade import PostInstallationFacade
import unittest
try:
    from unittest.mock import patch
except ImportError:
    from mock import patch


class TestPostInstallationFacade(unittest.TestCase):
    def setUp(self):
        self.create_facade()
        self.create_json_object()
        self.create_json_array()
        Logger.disable_all()

    def tearDown(self):
        Logger.enable()

    def create_facade(self):
        self.facade_under_test = PostInstallationFacade([
            Shell("Dummy", [ShellCommand(["ls"])]),
            Shell("Dummy", [ShellCommand(["ls"])])
        ])

    def create_json_object(self):
        Json = """\
        {
            "type":"shell",
            "name":"Dummy",
            "cmds":[
                {
                    "do":["ls"],
                    "root":false
                }
            ]
        }
        """
        self.json_object = json.loads(Json)

    def create_json_array(self):
        Json = """\
        [
            {
                "type":"shell",
                "name":"Dummy",
                "cmds":[
                    {
                        "do":["ls"],
                        "root":false
                    }
                ]
            },
            {
                "type":"shell",
                "name":"Dummy",
                "cmds":[
                    {
                        "do":["ls"],
                        "root":false
                    }
                ]
            }
        ]
        """
        self.json_list = json.loads(Json)

    @patch.object(Shell, 'run')
    def test_handle_post_installation_calls_run_on_PostInstallRunnable(self, mock):
        self.facade_under_test.handle_post_installation()
        self.assertEqual(2, mock.call_count)

    def test_from_json_creates_facade_with_list_if_json_list(self):
        facade = PostInstallationFacade.from_json(self.json_list)
        self.assertTrue(isinstance(facade.post_install_runnables, list))

    def test_from_json_creates_facade_with_list_if_json_object(self):
        facade = PostInstallationFacade.from_json(self.json_object)
        self.assertTrue(isinstance(facade.post_install_runnables, list))

    @patch.object(Shell, 'run')
    def test_handle_post_installalation_calls_run_on_PostInstallRunnable_if_one_object(self, mock):
        facade = PostInstallationFacade.from_json(self.json_object)
        facade.handle_post_installation()
        self.assertEqual(1, mock.call_count)