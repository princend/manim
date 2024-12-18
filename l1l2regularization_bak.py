from manim import *

class L1RegularizationWithLoss(Scene):
    def construct(self):
        # 坐標軸
        axes = Axes(
            x_range=[-3, 3, 1],
            y_range=[-3, 3, 1],
            axis_config={"color": BLUE},
        )
        labels = axes.get_axis_labels(x_label="w_1", y_label="w_2")

        # L1 範圍: 菱形
        l1_region = Polygon(
            [0, 2, 0], [2, 0, 0], [0, -2, 0], [-2, 0, 0],
            color=YELLOW, fill_opacity=0.2
        )
        l1_text = Text("此為 L1 正規化", font_size=24).next_to(l1_region, UP)

        # 損失函數的等高線圖，中心位移到 (0, 0) 以便與 L1 正規化區域相交
        loss_contours = VGroup(
            *[ParametricFunction(
                # lambda t: np.array([r * np.cos(t), r * np.sin(t), 0]),  # 中心改為 (0, 0)
                lambda t: np.array([2 + r * np.cos(t), 3 + r * np.sin(t), 0]),  # 中心改為 (a, b)
                t_range=[0, TAU],
                color=GRAY
            ) for r in np.linspace(1, 2, 4)]  # 調整半徑範圍以確保相交
        )

        # 顯示 L1 正規化與損失等高線
        self.play(Create(axes), Write(labels))
        self.play(FadeIn(l1_region), Write(l1_text))
        self.play(Create(loss_contours))
        self.wait(2)

        # 收尾
        self.play(FadeOut(axes), FadeOut(labels), FadeOut(l1_region), FadeOut(l1_text), FadeOut(loss_contours))
