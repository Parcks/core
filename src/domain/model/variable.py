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


class Variable:
    def __init__(self, name, description, value = None, default = None):
        """
        Default constructor
        :param name: The name of the variable
        :param description: The description or question to be displayed to the user
        :param value: The value of the variable (optional)
        :param default: The default value of the variable (optional)
        :type name: str
        :type description: str
        :type value: any
        :type default: any
        """
        self.name = name
        self.value = value
        self.default = default

    def is_question(self):
        """
        Checks if the variable value should be asked to the user
        :return: True if the variable is inputted by the user
        """
        return True if self.value is None else False
