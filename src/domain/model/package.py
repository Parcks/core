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

from src.domain.model.installable import Installable


class Package(Installable):
    def __init__(self, name, alternative_names=None, post_installation_runnables=[]):
        """
        Default constructor
        
        :param name: The name of the package
        :type name: str
        :param alternative_names: List of possible fallback/alternative package names
        :type alternative_names: list
        :param post_installation_runnables: An array containing all the PostInstallationRunnable's. Can be none
        :type post_installation_runnables: list
        """
        super(Package, self).__init__(name)
        self.post_installation_runnables = post_installation_runnables
        self.alternative_names = alternative_names

    def install(self):
        print("install package")
        
    def handle_post_installation(self):
        for post_installation_runnable in self.post_installation_runnables:
            post_installation_runnable.install()
