class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("to_html method not implemented")

    def props_to_html(self):
        if self.props is None:
            return ""
        props_html = ""
        for prop in self.props:
            props_html += f' {prop}="{self.props[prop]}"'
        return props_html

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("Invalid HTML: no value")
        if self.tag is None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("Invalid HTML: no tag")
        if self.children is None:
            raise ValueError("Invalid HTML: no children")
        children_html = ""
        for child in self.children:
            children_html += child.to_html()
        return f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"

    def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"
    
class TextNode:
    def __init__(self, text, text_type, href=None, src=None, alt=None):
        self.text = text
        self.text_type = text_type
        self.href = href
        self.src = src
        self.alt = alt

# Definir tipos de texto
text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = "link"
text_type_image = "image"
    
def text_node_to_html_node(text_node):
    if text_node.text_type == text_type_text:
        # No tag, raw text
        return LeafNode(tag=None, value=text_node.text)
    elif text_node.text_type == text_type_bold:
        # <b> tag for bold
        return LeafNode(tag="b", value=text_node.text)
    elif text_node.text_type == text_type_italic:
        # <i> tag for italic
        return LeafNode(tag="i", value=text_node.text)
    elif text_node.text_type == text_type_code:
        # <code> tag for code
        return LeafNode(tag="code", value=text_node.text)
    elif text_node.text_type == text_type_link:
        # <a> tag for link, requires 'href' prop
        if text_node.href is None:
            raise ValueError("Link TextNode must have an href.")
        return LeafNode(tag="a", value=text_node.text, props={"href": text_node.href})
    elif text_node.text_type == text_type_image:
        # <img> tag for image, requires 'src' and 'alt' props
        if text_node.src is None or text_node.alt is None:
            raise ValueError("Image TextNode must have src and alt.")
        return LeafNode(tag="img", value="", props={"src": text_node.src, "alt": text_node.alt})
    else:
        raise ValueError(f"Unknown text node type: {text_node.text_type}")

