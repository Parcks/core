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
import argparse


class ArgumentParser:
    def __init__(self, args_from_cli):
        """
        Default constructor
        :param args_from_cli: The arguments from the command-line
        :type args_from_cli: list of str
        """
        self.parser = argparse.ArgumentParser(description='A Standardized Packages Installer',
                                              prog='parcks',
                                              epilog='Written by Setarit. '
                                                     'Visit http://parcks.setarit.com for more info.'
                                              )
        self.add_arguments()
        self.args_from_cli = args_from_cli
        self.inputFile = None

    def add_arguments(self):
        self.parser.add_argument('file', help='Absolute path to the file to execute', metavar='File')

    def parse(self):
        """
        Parses the command-line arguments and sets self.inputFile
        """
        result = self.parser.parse_args(self.args_from_cli)

        self.inputFile = result.file