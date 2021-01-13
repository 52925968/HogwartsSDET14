# 调整测试用例的执行步骤
# 注意：多个装饰器时可能会有冲突
import pytest


@pytest.mark.run(order=3)
def test_bar1():
    assert True


@pytest.mark.run(order=2)
def test_bar2():
    assert True


@pytest.mark.first
def test_bar3():
    assert True


@pytest.mark.last
def test_bar4():
    assert True
