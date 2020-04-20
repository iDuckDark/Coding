class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def print(self):
        current = self
        string = ""
        while current is not None:
            string += str(current.value) + " "
            current = current.next
        print(string)


class LinkedList:
    def __init__(self):
        self.head = None

    def getHead(self):
        return self.head

    def add(self, value):
        if self.head is None:
            self.head = Node(value)
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = Node(value)

    def remove_all_n(self, head, value):
        head, head.next = Node(0), head
        current = head
        while current.next:
            if current.next.value == value:
                current.next = current.next.next
            else:
                current = current.next
        return head.next

    # def delete(self, value):
    #     current = self.head
    #     if current is None:
    #         return
    #     if current.value == value:
    #         self.head = current.next
    #         return
    #     previous = current
    #     current = current.next
    #     while current.next is not None:
    #         if current.value == value:
    #             previous.next = current.next
    #         previous = current
    #         current = current.next
    #     if current.value == value:
    #         previous.next = None
    #     else:
    #         raise Exception("Not found")

    def print(self):
        current = self.head
        string = ""
        while current is not None:
            string += str(current.value) + " "
            current = current.next
        print(string)

    def deleteDuplicates(self):
        current = self.head
        previous = None
        hashset = set()
        while current:
            if current.value in hashset:
                previous.next = current.next
            else:
                hashset.add(current.value)
                previous = current
            current = current.next

    def reverse(self):
        prev = None
        current = self.head
        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

    def _reverse(self, current):
        if current is None:
            return
        if current.next is None:
            self.head = current
            return
        self._reverse(current.next)
        current.next.next = current
        current.next = None

    def reverse(self):
        self._reverse(self.head)
        return self.head


def scrambled(orig):
    dest = orig[:]
    import random
    random.shuffle(dest)
    return dest


def sumList(l1, l2):
    return _sumList(l1, l2, 0)


def _sumList(l1, l2, carry):
    if l1 is None and l2 is None and carry == 0:
        return None
    value = carry
    if l1 is not None:
        value += l1.value
    if l2 is not None:
        value += l2.value
    result = Node(value % 10)
    if l1 is not None or l2 is not None:
        v1 = None if l1 is None else l1.next
        v2 = None if l2 is None else l2.next
        carryBit = 1 if value >= 10 else 0
        more = _sumList(v1, v2, carryBit)
        result.next = more
    return result


def LinkedListExample():
    l1 = LinkedList()
    l2 = LinkedList()
    for val in [7, 1, 6]: l1.add(val)
    for val in [5, 9, 2]: l2.add(val)
    l1.print()
    l2.print()


def findBeginning(head):
    slow = fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    if fast is None or fast.next is None:
        return None
    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next
    return fast.value


def makeLoop():
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n5 = Node(5)
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n3
    n5.next = n3
    print(findBeginning(n2))


# LinkedListExample()





# l1 = LinkedList()
# for val in [1, 3, 2, 3, 3]:
#     l1.add(val)
# l1.print()
#
# head = remove_all_n(l1.getHead(), 3)
# head.print()

#
# def Func(n):
#     if (n == 4):
#         return 2
#     else:
#         return 2 * Func(n + 1)
#
#
# print(Func(2))
