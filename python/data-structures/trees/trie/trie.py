from typing import Iterator


class Node:
    def __init__(self) -> None:
        self.children: dict[str, Node] = dict()
        self.valid_word: bool = False


class Trie:
    def __init__(self) -> None:
        self.root: Node = Node()
        self._size: int = 0

    def __len__(self) -> int:
        return self._size

    def __iter__(self) -> Iterator[str]:
        word_list: list[str] = self._iterate(self.root, "")

        for word in word_list:
            yield word

    def __repr__(self) -> str:
        return f"{list(self)}"

    def __contains__(self, word: str) -> bool:
        curr_node = self.root

        for char in word:
            if char not in curr_node.children:
                return False

            curr_node = curr_node.children[char]

        return True if curr_node.valid_word else False

    def _iterate(self, node: Node, prefix: str) -> list[str]:
        word_list: list[str] = []

        if node.valid_word:
            word_list.append(prefix)

        for key, next in node.children.items():
            temp = self._iterate(next, prefix + key)
            word_list.extend(temp)

        return word_list

    def _delete(self, node: Node, word: str, index: int) -> Node:
        pass

    def insert(self, word: str) -> None:
        curr_node = self.root

        for char in word:
            if char not in curr_node.children:
                curr_node.children[char] = Node()

            curr_node = curr_node.children[char]

        if curr_node.valid_word is False:
            curr_node.valid_word = True
            self._size += 1

    def search(self, word: str) -> bool:
        return self.__contains__(word)

    def delete(self, word: str) -> None:
        self._delete(self.root, word, 0)

    def starts_with(self, prefix: str) -> list[str]:
        curr_node = self.root

        for char in prefix:
            if char not in curr_node.children:
                return []

            curr_node = curr_node.children[char]

        return self._iterate(curr_node, prefix)
