"""
TheNexusAvenger

Controls the PWM fan of the system.
"""

from Observer import FileObserver
from Observer import Observer



# The minimum PWM signal (0-255) for the fan to turn on.
FAN_MINIMUM_PWM_SIGNAL = 64

# The location of the file for controlling the PWM signal.
PWM_FILE_LOCATION = "/sys/class/hwmon0/pwm1"



"""
Class representing a fan.
"""
class Fan(Observer.Observable):
    """
    Creates a fan object.
    """
    def __init__(self):
        super().__init__()

        # Throw an error if the PWM file doesn't exist.
        self.fileObserver = FileObserver.FileObserver(PWM_FILE_LOCATION)
        if not self.fileObserver.fileExists():
            raise Exception("PWM controller file does not exist: " + PWM_FILE_LOCATION)

        # Stop the fan.
        self.currentSpeed = 0
        self.setSpeed(0)

    """
    Sets the speed of the fan. Accepts a value
    between 0 and 1.
    """
    def setSpeed(self,speed):
        self.currentSpeed = speed

        # Convert the speed to a byte (0-255).
        newSpeed = int(speed * 255)
        if newSpeed < FAN_MINIMUM_PWM_SIGNAL:
            newSpeed = FAN_MINIMUM_PWM_SIGNAL

        # Write the speed.
        self.fileObserver.writeFileLines(newSpeed)

        # Notify the observers.
        self.notify()

    """
    Returns the current speed of the fan. Value
    is between 0 and 1.
    """
    def getSpeed(self):
        return self.currentSpeed