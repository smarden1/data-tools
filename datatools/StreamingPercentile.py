import datatools.Exceptions

# http://www.cs.wustl.edu/~jain/papers/ftp/psqr.pdf
# TODO - think about trying length of markers to 11 or 21 or 101 - abstract out desired_marker_positions_generator
class StreamingPercentile(object):

    def __init__(self, p):
        if p > 1.0:
            raise PercentageGreaterThanOne(p)

        self.p = p
        self.n = 0

        self.marker_positions, self.incremental_marker_positions = self.setup_markers()

        self.desired_marker_positions_generator = 
        {
            0: lambda : 0,
            1: lambda : (self.n - 1) * (self.p / 2) + 1,
            2: lambda : (self.n - 1) * self.p + 1,
            3: lambda : (self.n - 1) * (1 + self.p) / 2 + 1,
            4: lambda : self.n
        }

        self.full_markers = False
        self.markers = []
        self.postions = [1,2,3,4,5]


    def setup_markers(self):
        marker_positions = [
            1,
            1 + (2 * self.p),
            1 + (4 * self.p),
            3 + (2 * self.p),
            5
        ]

        incremental_marker_positions = [
            0,
            self.p / 2,
            self.p,
            (1 + self.p) / 2,
            1
        ]

        return marker_positions, incremental_marker_positions

    def result(self):
        return self.markers[2]
        
    def add(self, data_point):
        if not self.full_markers:
            self.markers.append(data_point)

            if len(self.markers) == 5:
                self.full_markers.sort()
                self.full_markers = True
        else:

            for i, m in enumerate(self.markers):
               if data_point >= m:
                   self.positions[i] += 1

            for i in range(1,4):
                desired_marker_position = self.desired_marker_position(i)
                if abs(self.positions[i] - desired_marker_position) > 1:
                    d = float(cmp(self.positions[i], desired_marker_position))
                    self.markers[i] += self.height_delta(i)
                    self.postions[i] += d

    def height_delta(self, i, d = 1.):
        p2 = self.parabolic_prediction(i, d)

        if self.markers[i] + p2 < self.markers[i-1] or self.markers[i] + p2 > self.markers[i+1]:
            return self.linear_prediction(i, d)

        return p2

    def linear_prediction(self, i, d = 1.):
        n = self.positions
        q = self.markers

        return q[i] + d * (q[i+d] - q[i]) / float(n[i+d] - n[i])
        
    def parabolic_prediction(self, i, d = 1.):
        n = self.positions
        q = self.markers

        return d / (n[i+1] - n[i-1]) * ((n[i] - n[i-1] + d) * ((q[i+1] - q[i]) / (n[i+1] - n[i])) + (n[i+1] - n[i] - d) * ((q[i] - q[i-1]) / (n[i] - n[i-1])))
           
    def desired_marker_positions(self):
        return map(self.desired_marker_position, range(5))

    def desired_marker_position(self, index):
        return self.desired_marker_positions_generator[index]()
