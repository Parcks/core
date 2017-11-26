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
from src.domain.parse.parsable import Parsable
from abc import abstractmethod

class JSONParsable(Parsable):
    def __init__(self, json_object):
        super(JSONParsable, self).__init__()
        """
        Default constructor
        :param json_object: The JSON-object to parse
        :type json_object: json
        """
        self.json_object = json_object

    @abstractmethod
    def parse(self):
        pass