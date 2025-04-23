class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

        # child classes will override this method to render themselves as HTML

    def to_html(self):
        if self.value is not None:
            return self.value

        if self.children is not None:
            children_html = "".join([child.to_html() for child in self.children])
        else:
            children_html = ""

        if self.tag is None:
            return children_html

        return f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"

    def props_to_html(self):
        if self.props is None:
            return ""
        return_string = ""
        for key, value in self.props.items():
            return_string += f' {key}="{value}"'

        return return_string

    def __repr__(self):
        return f"HTMLNode(tag={self.tag}, value={self.value}, children={self.children} props={self.props})"


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("invalid HTML: no tag")
        if self.children is None:
            raise ValueError("invalid HTML: no children")
        children_html = ""
        for child in self.children:
            children_html += child.to_html()
        return f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"

    def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"
