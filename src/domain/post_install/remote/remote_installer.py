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
from src.domain.post_install.remote.remote_validator import RemoteValidator
from src.domain.post_install.remote.remote_downloader import RemoteDownloader
from src.domain.post_install.remote.remote_runner import RemoteRunner
from src.service.cli_facade import CliFacade
from src.domain.log.logger import Logger
import sys


class RemoteInstaller:
    def __init__(self, remote):
        """
        Default constructor
        :param remote: The remote that needs to be installed
        :type remote: src.domain.remote
        """
        self.remote = remote
        self.remote_validator = RemoteValidator(remote)
        self.remote_downloader = RemoteDownloader(remote)
        self.remote_runner = RemoteRunner(remote)
        self.cli_facade = CliFacade()
        
    def run(self):
        self.remote_validator.validate()
        self.download_if_necessary()
        self.remote_runner.run()

    def download_if_necessary(self):
        if self.remote_validator.is_download_required():
            self.verify_url()
            self.download_remote_but_keep_local_name()

    def verify_url(self):
        if self.remote_validator.is_external_download_url():
            self.show_warning_and_ask_confirmation_to_continue()
            Logger().logger.warning("Downloading remote from unverified source")

    def download_remote_but_keep_local_name(self):
        local_remote_name = self.remote.name
        self.remote = self.remote_downloader.download()
        self.remote.name = local_remote_name
        self.remote_runner = RemoteRunner(self.remote) #update PluginRunner

    def show_warning_and_ask_confirmation_to_continue(self):
        """
        Displays a warning message and ask for confirmation to continue.
        If the user does not want to continue, this method ends the program.
        """
        self.cli_facade.print_warning("Parcks will download the remote from an unverified source.\n"
                                      "\tCheck https://github.com/Parcks/core/wiki/Unverified-sources for further info...")
        answer = self.ask_confirmation()
        if answer == "N":
            sys.exit(0)

    def ask_confirmation(self):
        answer = (self.cli_facade.ask_user("Are you sure you want to continue [y/n (default)]?", "n")).upper()
        if answer == "Y" or answer == "N":
            return answer
        else:
            return self.ask_confirmation()