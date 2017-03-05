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
import os
from src.controller.installation_controller import InstallationController
from src.exceptions.permission_denied_error import PermissionDeniedError
from src.cli.argument_parser import ArgumentParser

class StartupController:
    def __init__(self, args):
        self.version = 1.0
        self.argumentParser = ArgumentParser(args)

    def run(self):
        print ("Parcks v. {:0.2f} - (c) JValck - Setarit".format(self.version))
        if(not self.executedAsRoot()):
            raise PermissionDeniedError("Parcks must be runned as root")
        installationFile = self.parse_arguments()
        self.boot_install_controller(installationFile)

    def executedAsRoot(self):
        return os.geteuid() == 0

    def parse_arguments(self):
        """        
        @return: The location of the installation file 
        """
        self.argumentParser.parse()
        return self.argumentParser.inputFile

    def boot_install_controller(self, installationFile):
        controller = InstallationController(installationFile)
        controller.run()