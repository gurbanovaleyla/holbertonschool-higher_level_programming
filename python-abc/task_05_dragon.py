#!/usr/bin/env python3
"""Module demonstrating mixins with a Dragon class."""


class SwimMixin:
    """Mixin that provides swimming behavior."""

    def swim(self):
        """Swimming action."""
        print("The creature swims!")


class FlyMixin:
    """Mixin that provides flying behavior."""

    def fly(self):
        """Flying action."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Dragon class that combines swimming and flying abilities."""

    def roar(self):
        """Dragon roar action."""
        print("The dragon roars!")
