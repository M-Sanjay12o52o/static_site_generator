import re
from enum import Enum


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"


def block_to_block_type(block: str) -> BlockType:
    lines = block.strip().split("\n")

    if re.match(r"^#{1,6} ", lines[0]):
        return BlockType.HEADING

    if lines[0].startswith("```") and lines[-1].startswith("```"):
        return BlockType.CODE

    if all(line.startswith("> ") for line in lines):
        return BlockType.QUOTE

    if all(line.startswith("- ") for line in lines):
        return BlockType.UNORDERED_LIST

    if all(re.match(r"^\d+\.\s", line) for line in lines):
        return BlockType.ORDERED_LIST

    return BlockType.PARAGRAPH


def get_block_type(line):
    if re.match(r"^#{1,6} ", line):
        return "heading"
    elif re.match(r"^\d+\.\s", line):
        return "ordered-list"
    elif re.match(r"^[-*+]\s", line):
        return "unordered-list"
    else:
        return "paragraph"


def markdown_to_block(markdown):
    result = []

    lines = markdown.split("\n")
    # cleaned = [line.strip() for line in lines if line.strip()]

    current_block = ""
    current_type = None

    for line in lines:
        # block_type = get_block_type(line)
        stripped = line.strip()

        if not stripped:
            if current_block:
                result.append(current_block.strip())
                current_block = ""
                current_type = None
            continue

        block_type = get_block_type(stripped)

        if block_type == "heading":
            if current_block:
                result.append(current_block.strip())
                current_block = ""
            result.append(line.strip())
            current_type = None

        elif block_type in ["unordered-list", "ordered-list"]:
            if current_type == block_type:
                current_block += "\n" + stripped
            else:
                if current_block:
                    result.append(current_block.strip())
                current_block = stripped
                current_type = block_type

        elif block_type == "paragraph":
            if current_type == "paragraph":
                current_block += "\n" + line
            else:
                if current_block:
                    result.append(current_block.strip())
                current_block = line
                current_type = "paragraph"

    if current_block:
        result.append(current_block.strip())

    return result


# example_markdown = """# This is a heading
#
# This is a paragraph of text. It has some **bold** and _italic_ words inside of it.
#
# - This is the first list item in a list block
# - This is a list item
# - This is another list item
# """
# result = markdown_to_block(example_markdown)
#
# print("result: ", result)
#
#
md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""

result = markdown_to_block(md)
# print("result: ", result)
