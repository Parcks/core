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
from abc import ABCMeta, abstractmethod
from os.path import expanduser

from src.domain.model.post_install.post_install_runnable import PostInstallRunnable


class FileHandle(PostInstallRunnable):
    def __init__(self, name, file_path, as_root=False):
        """
        Default constructor
        :param name: The name of the post-installation script that is displayed to the user
        :param file_path: The absolute path to the file
        :param as_root: The file should be handled as root
        :type name: str
        :type file_path: str
        :type as_root: bool
        """
        super(FileHandle, self).__init__(name)
        __metaclass__ = ABCMeta
        self.file_path = self._verify_path(file_path)
        self.as_root = as_root

    def _verify_path(self, file_path):
        """
        Checks if the path doesn't contain illegal characters
        :param file_path: The file path
        :type file_path: str
        :return: The path without illegal characters
        """
        verified_path = file_path
        if file_path.startswith("~"):
            verified_path = self._replace_home(file_path)
        return verified_path

    def _replace_home(self, file_path):
        """
        Replaces the home dir symbol with the path to the home dir
        :param file_path: The path with the homedir
        :return: The absolute path
        """
        return expanduser("~")+file_path[1:]

    @abstractmethod
    def run(self):
        pass
