"""
TheNexusAvenger

Unit tests for the fan curve.
"""

import unittest
from Controller import FanCurve



"""
Tests the fan curve class.
"""
class TestFanCurve(unittest.TestCase):
    """
    Tests that no points returns the default speed.
    """
    def testNoPoints(self):
        # Create an empty fan curve.
        emptyFanCurve = FanCurve.FanCurve({})

        # Assert any point returns the default.
        self.assertEqual(emptyFanCurve.getFanSpeedForTemperature(0),FanCurve.DEFAULT_FAN_SPEED,"Default fan speed not returned.")

    """
    Tests that a proper fan curve with points returns the correct speeds.
    """
    def testPoints(self):
        # Create the points.
        points = {
            20 : 0.1,
            40 : 0.5,
            60 : 0.6,
            80 : 1,
        }

        # Create the fan curve.
        fanCurve = FanCurve.FanCurve(points)

        # Assert the values are correct.
        self.assertEqual(fanCurve.getFanSpeedForTemperature(0),0.1,"Fan speed not correct.")
        self.assertEqual(fanCurve.getFanSpeedForTemperature(20),0.1,"Fan speed not correct.")
        self.assertAlmostEqual(fanCurve.getFanSpeedForTemperature(30),0.3,msg="Fan speed not correct.")
        self.assertEqual(fanCurve.getFanSpeedForTemperature(40),0.5,"Fan speed not correct.")
        self.assertAlmostEqual(fanCurve.getFanSpeedForTemperature(50),0.55,msg="Fan speed not correct.")
        self.assertEqual(fanCurve.getFanSpeedForTemperature(60),0.6,"Fan speed not correct.")
        self.assertAlmostEqual(fanCurve.getFanSpeedForTemperature(70),0.8,msg="Fan speed not correct.")
        self.assertEqual(fanCurve.getFanSpeedForTemperature(80),1,"Fan speed not correct.")
        self.assertEqual(fanCurve.getFanSpeedForTemperature(100),1,"Fan speed not correct.")

"""
Runs the unit tests.
"""
def main():
    unittest.main()



# Run the tests.
if __name__ == '__main__':
    main()