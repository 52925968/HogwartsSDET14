# 测试计算器代码
import pytest
import sys

print(sys.path.append('..'))
from pythoncode.calc import Calculator


class TestCalc:
    def setup_class(self):
        self.cal = Calculator()
        print("类级别")

    def teardown_class(self):
        print("类级别2222")

    @pytest.mark.add
    def test_add(self):
        # cal=Calculator()
        assert 2 == self.cal.add(1, 1)

    @pytest.mark.add
    def test_add1(self):
        # cal=Calculator()
        assert 2 == self.cal.add(1, 2)

    def test_add3(self):
        # cal = Calculator()
        assert 2 == self.cal.add(1, 3)

    def test_div(self):
        # cal=Calculator()
        assert 2 == self.cal.div(2, 1)
