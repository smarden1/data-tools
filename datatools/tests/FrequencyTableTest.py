import unittest
from datatools.FrequencyTable import FrequencyTable

class TestFrequencyTable(unittest.TestCase):

    def setUp(self):
        self.empty_ft = FrequencyTable()

        self.solitary_ft = FrequencyTable()
        for i in range(10, 0, -1):
            self.solitary_ft.add(i)

        self.bucketed = FrequencyTable()
        self.bucketed.add(1)

        self.bucketed.add(2)
        self.bucketed.add(2)

        self.bucketed.add(3)
        self.bucketed.add(3)
        self.bucketed.add(3)

    def test_no_data_to_start(self):
        self.assertEqual(self.empty_ft.data, {})

    def test_add_data(self):
        self.empty_ft.add(1)
        self.empty_ft.add(3)

        self.assertEqual(self.empty_ft.data, {1:1, 3:1})

    def test_add_data_with_counts(self):
        self.empty_ft.add(1, 2)
        self.empty_ft.add(3)

        self.assertEqual(self.empty_ft.data, {1:2, 3:1})

    def test_ordered_data(self):
        self.assertEqual(self.solitary_ft.ordered_data(), [(1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1), (8, 1), (9, 1), (10, 1)])

    def test_ordered_data_bucketed(self):
        self.assertEqual(self.bucketed.ordered_data(), [(1,1), (2,2), (3,3)])

    def test_max(self):
        self.assertEqual(self.solitary_ft.max, 10)

    def test_min(self):
        self.assertEqual(self.solitary_ft.min, 1)

    def test_average(self):
        self.assertEqual(self.bucketed.mean(), 14/6.)

    def test_mode_with_obvious_mode(self):
        self.assertEqual(self.bucketed.mode(), 3)

    def test_mode_with_no_mode(self):
        # first item
        self.assertEqual(self.solitary_ft.mode(), 1)

    def test_exploded_data(self):
        exploded = [i for i in self.bucketed.explode()]
        self.assertEqual(exploded, [1,2,2,3,3,3])


if __name__ == "__main__":
    unittest.main()
