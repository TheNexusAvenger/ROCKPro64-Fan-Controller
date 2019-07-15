"""
TheNexusAvenger

Monitors the temperature of the processor.
"""

from Observer import FileObserver

# The location of the file for temperature monitoring.
TEMPERATURE_ZONE_FILE_LOCATION = "/sys/class/thermal/thermal_zone0/temp"



"""
Class representing a temperature monitor.
"""
class TemperatureMonitor(FileObserver.FileObserver):
    """
    Creates a temperature monitor.
    """
    def __init__(self):
        super().__init__(TEMPERATURE_ZONE_FILE_LOCATION)

        # Throw an error if the temperature file doesn't exist.
        if not self.fileExists():
            raise Exception("Thermal zone file does not exist: " + TEMPERATURE_ZONE_FILE_LOCATION)

        # Store the last temperature.
        self.lastTemperature = self.getTemperature()

    """
    Returns the current temperature.
    """
    def getTemperature(self):
        return int(self.readFileLines())