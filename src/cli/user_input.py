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
class UserInput:
    def ask(self,  input_method,  default_answer = False):
        """
        Asks a question to the user and waits for the input
        :param input_method: The method to request the input (use ask_native if in doubt)
        :type input_method: func
        :param default_answer: The default answer of the question when the user hit enter without answer
        :type default_answer: bool
        :returns: The answer on the question or the default answer if no answer given
        :rtype: str or bool
        """
        answer = input_method()
        return default_answer if len(answer) == 0 else answer
        
    def ask_native(self,  question_text):
        """
        Asks the question to the user and waits for the input
        :param question_text: The text to display to the user
        :type question_text: str
        :returns: The answer on the question
        :rtype: str
        """
        try:
            return raw_input(question_text)
        except NameError:
            return input(question_text)
