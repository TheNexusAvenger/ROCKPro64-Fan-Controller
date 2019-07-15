"""
TheNexusAvenger

Algorithm for a fan curve.
"""

from Observer import FileObserver
from Observer import Observer

# The default fan speed if there is no points.
DEFAULT_FAN_SPEED = 0



"""
Class representing a fan curve.
"""
class FanCurve(Observer.Observable):
    """
    Creates a fan curve with a set of points.
    """
    def __init__(self,defaultPoints):
        super().__init__()
        self.points = []

        # Set the points.
        self.setPoints(defaultPoints)

    """
    Sets the points.
    """
    def setPoints(self,points):
        # Convert the points to a list.
        newPoints = []
        for temperature,relativeFanSpeed in points.items():
            newPoints.append([temperature,relativeFanSpeed])

        # Returns the first value.
        def sortFunction(value):
            return value[0]

        # Sort the list.
        newPoints.sort(key=sortFunction)

        # Set the points and notify the observers.
        self.points = newPoints
        self.notify()

    """
    Returns the fan speed value for the given temperature.
    """
    def getFanSpeedForTemperature(self,temperature):
        # Get the bounding points.
        lessThanPoint = None
        greaterThanPoint = None
        for point in self.points:
            if point[0] <= temperature and (lessThanPoint == None or point[0] > lessThanPoint[0]):
                lessThanPoint = point
            if point[0] >= temperature and greaterThanPoint == None:
                greaterThanPoint = point

        # Return the point.
        if lessThanPoint == None and greaterThanPoint == None:
            return DEFAULT_FAN_SPEED
        elif lessThanPoint == None:
            return greaterThanPoint[1]
        elif greaterThanPoint == None:
            return lessThanPoint[1]
        else:
            # If the delta is 0, return one of the points.
            temperatureDelta = greaterThanPoint[0] - lessThanPoint[0]
            if temperatureDelta == 0:
                return lessThanPoint[1]

            # Calculate the interpolation.
            startFanSpeed = lessThanPoint[1]
            endFanSpeed = greaterThanPoint[1]
            interpolationRatio = (temperature - lessThanPoint[0])/temperatureDelta
            return startFanSpeed + (interpolationRatio * (endFanSpeed - startFanSpeed))

"""
Creates a fan curve from a file.
"""
def fromFile(fileLocation):
    # Create the file observer and empty fan curve.
    fileObserver = FileObserver.FileObserver(fileLocation)
    fanCurve = FanCurve({})

    """
    Updates the fan curve from the file.
    """
    def updateFanCurve():
        # If the file doesn't exist, empty the fan curve.
        if not fileObserver.fileExists():
            fanCurve.setPoints({})
            return

        # Parse the fan curve points.
        newPoints = {}
        for line in fileObserver.readFileLines().split("\n"):
            line = line.trim()
            numbers = line.split(",")

            try:
                newPoints[float(numbers[0])] = float(numbers[1])
            except:
                pass

        # Set the points.
        fanCurve.setPoints(newPoints)

    """
    Class that observes the file observer.
    """
    class FanCurveObserver(Observer.Observer):
        """
        Notifies an observer.
        """
        def notify(self,*args):
            updateFanCurve()

    # Set the default fan curve and add the observer.
    fileObserver.register(FanCurveObserver())
    updateFanCurve()

    # Return the fan curve.
    return fanCurve