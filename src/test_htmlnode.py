import unittest
from htmlnode import *

class TestHTMLNode(unittest.TestCase):
    def test_to_html_props(self):
        node = HTMLNode(
            "div",
            "Hello, world!",
            None,
            {"class": "greeting", "href": "https://boot.dev"},
        )
        self.assertEqual(
            node.props_to_html(),
            ' class="greeting" href="https://boot.dev"',
        )

    def test_values(self):
        node = HTMLNode(
            "div",
            "I wish I could read",
        )
        self.assertEqual(
            node.tag,
            "div",
        )
        self.assertEqual(
            node.value,
            "I wish I could read",
        )
        self.assertEqual(
            node.children,
            None,
        )
        self.assertEqual(
            node.props,
            None,
        )

    def test_repr(self):
        node = HTMLNode(
            "p",
            "What a strange world",
            None,
            {"class": "primary"},
        )
        self.assertEqual(
            node.__repr__(),
            "HTMLNode(p, What a strange world, children: None, {'class': 'primary'})",
        )

    def test_to_html_no_children(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")

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

    def test_to_html_many_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
        )

    def test_headings(self):
        node = ParentNode(
            "h2",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<h2><b>Bold text</b>Normal text<i>italic text</i>Normal text</h2>",
        )
# Test conversion of plain text
    def test_text_type_text(self):
        text_node = TextNode("This is plain text", text_type_text)
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.to_html(), "This is plain text")

    # Test conversion of bold text
    def test_text_type_bold(self):
        text_node = TextNode("Bold text", text_type_bold)
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.to_html(), "<b>Bold text</b>")

    # Test conversion of italic text
    def test_text_type_italic(self):
        text_node = TextNode("Italic text", text_type_italic)
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.to_html(), "<i>Italic text</i>")

    # Test conversion of code text
    def test_text_type_code(self):
        text_node = TextNode("Code snippet", text_type_code)
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.to_html(), "<code>Code snippet</code>")

    # Test conversion of link text
    def test_text_type_link(self):
        text_node = TextNode("Boot.dev", text_type_link, href="https://boot.dev")
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.to_html(), '<a href="https://boot.dev">Boot.dev</a>')

    # Test conversion of image text
    def test_text_type_image(self):
        text_node = TextNode("", text_type_image, src="https://boot.dev/logo.png", alt="Boot.dev logo")
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.to_html(), '<img src="https://boot.dev/logo.png" alt="Boot.dev logo"></img>')

    # Test invalid link (missing href)
    def test_invalid_link(self):
        text_node = TextNode("Link without href", text_type_link)
        with self.assertRaises(ValueError) as context:
            text_node_to_html_node(text_node)
        self.assertEqual(str(context.exception), "Link TextNode must have an href.")

    # Test invalid image (missing src or alt)
    def test_invalid_image(self):
        text_node = TextNode("", text_type_image, src=None, alt="Missing src")
        with self.assertRaises(ValueError) as context:
            text_node_to_html_node(text_node)
        self.assertEqual(str(context.exception), "Image TextNode must have src and alt.")

    # Test unknown text type
    def test_unknown_text_type(self):
        text_node = TextNode("Unknown type", "unknown")
        with self.assertRaises(ValueError) as context:
            text_node_to_html_node(text_node)
        self.assertEqual(str(context.exception), "Unknown text node type: unknown")




if __name__ == "__main__":
    unittest.main()