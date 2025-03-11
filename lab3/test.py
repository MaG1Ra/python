import pytest
from lab import sum_rec, sum_iter, rec, iter

def test_sum_rec():
    assert sum_rec([1, 2, 3]) == 6
    assert sum_rec([1, [2, [3, 4, [5]]]]) == 15
    assert sum_rec([[[]]]) == 0
    assert sum_rec([-1, [2, [-3, 4, [5]]]]) == 7

def test_sum_iter():
    assert sum_iter([1, 2, 3]) == 6
    assert sum_iter([1, [2, [3, 4, [5]]]]) == 15
    assert sum_iter([[[]]]) == 0
    assert sum_iter([-1, [2, [-3, 4, [5]]]]) == 7

def test_rec():
    assert rec(1) == (1, 1)
    assert rec(2) == (0.75, 2)

def test_iter():
    assert iter(1) == (1, 1)
    assert iter(2) == (0.75, 2)