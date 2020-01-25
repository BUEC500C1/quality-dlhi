import pytest
from arabicToRoman import toRoman


def test_ints():
    assert toRoman.convertNum(1) == 'I'
    assert toRoman.convertNum(100) == 'C'
    assert toRoman.convertNum(541) == 'DXLI'
    assert toRoman.convertNum(3999) == 'MMMCMXCIX'
