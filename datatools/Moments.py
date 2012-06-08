from abc import ABCMeta, abstractmethod
import math

# should make this abstract
class Moments(object):

    __metaclass__ = ABCMeta

    def mean(self):
        return self.moment(1) / self.n

    def average(self):
        return self.mean()

    def variance(self):
        return (self.moment(2)) - (self.mean() ** 2)

    def std(self):
        return math.sqrt(self.variance)

    def skew(self):
        return ((self.moment(3) / self.n) - (3 * self.mean() * self.variance) - self.mean ** 3) / (self.std **3)

    # http://www.ats.ucla.edu/stat/mult_pkg/faq/general/kurtosis.htm    
    def kurtosis(self):
        return ((self.moment(4) - (self.mean ** 4)) / self.n) / ((self.variance / n) ** 2) - 3

    @abstractmethod
    def moment(self, m):
        pass
