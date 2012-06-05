from abc import ABCMeta, abstractmethod
import math
import datatools.Moments

class FrequencyBase(datatools.Moments.Moments):

    __metaclass__ = ABCMeta

    def __init__(self):
        self.total = 0.
        self.n = 0.
        self.max = None
        self.min = float("inf")
        self.is_sorted = False

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
        return self.average()

    def range(self, zero_start = False):
        if zero_start:
            return self.max
        return self.max - self.min

    @abstractmethod
    def percentile(self, percentile):
        pass

    @abstractmethod
    def ordered_data(self):
        pass

    @abstractmethod
    def explode(self):
        pass

    @abstractmethod
    def mode(self):
        pass

    def moment(self, n):
        return sum(i ** n for i in self.explode())

    def pdf(self):
        return ((k, v / self.total) for k,v in self.ordered_data().iteritems())

    def cdf(self):
        cdf, current = {}, 0

        for k,v in self.pdf():
            current += v
            cdf[k] = current

        return cdf
