import os
import sys

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../src"))


def pytest_runtest_setup(item):
    pass


def pytest_runtest_teardown(item):
    pass
