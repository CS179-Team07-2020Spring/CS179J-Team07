import unittest
from pathPlanningHelper import *



class TestFunction(unittest.TestCase):

    def test_cal_dis1(self):
        self.assertEqual(calculateDistance((10,10), (10,10)), 0.0)

    def test_cal_dis2(self):
        self.assertAlmostEqual(calculateDistance((12,10), (10,10)), 2.0)

    def test_cal_dis3(self):
        self.assertAlmostEqual(calculateDistance((12,12), (10,10)), math.sqrt(8))

    def test_checkBoundry1(self):
        self.assertTrue(checkBoundry(3, 3, (5,5)))

    def test_checkBoundry2(self):
        self.assertTrue(checkBoundry(3, 4, (5,5)))

    def test_checkBoundry3(self):
        self.assertFalse(checkBoundry(3, 5, (5,5)))

    def test_checkBoundry4(self):
        self.assertFalse(checkBoundry(5, 3, (5,5)))

    def test_gen8dirList1(self):
        self.assertEqual(gen8dirList(2,2)[0], (3,2))

    def test_gen8dirList2(self):
        self.assertEqual(gen8dirList(2,2)[1], (3,3))

    def test_gen8dirList3(self):
        self.assertEqual(gen8dirList(2,2)[2], (2,3))

    def test_gen8dirList4(self):
        self.assertEqual(gen8dirList(2,2)[3], (1,3))

    def test_gen8dirList5(self):
        self.assertEqual(gen8dirList(2,2)[4], (1,2))

    def test_gen8dirList6(self):
        self.assertEqual(gen8dirList(2,2)[5], (1,1))

    def test_gen8dirList7(self):
        self.assertEqual(gen8dirList(2,2)[6], (2,1))

    def test_gen8dirList8(self):
        self.assertEqual(gen8dirList(2,2)[7], (3,1))

        

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)