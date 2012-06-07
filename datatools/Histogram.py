from datatools.FrequencyTable import FrequencyTable
import math

class Histogram(FrequencyTable):

    def __init__(self, bin_width = None):
        super(Histogram, self).__init__()
        self.bin_width = float(bin_width)

    def add(self, key, count = 1):
        bin_key = int(math.floor(key / self.bin_width))
        self.data[bin_key] += count
        self.total += key * count
        self.n += count
        self.max = max(self.max, key)
        self.min = min(self.min, key)
        self.is_sorted = False

    def ordered_data(self):
        if not self.is_sorted:
            self.ordered_data_list = [(i, self.data[i]) for i in xrange(0, self.max, self.bin_width)]
            self.is_sorted = True
        return self.ordered_data_list