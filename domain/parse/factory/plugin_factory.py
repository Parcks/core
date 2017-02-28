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
from domain.plugin import Plugin

class PluginFactory:
    def __init__(self, json_plugins_array):
        """
        Default constructor

        :param json_plugins_array: A JSON-array containing all the Plugins as JSON-objects
        """
        self.json_plugins_array = json_plugins_array


    def load_plugins(self):
        plugin_list = []
        for plugin in self.json_plugins_array:
            plugin_object = Plugin(plugin["name"], plugin["commands"])
            plugin_list.append(plugin_object)
        return plugin_list