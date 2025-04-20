import unittest

from split_markdown import split_nodes_image, split_nodes_link
from textnode import TextNode, TextType


class TestSplitNode(unittest.TestCase):
    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_split_links(self):
        node = TextNode(
            "This is text with a [link](https://boot.dev) and another [youtube](https://youtube.com)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://boot.dev"),
                TextNode(" and another ", TextType.TEXT),
                TextNode("youtube", TextType.LINK, "https://youtube.com"),
            ],
            new_nodes,
        )

    def test_split_links_no_match(self):
        node = TextNode("This is just plain text without any links", TextType.TEXT)
        expected_result = [
            TextNode("This is just plain text without any links", TextType.TEXT)
        ]

        new_nodes = split_nodes_link([node])

        self.assertEqual(expected_result, new_nodes)

    def test_split_images_link_mixed(self):
        node = TextNode(
            "![pic](https://img.com) and [site](https://site.com)", TextType.TEXT
        )

        expected_image_result = [
            TextNode("", TextType.TEXT),
            TextNode("pic", TextType.IMAGE, "https://img.com"),
            TextNode(" and [site](https://site.com)", TextType.TEXT),
        ]

        expected_link_result = [
            TextNode("![pic](https://img.com) and ", TextType.TEXT),
            TextNode("site", TextType.LINK, "https://site.com"),
        ]

        self.assertEqual(split_nodes_image([node]), expected_image_result)
        self.assertEqual(split_nodes_link([node]), expected_link_result)

    def test_split_broken_syntax(self):
        node = TextNode("[broken](missing end", TextType.TEXT)
        expected_result = [node]

        self.assertEqual(split_nodes_link([node]), expected_result)


if __name__ == "__main__":
    unittest.main()
