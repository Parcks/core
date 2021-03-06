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

from src.domain.model.post_install.shell_command import ShellCommand
from src.domain.parse.json_parsable import JSONParsable


#import json

class ShellCommandParser(JSONParsable):
    def __init__(self, json_shell_command):
        """
        Default constructor
        :param json_shell_command:The json representation of the ShellCommand
        :type json_shell_command: json
        """
        super(ShellCommandParser, self).__init__(json_shell_command)

    def parse(self):
        """
        Converts the JSON representation to a ShellCommand object
        :returns: The ShellCommand object
        :rtype: src.domain.shell_command.ShellCommand
        """
        return ShellCommand(self.json_object["do"], self.json_object["root"],  self.load_working_directory())
        
    def load_working_directory(self):
        try:
            return self.json_object["work-dir"]
        except KeyError:
            return None
