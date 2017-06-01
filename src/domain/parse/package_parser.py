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

Setarit - parcks[at]setarit.com
"""
from __future__ import absolute_import
from src.domain.parse.json_parsable import JSONParsable
from src.domain.package import Package
from src.domain.parse.post_installation_parser import PostInstallationParser

class PackageParser(JSONParsable):
    def __init__(self, json_package_array):
        """
        Default constructor
        :param json_package_array: An JSON-array containing Package JSON-objects
        """
        super(PackageParser, self).__init__(json_package_array)

    def parse(self):
        """
        Loads the packages from the JSON-array
        :returns: A list of packages or an empty list if no packages specified
        :rtype: list of Package
        """
        package_list = []
        for package in self.json_object:
            package_object = Package(package["package"])
            post_installation_parser = PostInstallationParser(package["post-installation"])
            package_object.plugins = post_installation_parser.parse()
            package_list.append(package_object)
        return package_list
