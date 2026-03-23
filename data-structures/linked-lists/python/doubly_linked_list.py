class Node:
    def __init__(
        self, val: int = 0, prev: "Node | None" = None, next: "Node | None" = None
    ):
        self.val = val
        self.prev = prev
        self.next = next
