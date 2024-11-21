from manim import *
import numpy as np

# 定義 tanh 函數
def tanh(x):
    return np.tanh(x)

class TanhPlot(Scene):
    def construct(self):
        # 左側座標系
        axes = Axes(
            x_range=[-5, 5, 2],
            y_range=[-1.0, 1.0, 0.25],  # Y 軸從 0 開始
            axis_config={"color": BLUE},
            x_length=5,
            y_length=5,
            tips=False
        ).add_coordinates().to_edge(LEFT, buff=1)

        # Sigmoid 函數圖形
        graph = axes.plot(tanh, x_range=[-6, 6], color=YELLOW, use_smoothing=True)
        
        # 右側標題與公式
        title = Text("Tanh Function", font_size=36).next_to(axes, RIGHT, buff=1.5).align_to(axes, UP)
        formula_tex = MathTex(r"\tanh(x) = \frac{e^x - e^{-x}}{e^x + e^{-x}}", font_size=32).next_to(title, DOWN*4, aligned_edge=LEFT)
        
        # Y 值範圍標記（使用 LaTeX）
        y_range_label = y_range_label = MathTex(r"\text{Range of } y: (-1, 1)", font_size=34).next_to(formula_tex, DOWN*3, aligned_edge=LEFT, buff=0.5)
        
        # 動畫播放順序
        self.play(Create(axes), Create(graph))
        self.play(Write(title))
        self.play(Write(formula_tex))
        self.play(Write(y_range_label))
        
        # 保持畫面
        self.wait(3)

        # 結束
        self.play(FadeOut(axes), FadeOut(graph), FadeOut(title), FadeOut(formula_tex), FadeOut(y_range_label))
