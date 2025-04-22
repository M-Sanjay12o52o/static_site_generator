import unittest

from markdown_to_blocks_fn import markdown_to_block


class TestMarkdownToBlock(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_block(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_heading_paragraph_unordered_list(self):
        md = """
# Heading

This is a paragraph.

- One
- Two
"""
        blocks = markdown_to_block(md)
        self.assertEqual(blocks, ["# Heading", "This is a paragraph.", "- One\n- Two"])

    def test_multiple_paragraphs(self):
        md = """
This is paragraph one

This is paragraph two

This is paragraph three

This is paragraph four
"""
        blocks = markdown_to_block(md)
        self.assertEqual(
            blocks,
            [
                "This is paragraph one",
                "This is paragraph two",
                "This is paragraph three",
                "This is paragraph four",
            ],
        )

    def test_ordered_list(self):
        md = """
1. This is ordered list item one 
2. This is ordered list item two
3. This is ordered list item three
4. This is oredred list item four
"""
        blocks = markdown_to_block(md)
        self.assertEqual(
            blocks,
            [
                "1. This is ordered list item one\n2. This is ordered list item two\n3. This is ordered list item three\n4. This is oredred list item four"
            ],
        )

    def test_mixed_block_types(self):
        md = """
1. This is ordered list item one 
2. This is ordered list item two
3. This is ordered list item three
4. This is oredred list item four

# This is heading one

- This is ordered list item one 
- This is ordered list item two
- This is ordered list item three
- This is oredred list item four

## This is heading two
"""

        blocks = markdown_to_block(md)
        self.assertEqual(
            blocks,
            [
                "1. This is ordered list item one\n2. This is ordered list item two\n3. This is ordered list item three\n4. This is oredred list item four",
                "# This is heading one",
                "- This is ordered list item one\n- This is ordered list item two\n- This is ordered list item three\n- This is oredred list item four",
                "## This is heading two",
            ],
        )
