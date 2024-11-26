from manim import *

class Array(Scene):
    def construct(self):
        text = VGroup(
            Text("A"),
            Text("B"),
            Text("C"),
            Text("D"),
            Text("E"),
            Text("F")
        ).arrange()

        text [0].set_color(RED)
        text [1].set_color(BLUE)
        text [2].set_color(GREEN)
        text [3].set_color(ORANGE)
        text [4].set_color("#DC28E2")
        text [5].set_color(PURPLE)

        a = Rectangle(
             width=2,
        height=1,
        stroke_width=3,          # 边线宽度
        stroke_color=WHITE,      # 边线颜色
        fill_opacity=1,          # 填充透明度
        fill_color=BLUE, 
        )
        # self.add(a)
        # self.play(Circumscribe(a))
        # self.wait(2)
        # self.remove(a)
        
        m1=Text("1")
        m2=Text("2")
        m3=Text("3")
        m4=Text("4")
        m5=Text("5")
        m6=Text("6")
        self.add(m1)
        m2.next_to(m1,DOWN)
        self.add(m2)
        # self.add(m1,m2,m3,m4,m5,m6)
        # m2.next_to(m1,DOWN)
        # m3.next_to(m2,DOWN)
        # m4.next_to(m3,DOWN)
        # m5.next_to(m4,DOWN)
        # m6.next_to(m5,DOWN)

        m1.to_corner(UL)
        self.play(Swap(m1,m2))
        
        # self.play(ReplacementTransform(m1,m2))
        self.wait(2)
        # self.play(ReplacementTransform(m2,m3))
        # self.wait(2)
        # self.play(ReplacementTransform(m3,m4))
        # self.wait(2)

