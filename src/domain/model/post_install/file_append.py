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

from src.domain.model.post_install.file_handle import FileHandle
from src.domain.post_install.file.file_append_runner import FileAppendRunner


class FileAppend(FileHandle):
    def __init__(self, name, file_path, contents, as_root=False):
        """
        Default constructor
        :param name: The name of the post-installation script that is displayed to the user
        :param file_path: The absolute path to the file
        :param contents: Contents to be appended to the file
        :param as_root: The file should be created as root
        :type name: str
        :type file_path: str
        :type contents: str
        :type as_root: bool
        """
        super(FileAppend, self).__init__(name, file_path, as_root)
        self.contents = contents

    def run(self):
        runner = FileAppendRunner(self)
        runner.append_to_file()
