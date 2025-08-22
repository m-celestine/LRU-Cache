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
        return self.cache[key] if key in self.cache else -1


    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """

        #check if already in hash
        
        
        # add a new pair
        self.cache[key] = value

        # update capacity
        self.cap -= 1

        if self.cap == 0:
            self.cache[key].remove(0)
            self.cap += 1




# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)