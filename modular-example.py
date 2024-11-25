from manim import *
from mylibrary import CustomCircle, bounce_animation

class ModularExample(Scene):
    def construct(self):
        circle = CustomCircle(color=GREEN)
        self.add(circle)
        bounce_animation(circle, self)
        self.wait(1)
