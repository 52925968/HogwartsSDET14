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
    # @pytest.mark.parametrize(("sum", "a", "b"), yaml.safe_load(open("data/calc.yml")))
    # def test_add1(self, sum, a, b):
    #     # cal=Calculator()
    #     assert sum == self.cal.add(a, b)

    def test_add3(self):
        # cal = Calculator()
        assert 2 == self.cal.add(1, 3)

    # 参数化
    @pytest.mark.parametrize("sum,a,b", [(3, 2, 2), (5, 5, 1)])
    def test_div(self, sum, a, b):
        # cal=Calculator()
        assert sum == self.cal.div(a, b)


with open("data/calc.yml") as f:
    datas = yaml.safe_load(f)
    myids = datas['add'].keys()
    mydatas = datas['add'].values()


def get_steps():
    with open("steps/add.yml") as f:
        steps = yaml.safe_load(f)

    return steps


cal = Calculator()


def steps(a, b, result):
    steps1 = get_steps()
    for step in steps1:
        if 'add1' == step:
            assert result == cal.add1(a, b)
        elif 'add2' == step:
            assert result == cal.add2(a, b)
        elif 'add3' == step:
            assert result == cal.add3(a, b)


@pytest.mark.parametrize('a,b,result', mydatas, ids=myids)
def test_add4(a, b, result):
    steps(a, b, result)
