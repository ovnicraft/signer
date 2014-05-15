# -*- coding: utf-8 -*-
import subprocess
import sys
import os


class Configuration(object):
    """
    Java Wrapper command
    """
    def __init__(self, java_cmd=None):
        """
        """
        self.java_cmd = java_cmd
        self.jar_opt = '-jar'

        if not self.java_cmd:
            wcmd = 'which'
            if sys.platform == 'win32':
                wcmd = 'where'
            self.java_cmd = subprocess.Popen([wcmd, 'java'],
                                         stdout=subprocess.PIPE).communicate()[0].strip()

        if not os.path.isfile(self.java_cmd):
            raise IOError('No java VM installed \n'
                          'Please install it.')
                

def main():
    conf = Configuration()

if __name__ == '__main__':
    """
    Allow check java installation
    """
    main()
