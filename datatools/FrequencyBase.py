from abc import ABCMeta, abstractmethod
import math
from datatools.Moments import Moments
from datatools.Percentiles import Percentiles

class FrequencyBase(Moments, Percentiles):

    __metaclass__ = ABCMeta

    def __init__(self):
        self.total = 0.
        self.n = 0.
        self.max = None
        self.min = float("inf")
        self.cumulative_data_list = []
        self.resetFlags()

    def __str__(self):
        return "%s n, %s total, %s min, %s max"%(self.n, self.total, self.min, self.max)

    def __repr__(self):
        return self.__str__

    def firstQuartile(self):
        return self.percentile(.25)

    def median(self):
        return self.percentile(.5)

    def thirdQuartile(self):
        return self.percentile(.75)

    def iqr(self):
        return self.thirdQuartile() - self.firstQuartile()

    def average(self):
        return self.total / self.n

    def mean(self):
        return self.total / self.n

    def range(self, zero_start = False):
        if zero_start:
            return self.max
        return self.max - self.min

    def resetFlags(self):
        self.is_sorted = False
        self.is_cumulative = False

    @abstractmethod
    def mode(self):
        pass

    @abstractmethod
    def percentile(self, percentile):
        #return bisect.bisect_left(self.ordered_data)
        # make this a custom bisect b/c of this data[bisect.bisect_left(map(lambda a:a[1],data), 70)][0]
        pass

    @abstractmethod
    def orderedData(self):
        pass

    @abstractmethod
    def cumulative_ordered_data(self):
        pass

    @abstractmethod
    def explode(self):
        pass

    @abstractmethod
    def condensed(self):
        pass

    def condensedData(self):
        for k,v in self.condensed():
            yield v

    def moment(self, n):
        return sum(i ** n for i in self.explode())

    def pdf(self):
        return dict((k, v / self.n) for k,v in self.condensed())

    def cdf(self):
        cdf, current = {}, 0

        for k,v in self.condensed():
            current += (v / self.n)
            cdf[k] = current

        return cdf

    def optimumBinWidth(self):
        return 2 * (self.iqr() / pow(self.n, 1/3.))

    def histogram(self, bin_width = None):
        bin_width = bin_width or self.optimumBinWidth()

        histogram = Histogram(bin_width)
        for k,v in self.condensed():
            histogram.add(k, v)

        return histogram

    def runningSum(self, data):
        # data should be [[0, 1], [1, 10]] in order

        running_sum = [0] # this is really hacky but necessary b/c += on an int returns a new int
        def getRunningSum(val):
            running_sum[0] += val
            return running_sum[0]

        return [[k, getRunningSum(v)] for k, v in data]
