class RingBuffer:
    def __init__(self, capacity):
        self.storage = [None]*capacity
        self.write_pointer = 0
        self.capacity = capacity
        
    def append(self, val):
        self.storage[self.write_pointer] = val
        self.write_pointer = (self.write_pointer + 1) % self.capacity
        
    def get(self):
        return [el for el in self.storage if el is not None]

# rb = RingBuffer(5)
# rb.append('a')
# foo  = rb.get()
# print(foo)                