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
from src.domain.log.logger import Logger
import tempfile, subprocess

class FileCreatorRunner:
    def __init__(self, file_creator):
        """
        Default constructor
        :param file_creator: The FileCreator object to be executed
        :type file_creator: :class:`src.domain.model.post_install.file_creator.FileCreator`
        """
        self.file_creator = file_creator
        self.temp_file_location = None
        self.call_array = None

    def create_file(self):
        self._write_to_temp_file()
        self._create_call_array()
        if self.file_creator.as_root:
            self._create_file_as_root()
        else:
            self._create_file_current_user()
        Logger.logger.info("File successfully created at "+self.file_creator.file_path)

    def _create_file_as_root(self):
        call_array = ["sudo"]+self.call_array
        subprocess.call(call_array)

    def _create_file_current_user(self):
        subprocess.call(self.call_array)

    def _write_to_temp_file(self):
        """
        Writes the contents of the FileCreator to a temporary file
        Sets the self.temp_file_location variable
        """
        temp_file = tempfile.NamedTemporaryFile(mode='w', delete=False)
        self.temp_file_location = temp_file.name
        Logger.logger.debug("Writing to temporary file: "+self.temp_file_location)
        temp_file.write(self.file_creator.contents)
        temp_file.close()

    def _create_call_array(self):
        call_array_as_str = "mv "+self.temp_file_location+" "+self.file_creator.file_path
        self.call_array = call_array_as_str.split(" ")
