import unittest

from extract_markdown import extract_markdown_images, extract_markdown_links


class TestExtractMarkdown(unittest.TestCase):
    def test_extarct_images(self):
        text = "![dog](https://i.com/dog.jpg) and ![cat](https://i.com/cat.jpg)"
        result = extract_markdown_images(text)

        expected_output = [
            ("dog", "https://i.com/dog.jpg"),
            ("cat", "https://i.com/cat.jpg"),
        ]

        self.assertEqual(expected_output, result)

    def test_extract_images(self):
        text = "![sun](https://i.com/sun.jpg) and [google](https://google.com)"
        result = extract_markdown_images(text)

        expected_output = [("sun", "https://i.com/sun.jpg")]

        self.assertEqual(expected_output, result)

    def test_extract_no_images(self):
        text = "[link](https://site.com) and another [link](https://a.com)"

        result = extract_markdown_images(text)

        expected_result = []

        self.assertEqual(expected_result, result)

    def test_extract_no_links(self):
        text = "![meme](https://img.com/meme.jpg)"

        result = extract_markdown_links(text)

        expected_result = []

        self.assertEqual(expected_result, result)

    def test_extract_mixed_content(self):
        text = "Check this ![logo](https://img.com/logo.png) and visit [homepage](https://site.com)"

        resut_links = extract_markdown_links(text)
        result_images = extract_markdown_images(text)

        expected_result = [("logo", "https://img.com/logo.png")]

        self.assertEqual(result_images, expected_result)

    def test_extract_mixed_content_two(self):
        text = "Check this ![logo](https://img.com/logo.png) and visit [homepage](https://site.com)"

        result_links = extract_markdown_links(text)

        expected_result = [("homepage", "https://site.com")]

        self.assertEqual(result_links, expected_result)


if __name__ == "__main__":
    unittest.main()
