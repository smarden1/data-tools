from datatools.FrequencyTable import FrequencyTable
from datatools.FrequencyArray import FrequencyArray
from datatools.SparkLines import SparkLines
import math

class Histogram(FrequencyTable):

    def __init__(self, bin_width = None):
        super(Histogram, self).__init__()
        self.bin_width = float(bin_width)
        self.max_bin_key = 0

    def add(self, key, count = 1):
        bin_key = self.bin_key(key)
        self.data[bin_key] += count
        self.total += key * count
        self.n += count
        self.max_bin_key = max(self.max_bin_key, bin_key)
        self.max = max(self.max, key)
        self.min = min(self.min, key)
        self.is_sorted = False

    def bin_key(self, key):
        return int(math.floor(key / self.bin_width))

    def bin_key_to_value(self, key):
        return int(key * self.bin_width)

    def orderedData(self):
        if not self.is_sorted:
            self.orderedData_list = [(self.bin_key_to_value(i), self.data[i]) for i in xrange(self.max_bin_key + 1)]
            self.is_sorted = True
        return self.orderedData_list

    def spark_line(self):
        s = SparkLines(FrequencyArray(self.ordered_values()))
        return s.prettyPrint()
