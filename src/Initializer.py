"""
TheNexusAvenger

Initializes the service.
"""

from Controller import FanController
from Controller import FanCurve
from Hardware import Fan
from Hardware import TemperatureMonitor

# File location of the fan curve.
FAN_CURVE_FILE_LOCATION = "FanCurve.txt"



# Create the fan, temperature monitor, and fan curve.
fan = Fan.Fan()
temperatureMonitor = TemperatureMonitor.TemperatureMonitor()
fanCurve = FanCurve.fromFile(FAN_CURVE_FILE_LOCATION)

# Create the fan controller.
FanController.FanController(temperatureMonitor,fan,fanCurve)