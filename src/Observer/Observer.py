"""
TheNexusAvenger

Classes for observing changes.
"""



"""
Class that observers an observable object.
"""
class Observer:
    """
    Notifies an observer.
    """
    def notify(self,*args):
        pass

"""
Abstract class the notifies observes.
"""
class Observable:
    """
    Constructor for the observable.
    """
    def __init__(self):
        self.observers = []

    """
    Notifies all the observers.
    """
    def notify(self,*args):
        for observer in self.observers:
            observer.notify(*args)

    """
    Registers an observer.
    """
    def register(self,observer):
        self.observers.append(observer)

    """
    Unregisters an observer.
    """
    def unregister(self,observer):
        self.observers.remove(observer)