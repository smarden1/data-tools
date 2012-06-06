import math

class SparkLines(object):
    """
        inspired by Stefan van der Walt <stefan@sun.ac.za>
        https://github.com/holman/spark
    """

    bars = [
        '\xe2\x96\x81',
        '\xe2\x96\x82',
        '\xe2\x96\x83',
        '\xe2\x96\x84',
        '\xe2\x96\x85',
        '\xe2\x96\x86',
        '\xe2\x96\x87',
        '\xe2\x96\x88'
    ]

    range = len(bars)

    def __init__(self, data, zero_start = False):
        self.data = data
        self.bin_size = math.ceil(self.data.range(zero_start) / self.range) + 1

    def result(self):
        return (self.getBar(i) for i in self.data.explode())

    def prettyPrint(self):
        print "".join(self.result())

    def getBar(self, value):
        i = int(math.floor((value - self.data.min) / self.bin_size))
        return self.bars[i]