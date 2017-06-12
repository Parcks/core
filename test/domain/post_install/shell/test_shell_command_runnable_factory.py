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

from src.domain.model.post_install.shell_command import ShellCommand
from src.domain.post_install.shell.shell_command_runnable_factory import ShellCommandRunnableFactory


class TestShellCommandRunnableFactory(unittest.TestCase):
    def setUp(self):
        self.factory = ShellCommandRunnableFactory()
        self.shell_command_root = ShellCommand(["pwd"],  True)
        self.shell_command_non_root = ShellCommand(["pwd"])
        
    def test_create_creates_RootShellCommandRunnable_if_shell_command_requires_root(self):
        result = self.factory.create(self.shell_command_root)
        self.assertEqual("RootShellCommandRunner",  result.__class__.__name__)
        
    def test_create_creates_ShellCommandRunnable_if_shell_command_does_not_require_root(self):
        result = self.factory.create(self.shell_command_non_root)
        self.assertEqual("ShellCommandRunner",  result.__class__.__name__)
