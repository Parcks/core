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

from src.domain.parse.json_parsable import JSONParsable
from src.domain.model.post_install.file_append import FileAppend
from src.exceptions.malformed_file_append_error import MalformedFileAppendError


class FileAppendParser(JSONParsable):
    def __init__(self, json_object):
        super(FileAppendParser, self).__init__(json_object)

    def parse(self):
        try:
            return FileAppend(
                self.json_object["name"],
                self.json_object["destination-path"],
                self.json_object["contents"],
                self.load_root()
            )
        except KeyError as error:
            raise MalformedFileAppendError("Missing "+str(error)+" field")

    def load_root(self):
        try:
            return self.json_object["root"]
        except KeyError:
            return False
