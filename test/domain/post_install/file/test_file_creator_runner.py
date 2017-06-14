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

import os
import unittest

from src.domain.log.logger import Logger
from src.domain.model.post_install.file_creator import FileCreator
from src.domain.post_install.file.file_creator_runner import FileCreatorRunner

try:
    from unittest.mock import patch
except ImportError:
    from mock import patch


class TestFileCreatorRunner(unittest.TestCase):
    def setUp(self):
        Logger.disable_all()
        self.test_file_creator_path = "/tmp/dummy_path"
        self.file_creator = FileCreator("Dummy creator", self.test_file_creator_path, "dummy contents")
        self.file_creator_as_root = FileCreator("Dummy creator", self.test_file_creator_path, "dummy contents", True)
        self.file_creator_runner = FileCreatorRunner(self.file_creator)
        self.file_creator_runner_as_root = FileCreatorRunner(self.file_creator_as_root)

    def tearDown(self):
        Logger.enable()
        if os.path.exists(self.test_file_creator_path):
            os.remove(self.test_file_creator_path)

    def line_counter(self, path_to_file):
        with open(path_to_file) as fi:
            lines = sum(1 for line in fi)
        return lines

    def test___init___creates_FileCreatorRunner_with_correct_FileCreator(self):
        result = FileCreatorRunner(self.file_creator)
        self.assertEqual(result.file_creator, self.file_creator)

    @patch.object(FileCreatorRunner, '_create_file_current_user')
    @patch.object(FileCreatorRunner, '_create_call_array')
    @patch.object(FileCreatorRunner, '_write_to_temp_file')
    def test_create_file_calls__write_to_temp_file(self, mock, mocked_call_array, mocked_as_current_user):
        self.file_creator_runner.create_file()
        self.assertTrue(mock.called)

    @patch.object(FileCreatorRunner, '_create_file_current_user')
    @patch.object(FileCreatorRunner, '_create_call_array')
    @patch.object(FileCreatorRunner, '_write_to_temp_file')
    def test_create_file_calls__create_call_array(self, mock, mocked_call_array, mocked_as_current_user):
        self.file_creator_runner.create_file()
        self.assertTrue(mocked_call_array.called)

    @patch.object(FileCreatorRunner, '_create_file_current_user')
    @patch.object(FileCreatorRunner, '_create_call_array')
    @patch.object(FileCreatorRunner, '_write_to_temp_file')
    def test_create_file_calls__create_file_current_user_if_non_root(self, mock, mocked_call_array, mocked_as_current_user):
        self.file_creator_runner.create_file()
        self.assertTrue(mocked_as_current_user.called)

    @patch('subprocess.call')
    @patch.object(FileCreatorRunner, '_create_file_as_root')
    @patch.object(FileCreatorRunner, '_create_call_array')
    @patch.object(FileCreatorRunner, '_write_to_temp_file')
    def test_create_file_calls__create_file_as_root_if_root(self, mock, mocked_call_array, mocked_as_root, mocked_subprocess):
        self.file_creator_runner_as_root.create_file()
        self.assertTrue(mocked_as_root.called)

    def test_create_file_writes_to_file(self):
        self.file_creator_runner.create_file()
        self.assertEqual(1, self.line_counter(self.file_creator_runner.file_creator.file_path))