import unittest

from extract_title import extract_title


class TestExtractTitle(unittest.TestCase):
    def test_one_line_markdown(self):
        result = extract_title("# My Blog Post")
        expected_result = "My Blog Post"

        self.assertEqual(result, expected_result)

    def test_multiline(self):
        result = extract_title("# The Heading one\n ## The Heading two")
        expected_result = "The Heading one"

        self.assertEqual(result, expected_result)

    def test_title_without_space(self):
        result = extract_title("# Another Title\nSome paragraph text")
        expected_result = "Another Title"

        self.assertEqual(result, expected_result)

    def test_subtitle(self):
        with self.assertRaises(Exception):
            extract_title("## Subtitle Only\nSome text")

    def test_no_title(self):
        with self.assertRaises(Exception):
            extract_title("Random text without any heading")

    def test_heading_three(self):
        with self.assertRaises(Exception):
            extract_title("### Heading Three but no H1")

    def test_eq(self):
        actual = extract_title("# This is a title")
        self.assertEqual(actual, "This is a title")

    def test_eq_double(self):
        actual = extract_title(
            """
# This is a title

# This is a second title that should be ignored
"""
        )
        self.assertEqual(actual, "This is a title")

    def test_eq_long(self):
        actual = extract_title(
            """
# title

this is a bunch

of text

- and
- a
- list
"""
        )
        self.assertEqual(actual, "title")

    def test_none(self):
        try:
            extract_title(
                """
no title
"""
            )
            self.fail("Should have raised an exception")
        except Exception as e:
            pass


if __name__ == "__main__":
    unittest.main()
