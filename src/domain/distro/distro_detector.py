"""
Scriptable Packages Installer - Parcks
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
import distro # pragma: no cover
from src.domain.log.logger import Logger

def detect_distro(): # pragma: no cover
    """
    Detects the distro name
    :returns: The name of the distro see `here <http://distro.readthedocs.io/en/latest/>`_
    :rtype: str
    """
    distro_name = distro.like()
    if not distro_name:
        distro_name = distro.id()
    Logger.logger.info("Detected distro:\t"+distro_name)
    return distro_name
