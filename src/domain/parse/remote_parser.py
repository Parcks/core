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

import src.domain.model.post_install.remote
from src.domain.parse.json_parsable import JSONParsable
from src.exceptions.malformed_remote_error import MalformedRemoteError


class RemoteParser(JSONParsable):
    def __init__(self, json_object):
        """
        Default constructor
        :param json_object: The JSON representation of the remote
        :type json_object: json
        """
        super(RemoteParser, self).__init__(json_object)

    def parse(self):
        """
        Loads the remote object from the JSON representation
        :returns: The loaded Plugin object
        :rtype: src.domain.remote.Remote
        :raises MalformedPluginError: If there is no url nor commands provided
        """
        name = self.load_name()
        url = self.load_url()
        if self.no_url_provided(url):
            raise MalformedRemoteError("No url provided")
        return src.domain.model.post_install.remote.Remote(name, url)
      
    def load_name(self):  
        """
        Reads the name (if any) of the remote form the JSON-object
        :returns: The name of the remote
        :rtype: str
        """
        try:
            return self.json_object["name"]
        except KeyError:
            return "Anonymous remote"

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

    def no_url_provided(self, url):
        return url is None
