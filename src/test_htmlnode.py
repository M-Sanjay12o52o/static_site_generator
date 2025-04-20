import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node1 = HTMLNode(props={"href": "https://example.com", "target": "_blank"})

        node1_result = node1.props_to_html()
        expected_result = ' href="https://example.com" target="_blank"'

        self.assertEqual(node1_result, expected_result)

    def test_empty_props(self):
        node1 = HTMLNode(props={})

        expected_result = ""

        node1_result = node1.props_to_html()

        self.assertEqual(node1_result, expected_result)

    def test_single_prop(self):
        node1 = HTMLNode(props={"class": "main"})
        expected_result = ' class="main"'

        node1_result = node1.props_to_html()

        self.assertEqual(node1_result, expected_result)


if __name__ == "__main__":
    unittest.main()
