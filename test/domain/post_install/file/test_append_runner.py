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
import unittest
import os
import getpass
from src.domain.log.logger import Logger
from src.domain.model.post_install.file_append import FileAppend
from src.domain.post_install.file.file_append_runner import FileAppendRunner

try:
    from unittest.mock import patch
except ImportError:
    from mock import patch

class TestAppendRunner(unittest.TestCase):
    FILE_CONTENTS = ["First line", "Second line"]
    def setUp(self):
        Logger.disable_all()
        self.test_file = self.create_test_file()
        self.file_append = FileAppend("Dummy append", self.test_file, "appended")
        self.file_append_runner = FileAppendRunner(self.file_append)

    def tearDown(self):
        Logger.enable()
        os.remove(self.test_file)
        if os.path.isfile("/tmp/test_file_append"):
            os.remove("/tmp/test_file_append")

    def create_test_file(self):
        with open("/home/"+getpass.getuser()+"/test_file_append", 'w') as file:
            file.write(TestAppendRunner.FILE_CONTENTS[0]+os.linesep)
            file.write(TestAppendRunner.FILE_CONTENTS[1]+os.linesep)
        return "/home/"+getpass.getuser()+"/test_file_append"

    @patch.object(FileAppendRunner, '_restore_permissions')
    @patch.object(FileAppendRunner, '_move_temp_to_destination')
    @patch.object(FileAppendRunner, '_append_new_contents')
    @patch.object(FileAppendRunner, '_copy_file_to_writable_temp')
    @patch.object(FileAppendRunner, '_store_old_permissions')
    def test_append_to_file_calls_all_steps(self, mock, mock2, mock3, mock4, mock5):
        self.file_append_runner.append_to_file()
        self.assertTrue(mock.called)
        self.assertTrue(mock2.called)
        self.assertTrue(mock3.called)
        self.assertTrue(mock4.called)
        self.assertTrue(mock5.called)

    @patch.object(FileAppendRunner, '_restore_permissions')
    def test_append_to_file_appends_to_file(self, mocked_restore_permissions):
        lines_before = self._count_lines_in_file()
        self.file_append_runner.append_to_file()
        lines_after = self._count_lines_in_file()
        self.assertTrue(lines_after > lines_before)

    def _count_lines_in_file(self):
        with open(self.file_append.file_path, 'r') as file:
            lines = file.readlines()
        return len(lines)