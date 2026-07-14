class ListNode:
    def __init__(self, val: int, next_node=None):
        self.val = val
        self.next = next_node


class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1

        curr = self.head

        for _ in range(index):
            curr = curr.next

        return curr.val

    def insertHead(self, val: int) -> None:
        new_node = ListNode(val)

        new_node.next = self.head
        self.head = new_node

        self.size += 1

    def insertTail(self, val: int) -> None:
        new_node = ListNode(val)

        if self.head is None:
            self.head = new_node
            self.size += 1
            return

        curr = self.head

        while curr.next is not None:
            curr = curr.next

        curr.next = new_node
        self.size += 1

    def remove(self, index: int) -> bool:
        if index < 0 or index >= self.size:
            return False

        # Removing the head node
        if index == 0:
            self.head = self.head.next
            self.size -= 1
            return True

        # Find the node before the one we remove
        curr = self.head

        for _ in range(index - 1):
            curr = curr.next

        # Skip the node to remove
        curr.next = curr.next.next

        self.size -= 1
        return True

    def getValues(self) -> list[int]:
        values = []

        curr = self.head

        while curr is not None:
            values.append(curr.val)
            curr = curr.next

        return values