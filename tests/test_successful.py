import os
import unittest
from parameterized import parameterized

from submitty_config.main import lint


def load_test_cases():
    current_dir = os.path.dirname(os.path.realpath(__file__))
    ret = []
    for entry in os.scandir(os.path.join(current_dir, 'data')):
        ret.append([entry.name, os.path.join(current_dir, 'data', entry.name)])
    return ret


class TestSuccessful(unittest.TestCase):
    @parameterized.expand(load_test_cases())
    def test_succesful(self, _, file_path):
        lint(file_path)


if __name__ == '__main__':
    unittest.main()