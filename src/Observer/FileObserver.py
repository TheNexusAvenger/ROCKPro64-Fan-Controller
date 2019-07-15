"""
TheNexusAvenger

Observes changes to files and handles IO operations.
"""

import threading
import time
import os
from Observer import Observer



"""
Class representing a file observer.
"""
class FileObserver(Observer.Observable):
    """
    Creates a file observer object.
    """
    def __init__(self,fileName):
        super().__init__()

        # Store the file and the last time.
        self.fileName = fileName
        if self.fileExists():
            self.lastContents = self.readFileLines()
        else:
            self.lastContents = None

        # Start polling in a thread.
        threading.Thread(target=self.startPolling).start()

    """
    Returns if the file exists.
    """
    def fileExists(self):
        return os.path.exists(self.fileName)

    """
    Returns the contents of the file. Throws an error
    if the file doesn't exist.
    """
    def readFileLines(self):
        # Throw an error if the file doesn't exist.
        if not self.fileExists():
            raise Exception("File does not exist: " + self.fileName)

        # Return the contents.
        with open(self.fileName) as file:
            return file.read()

    """
    Writes the contents of the files. Throws an error
    if the file doesn't exist.
    """
    def writeFileLines(self,lines):
        # Throw an error if the file doesn't exist.
        if not self.fileExists():
            raise Exception("File does not exist: " + self.fileName)

        # Write the contents.
        with open(self.fileName,"w") as file:
            file.writelines(str(lines))

    """
    Polling function that checks for file changes.
    """
    def startPolling(self):
        # Set up the loop.
        while True:
            # Check if the file has changed.
            if self.fileExists():
                newContents = self.readFileLines()

                # If the last modified time changed, notify the observers.
                if self.lastContents != newContents:
                    self.lastContents = newContents
                    self.notify()
            else:
                # If the file was removed, notify the observers.
                if self.lastContents != None:
                    self.lastContents = None
                    self.notify()

            # Sleep for 0.1 seconds.
            time.sleep(0.1)