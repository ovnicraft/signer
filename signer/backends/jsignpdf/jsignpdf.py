# -*- coding: utf-8 -*-

from signer.bindings.jsignpdf.binding import Binding


class JSignPdf(object):
    """
    JsignPDF API binding interfaces
    """
    name = 'jsignpdf'

    def __init__(self):
        self._binding = Binding()
        self.command = self._binding.command


