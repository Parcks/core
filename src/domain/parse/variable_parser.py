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

from src.domain.model.variable import Variable
from src.domain.parse.json_parsable import JSONParsable


class VariableParser(JSONParsable):
    def __init__(self, json_variable_array):
        """
        Creates a variable parser
        :param json_variable_array: The json array containing the variables
        """
        super(VariableParser, self).__init__(json_variable_array)

    def parse(self):
        """
        Parses the variables from a json array
        :return: The variables in a list of :class:`src.domain.variable.Variable`
        :rtype: list of :class:`src.domain.variable.Variable`
        """
        variables = []
        for variable in self.json_object:
            variables.append(self.parse_variable(variable))
        return variables

    def parse_variable(self, json_variable):
        current_variable = Variable(json_variable["name"], description=json_variable["description"])
        if "value" in json_variable:
            current_variable.value = json_variable["value"]
        if "default" in json_variable:
            current_variable.default = json_variable["default"]
