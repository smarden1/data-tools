import unittest
from datatools.FrequencyArray import FrequencyArray

class TestEmptyFrequencyArray(unittest.TestCase):

    def setUp(self):
        self.empty_fa = FrequencyArray()

        self.ranged_fa = FrequencyArray()
        for i in range(10, 0, -1):
            self.ranged_fa.add(i)

    def test_no_data_to_start(self):
        self.assertEqual(self.empty_fa.data, [])

    def test_add_data(self):
        self.empty_fa.add(1)
        self.empty_fa.add(3)

        self.assertEqual(self.empty_fa.data, [1, 3])

    def test_add_data_with_counts(self):
        self.empty_fa.add(1, 2)
        self.empty_fa.add(3)

        self.assertEqual(self.empty_fa.data, [1, 1, 3])

    def test_ordered_data(self):
        self.assertEqual(self.ranged_fa.ordered_data(), range(1, 11))

    def test_max(self):
        self.assertEqual(self.ranged_fa.max, 10)

    def test_min(self):
        self.assertEqual(self.ranged_fa.min, 1)

if __name__ == "__main__":
    unittest.main()
