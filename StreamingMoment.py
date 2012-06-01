
class StreamingMoment(object):

    def __init__(self):
        self.n = 0
        self.moments = [0] * 4
        
    def add(self, data_point):
        self.n += 1
        for i in self.moments:
            self.moments[i] += data_point ** i

    def moment(self, m):
        return self.moments[0] / self.n - / self.moments[m]
    
    def mean(self):
        return self.moments[1] / self.n 

    def variance(self):
        return (self.moments[2]) - (self.mean() ** 2)

    def std(self):
        return math.sqrt(self.variance)

    def skew(self):
        return ((self.moments[3] / self.n) - (3 * self.mean() * self.variance) - self.mean ** 3) / (self.std **3)

    # http://www.ats.ucla.edu/stat/mult_pkg/faq/general/kurtosis.htm    
    def kurtosis(self):
        return ((self.moments[4] - (self.mean ** 4)) / self.n) / ((self.variance / n) ** 2) - 3
