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

import os
import unittest

from src.domain.log.logger import Logger
from src.domain.model.post_install.file_create import FileCreate
from src.domain.post_install.file.file_create_runner import FileCreateRunner
import sys
from src.exceptions.file_creation_failed_error import FileCreationFailedError

try:
    from unittest.mock import patch
except ImportError:
    from mock import patch


class TestFileCreateRunner(unittest.TestCase):
    def setUp(self):
        Logger.disable_all()
        self.test_file_creator_path = "/tmp/dummy_path"
        self.file_create = FileCreate("Dummy creator", self.test_file_creator_path, "dummy contents")
        self.file_create_as_root = FileCreate("Dummy creator", self.test_file_creator_path, "dummy contents", True)
        self.file_create_runner = FileCreateRunner(self.file_create)
        self.file_create_runner_as_root = FileCreateRunner(self.file_create_as_root)

    def tearDown(self):
        Logger.enable()
        if os.path.exists(self.test_file_creator_path):
            os.remove(self.test_file_creator_path)

    def line_counter(self, path_to_file):
        with open(path_to_file) as fi:
            lines = sum(1 for line in fi)
        return lines

    def test___init___creates_FileCreatorRunner_with_correct_FileCreator(self):
        result = FileCreateRunner(self.file_create)
        self.assertEqual(result.file_create, self.file_create)

    @patch.object(FileCreateRunner, '_create_file_current_user')
    @patch.object(FileCreateRunner, '_create_call_array')
    @patch.object(FileCreateRunner, '_write_to_temp_file')
    def test_create_file_calls__write_to_temp_file(self, mock, mocked_call_array, mocked_as_current_user):
        self.file_create_runner.create_file()
        self.assertTrue(mock.called)

    @patch.object(FileCreateRunner, '_create_file_current_user')
    @patch.object(FileCreateRunner, '_create_call_array')
    @patch.object(FileCreateRunner, '_write_to_temp_file')
    def test_create_file_calls__create_call_array(self, mock, mocked_call_array, mocked_as_current_user):
        self.file_create_runner.create_file()
        self.assertTrue(mocked_call_array.called)

    @patch.object(FileCreateRunner, '_create_file_current_user')
    @patch.object(FileCreateRunner, '_create_call_array')
    @patch.object(FileCreateRunner, '_write_to_temp_file')
    def test_create_file_calls__create_file_current_user_if_non_root(self, mock, mocked_call_array, mocked_as_current_user):
        self.file_create_runner.create_file()
        self.assertTrue(mocked_as_current_user.called)

    @patch('subprocess.call')
    @patch.object(FileCreateRunner, '_create_file_as_root')
    @patch.object(FileCreateRunner, '_create_call_array')
    @patch.object(FileCreateRunner, '_write_to_temp_file')
    def test_create_file_calls__create_file_as_root_if_root(self, mock, mocked_call_array, mocked_as_root, mocked_subprocess):
        self.file_create_runner_as_root.create_file()
        self.assertTrue(mocked_as_root.called)

    def test_create_file_writes_to_file(self):
        self.file_create_runner.create_file()
        self.assertEqual(1, self.line_counter(self.file_create_runner.file_create.file_path))

    @patch.object(FileCreateRunner, '_write_to_temp_file')
    def test_run_raises_FileCreationFailedError_if_file_could_not_be_moved(self, mocked_write_to_temp):
        creator = FileCreate("Dummy creator", "/invalid/path", "dummy contents")
        runner = FileCreateRunner(creator)
        runner.temp_file_location = "/invalid/temp/path"
        with self.assertRaises(FileCreationFailedError):
            runner.create_file()

