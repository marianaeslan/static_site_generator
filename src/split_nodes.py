from markdown_extractor import extract_markdown_images, extract_markdown_links
from textnode import TextNode

text_type_text = "text"
text_type_link = "link"
text_type_image = "image"

def split_nodes_image (old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != text_type_text:
            new_nodes.append(node)
            continue
        
        # Extraia todas as imagens
        images = extract_markdown_images(node.text)
        if not images:
            new_nodes.append(node)
            continue
        
        # Split the text into segments around the images
        text = node.text
        for alt, link in images:
            # Divida o texto em partes, antes e depois da imagem
            sections = text.split(f"![{alt}]({link})", 1)
            
            # Adicione a parte anterior à imagem
            if sections[0]:
                new_nodes.append(TextNode(sections[0], text_type_text))
            
            # Adicione o nó da imagem
            new_nodes.append(TextNode("", text_type_image, {"src": link, "alt": alt}))
            
            # Continue com a parte restante do texto
            text = sections[1] if len(sections) > 1 else ""
        
        if text:
            new_nodes.append(TextNode(text, text_type_text))
    
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != text_type_text:
            new_nodes.append(node)
            continue
        
        # Extraia todos os links
        links = extract_markdown_links(node.text)
        if not links:
            new_nodes.append(node)
            continue
        
        # Split the text into segments around the links
        text = node.text
        for anchor, url in links:
            # Divida o texto em partes, antes e depois do link
            sections = text.split(f"[{anchor}]({url})", 1)
            
            # Adicione a parte anterior ao link
            if sections[0]:
                new_nodes.append(TextNode(sections[0], text_type_text))
            
            # Adicione o nó do link
            new_nodes.append(TextNode(anchor, text_type_link, url))
            
            # Continue com a parte restante do texto
            text = sections[1] if len(sections) > 1 else ""
        
        if text:
            new_nodes.append(TextNode(text, text_type_text))
    
    return new_nodes