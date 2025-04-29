import pytest
from lab import file_line_generator

def test_1():
    max_lenght = 20
    filename ='test.txt'
    generator = file_line_generator(filename, max_lenght)
    result = list(generator)
    assert result == ['olleH dlrow', 'nohtyP si emosewa']

def test_2():
    max_lenght = 0
    filename ='empty.txt'
    generator = file_line_generator(filename, max_lenght)
    result = list(generator)
    assert result == []

def test_3():
    max_lenght = 20
    filename ='test.txt'
    generator = file_line_generator(filename, max_lenght)
    result = list(generator)
    assert result == ['olleH dlrow', 'nohtyP si emosewa']
