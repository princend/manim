from manim import *
import numpy as np

# 定義 leaky relu 函數
def leaky_relu(x, alpha=0.01):
    return np.where(x > 0, x, alpha * x)

class LeakyReLUPlot(Scene):
    def construct(self):
        # 左側座標系
        sunbaby = ImageMobject("assets/sunbaby.png").scale(0.5)
        sunbaby.to_edge(DOWN+RIGHT)
        self.add(sunbaby)

        axes = Axes(
            x_range=[-20, 20, 4],
            y_range=[-1, 6, 1], 
            axis_config={"color": BLUE},
            x_length=5,
            y_length=5,
            tips=False
        ).add_coordinates().to_edge(LEFT, buff=1)

        # ReLU 函數圖形
        graph = axes.plot(leaky_relu, x_range=[-20, 7], color=YELLOW, use_smoothing=False)
        
        # 右側標題與公式
        title = Text("Leaky ReLU Function", font_size=36).next_to(axes, RIGHT, buff=1.5).align_to(axes, UP).shift(UP*0.7)
        formula_tex = MathTex(r"\text{LeakyReLU}(x) = \begin{cases} x, & x > 0 \\ \alpha x, & x \leq 0 \end{cases}", font_size=32).next_to(title, DOWN*4, aligned_edge=LEFT)

        alpha_range = MathTex(r"\alpha \in [0.01, 0.1]", r",\ \text{default}\ \alpha = 0.01", font_size=28).next_to(formula_tex, DOWN, buff=0.5)
        

        example1, point1, example2, point2, example3, point3 = self.generateExample(axes, alpha_range)

        # 動畫播放順序
        self.play(Create(axes), Create(graph))
        self.play(Write(title))
        self.play(Indicate(formula_tex,color=YELLOW))
        self.play(Write(alpha_range))
        self.play(Write(example1))
        self.play(Create(point1),Flash(point1,color=RED))
        self.play(Write(example2))
        self.play(Create(point2),Flash(point2,color=GREEN))
        self.play(Write(example3))
        self.play(Create(point3),Flash(point3,color=PURPLE))
        
        # 保持畫面
        self.wait(3)

        # 結束
        self.play(FadeOut(axes), FadeOut(graph), FadeOut(title), FadeOut(formula_tex),FadeOut(alpha_range),FadeOut(example1),FadeOut(point1),FadeOut(example2),FadeOut(point2),FadeOut(example3),FadeOut(point3),FadeOut(sunbaby))
        

    def generateExample(self, axes, alpha_range):
        example1 = Text("Leaky ReLU(-12) = -0.12", font_size=24,color=RED).next_to(alpha_range, DOWN*2)
        point1 = Dot(color=RED).move_to(axes.c2p(-12, -0.12))
        example2 = Text("Leaky ReLU(0) = 0", font_size=24,color=GREEN).next_to(example1, DOWN*2)
        point2 = Dot(color=GREEN).move_to(axes.c2p(0, 0))
        example3 = Text("Leaky ReLU(3) = 3", font_size=24,color=PURPLE).next_to(example2, DOWN*2)
        point3 = Dot(color=PURPLE).move_to(axes.c2p(3, 3))
        return example1,point1,example2,point2,example3,point3
