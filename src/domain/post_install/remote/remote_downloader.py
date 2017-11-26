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
import requests
from src.domain.log.logger import Logger

class RemoteDownloader:
    def __init__(self, remote):
        """
        Default constructor
        :param remote: The remote to download
        :type remote: src.domain.remote
        """
        self.remote = remote
        
    def download(self):
        """
        Downloads the package from the repository
        :returns: The plain package json
        :rtype: object or list
        """
        return self.download_from_repo()
        
    def download_from_repo(self):
        """
        Downloads the package from the repository
        :returns: The plain package json
        :rtype: json
        """
        Logger.logger.info("Downloading remote '" + self.remote.name + "' from repository")
        url = self.remote.url
        response = requests.get(url)
        return response.json()
