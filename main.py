from manim import *
from shapes import CustomCircle
from animations import bounce_animation

class ModularScene(Scene):
    def construct(self):
        circle = CustomCircle(radius=2, color=YELLOW)
        self.add(circle)
        bounce_animation(circle, self)
        self.wait(1)
