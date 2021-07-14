from collections import OrderedDict

class Lrucache:
    def __init__(self,capacity):
        self.capacity=capacity
        self.cache=OrderedDict()

    def get(self,key):
        if key not in self.cache:
            return -1
        else:
            self.cache.move_to_end(key)
            return self.cache[key]
    def put(self,key,val):
        self.cache[key] = val
        self.cache.move_to_end(key)
        if len(self.cache) > self.capacity:
            self.cache.popitem(last = False)

    def get_cache(self):
        print(self.cache)

def main():  
    obj=Lrucache(2)
    obj.put(1,1)
    assert(obj.cache)==OrderedDict([(1, 1)])
    obj.get_cache()
    obj.put(2,2)
    assert(obj.cache)==OrderedDict([(1, 1), (2, 2)])
    obj.get_cache()
    obj.get(1)
    assert(obj.cache)==OrderedDict([(2, 2), (1, 1)])
    obj.get_cache()
    obj.put(3,3)
    obj.get(2)
    obj.put(4,4)
    obj.get(3)
    assert(obj.cache)==OrderedDict([(4, 4), (3, 3)])
    obj.get_cache()
    obj.get(4)
    assert(obj.cache)==OrderedDict([(3, 3), (4, 4)])
    obj.get_cache()
    obj.put(4,4)
    #assert(obj.cache)==OrderedDict([(3, 3), (4, 4), (4,3)])
    obj.get_cache()
if __name__=="__main__":
    main()
