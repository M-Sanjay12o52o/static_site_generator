from textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []

    if not delimiter:
        new_nodes.extend(old_nodes)
        return new_nodes

    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        sections = old_node.text.split(delimiter)
        if len(sections) % 2 == 0:
            new_nodes.extend(old_nodes)
            continue
            # raise ValueError("invalid markdown, formatted section not closed")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], TextType.TEXT))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes


"""
def split_nodes_delimiter(old_nodes, delimiter, text_type):
    result_list = []

    if not delimiter:
        return old_nodes

    for item in old_nodes:
        print(f"Processing node: {item}")
        text = item.text
        parts = text.split(delimiter)

        if len(parts) < 3 or len(parts) % 2 == 0:
            result_list.append(item)
            continue

        for i, part in enumerate(parts):
            if i % 2 == 0:
                if part:
                    result_list.append(TextNode(part, TextType.TEXT))
            else:
                if part:
                    result_list.append(TextNode(part, text_type))

    return result_list
"""
