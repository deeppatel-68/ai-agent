import os
import sys
import unittest

# Add the functions directory to sys.path BEFORE importing
sys.path.append(os.path.abspath(os.path.join(
    os.path.dirname(__file__), 'functions')))
from get_file_content import get_file_content


class TestGetFileContent(unittest.TestCase):
    def test_file_content_truncate(self):
        content = get_file_content("calculator", "pkg/lorem.txt")
        print(repr(content))

        self.assertGreater(len(content), 10000)
        self.assertIn('truncated at 10000 characters', content)

    def test_file_content_main(self):
        content = get_file_content("calculator", "main.py")
        print(content)

        self.assertIsInstance(content, str)
        self.assertFalse(content.startswith("Error:"))

    def test_file_content_pkg_calculator(self):
        content = get_file_content("calculator", "pkg/calculator.py")
        print(content)
        self.assertIsInstance(content, str)
        self.assertFalse(content.startswith("Error:"))

    def test_file_content_outside(self):
        content = get_file_content("calculator", "/bin/cat")
        print(content)
        self.assertTrue(content.startswith("Error:"))


if __name__ == "__main__":
    unittest.main()
