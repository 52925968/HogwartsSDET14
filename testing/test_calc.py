# 测试计算器代码
import pytest
import sys

import yaml

print(sys.path.append('..'))
from pythoncode.calc import Calculator


class TestCalc:
    def setup_class(self):
        self.cal = Calculator()
        print("类级别")

    def teardown_class(self):
        print("类级别2222")

    # 增加标签（可以单独运行某个标签）
    @pytest.mark.add
    def test_add(self):
        # cal=Calculator()
        assert 2 == self.cal.add(1, 1)

    # 使用yamL的参数化
    @pytest.mark.parametrize(("sum", "a", "b"), yaml.safe_load(open("./data.yaml")))
    def test_add1(self, sum, a, b):
        # cal=Calculator()
        assert sum == self.cal.add(a, b)

    def test_add3(self):
        # cal = Calculator()
        assert 2 == self.cal.add(1, 3)

    # 参数化
    @pytest.mark.parametrize("sum,a,b", [(3, 2, 2), (5, 5, 1)])
    def test_div(self, sum, a, b):
        # cal=Calculator()
        assert sum == self.cal.div(a, b)
