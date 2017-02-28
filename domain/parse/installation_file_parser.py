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
from domain.parse.parsable import Parsable
from domain.software_catalog import SoftwareCatalog
from domain.parse.factory.package_factory import PackageFactory
import json

class InstallationFileParser(Parsable):
    def __init__(self, filePath):
        super().__init__(filePath)
        
    def parse(self):
        catalog = None
        with open(self.filePath) as installFile:
            data = json.load(installFile)
            catalog = self.create_software_catalog(data)
        return catalog

    def create_software_catalog(self, data):
        catalog = SoftwareCatalog(data["name"])
        packageFactory = PackageFactory(data["install"])
        catalog.packages = packageFactory.load_packages()        
        return catalog