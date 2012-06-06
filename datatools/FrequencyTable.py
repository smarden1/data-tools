﻿import collections
import Exceptions
from datatools.FrequencyBase import FrequencyBase

class FrequencyTable(FrequencyBase):

    def __init__(self):
        super(FrequencyTable, self).__init__() # how to call super with abstractbase
        self.data = collections.defaultdict(lambda : 0)
        self.ordered_data_list = []

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

        for k,v in self.ordered_data():
            c += v
            if c >= p:
                return k

        return k

    def mode(self):
        return max(self.data.iteritems(), key = lambda a:a[1])[0]

    def ordered_data(self):
        if not self.is_sorted:
            self.ordered_data_list = sorted(self.data.iteritems(), key = lambda a: a[0])
            self.is_sorted = True
        return self.ordered_data_list

    def explode(self):
        for k,v in self.ordered_data():
            for i in xrange(v):
                yield k

    # this is better than the explode_data version for the table
    def histogram(self, bins = None):
        bins, bin_width = self.__histogram_bins_and_width(bins)

        histogram = [0] * bins
        for k,v in self.ordered_data():
            histogram[k / bin_width] += v

        return histogram