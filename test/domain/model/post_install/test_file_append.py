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

from src.domain.log.logger import Logger
from src.domain.model.post_install.file_append import FileAppend
from src.domain.post_install.file.file_append_runner import FileAppendRunner

try:
    from unittest.mock import patch
except ImportError:
    from mock import patch

class TestFileAppend(unittest.TestCase):
    def setUp(self):
        Logger.disable_all()
        self.file_append = FileAppend("Dummy append", "/tmp/test", "appended")

    def tearDown(self):
        Logger.enable()

    @patch.object(FileAppendRunner, 'append_to_file')
    def test_run_calls_append_to_file_on_runner(self, mock):
        self.file_append.run()
        self.assertTrue(mock.called)

    def test_path_with_home_symbol_becomes_absolute_path(self):
        file_create = FileAppend("Dummy home", "~/test", "dummy contents")
        self.assertFalse(file_create.file_path.startswith("~"))
        self.assertTrue(file_create.file_path.startswith("/home"))
