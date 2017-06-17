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
import shutil
import os
import subprocess
from src.helper.file_permission_reader import FilePermissionReader


class FileAppendRunner:
    def __init__(self, file_append):
        """
        Default constructor
        :param file_append: The model containing the info for the runner
        :type file_append: :class:`src.domain.model.post_install.file_append.FileAppend`
        """
        self.file_append = file_append
        self.saved_permissions = None
        self.temp_file_path = None

    def append_to_file(self):
        """
        Appends the content to an existing file
        """
        self._store_old_permissions()
        self._copy_file_to_writable_temp()
        self._append_new_contents()
        self._move_temp_to_destination()
        self._restore_permissions()

    def _store_old_permissions(self):
        self.saved_permissions = FilePermissionReader(self.file_append.file_path)

    def _copy_file_to_writable_temp(self):
        """
        Copies the file to temp and make it writable
        """
        self.temp_file_path = shutil.copy2(self.file_append.file_path, '/tmp')
        if self.temp_file_path is None:  #python2.7
            self.temp_file_path = '/tmp/'+os.path.basename(self.file_append.file_path)
        os.chown(self.temp_file_path, os.getuid(), os.getgid())  # make writable

    def _append_new_contents(self):
        contents_to_append = self._prepend_newline_if_none_at_beginning_of_contents()
        with open(self.temp_file_path, 'a') as f:
            f.write(contents_to_append)

    def _prepend_newline_if_none_at_beginning_of_contents(self):
        """
        Adds the newline character to front of the contents to append
        :return: The corrected new contents
        :rtype: str
        """
        if self.file_append.contents.startswith(os.linesep):
            contents_to_append = self.file_append.contents
        else:
            contents_to_append = os.linesep + self.file_append.contents
        return contents_to_append

    def _move_temp_to_destination(self):
        if self.file_append.as_root:
            self._move_as_root()
        else:
            self._move_as_current()

    def _move_as_root(self):
        call_array = ["sudo", "mv", self.temp_file_path, self.file_append.file_path]
        subprocess.call(call_array)

    def _move_as_current(self):
        call_array = ["mv", self.temp_file_path, self.file_append.file_path]
        subprocess.call(call_array)

    def _restore_permissions(self):
        owner_cmd = ["sudo", "python", "-c"]+["\"import os; os.chown("+str(self.saved_permissions.uid)+","+str(self.saved_permissions.gid)+")\""]
        mode_cmd = ["sudo", "python", "-c"]+["\"import os; os.chmod("+str(self.saved_permissions.mode)+")\""]

        subprocess.call(owner_cmd)
        subprocess.call(mode_cmd)
