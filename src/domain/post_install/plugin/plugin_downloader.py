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
from src.domain.parse.plugin_parser import PluginParser
import requests
from src.domain.log.logger import Logger

class PluginDownloader:
    def __init__(self,  plugin):
        """
        Default constructor
        :param plugin: The plugin to download
        :type plugin: src.domain.plugin
        """
        self.plugin = plugin
        
    def download(self):
        """
        Downloads the package from the repository
        :returns: The downloaded package
        :rtype: src.domain.plugin.Plugin
        """
        package_json = self.download_from_repo()
        return self.parse(package_json)
        
    def download_from_repo(self):
        """
        Downloads the package from the repository
        :returns: The plain package json
        :rtype: json
        """
        Logger.logger.info("Downloading plugin "+self.plugin.name+" from repository")
        url = self.plugin.url
        response = requests.get(url)
        return response.json()
        
    def parse(self,  package_json):
        """
        Parses the plain package_json
        Uses :class:`src.domain.parse.plugin_parser.PluginParser`
        :returns: The downloaded package
        :rtype: src.domain.plugin.Plugin
        """
        parser = PluginParser(package_json)
        return parser.parse()
