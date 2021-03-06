#!/usr/bin/python

import os
import sys
import unittest

sys.path = [ os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')) ] + sys.path

from classproperties import classproperty


class ArrayTest(unittest.TestCase):
    def test_classproperty(self):
        class Bar:
            @classproperty
            def p(cls):
                return 'p'

            @classproperty
            def q():
                return 'q'


        self.assertEquals(
            Bar.p,
            'p'
        )

        self.assertEquals(
            Bar().p,
            'p'
        )

        self.assertEquals(
            Bar.q,
            'q'
        )


    def test_standard(self):
        class Foo:
            a = 'a'

            @staticmethod
            def b():
                return 'b'

            @classmethod
            def c(cls):
                return 'c'

            def d(self):
                return 'd'


        self.assertEquals(
            Foo.a,
            'a'
        )

        self.assertEquals(
            Foo.b(),
            'b'
        )

        self.assertEquals(
            Foo.c(),
            'c'
        )

        self.assertEquals(
            Foo().d(),
            'd'
        )


if __name__ == '__main__':
    unittest.main()
