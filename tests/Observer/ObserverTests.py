"""
TheNexusAvenger

Unit tests for the observer.
"""

import unittest
from Observer import Observer



"""
Test observer pattern.
"""
class TestObserverPattern(unittest.TestCase):
    """
    Tests observers are notified.
    """
    def testNotified(self):
        # Extend the observer class.
        class TestObserver(Observer.Observer):
            def notify(self,*args):
                self.notified = True

            def isNotified(self):
                if hasattr(self,"notified"):
                    return True

                return False

        # Create 3 observers.
        observer1 = TestObserver()
        observer2 = TestObserver()
        observer3 = TestObserver()

        # Create the observable and register observers.
        observable = Observer.Observable()
        observable.register(observer1)
        observable.register(observer2)

        # Notify the observers and run the assertions.
        observable.notify()
        self.assertTrue(observer1.isNotified(),"Observer 1 not notified.")
        self.assertTrue(observer2.isNotified(),"Observer 2 not notified.")
        self.assertFalse(observer3.isNotified(),"Observer 3 notified.")

    """
    Tests observers are notified with arguments.
    """
    def testNotifiedWithArgs(self):
        # Extend the observer class.
        class TestObserver(Observer.Observer):
            def notify(self_, *args):
                self.assertEqual(args[0],"Test1","Incorrect argument given.")
                self.assertEqual(args[1],"Test2","Incorrect argument given.")
                self.assertEqual(args[2],"Test3","Incorrect argument given.")

        # Create 3 observers.
        observer1 = TestObserver()
        observer2 = TestObserver()
        observer3 = TestObserver()

        # Create the observable and register observers.
        observable = Observer.Observable()
        observable.register(observer1)
        observable.register(observer2)
        observable.register(observer3)
        observable.unregister(observer3)

        # Notify the observers with arguments.
        observable.notify("Test1","Test2","Test3")

"""
Runs the unit tests.
"""
def main():
    unittest.main()



# Run the tests.
if __name__ == '__main__':
    main()
