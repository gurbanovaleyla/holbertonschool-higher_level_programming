#!/usr/bin/python3
"""This module represents Animal class and its subclasses like Dog and Cat."""


from abc import ABC, abstractmethod


class Animal(ABC):
    """An abstract class representing an animal."""

    @abstractmethod
    def sound(self):
        """Return the sound of animal."""
        pass


class Dog(Animal):
    """A class that inherits from Animal."""

    def sound(self):
        """Return the sound a dog makes."""
        return "Bark"


class Cat(Animal):
    """A class that inherits from Animal."""

    def sound(self):
        """Return the sound a cat makes."""
        return "Meow"
