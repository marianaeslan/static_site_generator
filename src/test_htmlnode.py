import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    #Test that the constructor sets default values correctly
    def test_defaults(self):
        node = HTMLNode()
        self.assertIsNone(node.tag)
        self.assertIsNone(node.value)
        self.assertIsNone(node.children)
        self.assertIsNone(node.props)

    #Test props_to_html returns empty string when no props are given 
    def test_props_empty(self):
        node = HTMLNode(tag="h1")
        self.assertEqual(node.props_to_html(),'')

    #Test that to_html raises NotImplementedError
    def test_to_html_error(self):
        node = HTMLNode(tag="p", value="Some text")
        with self.assertRaises(NotImplementedError):
            node.to_html()

    def test_to_html_props(self):
        node = HTMLNode("div", "Hello, world!",None, {"class": "greeting", "href": "https://boot.dev"})
        self.assertEqual(node.props_to_html(),' class="greeting" href="https://boot.dev"')

    def test_values(self):
        node = HTMLNode("div","I wish I could read")
        self.assertEqual(node.tag,"div")
        self.assertEqual(node.value,"I wish I could read")
        self.assertEqual(node.children,None)
        self.assertEqual(node.props, None)

    def test_repr(self):
        node = HTMLNode("p", "What a strange world", None, {"class": "primary"})
        self.assertEqual(node.__repr__(),"HTMLNode(p, What a strange world, children: None, {'class': 'primary'})")


if __name__ == "__main__":
    unittest.main()