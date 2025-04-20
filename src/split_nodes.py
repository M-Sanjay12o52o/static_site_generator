from textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    result_list = []

    if not delimiter:
        return old_nodes

    for item in old_nodes:
        text = item.text
        parts = text.split(delimiter)

        if len(parts) < 3 or len(parts) % 2 == 0:
            result_list.append(item)
            continue

        for i, part in enumerate(parts):
            if i % 2 == 0:
                if part:
                    result_list.append(TextNode(part, item.text_type))
            else:
                if part:
                    result_list.append(TextNode(part, text_type))

    return result_list


# node = TextNode("This is text with a `code block` word", TextType.TEXT)
# new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)

# print("new_nodes: ", new_nodes)


node1 = TextNode("This is just one long string with no text_type in it", TextType.TEXT)
new_nodes1 = split_nodes_delimiter([node1], "", TextType.TEXT)

# print("new_nodes1: ", new_nodes1)

# node2 = TextNode("**THIS IS AN EXAMPLE** of text_type in the beginning", TextType.TEXT)
# new_nodes2 = split_nodes_delimiter([node2], "**", TextType.BOLD)

# node3 = TextNode("This is an example with delimiter in the **END**", TextType.TEXT)
# new_nodes3 = split_nodes_delimiter([node3], "**", TextType.BOLD)

# one that doesn't contain any delimiter
#   Ex: "This is just one long string with no text_type in it"
# one that contains the delimiter at the beginning
#   Ex: "**THIS IS AN EXAMPLE** of text_type in the beginning"
# one where the delimiter string is the last string
#   Ex: "This is an example with delimiter in the **END**"
# delimiter in the middle of the string
#  Ex: "This is text with a `code block` word"

# Question:
# How does the if else statements work with
# the above different scenarios


"""
[
    TextNode("This is text with a ", TextType.TEXT),
    TextNode("code block", TextType.CODE),
    TextNode(" word", TextType.TEXT),
]
"""
