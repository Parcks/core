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
from src.domain.installable import Installable

class Shell(Installable):
    def __init__(self, shell_commands):
        """
        Default constructor
        :param shell_commands: The shell commands to be executed
        :type shell_commands: list of :class:`src.domain.shell_command.ShellCommand`
        """
        super(Shell, self).__init__()
        self.shell_commands = shell_commands

    def install(self):
        print("shell")