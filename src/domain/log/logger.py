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
import logging, time, os

class Logger(object):
    _instance = None
    logger = logging.getLogger("parcks")

    def __new__(cls):
        if(cls._instance is None):
            cls._instance = object.__new__(cls)
        return cls._instance
    
    def __init__(self):
        self.log_file_path = self.generate_path()
        self.set_up_log_to_file()
        self.set_up_log_to_console()

    def generate_path(self):
        """
        Generates the path to the log file, based on the time and user
        :returns: The path to the log file
        :rtype: str
        """
        time_as_string = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())
        home_path = os.path.expanduser("~")
        log_directory = os.path.join(home_path, ".parcks","logs")
        self.make_directory_if_not_exists(log_directory)
        return os.path.join(log_directory, time_as_string+".log")

    def make_directory_if_not_exists(self, log_directory):
        if not os.path.exists(log_directory):
            os.makedirs(log_directory)

    def set_up_log_to_file(self):
        logging.basicConfig(
            filename= self.log_file_path,
            level=logging.DEBUG,
            format= '[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s',
            datefmt='%H:%M:%S'
        )

    def set_up_log_to_console(self):
        console = logging.StreamHandler()
        console.setLevel(logging.INFO)
        # set a format which is simpler for console use
        formatter = logging.Formatter('%(levelname)-8s %(message)s')
        console.setFormatter(formatter)
        # add the handler to the root logger
        logging.getLogger('').addHandler(console)
        
    @staticmethod
    def disable_all():
        logging.disable(logging.CRITICAL)
      
    @staticmethod
    def enable():
        logging.disable(logging.NOTSET)
