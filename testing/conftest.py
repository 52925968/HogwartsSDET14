from typing import List

import pytest
import yaml


def pytest_collection_modifyitems(
        session: "Session", config: "Config", items: List["Item"]
) -> None:
    items.reverse()
    for item in items:
        item.name = item.name.encode('utf-8').decode('raw_unicode_escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('raw_unicode_escape')


def pytest_addoption(parser):
    mygroup = parser.getgroup("hogwarts")
    mygroup.addoption("--env",  # 注册一个命令行选项
                      default='test',
                      dest='env',
                      help='set your run env'
                      )


@pytest.fixture(scope='session')
def cmdoption(request):
    myenv = request.config.getoption("--env", default='test')
    if myenv == 'test':
        datapath = 'data/test/data.yml'

    if myenv == 'dev':
        datapath = 'data/dev/data.yml'

    with open(datapath) as f:
        datas = yaml.safe_load(f)

    return myenv, datas


# 通过方法动态的生成测试用例
def pytest_generate_tests(metafunc: "metafunc") -> None:
    if "param" in metafunc.fixturenames:
        metafunc.parametrize("param",
                             metafunc.module.mydatas,
                             ids=metafunc.module.myids,
                             scope='function')
