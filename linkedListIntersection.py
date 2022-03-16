class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, val):
        if self.head == None:
            self.head = Node(val)
        else:
            curr = self.head
            while curr.next is not None:
                curr = curr.next
            curr.next = Node(val)

    def printList(self):
        curr = self.head
        while curr is not None:
            print(curr.val, end='->')
            curr = curr.next
        print("None")

# Helper function to return length of linked list
def findLength(a):
    length = 0
    if a is None:
        return length
    curr = a.head
    while curr is not None:
        length += 1
        curr = curr.next
    return length

# Function to return value of the intersecting node
def findIntersection(a, b):
    l1 = findLength(a)
    l2 = findLength(b)
    curr_a = a.head
    curr_b = b.head
    if l1 < l2:
        d = l2 - l1
        for i in range(d):
            curr_b = curr_b.next
    if l2 < l1:
        d = l1 - l2
        for i in range(d):
            curr_a = curr_a.next
    while curr_a.val != curr_b.val:
        curr_a = curr_a.next
        curr_b = curr_b.next
    return curr_a.val

a = LinkedList()
for elem in [3, 7, 8, 10]:
    a.insert(elem)

b = LinkedList()
for elem in [99, 1, 8, 10]:
    b.insert(elem)

print(findIntersection(a, b))