import unittest
from datatools.FrequencyTable import FrequencyTable

class TestFrequencyTable(unittest.TestCase):

    def setUp(self):
        self.empty_ft = FrequencyTable()

        self.range_ft = FrequencyTable()
        for i in range(10, 0, -1):
            self.range_ft.add(i)

        self.bucketed = FrequencyTable()
        self.bucketed.add(1)
        self.bucketed.add(2, 2)
        self.bucketed.add(3, 3)

    def testNoDataToStart(self):
        self.assertEqual(self.empty_ft.data, {})

    def testAddData(self):
        self.empty_ft.add(1)
        self.empty_ft.add(3)

        self.assertEqual(self.empty_ft.data, {1:1, 3:1})

    def testAddDataWithCounts(self):
        self.empty_ft.add(1, 2)
        self.empty_ft.add(3)

        self.assertEqual(self.empty_ft.data, {1:2, 3:1})

    def testOrderedData(self):
        self.assertEqual(self.range_ft.orderedData(), [(1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1), (8, 1), (9, 1), (10, 1)])

    def testOrderedDataBucketed(self):
        self.assertEqual(self.bucketed.orderedData(), [(1,1), (2,2), (3,3)])

    def testMax(self):
        self.assertEqual(self.range_ft.max, 10)

    def testMin(self):
        self.assertEqual(self.range_ft.min, 1)

    def testAverage(self):
        self.assertEqual(self.bucketed.mean(), 14/6.)

    def testModeWithObviousMode(self):
        self.assertEqual(self.bucketed.mode(), 3)

    def testModeWithNoMode(self):
        # first item
        self.assertEqual(self.range_ft.mode(), 1)

    def testExplodedData(self):
        exploded = [i for i in self.bucketed.explode()]
        self.assertEqual(exploded, [1,2,2,3,3,3])

    def testMedianUneven(self):
        self.bucketed.add(1)
        self.assertEqual(self.bucketed.median(), 2)

    def testMedianEven(self):
        self.assertEqual(self.bucketed.median(), 2)
        self.assertEqual(self.range_ft.median(), 5)

    def testFirstPercentile(self):
        self.assertEqual(self.range_ft.percentile(0), 1)

    def testLastPercentile(self):
        self.assertEqual(self.range_ft.percentile(1), 10)

    def testFirstQuantile(self):
        self.assertEqual(self.range_ft.firstQuartile(), 3)

    def testThirdQuantile(self):
        self.assertEqual(self.range_ft.thirdQuartile(), 8)

    def testInterquartileRange(self):
        self.assertEqual(self.range_ft.iqr(), 5)

    def testAddingCounts(self):
        self.empty_ft.add(1, 5)

        empty_2 = FrequencyTable()
        empty_2.add(1)
        empty_2.add(1)
        empty_2.add(1)
        empty_2.add(1)
        empty_2.add(1)

        self.assertEquals(self.empty_ft.data, {1:5})
        self.assertEquals(empty_2.data, {1:5})

    def testPdfAsMap(self):
        self.assertEquals(self.bucketed.pdfAsMap(), {1:1/6.,2:2/6.,3:.5})

    def testCdfAsMap(self):
        self.assertEquals(self.bucketed.cdfAsMap(), {1:1/6.,2:3/6.,3:1})

if __name__ == "__main__":
    unittest.main()
