# -*- coding: utf-8 -*-

import sys
import subprocess

from signer.configuration import Configuration


class Binding(object):
    """
    JSignPDF API Wrapper.
    """
    _module_prefix = 'signer.bindings.jsignpdf.'
    _options = [
    ]

    def __init__(self):
        self._app_name = 'JSignPdf.jar'
        self._configuration = Configuration()
        self.command = ' '.join(
            self._configuration.java_cmd,
            self.jar_opt,
            self._app_name
        )
        


