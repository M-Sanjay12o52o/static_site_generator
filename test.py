# this function should return a new list of nodes.
# where any "text" type nodes in the input list are
# (potentially) split into multiple nodes based
# on the syntax
def split_nodes_delimiter(old_nodes, delimiter, text_type):
    pass


node = TextNode("This is text with a `code block` word", TextType.TEXT)
new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)

# new nodes becomes
"""
[
    TextNode("This is text with a ", TextType.TEXT),
    TextNode("code block", TextType.CODE),
    TextNode(" word", TextType.TEXT),
]
"""
