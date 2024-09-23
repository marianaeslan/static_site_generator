from textnode import TextNode
from split_nodes import *
from split_delimiter import *

text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = "link"
text_type_image = "image"

def text_to_textnodes(text):
    # Inicializa com o texto como um único TextNode
    nodes = [TextNode(text, text_type_text)]
    
    # Executa cada função de divisão em sequência para processar o texto
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    nodes = split_nodes_delimiter(nodes, "**", text_type_bold)  # Negrito
    nodes = split_nodes_delimiter(nodes, "*", text_type_italic)  # Itálico
    nodes = split_nodes_delimiter(nodes, "`", text_type_code)  # Código
    
    return nodes