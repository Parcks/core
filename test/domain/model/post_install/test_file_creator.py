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

from src.domain.log.logger import Logger
from src.domain.model.post_install.file_creator import FileCreator
from src.domain.post_install.file.file_creator_runner import FileCreatorRunner

try:
    from unittest.mock import patch
except ImportError:
    from mock import patch

class TestFileCreator(unittest.TestCase):
    def setUp(self):
        Logger.disable_all()
        self.file_creator = FileCreator("Dummy creator", "dummy path", "dummy contents")

    def tearDown(self):
        Logger.enable()

    @patch.object(FileCreatorRunner, 'create_file')
    def test_run_calls_create_file_on_FileCreatorRunner(self, mock):
        self.file_creator.run()
        self.assertTrue(mock.called)
