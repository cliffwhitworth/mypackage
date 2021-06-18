import pytest

from mypackage.myexample import example


@pytest.fixture()
def example_test():
    txt = 'hello'
    return example(txt)