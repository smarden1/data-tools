import math

class HistogramPlot(object):    

    defaultRange = 50

    def __init__(self, data, zero_start = False, displayRange = defaultRange):
        self.data = data
        self.range = displayRange
        self.bin_size = math.ceil(self.data.range(zero_start) / self.range) + 1

    def result(self):
        return (self.getBar(i) for i in self.data.data)

    def prettyPrint(self):
        return "\n".join(self.result())

    def getBar(self, value):
        return "".join(["*"] * int(math.floor((value - self.data.min) / self.bin_size)))