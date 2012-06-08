import math

class StemAndLeaf(object):

    def __init__(self, data, granularity = 10):
        self.data = data
        self.granularity = float(granularity)

    def result(self):
        results = self.__initiateRange()

        for i, v in enumerate(self.data.explode()):
            index = int(math.floor(v / self.granularity))
            results[index].append(v - index)

        return results

    def __initiateRange(self):
        r = int(math.ceil(self.data.range() / self.granularity))

        return [[i * self.granularity] for i in xrange(r)]

    def prettyPrint(self):
        for i in self.result():
            print "%s"%(i[0]) + " | " + " ".join(map(str, i[1::]))
            
