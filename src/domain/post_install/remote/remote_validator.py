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
from src.exceptions.malformed_remote_error import MalformedRemoteError

"""
Checks if the remote requires a download
"""
class RemoteValidator:
    def __init__(self, remote):
        """
        Default constructor
        :param remote: The remote to validate
        :type remote: src.domain.remote
        """
        self.remote = remote
        self.external_download_url = False
        
    def validate(self):
        """
        Validates the remote.
        :raises MalformedPluginError: If there is no url  provided
        """
        if(self.remote.url is None):
            raise MalformedRemoteError("No url provided")
        if(not self.remote.url.startswith("https://raw.githubusercontent.com/Parcks/plugins/")):
            self.external_download_url = True

    def is_external_download_url(self):
        """
        Getter
        :returns: True if the download url is not from the official repo
        :rtype: bool
        """
        return self.external_download_url
