from datatools.Moments import Moments

class StreamingMoments(Moments):

    def __init__(self):
        self.n = 0
        self.total = 0
        self.moments_data = [0] * 6
        self.__moment_count = range(len(self.moments_data))

    def add(self, data_point):
        self.n += 1
        self.total += data_point
        for i in self.__moment_count:
            self.moments_data[i] += data_point ** i

    def moment(self, n):
        return self.moments_data[n]