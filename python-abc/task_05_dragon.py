#!/usr/bin/env python3


class SwimMixin:
    """
    Mixin providing swim.
    """

    def swim(self):
        print("The creature swims!")


class FlyMixin:
    """
    Mixin providing fly.
    """

    def fly(self):
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """
    Dragon class with swim, fly, and roar.
    """

    def roar(self):
        print("The dragon roars!")
