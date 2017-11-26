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

import unittest

from src.domain.log.logger import Logger
from src.domain.model.post_install.shell_command import ShellCommand
from src.domain.post_install.shell.shell_command_runnable import ShellCommandRunnable
from src.domain.post_install.shell.shell_command_runner import ShellCommandRunner

try:
    from unittest.mock import patch
except ImportError:
    from mock import patch

class TestShellCommandRunner(unittest.TestCase):
    def setUp(self):
        Logger.disable_all()
        self.runner = ShellCommandRunner(ShellCommand(["pwd"]))
        self.runner_multiple = ShellCommandRunner(ShellCommand(["pwd",  "pwd"]))
        
    def tearDown(self):
        Logger.enable()
        
    @patch('subprocess.Popen')
    @patch.object(ShellCommandRunnable, 'create_executable_command_array')
    def test_run_calls_create_executable_command_array_once_if_one_command(self,  mock,  subprocess_mock):
        self.runner.run()
        self.assertEqual(1,  mock.call_count)
        
    @patch('subprocess.Popen')
    @patch.object(ShellCommandRunnable, 'create_executable_command_array')
    def test_run_calls_create_executable_command_array_twice_if_two_commands(self,  mock,  subprocess_mock):
        self.runner_multiple.run()
        self.assertEqual(2,  mock.call_count)
        
    @patch('subprocess.Popen')
    @patch.object(ShellCommandRunnable, 'handle_result')
    def test_run_calls_handle_result_once_if_one_command(self,  mock,  subprocess_mock):
        self.runner.run()
        self.assertEqual(1,  mock.call_count)
        
    @patch('subprocess.Popen')
    @patch.object(ShellCommandRunnable, 'handle_result')
    def test_run_calls_handle_result_twice_if_two_commands(self,  mock,  subprocess_mock):
        self.runner_multiple.run()
        self.assertEqual(2,  mock.call_count)
