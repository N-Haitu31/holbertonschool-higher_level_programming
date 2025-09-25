#!/usr/bin/env python3


from abc import ABC, abstractmethod


class Animal(ABC):
    """
    Abstract base class for animals.
    """

    @abstractmethod
    def sound(self):
        """
        Abstract method to return the sound of the animal.
        """
        pass


class Dog(Animal):
    """
    Dog class, subclass of Animal.
    """

    def sound(self):
        """
        Returns the sound of the dog.
        """
        return "Bark"


class Cat(Animal):
    """
    Cat class, subclass of Animal.
    """

    def sound(self):
        """
        Returns the sound of the cat.
        """
        return "Meow"
