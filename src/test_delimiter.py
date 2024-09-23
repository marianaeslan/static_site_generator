import unittest
from split_delimiter import *

class TestNodesDelimiter(unittest.TestCase):
    def test_split_bold(self):
        node = TextNode("This is **bold** text", text_type_text)
        new_nodes = split_nodes_delimiter([node], "**", text_type_bold)

        expected_nodes = [
            TextNode("This is ", text_type_text),
            TextNode("bold", text_type_bold),
            TextNode(" text", text_type_text),
        ]

        self.assertEqual(
            [n.__repr__() for n in new_nodes],
            [n.__repr__() for n in expected_nodes]
        )
        
    def test_split_italic(self):
        node = TextNode("This is *italic* text", text_type_text)
        new_nodes = split_nodes_delimiter([node], "*", text_type_italic)

        expected_nodes = [
            TextNode("This is ", text_type_text),
            TextNode("italic", text_type_italic),
            TextNode(" text", text_type_text),
        ]

        self.assertEqual(
            [n.__repr__() for n in new_nodes],
            [n.__repr__() for n in expected_nodes]
        )

    def test_split_with_code_block(self):
        node = TextNode("This is text with a `code block` word", text_type_text)
        new_nodes = split_nodes_delimiter([node], "`", text_type_code)

        expected_nodes = [
            TextNode("This is text with a ", text_type_text),
            TextNode("code block", text_type_code),
            TextNode(" word", text_type_text),
        ]

        self.assertEqual(
            [n.__repr__() for n in new_nodes],
            [n.__repr__() for n in expected_nodes]
        )
    def test_no_matching_delimiter(self):
        node = TextNode("This is text with a `code block word", text_type_text)
        with self.assertRaises(ValueError) as context:
            split_nodes_delimiter([node], "`", text_type_code)
        self.assertEqual(str(context.exception), "Delimiter type not found")

    def test_no_splitting_needed(self):
        node = TextNode("This is plain text", text_type_text)
        new_nodes = split_nodes_delimiter([node], "`", text_type_code)

        expected_nodes = [TextNode("This is plain text", text_type_text)]

        self.assertEqual(
            [n.__repr__() for n in new_nodes],
            [n.__repr__() for n in expected_nodes]
        )

if __name__ == "__main__":
    unittest.main()