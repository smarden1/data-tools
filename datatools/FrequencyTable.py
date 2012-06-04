import collections
import Exceptions
from datatools.FrequencyBase import FrequencyBase

class FrequencyTable(FrequencyBase):

    def __init__(self):
        super(FrequencyTable, self).__init__() # how to call super with abstractbase
        self.data = collections.defaultdict(lambda : 0)

    # cl tools casts this to int
    def add(self, key, count = 1):
        self.data[key] += count
        self.total += count
        self.n += 1
        self.max = max(self.max, key)
        self.min = min(self.min, key)
        self.is_sorted = False

    def percentile(self, percentile):
        """
            takes a percentile
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
        return max(self.data.iteritems(), key = lambda a:a[1])

    def ordered_data(self):
        if not self.is_sorted:
            self.data = sorted(self.data.iteritems(), key = lambda a: a[0])
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