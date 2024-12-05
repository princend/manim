from manim import *

class GradientDescentEscape(Scene):
    def construct(self):
        # 1. 定義函數圖形
        axes = Axes(
            x_range=[-3, 3, 1], y_range=[-2, 4, 1],
            axis_config={"color": BLUE},
        ).add_coordinates()

        func = axes.plot(
            lambda x: x**4 - 2*x**2 + 0.5,
            color=YELLOW,
            x_range=[-2.2, 2.2],
        )
        func_label = axes.get_graph_label(func, label="f(x)")

        # 2. 初始點
        dot = Dot(axes.c2p(-1.8, (-1.8)**4 - 2*(-1.8)**2 + 0.5), color=RED)
        path = TracedPath(dot.get_center, stroke_color=RED, stroke_width=4)

        # 3. 動畫展示梯度下降
        self.play(Create(axes), Create(func), Write(func_label))
        self.add(dot, path)

        # 梯度下降的步驟
        learning_rate = 0.1
        x = -1.8  # 初始位置
        for _ in range(20):
            grad = 4 * x**3 - 4 * x  # 導數 f'(x)
            new_x = x - learning_rate * grad
            if abs(new_x - x) < 0.01:  # 模擬局部最小點附近跳脫
                new_x += 0.5  # 加入隨機擾動來跳脫
            x = new_x
            new_y = x**4 - 2*x**2 + 0.5
            self.play(dot.animate.move_to(axes.c2p(x, new_y)), run_time=0.3)

        self.wait(2)
