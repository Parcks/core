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

class Package(Installable):
    def __init__(self, name, plugins = None):
        """
        Default constructor
        
        :param name: The name of the package
        :param plugins: An array containing all the plugins. Can be none
        """
        super(Package, self).__init__(name)

    def install(self):
        print("install package")
        
    def handle_post_installation(self):
        for plugin in self.plugins:
            plugin.install()
