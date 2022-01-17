import  pytest
# fixture标记的函数可以用装饰器来指定使用

@pytest.fixture()
def fix1():
    print("引入fix1")


@pytest.fixture()
def fix2():
    print("引入fix2")


@pytest.mark.usefixtures('fix1')
def test01():
    print("用例1执行")


if __name__ == '__main__':
    pytest.main(["-s", "test_usefixture.py"])