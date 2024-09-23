import unittest
from markdown_extractor import extract_markdown_images, extract_markdown_links

class TestMarkdownExtraction(unittest.TestCase):

    def test_extract_markdown_images(self):
        text = "Look at this ![cat](https://example.com/cat.png) and ![dog](https://example.com/dog.jpg)"
        expected = [("cat", "https://example.com/cat.png"), ("dog", "https://example.com/dog.jpg")]
        self.assertEqual(extract_markdown_images(text), expected)

    def test_extract_markdown_images_no_images(self):
        text = "There are no images here!"
        expected = []
        self.assertEqual(extract_markdown_images(text), expected)

    def test_extract_markdown_links(self):
        text = "Visit [Google](https://www.google.com) and [GitHub](https://github.com)"
        expected = [("Google", "https://www.google.com"), ("GitHub", "https://github.com")]
        self.assertEqual(extract_markdown_links(text), expected)

    def test_extract_markdown_links_no_links(self):
        text = "There are no links here!"
        expected = []
        self.assertEqual(extract_markdown_links(text), expected)

if __name__ == "__main__":
    unittest.main()