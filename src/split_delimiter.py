from textnode import TextNode

#Defining types of text
text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = "link"


def split_nodes_delimiter(old_nodes, delimiter, new_text_type):
    new_nodes = []

    for node in old_nodes:
        if node.text_type != text_type_text:
            # Se o tipo de texto não for "text", apenas adicionar à lista
            new_nodes.append(node)
            continue

        # Separar o conteúdo do nó com base no delimitador
        split_text = node.text.split(delimiter)

        # Verificar se o número de partes é ímpar (precisamos de pares de delimitadores)
        if len(split_text) % 2 == 0:
            raise ValueError("Delimiter type not found")

        # Iterar pelas partes divididas e criar novos nós
        for i, part in enumerate(split_text):
            if i % 2 == 0:
                # Parte fora dos delimitadores -> texto normal
                if part:
                    new_nodes.append(TextNode(part, text_type_text))
            else:
                # Parte dentro dos delimitadores -> novo tipo de texto (por exemplo, código)
                if part:
                    new_nodes.append(TextNode(part, new_text_type))

    return new_nodes
