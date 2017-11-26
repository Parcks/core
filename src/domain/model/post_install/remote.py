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

from src.domain.model.post_install.post_install_runnable import PostInstallRunnable
from src.domain.post_install.remote.remote_runner import RemoteRunner


class Remote(PostInstallRunnable):
    def __init__(self, name, url=None):
        """
        Default constructor
        
        :param name: The name of the post-installation script that is displayed to the user
        :param url: The url of the remote to be downloaded or None
        :type name: str
        :type url: str
        """
        super(Remote, self).__init__(name)
        self.url = url
        self.installer = RemoteRunner(self)

    def run(self):
        self.installer.run()
