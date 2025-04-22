from htmlnode import HTMLNode
from leafnode import LeafNode
from markdown_to_blocks_fn import BlockType, markdown_to_block, block_to_block_type
from text_node_to_html import text_node_to_html_node
from text_to_textnodes import text_to_textnodes


def markdown_to_html_node(markdown):
    # split the markdown into blocks (we already have a fn for this)
    blocks = markdown_to_block(markdown)

    children = []

    # loop over each blocks
    for block in blocks:
        # determine the type of block
        block_type = block_to_block_type(block)
        # based on the type of block, create a new HTMLNode with the proper data

        if block_type == BlockType.PARAGRAPH:
            clean_block = block.replace("\n", " ")
            text_nodes = text_to_textnodes(clean_block)
            leaf_nodes = [text_node_to_html_node(tn) for tn in text_nodes]
            paragraph_node = HTMLNode(tag="p", children=leaf_nodes)
            children.append(paragraph_node)

        elif block_type == BlockType.CODE:
            # code_content = block.strip("`\n")  # Remove ``` and newlines
            code_content = block.replace("```", "").strip() + "\n"
            code_node = HTMLNode(
                tag="pre",
                children=[
                    HTMLNode(
                        tag="code", children=[LeafNode(tag=None, value=code_content)]
                    )
                ],
            )
            children.append(code_node)

    return HTMLNode(tag="div", children=children)


md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

# result = markdown_to_html_node(md)
# print("result: ", result)
# Expected:
# "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>"
