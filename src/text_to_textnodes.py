from split_markdown import split_nodes_image, split_nodes_link
from split_nodes import split_nodes_delimiter
from textnode import TextNode, TextType


# This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)
def text_to_textnodes(text):
    result = [TextNode(text, TextType.TEXT)]

    # split BOLD
    result = split_nodes_delimiter(result, "**", TextType.BOLD)
    # split italic
    result = split_nodes_delimiter(result, "_", TextType.ITALIC)
    # split code
    result = split_nodes_delimiter(result, "`", TextType.CODE)
    # split image
    result = split_nodes_image(result)
    # split links
    result = split_nodes_link(result)

    return result


text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"

result = text_to_textnodes(text)
print("result: ", result)

# Example: output
#
"""
[
    TextNode("This is ", TextType.TEXT),
    TextNode("text", TextType.BOLD),
    TextNode(" with an ", TextType.TEXT),
    TextNode("italic", TextType.ITALIC),
    TextNode(" word and a ", TextType.TEXT),
    TextNode("code block", TextType.CODE),
    TextNode(" and an ", TextType.TEXT),
    TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
    TextNode(" and a ", TextType.TEXT),
    TextNode("link", TextType.LINK, "https://boot.dev"),
]
"""
