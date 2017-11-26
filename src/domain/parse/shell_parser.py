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

from src.domain.model.post_install.shell import Shell
from src.domain.parse.json_parsable import JSONParsable
from src.domain.parse.shell_command_parser import ShellCommandParser


class ShellParser(JSONParsable):
    def __init__(self, shell_json):
        """
        Default constructor
        :param shell_json: Contains the ShellCommands as JSON-array
        :type shell_json: list of json objects
        """
        super(ShellParser, self).__init__(shell_json)

    def parse(self):
        """
        Parses the JSON representation of the Shell
        :returns: The Shell object
        :rtype: src.domain.shell.Shell
        """
        shell_commands_list = []
        for json_command in self.json_object["cmds"]:
            parser = ShellCommandParser(json_command)
            shell_commands_list.append(parser.parse())
        return Shell(self.json_object["name"] , shell_commands_list)
