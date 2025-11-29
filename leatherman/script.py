import json
from abc import ABC, abstractmethod
import sys

from pathlib import Path
import locale

locale.setlocale(locale.LC_ALL, "en_US")


def format_number(number):
    return locale.format_string("%d", number, grouping=True).replace(",", " ")


class NoStartNode(Exception):
    pass


class Scenario:

    def __init__(self, content, title, author="Maxime Bettinelli") -> None:
        self.content = content
        self.author = author
        self.title = title
        self.full_content = f"""Title: {self.title}
Author: {self.author}


{self.content}"""


class Node(ABC):

    @classmethod
    def factory(cls, dic):
        if dic["type"] == "text":
            return TextNode(dic)
        elif dic["type"] == "file":
            return FileNode(dic)
        else:
            raise ValueError(f"Invalid node type {dic['type']}")

    def __init__(self, dic) -> None:
        self.dic = dic
        self.id = dic["id"]

    @property
    @abstractmethod
    def content(self):
        pass

    @abstractmethod
    def export(self, with_context=False):
        pass


class TextNode(Node):

    @property
    def content(self):
        return self.dic["text"]

    def export(self, with_context=False):
        if self.content == "START":
            return ""
        return f"\n\n## {self.content}"


class FileNode(Node):

    @property
    def content(self):
        return "\n".join(
            [
                line
                for line in self.content_with_context.split("\n")
                if not line.startswith("Contexte")
            ]
        )

    @property
    def content_with_context(self):
        content = (
            Path(self.dic["file"].replace("delete/", ""))
            .read_text()
            .replace(">", "#####")
        )
        if content.startswith("---"):
            content = content.split("---", 1)[1].split("---", 1)[1]

        return content

    def export(self, with_context=False):
        return self.content if not with_context else self.content_with_context


class Canvas:
    def __init__(self, filepath) -> None:
        with open(filepath, "r") as f:
            self.data = json.load(f)
            self.nodes = [Node.factory(x) for x in self.data["nodes"]]
            self.edges = self.data["edges"]

    @property
    def node_stream(self):
        if start_node := next(
            (
                node
                for node in self.nodes
                if isinstance(node, TextNode) and node.content == "START"
            ),
            None,
        ):
            next_node = start_node
            while next_node:
                yield next_node
                next_node = next(
                    (
                        node
                        for node in self.nodes
                        if any(
                            edge["fromNode"] == next_node.id
                            and edge["toNode"] == node.id
                            for edge in self.edges
                        )
                    ),
                    None,
                )

        else:
            raise NoStartNode("No start node found")

    def generate_concatenated_text(self, with_context=False):
        return "\n\n".join(
            node.export(
                with_context=with_context,
            )
            for node in self.node_stream
        ).strip()

    def export(
        self,
        path,
        display_lenght=False,
        with_context=False,
    ):
        text = self.generate_concatenated_text(with_context=with_context)
        if display_lenght:
            analysable_text = text.replace("\n", "")
            lenght_in_sec = format_number(len(analysable_text))
            lenght_in_words = format_number(len(analysable_text.split(" ")))

            text = f"{lenght_in_sec} sec\n{lenght_in_words} mots\n{text}"
        Path(path).write_text(text)


# if __name__ == "__main__":
#     canvas = Canvas(sys.argv[1])
#     canvas.export("final.md", display_lenght=True)
