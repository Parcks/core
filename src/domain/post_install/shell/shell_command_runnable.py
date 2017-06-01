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
from abc import ABCMeta, abstractmethod
from src.domain.log.logger import Logger
import src.exceptions.shell_command_failed_error

class ShellCommandRunnable(object):
    def __init__(self,  shell_command):
        __metaclass__ = ABCMeta
        self.shell_command = shell_command
        
    def handle_result(self,  result_code,  command):
        if result_code == 1:
            self.write_error_log_message(command)
            raise ShellCommandFailedError()
        else:
            self.write_success_log_message(command)
        
    def write_error_log_message(self, command):
        Logger.logger.debug("The command "+command+" failed to execute. Try running the command manually. Open an issue on GitHub to solve the error if it persists.")
        
    def write_success_log_message(self,  command):
        Logger.logger.debug("The command "+command+" executed successfully")
        
    def create_executable_command_array(self,  command):
        """
        Creates a list that is executable by the subprocess
        :param command: The command to execute
        :type command: str
        :returns: The executable command list
        :rtype: list
        """
        return command.split(" ")
    
    @abstractmethod
    def run(self):
        pass
