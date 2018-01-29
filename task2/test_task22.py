from __future__ import division

import numpy as np


def test_div():
    assert 2 / 8 == 0.25


def test_div_numpy():
    x = np.array([2])
    y = np.array([8])
    # assert np.divide(x, y) == np.array([0.25])
    assert x / y == np.array([0.25])
