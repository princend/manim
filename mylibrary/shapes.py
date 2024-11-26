from manim import *

class CustomCircle(VMobject):
    def __init__(self, radius=1, color=BLUE, **kwargs):
        super().__init__(**kwargs)
        circle = Circle(radius=radius, color=color)
        self.add(circle)