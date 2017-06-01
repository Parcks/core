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
from src.domain.installable import Installable
from src.domain.post_install.plugin.plugin_installer import PluginInstaller

class Plugin(Installable):
    def __init__(self, name, url=None, shell=None):
        """
        Default constructor
        
        :param name: The name of the package
        :param url: The url of the plugin to be downloaded or None
        :param shell: The Shell object of the plugin or None if it has to be downloaded
        :type name: str
        :type url: str
        :type shell: src.domain.shell.Shell
        """
        super(Plugin, self).__init__(name)
        self.url = url
        self.shell = shell
        self.installer = PluginInstaller(self)

    def install(self):
        self.installer.run()
