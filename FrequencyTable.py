﻿import collections
import Exceptions
from FrequencyBase import FrequencyBase

class FrequencyTable(object):

    def __init__(self):
        self.data = collections.defaultdict(lambda : 0)
        self.total = 0.
        self.n = 0.
        self.max = None
        self.min = float("inf")
        self.is_sorted = False

    # cl tools casts this to int
    def add(self, key, count = 1):
        self.data[key] += count
        self.total += count
        self.n += 1
        self.max = max(self.max, key)
        self.min = min(self.min, key)
        self.is_sorted = False

     # TODO - this percentile is wrong
    def percentile(self, percentile):
        """
            takes a percentoile
            returns the key for that percentile
        """
        if percentile > 1.0:
            raise PercentageGreaterThanOne(percentile)

        p = percentile * self.total
        c = 0

        for k,v in self.ordered_data().iteritems():
            c += v    
            if c >= p:
                return k
            
        return k

    def mode(self):
        most_popular_dict = {}

        for k,v in self.data.iteritems():
            if not most_popular_dict or current == v:
                most_popular_dict[k] = v
                current = v
            else
                most_popular_dict = {k: v}
                
        return most_popular_dict

    def pdf(self):
        return ((k, v / self.total) for k,v in self.ordered_data().iteritems())

    def cdf(self):
        cdf, current = {}, 0

        for k,v in self.pdf():
            current += v
            cdf[k] = current

        return cdf

    def ordered_data(self):
        if not self.is_sorted:
            self.data = sorted(self.data, key = lambda a: a[0])
            self.is_sorted = True
        return self.data

    def explode(self):
        for k,v in self.ordered_data():
            for i in xrange(v):
                yield k

# move these and lower to frequency of something math based and subclasses
#stem and leaf plot
#sparklines on cl
    def histogram(self, bins = None):
        if bins:
            bin_width = math.ceil(self.max / float(bins))
        else:
            bin_width = optimumBinWidth()
            bins = math.floor(self.max / bin_width)
        
        # and more!

    def optimumBinWidth(self):
        """Freedman–Diaconis' choice"""
        return 2 * (self.IQR() / pow(self.n, 1/3.))
    
FrequencyBase.register(FrequencyTable)