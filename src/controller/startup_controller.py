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
from src.cli.argument_parser import ArgumentParser
from src.domain.log.logger import Logger

class StartupController:
    def __init__(self, args):
        self.version = 2.0
        self.argumentParser = ArgumentParser(args)
        logger = Logger()
        self.logger = logger.logger

    def run(self):
        self.logger.info("v.{:0.2f} - (c) JValck - Setarit".format(self.version))
        installationFile = self.parse_arguments()
        self.boot_install_controller(installationFile)

    def executedAsRoot(self):
        """
        deprecated:: 2.0
        """
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
