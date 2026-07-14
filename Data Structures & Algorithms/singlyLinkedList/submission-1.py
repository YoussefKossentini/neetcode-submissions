

class ListNode:
    def __init__(self, val: int = 0, next_node=None):
        self.val = val
        self.next = next_node

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:   # fixed condition
            return -1
        curr = self.head
        for _ in range(index):
            curr = curr.next
        return curr.val

    def insertHead(self, val: int) -> None:
        self.head = ListNode(val, self.head)
        self.size += 1

    def insertTail(self, val: int) -> None:
        new_node = ListNode(val)
        if self.head is None:          # handle empty list
            self.head = new_node
        else:
            curr = self.head
            while curr.next is not None:
                curr = curr.next
            curr.next = new_node
        self.size += 1                 # increment size, not assign a node

    def remove(self, index: int) -> bool:
        if index < 0 or index >= self.size:
            return False
        if index == 0:
            self.head = self.head.next
        else:
            curr = self.head
            for _ in range(index - 1):
                curr = curr.next
            curr.next = curr.next.next
        self.size -= 1
        return True

    def getValues(self) -> List[int]:
        values = []
        curr = self.head
        while curr is not None:          # or for _ in range(self.size)
            values.append(curr.val)      # use .val, not .value
            curr = curr.next
        return values