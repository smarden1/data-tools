import unittest
from datatools.Histogram import Histogram
from datatools.FrequencyTable import FrequencyTable
from datatools.FrequencyArray import FrequencyArray

class TestHistogram(unittest.TestCase):

    def setUp(self):
        self.ranged_fa = FrequencyArray()
        self.ranged_ft = FrequencyTable()
        self.expected_all = {}

        for i in range(10, 0, -1):
            self.ranged_fa.add(i)
            self.ranged_ft.add(i)
            self.expected_all[i] = 1

    def test_range_to_histogram(self):
        histogram = Histogram(1)
        for i in range(10, 0, -1):
            histogram.add(i)

        self.assertEqual(histogram.data, self.expected_all)

    def test_array_to_histogram(self):
        histogram = Histogram(1)
        for i in self.ranged_fa.explode():
            histogram.add(i)

        self.assertEqual(histogram.data, self.expected_all)

    def test_table_to_histogram(self):
        histogram = Histogram(1)
        for i in self.ranged_ft.explode():
            histogram.add(i)

        self.assertEqual(histogram.data, self.expected_all)

    def test_histogram_bucket_width_of_two(self):
        histogram = Histogram(2)
        for i in range(10, 0, -1):
            histogram.add(i)

        self.assertEqual(histogram.data, {0:1, 1:2, 2:2, 3:2, 4:2, 5:1})

    def test_histogram_bucket_width_of_two(self):
        histogram = Histogram(2)
        for i in range(10, 0, -1):
            histogram.add(i)

        self.assertEqual(histogram.ordered_data(), [(0,1), (2,2), (4,2), (6,2), (8,2), (10,1)])

    def test_histogram_bucket_width_of_three(self):
        histogram = Histogram(3)
        for i in range(10, 0, -1):
            histogram.add(i)

        self.assertEqual(histogram.ordered_data(), [(0,2), (3,3), (6,3), (9,2)])

if __name__ == "__main__":
    unittest.main()
