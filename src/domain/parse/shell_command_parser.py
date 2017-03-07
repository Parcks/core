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
from src.domain.shell_command import ShellCommand
import json

class ShellCommandParser:
    def __init__(self, json_shell_command):
        """
        Default constructor
        :param json_shell_command:The json representation of the ShellCommand
        :type json_shell_command: json
        """
        self.json_shell_command = json_shell_command

    def parse_shell_command(self):
        """
        Converts the JSON representation to a ShellCommand object
        :returns: The ShellCommand object
        :rtype: src.domain.shell_command.ShellCommand
        """
        return ShellCommand(self.json_shell_command["do"], self.json_shell_command["root"])