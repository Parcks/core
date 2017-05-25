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

class ShellCommandRunner(ShellCommandRunnable):
    def __init__(self,  shell_command):
        """
        Default constructor
        :param shell_command: The ShellCommand to run
        :type shell_command: `src.domain.shell_command.ShellCommand`
        """
        super(ShellCommandRunner,  self).__init__(shell_command)
        
    def run(self):
        for command in self.shell_command.commands:            
            executable_commands  = self.create_executable_command_array(command)
            result = subprocess.call(executable_commands)
            self.handle_result(result,  command)
