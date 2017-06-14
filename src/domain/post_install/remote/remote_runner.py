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
from src.service.cli_facade import CliFacade
from src.domain.log.logger import Logger
import sys

from src.service.post_installation_facade import PostInstallationFacade


class RemoteRunner:
    def __init__(self, remote):
        """
        Default constructor
        :param remote: The remote that needs to be installed
        :type remote: src.domain.remote
        """
        self.remote = remote
        self.downloaded_json = None
        self.remote_validator = RemoteValidator(remote)
        self.remote_downloader = RemoteDownloader(remote)
        self.cli_facade = CliFacade()
        
    def run(self):
        self.remote_validator.validate()
        self._download()
        self._boot_post_installation_facade()

    def _download(self):
        self._verify_url()
        self._download_remote_from_repository()

    def _verify_url(self):
        if self.remote_validator.is_external_download_url():
            self._show_warning_and_ask_confirmation_to_continue()
            Logger().logger.warning("Downloading remote from unverified source")

    def _download_remote_from_repository(self):
        self.downloaded_json = self.remote_downloader.download()

    def _show_warning_and_ask_confirmation_to_continue(self):
        """
        Displays a warning message and ask for confirmation to continue.
        If the user does not want to continue, this method ends the program.
        """
        self.cli_facade.print_warning("Parcks will download the remote from an unverified source.\n"
                                      "\tCheck https://github.com/Parcks/core/wiki/Unverified-sources for further info...")
        answer = self._ask_confirmation()
        if answer == "N":
            sys.exit(0)

    def _ask_confirmation(self):
        answer = (self.cli_facade.ask_user("Are you sure you want to continue [y/n (default)]?", "n")).upper()
        if answer == "Y" or answer == "N":
            return answer
        else:
            return self._ask_confirmation()

    def _boot_post_installation_facade(self):
        """
        Creates a PostInstallationFacade from the downloaded json
        and starts executing the downloaded PostInstallationRunnable(s)
        """
        facade = PostInstallationFacade.from_json(self.downloaded_json)
        facade.handle_post_installation()