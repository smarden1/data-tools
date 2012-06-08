from abc import ABCMeta, abstractmethod

class Percentiles:

    __metaclass__ = ABCMeta

    @abstractmethod
    def percentile(self, p):
        pass

    def firstQuartile(self):
        return self.percentile(.25)

    def median(self):
        return self.percentile(.5)

    def thirdQuartile(self):
        return self.percentile(.75)

    def iqr(self):
        return self.thirdQuartile() - self.firstQuartile()

