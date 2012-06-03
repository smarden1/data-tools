import math

class Moments(object):

    def mean(self):
        return self.moments(1) / self.n

    def variance(self):
        return (self.moments(2)) - (self.mean() ** 2)

    def std(self):
        return math.sqrt(self.variance)

    def skew(self):
        return ((self.moments(3) / self.n) - (3 * self.mean() * self.variance) - self.mean ** 3) / (self.std **3)

    # http://www.ats.ucla.edu/stat/mult_pkg/faq/general/kurtosis.htm    
    def kurtosis(self):
        return ((self.moments(4) - (self.mean ** 4)) / self.n) / ((self.variance / n) ** 2) - 3
