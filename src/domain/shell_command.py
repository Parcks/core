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
from src.domain.installable import Installable

class ShellCommand(Installable):
    def __init__(self, commands, asRoot=False):
        """
        Default constructor
        :param commands: The commands to be executed
        :type commands: list of str
        :param asRoot: Indicates if the shell command object should run as root
        :type asRoot: bool
        """
        super().__init__(None)
        self.commands = commands

    def install(self):
        print("Shell Command installation")