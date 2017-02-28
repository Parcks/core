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
from domain.package import Package
from domain.parse.factory.plugin_factory import PluginFactory

class PackageFactory:
    def __init__(self, json_package_array):
        """
        Default constructor
        :param json_package_array: An JSON-array containing Package JSON-objects
        """
        self.json_package_array = json_package_array

    def load_packages(self):
        package_list = []
        for package in self.json_package_array:
            package_object = Package(package["package"])
            plugin_factory = PluginFactory(package["post-installation"])
            package_object.plugins = plugin_factory.load_plugins()
            package_list.append(package_object)
        return package_list
            
        