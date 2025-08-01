from collections import deque

class LRUCache:

    def __init__(self, capacity: int):
        # initialize cache of the size -> "capacity"
        self.cache = {}
        self.cap = capacity
        self.queue = deque()


    def get(self, key: int) -> int:
        #return value at key
        if key in self.cache:
            return self.cache[key]
        #else return -1
        return -1


    def put(self, key: int, value: int) -> None:
        #if key is in cache it will update val,
        #   if not in cache it will ad new pair
        self.cache[key] = value
        #add to queue
        self.queue.append(key)

        #if we reached capacity, dequeue and remove from  hashmap
        if self.cap <= 0:
            del self.cache[self.queue.popleft()]

        else:
            #decrement capacity
            self.cap -= 1




        '''# update "value" of "key",   if "key exists"
            if key in self.cache:
                self.cache[key] = value
            #else add pair to cache
            else:
                self.cache[key] = value
'''



