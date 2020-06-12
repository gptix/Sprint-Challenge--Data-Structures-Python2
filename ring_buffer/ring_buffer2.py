class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False
        
class RingBuffer:
    def __init__(self, capacity):
        self.storage = LinkedList()
        # populate ring with Nones
        for i in range(capacity+1):
            self.storage.add_to_head(None)
        
        # find end of LL
        self.write_node = self.storage.head
        while self.write_node.next_node is not None:
            self.write_node = self.write_node.next_node
        
        # make it a ring
        self.write_node.next_node = self.storage.head
        self.write_node = self.storage.head
        self.capacity = capacity
        
    def append(self, val):
        self.write_node.value = val
        self.write_node = self.write_node.next_node

        
    def get(self):
        ret_list = []
        read_node = self.storage.head
        for i in range(self.capacity):
            if read_node.value is not None:
                ret_list.append(read_node.value)
                read_node = read_node.next_node

        return ret_list

# rb = RingBuffer(5)
# rb.append('a')
# foo  = rb.get()
# print(foo)                