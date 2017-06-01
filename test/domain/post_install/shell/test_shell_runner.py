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
from src.domain.shell import Shell
from src.domain.shell_command import ShellCommand
from src.domain.post_install.shell.shell_command_runnable_factory import ShellCommandRunnableFactory
from src.domain.post_install.shell.shell_runner import ShellRunner
import unittest
try:
    from unittest.mock import patch
except ImportError:
    from mock import patch
    
class TestShellRunner(unittest.TestCase):
    def setUp(self):
        self.shell = Shell([ShellCommand(["pwd"])])
        self.shell_runner = ShellRunner(self.shell)
        self.shell_multiple_commands = Shell([ShellCommand(["pwd"]), ShellCommand(["pwd"])])
        self.shell_runner_multiple_commands = ShellRunner(self.shell_multiple_commands)
        Logger.disable_all()
        
    def tearDown(self):
        Logger.enable()
        
    @patch.object(ShellRunner,  'execute_shell_command_runnable')
    @patch.object(ShellRunner,  'create_shell_command_runnable')
    def test_run_calls_create_shell_command_runnable_once_if_one_shell_command(self,  mock,  mocked_execute_method):
        self.shell_runner.run()
        self.assertEqual(mock.call_count,  1)
        
    @patch.object(ShellRunner,  'execute_shell_command_runnable')
    @patch.object(ShellRunner,  'create_shell_command_runnable')
    def test_run_calls_create_shell_command_runnable_twice_if_two_shell_commands(self,  mock,  mocked_execute_method):
        self.shell_runner_multiple_commands.run()
        self.assertEqual(mock.call_count,  2)
        
    @patch.object(ShellRunner,  'execute_shell_command_runnable')
    @patch.object(ShellRunner,  'create_shell_command_runnable')
    def test_run_calls_execute_shell_command_runnable_once_if_one_shell_command(self,  mock,  mocked_execute_method):
        self.shell_runner.run()
        self.assertEqual(mocked_execute_method.call_count,  1)
        
    @patch.object(ShellRunner,  'execute_shell_command_runnable')
    @patch.object(ShellRunner,  'create_shell_command_runnable')
    def test_run_calls_execute_shell_command_runnable_twice_if_two_shell_commands(self,  mock,  mocked_execute_method):
        self.shell_runner_multiple_commands.run()
        self.assertEqual(mocked_execute_method.call_count,  2)
      
    @patch.object(ShellCommandRunnableFactory,  'create')  
    def test_create_shell_command_runnable_calls_factory_to_create_shell_command_runnable(self,  mock):
        self.shell_runner.create_shell_command_runnable(self.shell.shell_commands[0])
        self.assertTrue(mock.called)
