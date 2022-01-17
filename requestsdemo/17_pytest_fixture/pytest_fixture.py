import pytest


@pytest.fixture
def first_fix():
    return ["a"]


def test_case01(first_fix):
    first_fix.append("b")
    assert first_fix == ["a", "b"]
    print(first_fix)


if __name__ == '__main__':

    # print("gsd啊哈哈g")
    pytest.main(["-s", "pytest_fixture.py"])
    # print("fsgsgfsg")
