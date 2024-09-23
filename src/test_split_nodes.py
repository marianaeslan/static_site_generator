import unittest
from split_nodes import split_nodes_image, split_nodes_link
from textnode import TextNode

class TestSplitNodes(unittest.TestCase):

    def test_split_nodes_image(self):
        node = TextNode(
            "Look at this image ![cat](https://example.com/cat.png) and another ![dog](https://example.com/dog.jpg)",
            "text"
        )
        new_nodes = split_nodes_image([node])
        expected = [
            TextNode("Look at this image ", "text"),
            TextNode("", "image", {"src": "https://example.com/cat.png", "alt": "cat"}),
            TextNode(" and another ", "text"),
            TextNode("", "image", {"src": "https://example.com/dog.jpg", "alt": "dog"}),
        ]
        self.assertEqual(new_nodes, expected)

    def test_split_nodes_link(self):
        node = TextNode(
            "Visit [Google](https://www.google.com) and [GitHub](https://github.com)",
            "text"
        )
        new_nodes = split_nodes_link([node])
        expected = [
            TextNode("Visit ", "text"),
            TextNode("Google", "link", "https://www.google.com"),
            TextNode(" and ", "text"),
            TextNode("GitHub", "link", "https://github.com"),
        ]
        self.assertEqual(new_nodes, expected)

    def test_no_image(self):
        node = TextNode("This text has no image", "text")
        new_nodes = split_nodes_image([node])
        self.assertEqual(new_nodes, [node])

    def test_no_link(self):
        node = TextNode("This text has no link", "text")
        new_nodes = split_nodes_link([node])
        self.assertEqual(new_nodes, [node])

if __name__ == "__main__":
    unittest.main()