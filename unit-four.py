from manim import *
class PracticeFormula1(Scene):
    def construct(self):
        formula = MathTex("E = mc^2")
        self.add(formula)
        self.wait(1)

class PracticeFormula2(Scene):
    def construct(self):
        multiline_formula = MathTex(
            "a^2 + b^2 = c^2",
            "\\sin^2\\theta + \\cos^2\\theta = 1"
        ).arrange(DOWN)  # 垂直排列
        self.add(multiline_formula)
        self.wait(1)

class PracticeFormula3(Scene):
    def construct(self):
        formula = MathTex("E", "=", "mc^2")  # 将公式分成几个部分
        self.add(formula)
        self.wait(1)
        formula.set_color_by_tex("mc^2", RED)  # 将 "mc^2" 设为红色
        self.wait(1)


class PracticeFormula4(Scene):
    def construct(self):
        formula = MathTex("E", "=", "mc^2")
        self.play(Write(formula)) 
        formula.scale(1.5)
        self.wait(1)

class PracticeFormula5(Scene):
    def construct(self):
        text_formula = VGroup(
            Text("The famous equation:"),
            MathTex("E = mc^2")
        ).arrange(DOWN)  # 垂直排列
        self.add(text_formula)
        self.wait(1)

class PracticeFormula6(Scene):
    def construct(self):
        text_formula = VGroup(
            Text("The famous equation:"),
            MathTex("E = mc^2")
        ).arrange(DOWN)  # 垂直排列
        self.play(FadeIn(text_formula))
        self.wait(1)

class PracticeFormula7(Scene):
    def construct(self):
        text_formula = VGroup(
            Text("The famous equation:"),
            MathTex("E = mc^2")
        ).arrange(DOWN)  # 垂直排列
        self.play(text_formula[0].animate.shift(LEFT))
        self.play(text_formula[1].animate.shift(RIGHT))
        self.wait(1)

class Exercise1(Scene):
     def construct(self):
        text = Text("This is a formula:")
        formula = MathTex("a^2 + b^2 = c^2")
        group = VGroup(text, formula).arrange(DOWN)
        self.play(FadeIn(group[0]))
        self.play(FadeIn(group[1]))
        self.wait(1)

class Exercise2(Scene):
    def construct(self):
        formula = MathTex("E = ","m","c^2")
        formula.set_color_by_tex("m", BLUE)
        formula.set_color_by_tex("c^2", RED)
        self.play(Write(formula))
        self.wait(1)

class Exercise3(Scene):
    def construct(self):
        formula = MathTex("a^2" , "+", "b^2" , "=", "c^2")
        self.play(Write(formula[:2]))  # 顯示 "a^2 +"
        self.play(Write(formula[2:4]))  # 顯示 "b^2 ="
        self.play(Write(formula[4:]))  # 顯示 "c^2"
        self.wait(1)

