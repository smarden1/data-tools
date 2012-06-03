import datatools.Moments

class StreamingMoments(Moments.Moments):

    def __init__(self):
        self.n = 0
        self.moments = [0] * 4

    def add(self, data_point):
        self.n += 1
        for i in self.moments:
            self.moments[i] += data_point ** i
