# -*- coding: utf-8 -*-

import re
import subprocess
import sys
import resource


class SignerOption(object):
    """
    TODO:
    """

    def __init__(self, name, shortcut, default=None, value=None, help=None):
        self.name = name
        self.shortcut = shortcut
        self.default = default
        self.help = help
        self.value = value and value or self.default

    def to_cmd(self):
        pass


class Signer(object):
    """
    TODO:
    """
