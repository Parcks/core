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
from src.exceptions.malformed_plugin_error import MalformedPluginError

class PluginValidator:
    def __init__(self,  plugin):
        """
        Default constructor
        :param plugin: The plugin to validate
        :type plugin: src.domain.plugin
        """
        self.plugin = plugin
        self.require_download = False
        
    def validate(self):
        """
        Validates the plugin.
        :raises MalformedPluginError: If there is no url nor a shell object provided
        """
        if(self.plugin.shell is None):
            self.require_download = True
        if(self.plugin.shell is None and self.plugin.url is None):
            raise MalformedPluginError("No url and commands provided")
        
    def is_download_required(self):
        """
        Getter
        :returns: True if the plugin needs to be downloaded
        :rtype: bool
        """
        return self.require_download
