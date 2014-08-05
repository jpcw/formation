#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Doc here.
"""

__docformat__ = 'restructuredtext en'

from unittest import TestCase


class Testjpcw_formation(TestCase):

    def test_sample(self):
        """A sample test here."""
        docfmt = 'restructuredtext en'
        from jpcw import formation
        self.assertTrue(formation.__docformat__ == docfmt)


# vim:set et sts=4 ts=4 tw=80:
