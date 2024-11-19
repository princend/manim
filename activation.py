from manim import *
import numpy as np

# 定義激活函數
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def tanh(x):
    return np.tanh(x)

def relu(x):
    return np.maximum(0, x)

def leaky_relu(x, alpha=0.01):
    return np.where(x > 0, x, alpha * x)

def elu(x, alpha=1.0):
    return np.where(x > 0, x, alpha * (np.exp(x) - 1))

def gelu(x):
    return x * 0.5 * (1.0 + np.tanh(np.sqrt(2 / np.pi) * (x + 0.044715 * x**3)))

class ActivationFunctions(Scene):
    def plot_function(self, func, x_range, y_range, func_name, formula):
        # 左側座標系
        axes = Axes(
            x_range=x_range,
            y_range=y_range,
            axis_config={"color": BLUE},
            x_length=5,  # 縮小座標系
            y_length=5,
            tips=False
        ).add_coordinates().to_edge(LEFT, buff=1)

        graph = axes.plot(func, x_range=x_range, color=YELLOW)

        # 右側標題與公式
        title = Text(func_name, font_size=36).next_to(axes, RIGHT, buff=1.5).align_to(axes, UP)
        formula_tex = MathTex(formula, font_size=30).next_to(title, DOWN, aligned_edge=LEFT)

        # 顯示軸、函數圖和公式
        self.play(Create(axes), Create(graph))
        self.play(Write(title), Write(formula_tex))
        self.wait(2)
        self.play(FadeOut(axes), FadeOut(graph), FadeOut(title), FadeOut(formula_tex))

    def construct(self):
        functions = [
            (sigmoid, [-6, 6, 1], [-0.5, 1.5, 0.5], "Sigmoid", r"\sigma(x) = \frac{1}{1 + e^{-x}}"),
            # (tanh, [-6, 6, 1], [-1.5, 1.5, 0.5], "Tanh", r"\tanh(x) = \frac{e^x - e^{-x}}{e^x + e^{-x}}"),
            # (relu, [-6, 6, 1], [-1, 6, 1], "ReLU", r"\text{ReLU}(x) = \max(0, x)"),
            # (leaky_relu, [-6, 6, 1], [-1, 6, 1], "Leaky ReLU", r"\text{Leaky ReLU}(x) = \begin{cases} x, & x > 0 \\ \alpha x, & x \leq 0 \end{cases}"),
            # (elu, [-6, 6, 1], [-2, 6, 1], "ELU", r"\text{ELU}(x) = \begin{cases} x, & x > 0 \\ \alpha (e^x - 1), & x \leq 0 \end{cases}"),
            # (gelu, [-6, 6, 1], [-1, 6, 1], "GELU", r"\text{GELU}(x) = x \cdot \Phi(x)")
        ]

        for func, x_range, y_range, func_name, formula in functions:
            self.plot_function(func, x_range, y_range, func_name, formula)
