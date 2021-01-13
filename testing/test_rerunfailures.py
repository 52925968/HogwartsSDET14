# 执行失败的测试用例重复执行
# 1.控制台直接执行 pytest -vs--reruns 3 pytest_rerunfailures.py
# 2.执行时间隔1s  pytest -vs--reruns 5--reruns-delay 1
# 3.直接在用例上增加标签：@pytest.mark.flaky(rerun=5,reruns_delay=1)
import pytest


@pytest.mark.flaky(reruns=3, reruns_delay=1)
def test_rerunfa():
    assert 1 == 2


# 场景：多条断言，assert如果第一条执行失败，其他就不执行了；使用pytest.assume可以继续进行执行
def test_rerunfa2():
    pytest.assume(3 == 3)
    pytest.assume(1 == 2)
    pytest.assume(2 == 3)
    pytest.assume(5 == 5)
