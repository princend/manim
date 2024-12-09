from manim import *
import numpy as np

class RejectionSampling(Scene):
    def construct(self):
        # 設定目標分佈（正態分佈）和提案分佈（均勻分佈）
        def target_distribution(x):
            return np.exp(-x**2)

        def proposal_distribution(x):
            return 1

        # 繪製目標分佈和提案分佈
        axes = Axes(
            x_range=[-3, 3, 1],
            y_range=[0, 1.2, 0.2],
            axis_config={"include_tip": False},
        ).add_coordinates()

        target_graph = axes.plot(target_distribution, color=BLUE, x_range=[-3, 3])
        proposal_graph = axes.plot(
            lambda x: proposal_distribution(x), color=GREEN, x_range=[-3, 3]
        )

        target_label = MathTex("p(x)").next_to(target_graph, RIGHT).set_color(BLUE)
        proposal_label = MathTex("c \\cdot q(x)").next_to(proposal_graph, RIGHT).set_color(GREEN)

        self.play(Create(axes))
        self.play(Create(target_graph), Write(target_label))
        self.play(Create(proposal_graph), Write(proposal_label))

        # 拒絕抽樣過程
        samples = []
        dots = VGroup()
        for _ in range(30):  # 抽樣 30 次
            x = np.random.uniform(-3, 3)
            y = np.random.uniform(0, 1)
            dot = Dot(axes.c2p(x, y))
            if y < target_distribution(x):
                dot.set_color(GREEN)  # 接受
                samples.append(x)
            else:
                dot.set_color(RED)  # 拒絕
            dots.add(dot)
            self.add(dot)
            self.wait(0.1)  # 漸進可視化

        # 顯示接受樣本
        self.play(
            AnimationGroup(
                *[dot.animate.scale(1.5).set_color(GREEN) for dot in dots if dot.get_color() == GREEN],
                lag_ratio=0.1
            )
        )
        self.wait()

        # 標示接受和拒絕
        accept_label = Tex("Accepted").set_color(GREEN).to_corner(UL)
        reject_label = Tex("Rejected").set_color(RED).to_corner(UR)
        self.play(FadeIn(accept_label), FadeIn(reject_label))
        self.wait()
