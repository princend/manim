from manim import *

class RegularizationVisual(Scene):
    def construct(self):
        # 設定標題
        l2_title = Text("L2 Regularization").scale(0.7).shift(DOWN * 3.2 + LEFT * 3.2)
        l1_title = Text("L1 Regularization").scale(0.7).shift(DOWN * 3.2 + RIGHT * 3.2)

        # L2 正則化 - 圓形約束
        l2_circle = Circle(radius=1.5, color=RED).shift(LEFT * 3.2)  # 約束圓
        l2_contours = VGroup(
            *[Circle(radius=r, color=BLUE).shift(LEFT * 3.2 + UP * 2.98 + RIGHT * 0.5)
            for r in [0.5, 1.0, 1.5]]
        )  # 等高線（偏移中心）
        l2_dot = Dot(point=LEFT * 3.4 + UP * 1.49 + RIGHT * 0.5, color=WHITE)  # 最佳解點
        l2_label = MathTex("w^*").next_to(l2_dot, DOWN * 0.5)
        l2_axes = Axes(x_range=[-2, 2], y_range=[-2, 2], axis_config={"color": WHITE},x_length=6).shift(LEFT * 3.2)
        l2_group=VGroup(l2_title,l2_circle,l2_contours,l2_dot,l2_label,l2_axes)
        l2_group.scale(0.7)
        # L1 正則化 - 菱形約束
        l1_diamond = Polygon(
            [-1.5, 0, 0], [0, 1.5, 0], [1.5, 0, 0], [0, -1.5, 0],
            color=RED
        ).shift(RIGHT * 3.2)  # 約束菱形
        l1_contours = VGroup(
           *[ Circle(radius=r, color=BLUE).shift(RIGHT * 3.2 + UP * 2.95 + RIGHT * 0.5)
            for r in [0.5, 1.0, 1.5]]
        )  # 等高線（偏移中心）
        l1_dot = Dot(point=RIGHT * 3.2 + UP * 1.5 , color=WHITE)  # 最佳解點
        l1_label = MathTex("w^*").next_to(l1_dot, DOWN * 0.5)

        # 座標軸
        l1_axes = Axes(x_range=[-2, 2], y_range=[-2, 2], axis_config={"color": WHITE},x_length=6).shift(RIGHT * 3.2)
        l1_group=VGroup(l1_title,l1_diamond,l1_contours,l1_dot,l1_label,l1_axes)
        l1_group.scale(0.7)
        # 加入圖形
        self.play(Write(l2_title), Write(l1_title))
        self.play(Create(l2_axes), Create(l1_axes))
        self.play(Create(l2_circle), Create(l1_diamond))
        self.play(Create(l2_contours), Create(l1_contours))
        self.play(FadeIn(l2_dot), Write(l2_label),FadeIn(l1_dot), Write(l1_label))
        

        # 停留畫面
        self.wait(2)
