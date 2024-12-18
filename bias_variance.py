from manim import *


class BiasVarianceAnimation(Scene):
    def construct(self):
        # 創建標靶圖的 function
        def create_target(x, y, radius=1.0, color=WHITE):
            target = VGroup()
            for r in range(1, 5):
                circle = Circle(radius=0.4 * r, color=WHITE, stroke_width=1.2)
                target.add(circle)
            target.move_to(np.array([x, y, 0])).scale(0.8).shift(DOWN * 0.5)
            return target

        # 生成每個標靶的中心座標
        centers = [
            (-4, 2, 0),  # Low Bias, Low Variance
            (4, 2, 0),  # Low Bias, High Variance
            (-4, -2, 0),  # High Bias, Low Variance
            (4, -2, 0),  # High Bias, High Variance
        ]

        # 逐步繪製每個標靶
        targets = [create_target(*c) for c in centers]
        self.play(*[Create(target) for target in targets])
        self.wait(0.5)

        # 添加標靶中心點
        red_dots = [
            Dot(color=RED).scale(0.8).move_to(center).shift(DOWN * 0.5)
            for center in centers
        ]
        self.play(*[Create(dot) for dot in red_dots])
        self.wait(0.5)

        # 動畫繪製點 (Bias 和 Variance)
        # Low Bias, Low Variance (左上)
        low_variance_low_bias_points = [
            Dot(color=BLUE)
            .scale(0.5)
            .move_to(np.array([-4, 2, 0]) + np.random.normal(0, 0.2, 3))
            .shift(DOWN * 0.5)
            for _ in range(8)
        ]
        self.play(*[FadeIn(point) for point in low_variance_low_bias_points])
        self.wait(0.5)

        # Low Bias, High Variance (右上)
        low_variance_high_bias_points = [
            Dot(color=BLUE)
            .scale(0.5)
            .move_to(np.array([4, 2, 0]) + np.random.normal(0, 0.6, 3))
            .shift(DOWN * 0.5)
            for _ in range(8)
        ]
        self.play(*[FadeIn(point) for point in low_variance_high_bias_points])
        self.wait(0.5)

        # High Bias, Low Variance (左下)
        high_bias_low_variance_points = [
            Dot(color=BLUE)
            .scale(0.5)
            .move_to(np.array([-3.5, -2, 0]) + np.random.normal(0, 0.2, 3))
            .shift(DOWN * 0.5)
            for _ in range(8)
        ]
        self.play(*[FadeIn(point) for point in high_bias_low_variance_points])
        self.wait(0.5)

        # High Bias, High Variance (右下)
        high_bias_high_variance_points = [
            Dot(color=BLUE)
            .scale(0.5)
            .move_to(np.array([5, -2, 0]) + np.random.normal(0, 0.6, 3))
            .shift(DOWN * 0.5)
            for _ in range(8)
        ]
        self.play(*[FadeIn(point) for point in high_bias_high_variance_points])
        self.wait(0.5)

        # 標示文字
        text1 = Text("Low Variance", font_size=24).move_to([-4, 3.5, 0])
        text2 = Text("High Variance", font_size=24).move_to([4, 3.5, 0])
        text3 = Text("Low Bias", font_size=24).rotate(PI / 2).move_to([-6, 2, 0]).shift(DOWN*0.5)
        text4 = Text("High Bias", font_size=24).rotate(PI / 2).move_to([-6, -2, 0]).shift(DOWN*0.5) 

        self.play(Write(text1), Write(text2), Write(text3), Write(text4))
        self.wait(2)
