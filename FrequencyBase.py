from abc import ABCMeta, abstractmethod

import math

class FrequencyBase(object):
    
    __metaclass__ = ABCMeta
    
    def firstQuartile(self):
        return self.percentile(.25)
    
    def median(self):
        return self.percentile(.5)

    def thirdQuartile(self):
        return self.percentile(.75)

    def IQR(self):
        return thirdQuartile() - firstQuartile()

    def average(self):
        return self.total / self.n

    def mean(self):
        return self.average()

    @abstractmethod
    def percentile(self, percentile):
        pass

    @abstractmethod
    def ordered_data(self):
        pass

    @abstractmethod
    def explode(self):
        pass

    def moment(self, n):
        return sum(i ** n for i in self.explode())
