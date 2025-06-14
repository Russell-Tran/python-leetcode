import heapq
from functools import total_ordering

# Not so sure how you'd have access to total_ordering during an interview though
# unless you memorize it and the __eq__ and __lt__ functions
@total_ordering
class Node:
    def __init__(self, val: int):
        self.val = val
        self.valid = True
    
    def __eq__(self, other):
        return self.val == other.val

    def __lt__(self, other):
        return self.val < other.val

class MinStack:

    def __init__(self):
        self.minheap = []
        self.stack = []

    def push(self, val: int) -> None:
        node = Node(val)
        heapq.heappush(self.minheap, node)
        self.stack.append(node)

    def pop(self) -> None:
        node = self.stack.pop()
        while not node.valid:
            node = self.stack.pop()
        node.valid = False

    def top(self) -> int:
        node = self.stack[-1]
        while not node.valid:
            self.stack.pop()
            node = self.stack[-1]
        return node.val

    def getMin(self) -> int:
        node = self.minheap[0]
        while not node.valid:
            heapq.heappop(self.minheap)
            node = self.minheap[0]
        return node.val


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

"""
Interesting,
I think for this you implement a minheap and a stack, but maybe have a special node structure
to link the two together

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Equality based on name
    def __eq__(self, other):
        return self.name == other.name

    # Less than based on age
    def __lt__(self, other):
        return self.age < other.age

    # Greater than based on age
    def __gt__(self, other):
        return self.age > other.age


I would say the minheap would be the harder structure, so you could use the python
minheap off the shelf and create linking pointers in there. something that's deleted
by the stack and just be marked for deletion, and if it surfaces on getmin, then you know
to skip/delete it by popping it off the minheap    

oh you know what, it's kind of overkill to do a linked list for the stack, though
but i still think you need a custom class to mark elements for removal ,
which allows for amortized , like lazy removal

"""