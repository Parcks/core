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
from src.domain.log.logger import Logger
import tempfile, subprocess

from src.exceptions.file_creation_failed_error import FileCreationFailedError


class FileCreateRunner:
    def __init__(self, file_create):
        """
        Default constructor
        :param file_create: The FileCreator object to be executed
        :type file_create: :class:`src.domain.model.post_install.file_create.FileCreate`
        """
        self.file_create = file_create
        self.temp_file_location = None
        self.call_array = None

    def create_file(self):
        self._write_to_temp_file()
        self._create_call_array()
        if self.file_create.as_root:
            self._create_file_as_root()
        else:
            self._create_file_current_user()
        Logger.logger.info("File successfully created at " + self.file_create.file_path)

    def _create_file_as_root(self):
        call_array = ["sudo"]+self.call_array
        self._handle_result(subprocess.call(call_array))

    def _create_file_current_user(self):
        self._handle_result(subprocess.call(self.call_array))

    def _handle_result(self, result_code):
        """
        Handles the result of the move to the destination-path
        :param result_code: The result code
        :raises: FileCreationFailedError if the file could not be moved
        """
        if result_code != 0:
            raise FileCreationFailedError("Could not move the file to " + self.file_create.file_path)

    def _write_to_temp_file(self):
        """
        Writes the contents of the FileCreator to a temporary file
        Sets the self.temp_file_location variable
        """
        temp_file = tempfile.NamedTemporaryFile(mode='w', delete=False)
        self.temp_file_location = temp_file.name
        Logger.logger.debug("Writing to temporary file: "+self.temp_file_location)
        temp_file.write(self.file_create.contents)
        temp_file.close()

    def _create_call_array(self):
        call_array_as_str = "mv "+self.temp_file_location+" "+self.file_create.file_path
        self.call_array = call_array_as_str.split(" ")
