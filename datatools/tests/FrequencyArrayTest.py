import unittest
from datatools.FrequencyArray import FrequencyArray

class TestEmptyFrequencyArray(unittest.TestCase):

    def setUp(self):
        self.empty_fa = FrequencyArray()

        self.ranged_fa = FrequencyArray()
        for i in range(10, 0, -1):
            self.ranged_fa.add(i)

    def testNoDataToStart(self):
        self.assertEqual(self.empty_fa.data, [])

    def testAddData(self):
        self.empty_fa.add(1)
        self.empty_fa.add(3)

        self.assertEqual(self.empty_fa.data, [1, 3])

    def testAddDataWithCounts(self):
        self.empty_fa.add(1, 2)
        self.empty_fa.add(3)

        self.assertEqual(self.empty_fa.data, [1, 1, 3])

    def testOrderedData(self):
        self.assertEqual(self.ranged_fa.orderedData(), range(1, 11))

    def testMax(self):
        self.assertEqual(self.ranged_fa.max, 10)

    def testMin(self):
        self.assertEqual(self.ranged_fa.min, 1)

if __name__ == "__main__":
    unittest.main()
