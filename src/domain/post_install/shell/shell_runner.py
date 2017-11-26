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
from src.domain.post_install.shell.shell_command_runnable_factory import ShellCommandRunnableFactory
from src.domain.log.logger import Logger
class ShellRunner():
    def __init__(self,  shell):
        self.shell = shell
        self.shell_command_runnable = None
        self.factory = ShellCommandRunnableFactory()
        
    def run(self):
        Logger.logger.info("Starting shell scripts. Please wait...")
        for shell_command in self.shell.shell_commands:
            self.create_shell_command_runnable(shell_command)        
            self.execute_shell_command_runnable()
        
    def create_shell_command_runnable(self,  shell_command):
        """
        Calls the factory to create the correct ShellCommandRunnable
        :param shell_command: The current :obj:`src.domain.shell_command.ShellCommand` whose runnable that should be created
        :type shell_command: :obj:`src.domain.shell_command.ShellCommand`
        """
        Logger.logger.debug("Creating ShellCommandRunnable")
        self.shell_command_runnable = self.factory.create(shell_command)
        
    def execute_shell_command_runnable(self):
        """
        Executes the ShellCommandRunnable
        """
        Logger.logger.debug("Executing ShellCommandRunnable")
        self.shell_command_runnable.run()
        
