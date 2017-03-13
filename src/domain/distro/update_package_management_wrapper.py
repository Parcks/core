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
from src.domain.distro.package_management_wrapper import PackageManagementWrapper
from abc import ABCMeta, abstractmethod

class UpdatePackageManagementWrapper(PackageManagementWrapper):
    def __init__(self, package_name):
        """
        Default constructor
        :param package_name: The name of the package to install
        :type package_name: str
        """
        __metaclass__=ABCMeta
        super(PackageManagementWrapper, self).__init__(package_name)

    @abstractmethod
    def update(self):
        pass