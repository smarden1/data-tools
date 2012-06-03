import math
from FrequencyBase import FrequencyBase
from collections import namedtuple

class FrequencyArray(object):

    def __init__(self, data = None, is_sorted = False, **kwargs):
        self.data = data or []
        self.n = len(self.data)
        self.is_sorted = is_sorted

        if self.n:
            self.total = kwargs.get("total", sum(self.data))
            self.max = kwargs.get("max", max(self.data))
            self.min = kwargs.get("min", min(self.data))
        else:
            self.total = kwargs.get("total", 0)
            self.max = kwargs.get("max", None)
            self.min = kwargs.get("min", float("inf"))
        

    def add(self, key, count = 1):
        self.max = max(self.max, key)
        self.min = min(self.min, key)
        self.n += count
        self.total += (key * count)

        for i in xrange(count):
            self.data.append(key)
            

    def ordered_data(self):
        if not self.is_sorted:
            self.data.sort()
            self.is_sorted = True
        return self.data

    def percentile(self, percentile):
        """
            takes a percentoile
            returns the key for that percentile
        """
        if percentile > 1.0:
            raise PercentageGreaterThanOne(percentile)

        p = math.floor(percentile * self.n)

        return self.ordered_data()[p]

    def explode(self):
        for i in self.ordered_data:
            yield i

    def mode(self):
        Pair = namedtuple("Pair", "key value")
        f = lambda k,v : max(k, v, key = lambda a: a.value)

        current_pair = Pair(self.ordered_data[0], 1)
        max_pair = current_pair

        for i in self.ordered_data[1:]:
            if i != current_pair.key:
                max_pair = f(max_pair, current_pair)
                current_pair = Pair(i, 1)
            current_pair.value += 1

        # edge case of last being most common
        return f(max_pair, current_pair).key
    
FrequencyBase.register(FrequencyArray)
