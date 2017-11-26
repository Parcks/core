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
import os

from src.domain.log.logger import Logger
from src.helper.file_permission_reader import FilePermissionReader


class TestFilePermissionReader(unittest.TestCase):
    def setUp(self):
        self.test_file = "/tmp/test_file_permission_reader"
        self.create_file_to_test()
        Logger.disable_all()

    def tearDown(self):
        Logger.enable()
        os.remove(self.test_file)

    def create_file_to_test(self):
        with open(self.test_file, 'w') as file:
            file.write("Dummy content")

    def test_fetches_permission_from_file(self):
        reader = FilePermissionReader(self.test_file)
        self.assertFalse(reader.mode is None)

    def test_fetches_gid_from_file(self):
        reader = FilePermissionReader(self.test_file)
        self.assertFalse(reader.gid is None)

    def test_fetches_uid_from_file(self):
        reader = FilePermissionReader(self.test_file)
        self.assertFalse(reader.uid is None)