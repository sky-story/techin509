# Abstractions (Abstract Base Class)
from abc import ABC, abstractmethod

# Abstract base classes are used to define interfaces and cannot be directly instantiated.
# Subclasses must implement all interfaces marked as abstract methods and then can be instantiated
class NotificationMethod(ABC):
    @abstractmethod
    def send(self, message):
        pass
