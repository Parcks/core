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

from src.domain.model.package import Package
from src.domain.parse.json_parsable import JSONParsable
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
            package_object.post_installation_runnables = self.boot_installation_parser(package)
            package_object.alternative_names = self.fetch_alternative_names(package)
            package_list.append(package_object)
        return package_list

    def boot_installation_parser(self, package_json):
        """
        Fires the :class:`src.domain.parse.post_installation_parser.PostInstallationParser` to parse
        the remotes to be executed after the installation of the package
        :param package_json: The json containing the package
        :type package_json: json
        :returns: list of remotes or an empty list if no post-installation key provided
        """
        try:
            post_installation_parser = PostInstallationParser(package_json["post-installation"])
            return post_installation_parser.parse()
        except KeyError:
            return []

    def fetch_alternative_names(self, package_json):
        """
        Will add alternative package names (if any) to the package object
        :param package_json: The json containing the package
        :type package_json: json
        :returns: list of alternative package names
        """
        try:
            return package_json["alternative-names"]
        except KeyError:
            return None