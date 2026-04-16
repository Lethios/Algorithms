from typing import Iterator


class Node:
    def __init__(
        self, val: int, left: "Node | None" = None, right: "Node | None" = None
    ) -> None:
        self.val: int = val
        self.left: Node | None = left
        self.right: Node | None = right


class BinarySearchTree:
    def __init__(self) -> None:
        self.root: Node | None = None
        self._size: int = 0

    def __len__(self) -> int:
        return self._size

    def __iter__(self) -> Iterator[int]:
        def _inorder(node):
            if node is not None:
                yield from _inorder(node.left)
                yield node.val
                yield from _inorder(node.right)

        yield from _inorder(self.root)

    def __repr__(self) -> str:
        return f"{list(self)}"

    def __contains__(self, val) -> bool:
        curr_node = self.root

        if curr_node is None:
            return False

        while True:
            if val < curr_node.val:
                if curr_node.left is None:
                    return False

                curr_node = curr_node.left
            elif val > curr_node.val:
                if curr_node.right is None:
                    return False

                curr_node = curr_node.right
            else:
                return True

    def insert(self, val: int) -> None:
        node = Node(val)

        if self.root is None:
            self.root = node
        else:
            parent: Node = self.root

            while True:
                if node.val < parent.val:
                    if parent.left is None:
                        parent.left = node
                        break

                    parent = parent.left
                elif node.val > parent.val:
                    if parent.right is None:
                        parent.right = node
                        break

                    parent = parent.right
                else:
                    return

        self._size += 1

    def search(self, val: int) -> bool:
        return self.__contains__(val)

    def delete(self, val: int) -> None:
        pass

    def height(self) -> int:
        def _height(node: Node | None) -> int:
            if node is None:
                return -1

            return 1 + max(_height(node.left), _height(node.right))

        return _height(self.root)

    def min(self) -> int:
        curr_node = self.root

        if curr_node is None:
            raise ValueError

        while curr_node.left is not None:
            curr_node = curr_node.left

        return curr_node.val

    def max(self) -> int:
        curr_node = self.root

        if curr_node is None:
            raise ValueError

        while curr_node.right is not None:
            curr_node = curr_node.right

        return curr_node.val
