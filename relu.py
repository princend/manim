from manim import *
import numpy as np

# 定義 relu 函數
def relu(x):
    return np.maximum(0, x)

class ReLUPlot(Scene):
    def construct(self):
        # 左側座標系
        axes = Axes(
            x_range=[-5, 5, 2],
            y_range=[-1, 5, 1],  # Y 軸從 0 開始
            axis_config={"color": BLUE},
            x_length=5,
            y_length=5,
            tips=False
        ).add_coordinates().to_edge(LEFT, buff=1)

        # ReLU 函數圖形
        graph = axes.plot(relu, x_range=[-5, 5], color=YELLOW, use_smoothing=False)
        
        # 右側標題與公式
        title = Text("ReLU Function", font_size=36).next_to(axes, RIGHT, buff=1.5).align_to(axes, UP)
        formula_tex = MathTex(r"\boldsymbol{ReLU(x) = \begin{cases}x & \text{if } x \geq 0 \\ 0 & \text{if } x < 0\end{cases}}", font_size=36).next_to(title, DOWN*4, aligned_edge=LEFT)
        example1, point1, example2, point2, example3, point3 = self.generateExample(axes, formula_tex)

        # 動畫播放順序
        self.play(Create(axes), Create(graph))
        self.play(Write(title))
        self.play(Indicate(formula_tex,color=YELLOW))
        self.play(Write(example1))
        self.play(Create(point1),Flash(point1,color=RED))
        self.play(Write(example2))
        self.play(Create(point2),Flash(point2,color=GREEN))
        self.play(Write(example3))
        self.play(Create(point3),Flash(point3,color=BLUE))
        
        # 保持畫面
        self.wait(3)

        # 結束
        self.play(FadeOut(axes), FadeOut(graph), FadeOut(title), FadeOut(formula_tex),FadeOut(example1),FadeOut(point1),FadeOut(example2),FadeOut(point2),FadeOut(example3),FadeOut(point3))

    def generateExample(self, axes, formula_tex):
        example1 = Text("ReLU(-2) = 0", font_size=24,color=RED).next_to(formula_tex, DOWN*2)
        point1 = Dot(color=RED).move_to(axes.c2p(-2, 0))
        example2 = Text("ReLU(0) = 0", font_size=24,color=GREEN).next_to(example1, DOWN*2)
        point2 = Dot(color=GREEN).move_to(axes.c2p(0, 0))
        example3 = Text("ReLU(3) = 3", font_size=24,color=BLUE).next_to(example2, DOWN*2)
        point3 = Dot(color=BLUE).move_to(axes.c2p(3, 3))
        return example1,point1,example2,point2,example3,point3
