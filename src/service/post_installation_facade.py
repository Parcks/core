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

from src.domain.parse.post_installation_parser import PostInstallationParser


class PostInstallationFacade:
    def __init__(self, post_install_runnables):
        """
        Default constructor
        :param post_install_runnables: List of PostInstallRunnable's to execute
        :type post_install_runnables: list of :class:`src.domain.model.post_install.post_install_runnable.PostInstallRunnable
        """
        self.post_install_runnables = post_install_runnables

    @classmethod
    def from_json(cls, json):
        """
        Create a PostInstallationFacade from a json object
        :param json: The json
        :return: The created PostInstallationFacade
        """
        json_array = cls._check_if_json_is_list(json)
        parser = PostInstallationParser(json_array)
        post_installation_runnables = parser.parse()
        return cls(post_installation_runnables)

    @classmethod
    def _check_if_json_is_list(cls, json):
        """
        Checks if the json is a lost
        :param json: The json to be verified
        :return: The json as list
        :rtype: list
        """
        if not isinstance(json, list):
            return [json]
        else:
            return json

    def handle_post_installation(self):
        """
        Executes all the PostInstallRunnable's
        """
        for post_install_runnable in self.post_install_runnables:
            post_install_runnable.run()
