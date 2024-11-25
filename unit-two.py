from manim import *

class BasicScene(Scene):
    def construct(self):
        square = Square()  # 創建一個方形
        self.add(square)  # 將方形添加到場景中
        self.wait(1)  # 等待 1 秒


from manim import *

class PracticeScene(Scene):
    def construct(self):
        circle = Circle().set_color(BLUE).shift(LEFT * 3)
        square = Square().set_color(RED).shift(RIGHT * 3)
        group = VGroup(circle, square)
       
        self.play(circle.animate.move_to(ORIGIN), square.animate.move_to(ORIGIN))
        self.wait(1) 
        self.play(Rotate(group, angle=PI/2))     
        self.wait(1) 
         