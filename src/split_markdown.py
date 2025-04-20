from textnode import TextNode, TextType
import re


def split_nodes_image(old_nodes):
    result = []
    for item in old_nodes:
        text = item.text
        last_index = 0

        for match in re.finditer(r"!\[(.*?)\]\((.*?)\)", text):
            start, end = match.span()
            alt, url = match.group(1), match.group(2)

            print(f"\nMatch: {match.group(0)}")
            print(f"Start: {start}, End: {end}")
            print(f"Text before match: '{text[last_index:start]}'")
            print("\n")

            if start > last_index:
                result.append(TextNode(f"{text[last_index:start]}", TextType.TEXT))

            result.append(TextNode(alt, TextType.IMAGE, url))

            last_index = end

        if last_index < len(text):
            result.append(TextNode(f"{text[last_index:]}", TextType.TEXT))

    return result


def split_nodes_link(old_nodes):
    result = []
    for item in old_nodes:
        text = item.text
        last_index = 0

        for match in re.finditer(r"(?<!\!)\[(.*?)\]\((.*?)\)", text):
            start, end = match.span()
            alt, url = match.group(1), match.group(2)

            print(f"\nMatch: {match.group(0)}")
            print(f"Start: {start}, End: {end}")
            print(f"Text before match: '{text[last_index:start]}'")
            print(f"\n")

            if start > last_index:
                result.append(TextNode(text[last_index:start], TextType.TEXT))

            result.append(TextNode(alt, TextType.LINK, url))

            last_index = end

        if last_index < len(text):
            trailing = text[last_index:]
            print(f"Trailing text: '{trailing}'")
            result.append(TextNode(trailing, TextType.TEXT))

    return result


node1 = TextNode(
    "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
    TextType.TEXT,
)
new_nodes = split_nodes_link([node1])
print("split_nodes_link: ", new_nodes)
# [
#     TextNode("This is text with a link ", TextType.TEXT),
#     TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
#     TextNode(" and ", TextType.TEXT),
#     TextNode(
#         "to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"
#     ),
# ]
