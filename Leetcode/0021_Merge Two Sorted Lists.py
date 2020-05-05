class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None


# iteratively
def mergeTwoLists1(l1, l2):
    dummy = cur = ListNode(0)
    while l1 and l2:
        if l1.val < l2.val:
            cur.next = l1
            l1 = l1.next
        else:
            cur.next = l2
            l2 = l2.next
        cur = cur.next
    cur.next = l1 or l2
    return dummy.next


l1, l2 = ListNode(), ListNode()
current = l1.next
for i in range(0, 10, 2):
    current = i
    current = current.next
