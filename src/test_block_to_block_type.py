import unittest
from markdown_to_blocks_fn import BlockType, block_to_block_type


class TestExtractMarkdown(unittest.TestCase):
    def test_paragraph_block(self):
        input = "This is a test paragraph"
        result = block_to_block_type(input)

        expected_result = BlockType.PARAGRAPH

        self.assertEqual(result, expected_result)

    def test_heading(self):
        input = "### This is heading 3"
        result = block_to_block_type(input)

        expected_result = BlockType.HEADING

        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    unittest.main()
