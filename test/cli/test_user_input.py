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
from src.cli.user_input import UserInput
import unittest
class TestUserInput(unittest.TestCase):
    def setUp(self):
        self.input_class = UserInput()
    
    def test_ask_returns_user_input(self):
        answer = self.input_class.ask(lambda: "Dummy input")
        self.assertEqual("Dummy input",  answer)
        
    def test_ask_returns_default_answer_if_no_answer_given(self):
        answer = self.input_class.ask(lambda: "", "Dummy input")        
        self.assertEqual("Dummy input",  answer)
