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
from src.domain.parse.json_parsable import JSONParsable
from src.domain.plugin import Plugin
from src.domain.parse.shell_parser import ShellParser
from src.exceptions.malformed_plugin_error import MalformedPluginError

class PluginParser(JSONParsable):
    def __init__(self, json_object):
        """
        Default constructor
        :param json_object: The JSON representation of the plugin
        :type json_object: json
        """
        super(PluginParser, self).__init__(json_object)

    def parse(self):
        """
        Loads the plugin object from the JSON representation
        :returns: The loaded Plugin object
        :rtype: src.domain.plugin.Plugin
        :raises MalformedPluginError: If there is no url nor commands provided
        """
        name = self.json_object["name"]
        url = self.load_url()
        commands = self.load_commands()
        if self.no_url_and_commands_provided(url, commands):
            raise MalformedPluginError("No url and commands provided")
        return Plugin(name, url, commands)
        

    def load_url(self):
        """
        Reads the url from the JSON-object
        :returns: The url from the JSON-object or None if no url provided
        :rtype: str
        """
        try:
            return self.json_object["url"]
        except KeyError:
            return None

    def load_commands(self):
        """
        Loads the commands for the plugin
        Uses :func:`src.domain.parse.shell_parser.ShellParser.load_shell`

        :returns: The :class:`src.domain.shell.Shell` object
            or None if no shell available
        :rtype: src.domain.shell.Shell
        """
        try:
            shell_parser = ShellParser(self.json_object["cmds"])            
            return shell_parser.parse()
        except KeyError:
            return None

    def no_url_and_commands_provided(self, url, commands):
        return url == None and commands == None
