import unittest

from split_nodes import split_nodes_delimiter
from textnode import TextNode, TextType


class TestSplitNode(unittest.TestCase):
    def test_split_single_code_block(self):
        node = TextNode("This is `code`.", TextType.TEXT)
        result = split_nodes_delimiter([node], "`", TextType.CODE)

        expected_result = [
            TextNode("This is ", TextType.TEXT),
            TextNode("code", TextType.CODE),
            TextNode(".", TextType.TEXT),
        ]

        self.assertEqual(expected_result, result)

    def test_split_mixed_nodes(self):
        node1 = TextNode("Hello ", TextType.TEXT)
        node2 = TextNode("`world` !", TextType.TEXT)
        result = split_nodes_delimiter([node1, node2], "`", TextType.CODE)

        expected_result = [
            TextNode("Hello ", TextType.TEXT),
            TextNode("world", TextType.CODE),
            TextNode(" !", TextType.TEXT),
        ]

        self.assertEqual(expected_result, result)

    def test_split_no_delimiter(self):
        node = TextNode("Nothing to split here.", TextType.TEXT)
        result = split_nodes_delimiter([node], "", TextType.TEXT)

        expected_result = [TextNode("Nothing to split here.", TextType.TEXT)]

        self.assertEqual(expected_result, result)

    def test_split_unclosed_delimiter(self):
        node = TextNode("Start of `something strange", TextType.TEXT)
        result = split_nodes_delimiter([node], "`", TextType.CODE)

        expected_result = [TextNode("Start of `something strange", TextType.TEXT)]

        self.assertEqual(expected_result, result)

    def test_multiple_delimiter(self):
        node = TextNode("A `B` and `C`.", TextType.TEXT)
        result = split_nodes_delimiter([node], "`", TextType.CODE)

        expected_result = [
            TextNode("A ", TextType.TEXT),
            TextNode("B", TextType.CODE),
            TextNode(" and ", TextType.TEXT),
            TextNode("C", TextType.CODE),
            TextNode(".", TextType.TEXT),
        ]

        self.assertEqual(expected_result, result)


if __name__ == "__main__":
    unittest.main()
