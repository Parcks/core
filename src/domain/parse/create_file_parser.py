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

from src.domain.model.post_install.file_create import FileCreate
from src.domain.parse.json_parsable import JSONParsable
from src.exceptions.malformed_create_file_error import MalformedCreateFileError


class CreateFileParser(JSONParsable):
    def __init__(self, json_object):
        super(CreateFileParser, self).__init__(json_object)

    def parse(self):
        try:
            return FileCreate(
                self.json_object["name"],
                self.json_object["destination-path"],
                self.json_object["contents"],
                self.load_root()
            )
        except KeyError as error:
            raise MalformedCreateFileError("Missing "+str(error)+" field")

    def load_root(self):
        try:
            return self.json_object["root"]
        except KeyError:
            return False