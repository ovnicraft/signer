# -*- coding: utf-8 -*-
import subprocess
import sys
import os


class Configuration(object):
    def __init__(self, java=None):
        """
        """
        self.java = java

        if not self.java:
            wcmd = 'which'
            if sys.platform == 'win32':
                wcmd = 'where'
            self.java = subprocess.Popen([wcmd, 'java'],
                                         stdout=subprocess.PIPE).communicate()[0].strip()

        if not os.path.isfile(self.java):
            raise IOError('No java VM installed \n'
                          'Please installed it.')
                

def main():
    conf = Configuration()

if __name__ == '__main__':
    """
    Allow check java installation
    """
    main()
