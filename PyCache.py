import datetime
import random

class CacheImplement:
    """"""
    def __init__(self):
        self.cache = {}
        self.max = 14

    def __contains__(self, key):
        return key in self.cache

    def update(self, key, value):
        if key not in self.cache and len(self.cache) >= self.max:
            self.pop_old()
        self.cache[key] = {'tstamp': datetime.datetime.now(),'value': value}

    def pop_old(self):
        first = None
        for key in self.cache:
            if first is None:
                first = key
            elif self.cache[key]['tstamp'] < self.cache[first]['tstamp']:
                first = key
        self.cache.pop(first)

    def size(self):
        return len(self.cache)

if __name__ == '__main__':
    test = ['he','who','must','not','be','named','you-know-who','avada','kedavra','wand','cloak','stone','seven','severus','snape']

    cache = CacheImplement()
    for i, key in enumerate(test):
        if key in cache:
            continue
        else:
            value = random.randint(0,20)
            cache.update(key, value)
    print(cache.cache)
    """ 
    "he" has been removed as per (fixed cache size) as we added "snape"
    """

