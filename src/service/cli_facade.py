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
from src.cli.user_input import UserInput
from src.cli.colored_user_output import ColoredUserOutput

class CliFacade:
    def __init__(self):
        self.user_input = UserInput()
        self.colored_user_output = ColoredUserOutput()
        
    def print_warning(self,  message):
        """
        Prints a colored warning message
        :param message: The message to print
        :type message: str
        """
        self.colored_user_output.print_warning(message)
        
    def ask_user(self,  question,  default_answer = False):
        """
        Asks a question to the user and waits for the input
        :param question: The text to display to the user
        :type question: str
        :param default_answer: The default answer of the question when the user hit enter without answer, if none specified it will be False
        :type default_answer: bool
        :returns: The answer on the question or the default answer if no answer given
        :rtype: str or bool
        """
        return self.user_input.ask(lambda: self.user_input.ask_native(question),  default_answer)
