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

import unittest

from src.database.database_connection import DatabaseConnection
from src.database.variable_table_creator import VariableTableCreator
from src.domain.log.logger import Logger
try:
    from unittest.mock import patch
except ImportError:
    from mock import patch


class TestVariableTableCreator(unittest.TestCase):
    def setUp(self):
        Logger.disable_all()
        self.creator = VariableTableCreator()
        self.creator.open_connection()

    def tearDown(self):
        Logger.enable()
        self.creator.close_connection()

    @patch.object(DatabaseConnection, "execute_command")
    def test_create_table_calls_execute_command(self, execute_command):
        self.creator.create_table()
        self.assertTrue(execute_command.called)

    def test_create_table_creates_the_table(self):
        self.creator.create_table()
        self.creator.execute_command_keep_cursor_open("SELECT name FROM sqlite_master WHERE type=:type AND name=:name",
                                                      ("table", "variables",))
        table_name = (self.creator.cursor.fetchone())
        self.creator.close_cursor()
        self.assertEqual("variables", table_name[0])
