from manim import *

class SlideTransition(Scene):
    def construct(self):
        square = Square()
        self.play(Create(square))
        circle = Circle()
        self.play(Create(circle))
        self.play(Transform(square, circle))
        self.wait(1)


class PracticeAnimation(Scene):
    def construct(self):
        circle = Circle()
        self.play(Create(circle))
        self.play(circle.animate.move_to(UP + RIGHT))
        self.wait(1)

class PracticeAnimation2(Scene):
    def construct(self):
        square = Square()
        self.play(Rotate(square, angle=2*PI))
        self.play(square.animate.scale(0.5))
        self.wait(1)

class PracticeAnimation3(Scene):
    def construct(self):
        square = Square().shift(LEFT)
        circle = Circle().next_to(square,direction=RIGHT)
        triangle = Triangle().next_to(circle,direction=RIGHT)
        self.play(LaggedStart(FadeIn(square), FadeIn(circle), FadeIn(triangle)))
        self.wait(1)

