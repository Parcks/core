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
import unittest
from src.cli.argument_parser import ArgumentParser
from src.exceptions.no_installation_file_provided_error import NoInstallationFileProvidedError

class TestArgumentParser(unittest.TestCase):
    def test_parse_sets_input_file(self):
        parser = ArgumentParser("-i file.parcks".split())
        parser.parse()
        self.assertEqual("file.parcks", parser.inputFile)

    def test_parse_sets_input_file_long_parameter(self):
        parser = ArgumentParser("--installer-file=file.parcks".split())
        parser.parse()
        self.assertEqual("file.parcks", parser.inputFile)

    def test_parse_raises_NoInstallationFilePassedError(self):
        parser = ArgumentParser([])
        with self.assertRaises(NoInstallationFileProvidedError):
            parser.parse()
        