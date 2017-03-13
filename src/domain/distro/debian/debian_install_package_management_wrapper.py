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
from src.domain.distro.install_package_management_wrapper import InstallPackageManagementWrapper
from src.domain.log.logger import Logger
from src.exceptions.package_installation_failure_error import PackageInstallationFailureError
import subprocess

class DebianInstallPackageManagementWrapper(InstallPackageManagementWrapper):
    def __init__(self, package_name):
        """
        Default constructor
        :param package_name: The name of the package to install
        :type package_name: str
        """
        super(InstallPackageManagementWrapper, self).__init__(package_name)

    def install(self):
        result = subprocess.call(['sudo', 'apt', 'install', '-y', self.package_name])
        self.handle_result(result)

    def is_installed(self):
        return False

    def handle_result(self, result_code):
        """
        Handles the result of an package installation call
        :param result_code: The result code of the installation call
        :type result_code: int
        """
        if result_code == 0:
            Logger.logger.info("Package "+self.package_name+" installed")
        else:
            raise PackageInstallationFailureError("Package "+self.package_name+" failed to complete the installation")