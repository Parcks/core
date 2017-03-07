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
from src.domain.parse.shell_command_parser import ShellCommandParser
from src.domain.shell import Shell
import json

class ShellParser:
    def __init__(self, shell_json):
        """
        Default constructor
        :param shell_json: Contains the ShellCommands as JSON-array
        :type shell_json: list of json objects
        """
        self.shell_json = shell_json

    def load_shell(self):
        shell_commands_list = []
        for json_command in self.shell_json:
            parser = ShellCommandParser(json_command)
            shell_commands_list.append(parser.parse_shell_command())
        return shell_commands_list