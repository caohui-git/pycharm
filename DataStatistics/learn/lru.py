from collections import OrderedDict
class LRUCache:
    def __init__(self, Capacity):
        self.size = Capacity
        self.cache = OrderedDict()

    def get(self, key):
        if key not in self.cache: return -1
        val = self.cache[key]
        self.cache.move_to_end(key)
        #print("%d%d",self.cache[j][0],self.cache[j][1])
        return val

    def put(self, key, val):
        if key in self.cache: del self.cache[key]
        self.cache[key] = val
        if len(self.cache) > self.size:
            self.cache.popitem(last=False)

obj = LRUCache(2)
res=[0]*7
j=0
for i in [[1,1],[2,2],[1],[3,3],[1]]:
    if len(i)==1:
        res[j]=obj.get(i[0])
        j+=1
    else:
        obj.put(i[0],i[1])

for k,v in obj.cache.items():
    print(k,v)

print(obj.cache)