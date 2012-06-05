

class StemAndLeaf(object):

    def __init__(self, data, granularity = 10):
        self.data = data
        self.granularity = granularity
        self.result = [[self.granularity * i] for i in self.data.range]

    def result(self):
        for i, v in enumerate(self.data.ordered_data()):
            yield self.result[v / self.granularity][1].append(v - i * self.granularity)

    def prettyPrint(self):
        for k,v in self.result():
            print k + " | " + " ".join(v)
            