import unittest
from helper_function import *



class TestFunction(unittest.TestCase):

    def test_in_range_1(self):
        self.assertEqual(check_angle(90), 90)
        
    def test_in_range_2(self):
        self.assertEqual(check_angle(30), 30)
        
    def test_in_range_3(self):
        self.assertEqual(check_angle(0), 0)
        
    def test_in_range_4(self):
        self.assertEqual(check_angle(210), 210)
        
    def test_in_range_5(self):
        self.assertEqual(check_angle(359), 359)
        
    def test_out_range_1(self):
        self.assertEqual(check_angle(-1), 359)
        
    def test_out_range_2(self):
        self.assertEqual(check_angle(-180), 180)
        
    def test_out_range_3(self):
        self.assertEqual(check_angle(-359), 1)

    def test_out_range_4(self):
        self.assertEqual(check_angle(-210), 150)

    def test_angle_range_convert_1(self):
        self.assertEqual(angle_range_convert(180), 180)

    def test_angle_range_convert_2(self):
        self.assertEqual(angle_range_convert(210), -150)

    def test_angle_range_convert_3(self):
        self.assertEqual(angle_range_convert(-190), 170)

    def test_angle_range_convert_4(self):
        self.assertEqual(angle_range_convert(-290), 70)

    def test_update_info_straight_1(self):
        self.assertAlmostEqual(update_info_straight(0,0,180,1)[0], -1.0)

    def test_update_info_straight_2(self):
        self.assertAlmostEqual(update_info_straight(0,0,180,1)[1], 0)

    def test_update_info_straight_3(self):
        self.assertAlmostEqual(update_info_straight(0,0,90,1)[0], 0)
        
    def test_update_info_straight_4(self):
        self.assertAlmostEqual(update_info_straight(0,0,90,1)[1], 1)

    def test_reach_destination_1(self):
        self.assertTrue(reach_destination(0, 0, 1 , 1))
        
    def test_reach_destination_2(self):
        self.assertTrue(reach_destination(0, 0.09, 1 , 1))
        
    def test_reach_destination_3(self):
        self.assertTrue(reach_destination(0, 0.05, 1 , 0.95))
        
    def test_reach_destination_4(self):
        self.assertFalse(reach_destination(0, 0.10, 1 , 1))
        
    def test_reach_destination_5(self):
        self.assertFalse(reach_destination(0, 0.05, 1 , 0.90))
        
    def test_reach_destination_6(self):
        self.assertFalse(reach_destination(0, 0, 1 , 0.899))

    def test_convert_angle_1(self):
        self.assertAlmostEqual(convert_angle(1,1), 45)
        
    def test_convert_angle_2(self):
        self.assertAlmostEqual(convert_angle(2,2*math.sqrt(3)), 60)
    
    def test_convert_angle_3(self):
        self.assertAlmostEqual(convert_angle(-2,2*math.sqrt(3)), 120)
        
    def test_convert_angle_4(self):
        self.assertAlmostEqual(convert_angle(-2,-2*math.sqrt(3)), -120)
        
    def test_convert_angle_5(self):
        self.assertAlmostEqual(convert_angle(2,-2*math.sqrt(3)), -60)
        

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)