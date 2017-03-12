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

Setarit - support[at]setarit.com
"""
from __future__ import absolute_import
import unittest, os, sys
from src.domain.log.logger import Logger
try:
    from unittest.mock import patch
except ImportError:
    from mock import patch

class TestLogger(unittest.TestCase):
    def line_counter(self):
        with open(self.test_logger.log_file_path) as fi:
            lines = sum(1 for line in fi)
        return lines
    
    def setUp(self):
        self.test_logger = Logger() 

    def tearDown(self):
        if(os.path.exists(self.test_logger.log_file_path)):
            os.remove(self.test_logger.log_file_path)

    def test_logger_is_singleton(self):
        logger = Logger()
        self.assertEqual(logger, self.test_logger)

    @patch.object(Logger, 'make_directory_if_not_exists')
    def test_generate_path_calls_make_directory_if_not_exists(self, mocked_method):
        logger = Logger()
        path = logger.generate_path()
        self.assertTrue(mocked_method.called)