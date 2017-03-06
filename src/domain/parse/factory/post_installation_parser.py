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

class PostInstallationParser:
    def __init__(self, json_post_installation_array):
        """
        Default constructor

        :param json_plugins_array: A JSON-array containing all post-installation actions (plugin, commands)
        """
        self.json_plugins_array = json_post_installation_array


    def parse_post_installation(self):
        plugin_list = []
        for plugin in self.json_plugins_array:
            plugin_object = self.load_post_installation_object(plugin)
            plugin_list.append(plugin_object)
        return plugin_list

    def load_post_installation_object(self, post_installation_json_object):
        print(post_installation_json_object)