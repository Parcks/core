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

class InstallFacade:
    def __init__(self, installFileLocation):
        self.installFileLocation = installFileLocation

    def parse_installation_file(self):
        parser = InstallationFileParser(self.installFileLocation)
        self.software_catalog = parser.parse()

    def install(self):
        print(self.software_catalog.packages[0].plugins)
        

    

    
        