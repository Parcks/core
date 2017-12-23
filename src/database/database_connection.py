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
import sqlite3


class DatabaseConnection(object):

    def __init__(self):
        self.connection = None
        self.cursor = None

    def open_connection(self):
        self.connection = sqlite3.connect(':memory:')

    def open_cursor_to_connection(self):
        """
        Opens a the cursor to the connection
        """
        self.cursor = self.connection.cursor()

    def close_connection(self):
        """
        Closes the current connection to the database
        """
        self.connection.close()

    def close_cursor(self):
        self.cursor.close()

    def execute_command(self, command, parameters = ()):
        """
        Executes a command on the database
        :param command: The command to execute
        :param parameters: optional parameters
        :type command: str
        :type parameters: tuple
        """
        self.execute_command_keep_cursor_open(command, parameters)
        self.close_cursor()

    def execute_command_keep_cursor_open(self, command, parameters = ()):
        """
        Executes a command on the database but keeps the cursor open
        :param command: The command to execute
        :param parameters: optional parameters
        :type command: str
        :type parameters: tuple
        """
        self.open_cursor_to_connection()
        self.cursor.execute(command, parameters)
        self.connection.commit()
