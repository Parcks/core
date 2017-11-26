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

from src.domain.model.installable import Installable


class ShellCommand(Installable):
    def __init__(self, commands, as_root=False, work_directory=None):
        """
        Default constructor
        :param commands: The commands to be executed
        :type commands: list of str
        :param as_root: Indicates if the shell command object should run as root
        :type as_root: bool
        :param work_directory: The directory where the commands should be executed
        :type work_directory: str
        """
        super(ShellCommand, self).__init__()
        self.asRoot = as_root
        self.commands = commands
        self.work_directory = work_directory

    def install(self):
        print("Shell Command installation")
