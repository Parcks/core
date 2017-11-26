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
import os, pkg_resources
from src.controller.installation_controller import InstallationController
from src.cli.argument_parser import ArgumentParser
from src.domain.log.logger import Logger
from src.service.cli_facade import CliFacade


class StartupController:
    def __init__(self, args):
        self.version = self.fetch_version_from_setup()
        self.argumentParser = ArgumentParser(args)
        self.cli_facade = CliFacade()
        logger = Logger()
        self.logger = logger.logger

    def run(self):
        self.logger.info("v." + self.version + " - (GPLv2) JValck - Setarit")
        self.display_warning_if_executing_as_root()
        installationFile = self.parse_arguments()
        self.boot_install_controller(installationFile)

    def fetch_version_from_setup(self):
        try:
            return pkg_resources.require("Parcks")[0].version
        except pkg_resources.DistributionNotFound:
            return "DEVELOPMENT"


    def display_warning_if_executing_as_root(self):
        if(self.executingAsRoot()):
            self.logger.warning("Executing as root")
            self.cli_facade.print_warning(
                "You are executing Parcks as root. This can cause security issues and unwanted results."
                "\n\tCheck https://github.com/Parcks/core/wiki/Running-as-root for further info..."
            )

    def executingAsRoot(self):
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
