import pytest
from arabicToRoman import toRoman

# Define functions to test file arabicToRoman.py
def test_ints():
    assert toRoman.convertNum(1) == 'I'
    assert toRoman.convertNum(100) == 'C'
    assert toRoman.convertNum(541) == 'DXLI'
    assert toRoman.convertNum(3999) == 'MMMCMXCIX'

def test_incorrect_type():
    with pytest.raises(TypeError):
        toRoman.convertNum('100')

    with pytest.raises(TypeError):
        toRoman.convertNum('#')

    with pytest.raises(TypeError):
        toRoman.convertNum('1#')

    with pytest.raises(TypeError):
        toRoman.convertNum('MCX')

    with pytest.raises(TypeError):
        toRoman.convertNum()
    
    with pytest.raises(TypeError):
        toRoman.convertNum(0.64)

    with pytest.raises(TypeError):
        toRoman.convertNum(5.041)

    with pytest.raises(TypeError):
        toRoman.convertNum(-123.4)

def test_incorrect_range():
    with pytest.raises(ValueError):
        toRoman.convertNum(4000)

    with pytest.raises(ValueError):
        toRoman.convertNum(0)

    with pytest.raises(ValueError):
        toRoman.convertNum(-100)

    with pytest.raises(ValueError):
        toRoman.convertNum(10**1000)