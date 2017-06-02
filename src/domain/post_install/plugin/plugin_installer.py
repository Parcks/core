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
from src.domain.post_install.plugin.plugin_validator import PluginValidator
from src.domain.post_install.plugin.plugin_downloader import PluginDownloader
from src.domain.post_install.plugin.plugin_runner import PluginRunner
from src.service.cli_facade import CliFacade
from src.domain.log.logger import Logger
import sys


class PluginInstaller:
    def __init__(self,  plugin):
        """
        Default constructor
        :param plugin: The plugin that needs to be installed
        :type plugin: src.domain.plugin
        """
        self.plugin = plugin
        self.plugin_validator = PluginValidator(plugin)
        self.plugin_downloader = PluginDownloader(plugin)
        self.plugin_runner = PluginRunner(plugin)
        self.cli_facade = CliFacade()
        
    def run(self):
        self.plugin_validator.validate()
        self.download_if_necessary()
        self.plugin_runner.run()

    def download_if_necessary(self):
        if self.plugin_validator.is_download_required():
            self.verify_url()
            self.download_plugin_but_keep_local_name()

    def verify_url(self):
        if self.plugin_validator.is_external_download_url():
            self.show_warning_and_ask_confirmation_to_continue()
            Logger().logger.warning("Downloading plugin from unverified source")

    def download_plugin_but_keep_local_name(self):
        local_plugin_name = self.plugin.name
        self.plugin = self.plugin_downloader.download()
        self.plugin.name = local_plugin_name
        self.plugin_runner = PluginRunner(self.plugin) #update PluginRunner

    def show_warning_and_ask_confirmation_to_continue(self):
        """
        Displays a warning message and ask for confirmation to continue.
        If the user does not want to continue, this method ends the program.
        """
        self.cli_facade.print_warning("Parcks will download the plugin from an unverified source.\n"
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