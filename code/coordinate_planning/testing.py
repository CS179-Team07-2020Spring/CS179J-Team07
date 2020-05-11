import unittest
from coordinate_planning1.py import check_angle



class TestFunction(unittest.TestCase):

    def test_in_range_1(self):
        self.assertEqual(check_angle(90), 90)
        
    def test_in_range_2(self):
        self.assertEqual(check_angle(30), 30)
        
    def test_in_range_3(self):
        self.assertEqual(check_angle(0), 0)
        
    def test_in_range_4(self):
        self.assertEqual(check_angle(-78), -78)
        
    def test_in_range_5(self):
        self.assertEqual(check_angle(-168), -168)
        
    def test_out_range_1(self):
        self.assertEqual(check_angle(-181), 179)
        
    def test_out_range_2(self):
        self.assertEqual(check_angle(181), -179)
        
    def test_out_range_3(self):
        self.assertEqual(check_angle(-359), 1)

    def test_out_range_4(self):
        self.assertEqual(check_angle(321), -39)
        
    def test_decimal_in_range_1(self):
        self.assertEqual(check_angle(67.4), 67.4)
        
    def test_decimal_in_range_2(self):
        self.assertEqual(check_angle(123.45), 123.45)
        
    def test_decimal_out_range_1(self):
        self.assertEqual(check_angle(-183.3), 176.7)
        
    def test_decimal_out_range_2(self):
        self.assertEqual(check_angle(212.7), -147.3)

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)