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
from src.service.cli_facade import CliFacade
from src.cli.colored_user_output import ColoredUserOutput
from src.cli.user_input import UserInput
import unittest
try:
    from unittest.mock import patch
except ImportError:
    from mock import patch
    
class TestCliFacade(unittest.TestCase):
    def setUp(self):
        self.facade = CliFacade()
        
    @patch.object(ColoredUserOutput,  'print_warning')
    def test_print_warning_calls_print_warning_on_ColoredUserOutput(self,  mock):
        self.facade.print_warning("Dummy warning")
        self.assertEqual(1,  mock.call_count)
        
    @patch.object(UserInput,  "ask_native")
    @patch.object(UserInput,  "ask")
    def test_ask_user_calls_ask_on_UserInput(self,  mock,  mocked_input_method):
        self.facade.ask_user("Dummy question")
        self.assertEqual(1,  mock.call_count)
