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
from abc import ABCMeta, abstractmethod


class PackageManagementWrapper(object):
    def __init__(self):
        """
        Default parent constructor
        """
        __metaclass__ = ABCMeta
        self.package_name = None

    def set_package_name(self, package_name):
        """
        Setter
        :param package_name: The name of the package
        :type package_name: str
        """
        self.package_name = package_name
        
    @abstractmethod
    def install(self):
        pass

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def is_installed(self):
        pass