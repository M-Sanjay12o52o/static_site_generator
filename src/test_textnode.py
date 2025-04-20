import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD, None)
        node2 = TextNode("This is a text node", TextType.BOLD, None)
        self.assertEqual(node, node2)

    def test_url_different(self):
        node = TextNode("This is a text node", TextType.BOLD, None)
        node2 = TextNode("This is a text node", TextType.BOLD, "https:boot.dev.com")
        self.assertNotEqual(node, node2)

    def test_text_type(self):
        node = TextNode("This is a text node", TextType.BOLD, None)
        node2 = TextNode("This is a text node", TextType.ITALIC, None)
        self.assertNotEqual(node, node2)

    def test_text_difference(self):
        node = TextNode("This is a text node", TextType.BOLD, None)
        node2 = TextNode(
            "This is a text node but different from the above", TextType.BOLD, None
        )
        self.assertNotEqual(node, node2)

    def test_comparison_with_different_type(self):
        node = TextNode("This is a text node", TextType.BOLD, None)
        node2 = None
        self.assertNotEqual(node, node2)

    def test_empty_text_not_equal(self):
        node = TextNode("This is a text node", TextType.BOLD, None)
        node2 = TextNode("", TextType.BOLD, None)
        self.assertNotEqual(node, node2)


if __name__ == "__main__":
    unittest.main()
