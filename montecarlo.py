from manim import *
import numpy as np

class MonteCarloPi(Scene):
    def construct(self):
        # 創建坐標系
        plane = NumberPlane(
            x_range=[-1.5, 1.5, 0.5],
            y_range=[-1.5, 1.5, 0.5],
            background_line_style={"stroke_opacity": 0.3}
        )
        self.play(Create(plane),run_time=0.05)  # 動畫顯示坐標平面

        # 畫出單位圓
        circle = Circle(radius=1, color=BLUE)
        self.play(Create(circle),run_time=0.05)  # 動畫顯示單位圓
        
        # 初始化計數器
        inside_count = 0
        total_points = 0

        # 顯示估計值
        pi_text = MathTex(r"\pi \approx 0").to_corner(UL)
        self.play(Write(pi_text),run_time=0.05)  # 動畫顯示初始估計值

        # 動畫: 逐點生成
        for _ in range(300):  # 生成300個點
        # for _ in range(300):  # 生成300個點
            total_points += 1
            # 隨機生成點
            x, y = np.random.uniform(-1, 1), np.random.uniform(-1, 1)
            point = Dot([x, y, 0], radius=0.03)

            # 檢查點是否在圓內
            if x**2 + y**2 <= 1:
                point.set_color(GREEN)
                inside_count += 1
            else:
                point.set_color(RED)

            # 使用動畫顯示點
            self.play(FadeIn(point, scale=0.5), run_time=0.001)

            # 更新 pi 的估計值
            pi_estimate = 4 * (inside_count / total_points)
            new_pi_text = MathTex(rf"\pi \approx {pi_estimate:.4f}").to_corner(UL)
            self.play(Transform(pi_text, new_pi_text), run_time=0.001)

        self.wait(1)
