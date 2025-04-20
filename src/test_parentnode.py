import unittest

from parentnode import ParentNode
from leafnode import LeafNode


class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    # Nesting parentnode objects inside of one another
    def test_nesting_parentnode(self):
        child_h1 = LeafNode("h1", "This is a heading")
        child_p1 = LeafNode("p", "This is paragraph one")
        child_p2 = LeafNode("p", "This is paragraph two")

        inner_div_1 = ParentNode("div", [child_h1])
        inner_div_2 = ParentNode("div", [child_p1, child_p2])

        outer_div = ParentNode("div", [inner_div_1, inner_div_2])

        expected_html = (
            "<div>"
            "<div><h1>This is a heading</h1></div>"
            "<div><p>This is paragraph one</p><p>This is paragraph two</p></div>"
            "</div>"
        )

        result_html = outer_div.to_html()

        self.assertEqual(result_html, expected_html)

    def test_multiple_children(self):
        child_h1 = LeafNode("h1", "This is a heading")
        child_p1 = LeafNode("p", "This is paragraph one")
        child_p2 = LeafNode("p", "This is paragraph two")

        outer_div = ParentNode("div", [child_h1, child_p1, child_p2])

        expected_html = (
            "<div>"
            "<h1>This is a heading</h1>"
            "<p>This is paragraph one</p>"
            "<p>This is paragraph two</p>"
            "</div>"
        )

        result_html = outer_div.to_html()

        self.assertEqual(result_html, expected_html)

    def test_no_children(self):
        outer_div = ParentNode("div", [])

        expected_html = "<div></div>"

        result_html = outer_div.to_html()

        self.assertEqual(result_html, expected_html)


if __name__ == "__main__":
    unittest.main()
