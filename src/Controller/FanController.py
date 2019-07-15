"""
TheNexusAvenger

Controls the fan based on the given fan curve.
"""

from Observer import Observer



"""
Class representing an observer.
"""
class UpdaterObserver(Observer.Observer):
    """
    Creates an observers.
    """
    def __init__(self,fanController):
        self.fanController = fanController

    """
    Notifies an observer.
    """
    def notify(self,*args):
        self.fanController.updateFanSpeed()

"""
Class representing a fan controller.
"""
class FanController:
    """
    Creates a fan controller.
    """
    def __init__(self,temperatureMonitor,fan,fanCurve):
        self.temperatureMonitor = temperatureMonitor
        self.fan = fan
        self.fanCurve = fanCurve

        # Create an observer and register it.
        observer = UpdaterObserver(self)
        temperatureMonitor.register(observer)
        fanCurve.register(observer)

        # Update the fan speed.
        self.updateFanSpeed()

    """
    Updates the fan speed.
    """
    def updateFanSpeed(self):
        temperature = self.temperatureMonitor.getTemperature()
        fanSpeed = self.fanCurve.getFanSpeedForTemperature(temperature)
        self.fan.setSpeed(fanSpeed)