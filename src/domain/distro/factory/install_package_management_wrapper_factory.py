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
from src.exceptions.unsupported_distro_name_error import UnsupportedDistroNameError
from src.domain.distro.debian.debian_install_package_management_wrapper import DebianInstallPackageManagementWrapper

class InstallPackageManagementWrapperFactory:
    def create(self, distro_name, package_name):
        """
        Creates the correct :class:`src.domain.distro.install_package_management_wrapper.InstallPackageManagementWrapper`
        depending on the distro
        :param distro_name: The name of the distro
        :type distro_name: str
        :param package_name: The name of the package to install
        :type package_name: str
        :raises UnsupportedDistroName: If the distro name is not yet supported
        """
        install_package_management_wrapper = None
        if(distro_name == "debian"):
            install_package_management_wrapper = DebianInstallPackageManagementWrapper(package_name)
        else:
            raise UnsupportedDistroNameError("The distro "+distro_name+" is not (yet) supported")
        return install_package_management_wrapper