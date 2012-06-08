from abc import ABCMeta, abstractmethod
import math
import Moments from datatools.Moments
import Percentiles from datatools.Percentiles

class FrequencyBase(Moments, Percentiles):

    __metaclass__ = ABCMeta

    def __init__(self):
        self.total = 0.
        self.n = 0.
        self.max = None
        self.min = float("inf")
        self.is_sorted = False

    def mean(self):
        return self.total / self.n

    def range(self, zero_start = False):
        if zero_start:
            return self.max
        return self.max - self.min

    @abstractmethod
    def mode(self):
        pass

    @abstractmethod
    def percentile(self, percentile):
        pass

    @abstractmethod
    def orderedData(self):
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
