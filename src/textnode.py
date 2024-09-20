class TextNode:
    def __init__(self, text, text_type, url = None):
        # The text content of the node
        self.text = text
        # The type of text (e.g., "bold", "italic")
        self.text_type = text_type
         # The URL if the text is a link or image, defaults to None
        self.url = url

    def __eq__(self, other):
        if isinstance(other, TextNode):
            return (self.text == other.text and 
                    self.text_type == other.text_type and 
                    self.url == other.url)
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"