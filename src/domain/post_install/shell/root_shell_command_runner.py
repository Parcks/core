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
from src.domain.post_install.shell.shell_command_runnable import ShellCommandRunnable
import subprocess

class RootShellCommandRunner(ShellCommandRunnable):
    def __init__(self,  shell_command):
        """
        Default constructor
        :param shell_command: The ShellCommand to run
        :type shell_command: `src.domain.shell_command.ShellCommand`
        """
        super(RootShellCommandRunner,  self).__init__(shell_command)
        self.executable_command_prefix = ["sudo"]
        
    def run(self):
        for command in self.shell_command.commands:            
            executable_commands  = self.create_root_executable_command_array(command)
            result = subprocess.Popen(executable_commands,  cwd=self.shell_command.work_directory)
            self.handle_result(result,  command)
            
    def create_root_executable_command_array(self,  command):
        """
        Creates a list that is executable by the subprocess
        Requests root privileges in the executable command list
        :param command: The command to execute
        :type command: str
        :returns: The executable command list
        :rtype: list
        """
        return self.executable_command_prefix + self.create_executable_command_array(command)
