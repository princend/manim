from manim import *

class CustomShape(VMobject):
    def __init__(self, color=BLUE, **kwargs):
        super().__init__(**kwargs)
        self.set_points_as_corners([UP, RIGHT, DOWN*2, LEFT, UP])
        self.set_color(color)

class CustomShapeScene(Scene):
    def construct(self):
        shape = CustomShape(color=YELLOW)
        self.play(Create(shape))
        self.wait(1)

class RotatingSquare(VGroup):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        square = Square(color=BLUE)
        self.add(square)
    # 旋轉動畫
    def rotate_with_animation(self, scene):
        scene.play(self.animate.rotate(PI / 2))        

class AnimationExample(Scene):
    def construct(self):
        rotating_square = RotatingSquare()
        self.add(rotating_square)
        rotating_square.rotate_with_animation(self)
        self.wait(1)