class HTMLNode:
    def __init__(self, tag = None, value = None, children = None, props = None):
        #tag -> a string representing the html tag name
        #value -> a string representing the value of the html tag
        #children -> a list of htmlNode objects representing the children of this node
        #props -> a dictionary key-value representing the attributes of the html tag
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if self.props is None:
            return ""
        props_html = ""
        for prop in self.props:
            props_html += f' {prop}="{self.props[prop]}"'
        return props_html 
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"

