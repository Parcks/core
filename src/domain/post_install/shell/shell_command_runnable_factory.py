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
from src.domain.post_install.shell.shell_command_runner import ShellCommandRunner
from src.domain.post_install.shell.root_shell_command_runner import RootShellCommandRunner

class ShellCommandRunnableFactory():
    def create(self, shell_command):
        """
        Creates the correct :class:`src.domain.shell_command.ShellCommand`
        :param shell_command: Indicates if the ShellCommand requires root privileges
        :type shell_command: :obj:`src.domain.shell_command.ShellCommand`
        :returns: The :class:`src.domain.post_install.shell.shell_command_runnable.ShellCommandRunnable` that will execute the ShellCommand
        :rtype: :obj:`src.domain.post_install.shell.shell_command_runnable.ShellCommandRunnable`
        """
        if(shell_command.asRoot):
            return RootShellCommandRunner(shell_command)
        else:
            return ShellCommandRunner(shell_command)
