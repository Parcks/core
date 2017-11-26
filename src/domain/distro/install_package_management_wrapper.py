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
from src.domain.distro.package_management_wrapper import PackageManagementWrapper
from src.exceptions.package_installation_failure_error import PackageInstallationFailureError
from src.domain.log.logger import Logger
from abc import ABCMeta, abstractmethod


class InstallPackageManagementWrapper(PackageManagementWrapper):
    def __init__(self):
        """
        Default constructor
        """
        __metaclass__=ABCMeta
        super(PackageManagementWrapper, self).__init__()

    @abstractmethod
    def install(self):
        pass

    @abstractmethod
    def is_installed(self):
        pass

    def handle_result(self, result_code):
        """
        Handles the result of an package installation call
        :param result_code: The result code of the installation call
        :type result_code: int
        """
        if result_code == 0:
            Logger.logger.info("Package "+self.package_name+" installed")
        else:
            Logger.logger.warning("Package "+self.package_name+" failed to complete the installation")
            raise PackageInstallationFailureError(self.package_name)