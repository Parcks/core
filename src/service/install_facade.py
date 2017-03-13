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
from src.domain.parse.installation_file_parser import InstallationFileParser
from src.domain.log.logger import Logger
from src.domain.distro.distro_detector import detect_distro
from src.domain.distro.factory.install_package_management_wrapper_factory import InstallPackageManagementWrapperFactory
import logging

class InstallFacade:
    def __init__(self, installFileLocation):
        self.installFileLocation = installFileLocation
        self.logger = Logger.logger
        self.distro_name = self.detect_distro_name()
        self.install_package_management_wrapper_factory = InstallPackageManagementWrapperFactory()

    def parse_installation_file(self):
        parser = InstallationFileParser(self.installFileLocation)
        self.software_catalog = parser.parse()

    def install(self):
        self.logger.info("Starting installation:\t "+self.software_catalog.name)
        for package in self.software_catalog.packages:
            install_package_management_wrapper = self.create_install_package_management_wrapper(package)
            install_package_management_wrapper.install()

    def detect_distro_name(self):        
        return detect_distro()

    def create_install_package_management_wrapper(self, package):
        factory = InstallPackageManagementWrapperFactory()
        return factory.create(self.distro_name, package.name)

    
    