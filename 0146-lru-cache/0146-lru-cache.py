class Node:
    def __init__(self, key, prev=None, nxt=None):
        self.key = key
        self.prev = prev
        self.next = nxt

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.directory = {} # key -> (value, node)
        self.head = Node(key=0, prev=None, nxt=None) # bookend, will never have a prev
        self.tail = Node(key=0, prev=None, nxt=None) # bookend, will never have a next

        self.head.next = self.tail
        self.tail.prev = self.head

    def _insert_LRU_top(self, node: Node) -> None:
        firstnode = self.head.next 

        node.next = firstnode
        node.prev = self.head

        firstnode.prev = node
        self.head.next = node
        return

    def _update_LRU(self, node: Node) -> None:
        if len(self.directory) == 1:
            return

        # Step 1: excise
        node.prev.next = node.next
        node.next.prev = node.prev

        # Step 2: re-insert at the top 
        self._insert_LRU_top(node)
        return


    def get(self, key: int) -> int:    

        if self.capacity == 0:
            return -1

        elif self.capacity == 1:
            if key not in self.directory:
                return -1
            else:
                value, _ = self.directory[key]
                return value

        else:
            if key not in self.directory:
                return -1
            else:
                # Lookup element
                value, node = self.directory[key]
                self._update_LRU(node)
                return value   

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return

        elif self.capacity == 1:
            self.directory.clear()
            self.directory[key] = (value, None)
            return

        elif key in self.directory:
            _, node = self.directory[key]

            # overwrite the value
            self.directory[key] = (value, node)
            self._update_LRU(node)
            return

        elif len(self.directory) == self.capacity:
            # Eviction
            # clean implementation is to overwrite whomever's at the bottom 
            # and pull them to the top of the LRU

            lastnode = self.tail.prev

            del self.directory[lastnode.key] 
            self.directory[key] = (value, lastnode)
            lastnode.key = key

            self._update_LRU(lastnode)      
            return

        else:
            # Insertion when we haven't hit capacity yet
            node = Node(key)
            self.directory[key] = (value, node)
            self._insert_LRU_top(node)
            return


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)




""" RUSSELL'S OLD IMPLEMENTATION ATTEMPT:
class Node:
    def __init__(self, key, prev=None, nxt=None):
        self.key = key
        self.prev = prev
        self.next = nxt


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hashmap = {} # key -> (val, node)
        self.head = None
        self.tail = None

        self.capacity_one_pedestal = None

    def get(self, key: int) -> int:
        print("GET key={}".format(key))

        if self.capacity == 0:
            return -1
        
        if self.capacity == 1:
            if not self.capacity_one_pedestal:
                return -1
            k, v = self.capacity_one_pedestal
            if key == k:
                return v
            else:
                return -1

        if key in self.hashmap:
            val, node = self.hashmap[key]

            # edge case - if the tail just got pulled up to the front
            if self.tail == node:
                self.tail = node.prev

            # update recent usage
            if node.prev:
                node.prev.next = node.next
            node.next = self.head
            self.head.prev = node
            self.head = node

            if self.head:
                print("GET HEAD KEY={}".format(self.head.key))
            if self.tail:
                print("GET TAIL KEY={}".format(self.tail.key))
            print(self.hashmap)
            # return value
            return val
        else:
            return -1

        

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return

        if self.capacity == 1:
            self.capacity_one_pedestal = (key, value)
            return

        if key in self.hashmap:
            print('put - already present/update')
            _, node = self.hashmap[key]

            # overwrite the value
            self.hashmap[key] = (value, node)

            # update recent usage
            if node.prev:
                node.prev.next = node.next
            node.next = self.head
            self.head.prev = node
            self.head = node

        elif len(self.hashmap) == self.capacity: 
            # eviction
            # remove whomever's at the tail
            del self.hashmap[self.tail.key]
            # self.hashmap.remove(self.tail.key) 
            temp = self.tail
            self.tail = self.tail.prev
            self.tail.next = None
            del temp

            node = Node(key, prev=None, nxt=None)
            # room for novel addition
            node.next = self.head
            self.head.prev = node
            self.head = node

            self.hashmap[key] = (value, node)

        else:
            node = Node(key, prev=None, nxt=None)
            # room for novel addition
            if len(self.hashmap) == 0:
                self.head = node
                self.tail = node
            else:
                node.next = self.head
                self.head.prev = node
                self.head = node
            self.hashmap[key] = (value, node)

        if self.head:
            print("GET HEAD KEY={}".format(self.head.key))
        if self.tail:
            print("GET TAIL KEY={}".format(self.tail.key))
        print(self.hashmap)
        return





"""


"""
....A B C....
A - > C

Front of list:
No op

Back of list:
Mindful of the fact "C" is a nullptr

put(5, 10)
put(5, 12)

EDGE CASES:
capacity 0
do no ops and -1 all the time

put(novel key, 10) -> access tail of double linked list and (node should say what the key is so you can go over to the hashmap and delete the key, val pair in the hashmap)

GET CALL:
if key not in hashmap:
    return -1 

"""



"""
cache: 2

insert 1
insert 2
insert 3 (evicts 1)




"""