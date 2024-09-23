import unittest
from txt_textnodes import text_to_textnodes
from textnode import TextNode

class TestTextToTextnodes(unittest.TestCase):
    
    def test_simple_text(self):
        text = "This is a simple text."
        expected = [TextNode("This is a simple text.", "text")]
        result = text_to_textnodes(text)
        self.assertEqual(result, expected)

    def test_bold_text(self):
        text = "This is **bold** text."
        expected = [
            TextNode("This is ", "text"),
            TextNode("bold", "bold"),
            TextNode(" text.", "text"),
        ]
        result = text_to_textnodes(text)
        self.assertEqual(result, expected)

    def test_italic_and_code(self):
        text = "This is *italic* and `code`."
        expected = [
            TextNode("This is ", "text"),
            TextNode("italic", "italic"),
            TextNode(" and ", "text"),
            TextNode("code", "code"),
            TextNode(".", "text"),
        ]
        result = text_to_textnodes(text)
        self.assertEqual(result, expected)

    def test_image_and_link(self):
        text = "This is an ![image](https://example.com/image.jpg) and a [link](https://example.com)."
        expected = [
            TextNode("This is an ", "text"),
            TextNode("", "image", {"src": "https://example.com/image.jpg", "alt": "image"}),
            TextNode(" and a ", "text"),
            TextNode("link", "link", "https://example.com"),
            TextNode(".", "text"),
        ]
        result = text_to_textnodes(text)
        self.assertEqual(result, expected)

    def test_combined(self):
        text = "This is **bold** and *italic* with `code`, ![image](https://example.com/image.jpg), and [link](https://example.com)."
        expected = [
            TextNode("This is ", "text"),
            TextNode("bold", "bold"),
            TextNode(" and ", "text"),
            TextNode("italic", "italic"),
            TextNode(" with ", "text"),
            TextNode("code", "code"),
            TextNode(", ", "text"),
            TextNode("", "image", {"src": "https://example.com/image.jpg", "alt": "image"}),
            TextNode(", and ", "text"),
            TextNode("link", "link", "https://example.com"),
            TextNode(".", "text"),
        ]
        result = text_to_textnodes(text)
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()