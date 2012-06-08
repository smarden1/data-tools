import collections
import Exceptions
from datatools.FrequencyBase import FrequencyBase

class FrequencyTable(FrequencyBase):

    def __init__(self):
        super(FrequencyTable, self).__init__()
        self.data = collections.defaultdict(lambda : 0)
        self.orderedData_list = []

    # cl tools casts this to int
    def add(self, key, count = 1):
        self.data[key] += count
        self.total += key * count
        self.n += count
        self.max = max(self.max, key)
        self.min = min(self.min, key)
        self.is_sorted = False

    def percentile(self, percentile):
        """
            takes a percentile
            returns the key for that percentile
        """
        if percentile > 1.0:
            raise PercentageGreaterThanOne(percentile)

        p = percentile * self.n
        c = 0

        for k,v in self.orderedData():
            c += v
            if c >= p:
                return k

        return k

    def mode(self):
        return max(self.data.iteritems(), key = lambda a:a[1])[0]

    def orderedData(self):
        if not self.is_sorted:
            self.orderedData_list = sorted(self.data.iteritems(), key = lambda a: a[0])
            self.is_sorted = True
        return self.orderedData_list

    def ordered_keys(self):
        return map(lambda a: a[0], self.orderedData())

    def ordered_values(self):
        return map(lambda a: a[1], self.orderedData())

    def explode(self):
        for k,v in self.orderedData():
            for i in xrange(v):
                yield k

    def condensed(self):
        for i in self.orderedData():
            yield i