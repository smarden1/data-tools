import math

class SparkLines(object):

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

        try:
            self.max = data.max
            self.min = data.min
            self.n = data.n
        except AttributeError:
            self.max = max(self.data)
            self.min = min(self.data)
            self.n = len(self.data)
        finally:
            self.min = 0 if zero_start else self.min
            self.spread = self.max - self.min
            self.bin_size = math.ceil(self.spread / self.range) + 1

    def result(self):
        if hasattr(self.data, "explode"):
            return (self.getBar(i) for i in self.data.explode())
        return (self.getBar(i) for i in self.data)

    def getBar(self, value):
        i = int(math.floor((value - self.min)/self.bin_size))
        return self.bars[i]