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
from src.exceptions.package_installation_failure_error import PackageInstallationFailureError
from src.exceptions.no_alternative_package_suitable_error import NoAlternativePackageSuitableError
from src.domain.log.logger import Logger


class PackageInstaller:
    def __init__(self, package, install_package_management_wrapper):
        self.package = package
        self.install_package_management_wrapper = install_package_management_wrapper

    def install(self):
        """
        Installs the package
        Will try alternatives if specified
        """
        if self.package.alternative_names is None:
            self.try_package()
        else:
            self.install_package_with_alternatives()

    def install_package_with_alternatives(self):
        """
        Installs the package
        Will try alternatives if specified
        """
        try:
            self.try_package()
        except PackageInstallationFailureError:
            self.try_alternatives()

    def try_package(self):
        """
        Installs the package specified by the name
        :raises NoAlternativePackageSuitableError: If there is no suitable alternative found
        """
        self.install_package_management_wrapper.set_package_name(self.package.name)
        self.install_package_management_wrapper.install()

    def try_alternatives(self):
        for index, alternative_name in enumerate(self.package.alternative_names):
            try:
                self.try_alternative_package(alternative_name)
                return
            except PackageInstallationFailureError:
                pass
        raise NoAlternativePackageSuitableError()

    def try_alternative_package(self, alternative_name):
        Logger.logger.info("Trying alternative package: "+alternative_name)
        self.install_package_management_wrapper.set_package_name(alternative_name)
        self.install_package_management_wrapper.install()