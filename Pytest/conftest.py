"""
It is use to connect pytest fixtures to all  files within package

We can implement pytest fixture by two ways
1] Passing method name of fixture as arguments in another test methods
2] Passing parameter of scope=session and autouse=True

"""
import pytest


@pytest.fixture(scope="session",autouse=True)
def setup():
    print("Open browser")
    yield
    print("Close browser")

@pytest.fixture(scope="function",autouse=True)
def function():
    print("at function level")