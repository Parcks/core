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

Setarit - parcks[at]setarit.com
"""
from __future__ import absolute_import

import json

from src.domain.model.software_catalog import SoftwareCatalog
from src.domain.parse.file_parsable import FileParsable
from src.domain.parse.package_parser import PackageParser
from src.exceptions.invalid_installation_file_extension_error import InvalidInstallationFileExtensionError


class InstallationFileParser(FileParsable):
    def __init__(self, file_path):
        super(InstallationFileParser, self).__init__(file_path)
        
    def parse(self):
        catalog = None
        self.validate_file_extension()
        with open(self.file_path) as installFile:
            data = json.load(installFile)
            catalog = self.create_software_catalog(data)
        return catalog
        
    def validate_file_extension(self):
        if(not self.file_path.endswith(".parcks")):
            raise InvalidInstallationFileExtensionError("The installation file extension does not meet the requirements.")

    def create_software_catalog(self, data):
        catalog = SoftwareCatalog(data["name"])
        package_parser = PackageParser(data["install"])
        catalog.packages = package_parser.parse()        
        return catalog
