# -*- coding: utf-8 -*-
from __future__ import print_function, division, absolute_import

import unittest

from blaze import error
from blaze.overloading import best_match, overload
from blaze import dshape
from blaze.datashape import unify, dshapes

#------------------------------------------------------------------------
# Tests
#------------------------------------------------------------------------

@overload('X, Y, float32 -> X, Y, float32 -> X, Y, float32')
def f(a, b):
    return a

@overload('X, Y, complex64 -> X, Y, complex64 -> X, Y, complex64')
def f(a, b):
    return a

@overload('X, Y, complex128 -> X, Y, complex128 -> X, Y, complex128')
def f(a, b):
    return a


class TestOverloading(unittest.TestCase):

    def test_best_match(self):
        d1 = dshape('10, T1, int32')
        d2 = dshape('T2, T2, float32')
        dst_sig, sig, func = best_match(f, [d1, d2])
        print(dst_sig, sig)


if __name__ == '__main__':
    TestOverloading('test_best_match').debug()
    # unittest.main()