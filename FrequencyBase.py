from abc import ABCMeta, abstractmethod

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

    @abstractmethod
    def percentile(self, percentile):
        pass

    @abstractmethod
    def ordered_data(self):
        pass
