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
from src.domain.log.logger import Logger
from src.domain.plugin import Plugin
from src.domain.shell import Shell
from src.domain.shell_command import ShellCommand
from src.domain.post_install.plugin.plugin_runner import PluginRunner
from src.domain.post_install.shell.shell_runner import ShellRunner
import unittest
try:
    from unittest.mock import patch
except ImportError:
    from mock import patch

class TestPluginRunner(unittest.TestCase):    
    def setUp(self):
        self.plugin = Plugin("dummy_plugin",  shell=Shell([ShellCommand(["pwd"])]))
        self.plugin_runner = PluginRunner(self.plugin)
        self.plugin_multiple_commands = Plugin("Dummy Plugin",  shell = Shell([ShellCommand(["pwd"]),  ShellCommand(["pwd"])]))
        self.plugin_runner_multiple_commands = PluginRunner(self.plugin_multiple_commands)
        Logger.disable_all()
        
    def tearDown(self):
        Logger.enable()
        
    def test_constructor_sets_plugin(self):
        self.assertEqual(self.plugin_runner.plugin,  self.plugin)
        
    @patch.object(ShellRunner,  'run')
    def test_run_calls_shell_runner_once(self,  mocked_run_method):
        self.plugin_runner.run()
        self.assertEqual(mocked_run_method.call_count,  1)
        
    @patch.object(ShellRunner,  'run')
    def test_run_calls_shell_runner_once_if_multiple_shell_commands(self,  mocked_run_method):
        self.plugin_runner_multiple_commands.run()
        self.assertEqual(mocked_run_method.call_count,  1)      
