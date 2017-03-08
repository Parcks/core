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
from src.domain.plugin import Plugin
from src.domain.parse.json_parsable import JSONParsable
from src.domain.parse.plugin_parser import PluginParser
from src.domain.parse.shell_parser import ShellParser

class PostInstallationParser(JSONParsable):
    def __init__(self, json_post_installation_array):
        """
        Default constructor

        :param json_plugins_array: A JSON-array containing all post-installation actions (plugin, commands)
        """
        super(PostInstallationParser, self).__init__(json_post_installation_array)


    def parse(self):
        """
        Parses the post-installation actions an creates a list of Plugins
        :returns: A list of :class:`src.domain.plugin.Plugin`s
        :rtype: list
        """
        plugin_list = []
        for plugin in self.json_object:
            plugin_object = self.load_post_installation_object(plugin)
            plugin_list.append(plugin_object)
        return plugin_list

    def load_post_installation_object(self, post_installation_json_object):
        if(post_installation_json_object["type"].upper()=="PLUGIN"):
            parser = PluginParser(post_installation_json_object)
            return parser.parse()
        elif(post_installation_json_object["type"].upper()=="SHELL"):
            parser = ShellParser(post_installation_json_object["cmds"])
            return parser.parse()