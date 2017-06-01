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
import getopt
from src.exceptions.no_installation_file_provided_error import NoInstallationFileProvidedError

class ArgumentParser:
    def __init__(self, args):
        """
        Default constructor
        :param args: The arguments from the command-line
        :type args: list of str
        """
        self.options, self.args = getopt.getopt(args, "i:", ["installer-file="])
        self.inputFile = None

    def parse(self):
        """
        Parses the command-line arguments and sets self.inputFile
        """
        for option, argument in self.options:            
            if(option in ("-i","--installer-file")):
                self.inputFile = argument
        if(self.inputFile == None):
            raise NoInstallationFileProvidedError("No installation file provided")