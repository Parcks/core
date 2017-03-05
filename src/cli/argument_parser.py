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
import getopt
from src.exceptions.no_installation_file_provided import NoInstallationFileProvided

class ArgumentParser:
    def __init__(self, args):
        self.options, self.args = getopt.getopt(args, "i:", ["installer-file="])
        self.inputFile = None

    def parse(self):
        for option, argument in self.options:            
            if(option in ("-i","--installer-file")):
                self.inputFile = argument
        if(self.inputFile == None):
            raise NoInstallationFileProvided("No installation file provided")