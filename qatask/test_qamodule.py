import pytest
from pytest_mock import mocker
import requests
import json
import calculator as c
from math import pi as PI

def read_json(path):
    with open(path) as file:
        return json.loads(file.read())


class TestCalculator:
    @pytest.mark.parametrize("a, b, expected_value",[(5,2,7),
                                                    (124,56,180),
                                                    (-44,32,-12),
                                                    (10000,-25000,-15000)])
    def test_int_sum(self,a,b,expected_value):  
            assert c.int_sum(a,b)==expected_value


    @pytest.mark.parametrize("a, b, expected_value",[(4.2,3.8,8.0),
                                                    (-14.6,-2.6,-17.2),
                                                    (-32.0000000006,56.400000003,24.400000002400006)])
    def test_float_sum(self,a,b,expected_value):  
            assert c.float_sum(a,b)==expected_value

    @pytest.mark.parametrize("a, b, expected_value",[(5,2,3),
                                                    (124,56,68),
                                                    (-44,32,-76),
                                                    (0,0,0),
                                                    (55185157313464846,55185157313464846,0)])
    def test_int_sub(self,a,b,expected_value):
        assert c.int_sub(a,b)==expected_value

    @pytest.mark.parametrize("a, b, expected_value",[(4.2,3.8,0.4),
                                                    (-14.6,-2.6,-12),
                                                    (6631384646.8632186188,6631384646.8632186188,0)])
    def test_float_sub(self,a,b,expected_value):
        if isinstance(expected_value,float):
            expected_value = float(a)-float(b)
        assert c.float_sub(a,b)==expected_value

    @pytest.mark.parametrize("a, b, expected_value",[(5,2,10),
                                                    (124,56,6944),
                                                    (-44,32,-1408),
                                                    (654321,4321,2827321041)])
    def test_int_mult(self,a,b,expected_value):
        assert c.int_mult(a,b)==expected_value

    @pytest.mark.parametrize("a, b, expected_value",[(4.2,3.8,15.96),
                                                    (-14.6,-2.6,37.96),
                                                    (45.6343823840464,25.3541,1157.0186944033508)])
    def test_float_mult(self,a,b,expected_value):
        assert c.float_mult(a,b)==expected_value

    @pytest.mark.parametrize("a, b, expected_value",[(168,56,3),
                                                    (-100,20,-5)])
    def test_int_div(self,a,b,expected_value):
        assert c.int_div(a,b)==int(expected_value)

    def test_int_div_error(self):
        with pytest.raises(ZeroDivisionError):
            c.int_div(1,0)

    @pytest.mark.parametrize("a, b, expected_value",[(5,2,2.5),
                                                    (7.68,2.4,3.2)])
    def test_float_div(self,a,b,expected_value):
        expected_value = float(a)/float(b)
        assert c.float_div(a,b)==expected_value

    @pytest.mark.parametrize("a, b, expected_value",[(5,2,25),
                                                    (16,0.5,4),
                                                    (4.2,2,17.64)])
    def test_pow(self,a,b,expected_value):
        assert c.pow(a,b)==expected_value

    @pytest.mark.parametrize("a, expected_value",[(4,2),
                                                (144,12),
                                                (6.25,2.5)])
    def test_sqrt(self,a,expected_value):
        assert c.sqrt(a)==expected_value

    @pytest.mark.parametrize("a, expected_error",[(-9,ValueError)])
    def test_sqrt_error(self,a,expected_error):
        with pytest.raises(expected_error):
            c.sqrt(a)

    @pytest.mark.parametrize("a, expected_value",[(PI/4,1),
                                                (PI/2,0)])
    def test_ctg(self,a,expected_value):
        assert round(c.ctg(a),8)==expected_value

    @pytest.mark.parametrize("a, expected_value",[(0,1),
                                                (PI,-1)])
    def test_cos(self,a,expected_value):
        assert round(c.cos(a),8)==expected_value

    @pytest.mark.parametrize("a, expected_value",[(PI,0),
                                                (0,0)])
    def test_sin(self,a,expected_value):
        assert round(c.sin(a),8)==expected_value

class TestAPI:
    def test_get_code(self):
        assert requests.get("https://jsonplaceholder.typicode.com/users").status_code==200

    def test_header_ct_exists(self):
        assert len(requests.get("https://jsonplaceholder.typicode.com/users").headers['Content-Type'])>0
        
    def test_header_ct_values(self):
        assert requests.get("https://jsonplaceholder.typicode.com/users").headers['Content-Type']=='application/json; charset=utf-8'

    def test_body_users(self):
        req = requests.get("https://jsonplaceholder.typicode.com/users").json()
        assert len(req) == 10

class TestMock:
    def test_mock_users(self, mocker):
        mocker.patch('requests.get',return_value=read_json('qatask/user_data.json'))
        req = requests.get("https://jsonplaceholder.typicode.com/users")
        assert len(req) == 10