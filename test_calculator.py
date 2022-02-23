import pytest
import calculator as c
from math import pi as PI

@pytest.mark.parametrize("a, b, expected_value",[(5,2,7),
                                                (124,56,180),
                                                (-44,32,-12)])
def test_int_sum(a,b,expected_value):  
        assert c.int_sum(a,b)==expected_value


@pytest.mark.parametrize("a, b, expected_value",[(4.2,3.8,8.0),
                                                (-14.6,-2.6,-17.2)])
def test_float_sum(a,b,expected_value):  
        assert c.float_sum(a,b)==expected_value

@pytest.mark.parametrize("a, b, expected_value",[(5,2,3),
                                                (124,56,68),
                                                (-44,32,-76)])
def test_int_sub(a,b,expected_value):
    assert c.int_sub(a,b)==expected_value

@pytest.mark.parametrize("a, b, expected_value",[(4.2,3.8,0.4),
                                                (-14.6,-2.6,-12)])
def test_float_sub(a,b,expected_value):
    if isinstance(expected_value,float):
        expected_value = float(a)-float(b)
    assert c.float_sub(a,b)==expected_value

@pytest.mark.parametrize("a, b, expected_value",[(5,2,10),
                                                (124,56,6944),
                                                (-44,32,-1408)])
def test_int_mult(a,b,expected_value):
    assert c.int_mult(a,b)==expected_value

@pytest.mark.parametrize("a, b, expected_value",[(4.2,3.8,15.96),
                                                (-14.6,-2.6,37.96)])
def test_float_mult(a,b,expected_value):
    assert c.float_mult(a,b)==expected_value

@pytest.mark.parametrize("a, b, expected_value",[(5,2,2.5),
                                                (168,56,3)])
def test_int_div(a,b,expected_value):
    assert c.int_div(a,b)==int(expected_value)

@pytest.mark.parametrize("a, b, expected_value",[(5,2,2.5),
                                                (7.68,2.4,3.2)])
def test_float_div(a,b,expected_value):
    expected_value = float(a)/float(b)
    assert c.float_div(a,b)==expected_value

@pytest.mark.parametrize("a, b, expected_value",[(5,2,25),
                                                (16,0.5,4),
                                                (4.2,2,17.64)])
def test_pow(a,b,expected_value):
    assert c.pow(a,b)==expected_value

@pytest.mark.parametrize("a, expected_value",[(4,2),
                                            (144,12),
                                            (6.25,2.5)])
def test_sqrt(a,expected_value):
    assert c.sqrt(a)==expected_value

@pytest.mark.parametrize("a, expected_value",[(PI/4,1),
                                            (PI/2,0)])
def test_ctg(a,expected_value):
    assert round(c.ctg(a),8)==expected_value

@pytest.mark.parametrize("a, expected_value",[(0,1),
                                            (PI,-1)])
def test_cos(a,expected_value):
    assert round(c.cos(a),8)==expected_value

@pytest.mark.parametrize("a, expected_value",[(PI,0),
                                            (0,0)])
def test_sin(a,expected_value):
    assert round(c.sin(a),8)==expected_value