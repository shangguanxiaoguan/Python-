import pytest


@pytest.fixture(scope='package', autouse=True)
def st_emptyEnv():
    print(f'\n#### 初始化-目录级别 ####')
    yield
    print(f'\n ###  清除-目录级别 ####')

