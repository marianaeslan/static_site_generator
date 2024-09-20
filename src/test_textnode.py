import unittest
from textnode import TextNode

class TestTextNode(unittest.TestCase):
    # Test when all properties are equal
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    # Test when the text_type property is different
    def test_dif(self):
        node = TextNode("This is a text node", "bold", "http://example.com")
        node2 = TextNode("This is a text node", "italic", "http://example.com")
        self.assertNotEqual(node, node2)

    # Test when the url property is None
    def test_none_url(self):
        node = TextNode("This is a text node", "bold", None)
        node2 = TextNode("This is a text node", "bold", None)
        self.assertEqual(node, node2)

    # Test when the url property is different
    def test_is_different_url(self):
        node = TextNode("This is a text node", "bold", "http://example.com")
        node2 = TextNode("This is a text node", "bold", "http://other.com")
        self.assertNotEqual(node, node2)
        
 # Test when the text property is different
    def test__different_text(self):
        node = TextNode("Sample Text", "bold", "http://example.com")
        node2 = TextNode("Different Text", "bold", "http://example.com")
        self.assertNotEqual(node, node2)   

if __name__ == "__main__":
    unittest.main()
