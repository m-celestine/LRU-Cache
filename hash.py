from collections import OrderedDict

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cache = OrderedDict()
        self.cap = capacity


    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        # check if already in hash
        if key in self.cache:
            self.cache.move_to_end(key)
            return self.cache[key]

        # return -1 if not found
        return -1


    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """

        
        
        # add a new pair
        self.cache[key] = value
        # update position
        self.cache.move_to_end(key)
        # update capacity
        self.cap -= 1

        # remove least used when cap gets full
        if self.cap == 0:
            self.cache.popitem(last=False)
            self.cap += 1




# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)