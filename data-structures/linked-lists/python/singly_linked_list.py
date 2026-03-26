class Node:
    def __init__(self, val: int = 0, next: "Node | None" = None):
        self.val: int = val
        self.next: Node | None = next


class SinglyLinkedList:
    def __init__(self) -> None:
        self.head: Node | None = None
        self.tail: Node | None = None
        self._size: int = 0

    def __len__(self) -> int:
        return self._size

    def __iter__(self):
        current = self.head

        while current:
            yield current.val
            current = current.next

    def __repr__(self) -> str:
        return " -> ".join(str(val) for val in self) + " -> None"

    def append(self, val: int) -> None:
        node = Node(val)

        if self.head is None:
            self.head = self.tail = node
        else:
            if self.tail is not None:
                self.tail.next = node
            self.tail = node

        self._size += 1

    def prepend(self, val: int) -> None:
        node = Node(val)

        if self.head is None:
            self.head = self.tail = node
        else:
            node.next = self.head
            self.head = node

        self._size += 1

    def delete(self, val: int) -> None:
        current, prev = self.head, None

        while current:
            if current.val == val:
                if prev is None:
                    self.head = current.next
                else:
                    prev.next = current.next

                if current.next is None:
                    self.tail = prev

                self._size -= 1
                break

            prev = current
            current = current.next

    def search(self, val: int) -> int:
        current = self.head
        idx: int = 0

        while current:
            if current.val == val:
                return idx

            current = current.next
            idx += 1

        return -1


if __name__ == "__main__":
    lst = SinglyLinkedList()

    print("Appending...")
    lst.append(1)
    lst.append(2)
    lst.append(3)

    print("Length:", len(lst))
    print("Search 2:", lst.search(2))
    print("Search 5:", lst.search(5))

    print("Deleting 2...")
    lst.delete(2)

    print("Search 2:", lst.search(2))
    print("Length:", len(lst))
    print(lst)
    print(len(lst))
