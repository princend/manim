from manim import *
import numpy as np

class RejectionSamplingWithColoredLines(Scene):
    def construct(self):
        # 設定目標分佈（雙峰高斯分佈）和提案分佈（單峰高斯分佈）
        def target_distribution(x):
            return 0.5 * np.exp(-0.5 * ((x - 1) / 0.8) ** 2) + \
                   0.5 * np.exp(-0.5 * ((x + 1) / 0.5) ** 2)

        def proposal_distribution(x):
            return np.exp(-0.5 * (x / 1.5) ** 2)
        c = 1.2  # 提案分佈的縮放常數
        # 繪製目標分佈和提案分佈
        axes = Axes(
            x_range=[-4, 4, 1],
            y_range=[0, 1.2, 0.2],
            axis_config={"include_tip": False},
        ).add_coordinates()

        target_graph = axes.plot(target_distribution, color=BLUE, x_range=[-4, 4])
        proposal_graph = axes.plot(lambda x: c * proposal_distribution(x), color=WHITE, x_range=[-4, 4])

        target_label = MathTex("p(x)").next_to(target_graph, RIGHT).shift(LEFT).set_color(BLUE)
        proposal_label = MathTex("c \\cdot q(x)").next_to(proposal_graph, RIGHT).shift(LEFT*3+UP*2).set_color(WHITE)

        self.play(Create(axes))
        self.play(Create(target_graph), Write(target_label))
        self.play(Create(proposal_graph), Write(proposal_label))
         # 顯示接受和拒絕標籤
        accept_label = Tex("Green dot: Accepted").set_color(GREEN).to_corner(UL)
        reject_label = Tex("Red dot: Rejected").set_color(RED).next_to(accept_label, DOWN)
        self.play(Write(accept_label), Write(reject_label))
        # 拒絕抽樣過程
        dots = VGroup()
        line_group=VGroup()
        for _ in range(10):  # 抽樣 30 次
            x = np.random.normal(0, 1.5)  # 從提案分佈抽樣
            y = np.random.uniform(0, c * proposal_distribution(x))

            # 點在初始時為白色
            dot = Dot(axes.c2p(x, y), color=WHITE).scale(1.2)
            self.add(dot)
            dots.add(dot)
            self.wait(0.5)
            # 畫垂直線
            y_px = target_distribution(x)
            line_below = Line(axes.c2p(x, 0), axes.c2p(x, y_px), color=GREEN)  # 綠色線段
            line_above = Line(axes.c2p(x, y_px), axes.c2p(x, c * proposal_distribution(x)), color=RED)  # 紅色線段
            line_group.add(line_below,line_above)
            self.play(Create(line_below), run_time=0.25)
            self.wait(0)
            self.play( Create(line_above), run_time=0.25)

            # 接受或拒絕的顏色變化
            if y < y_px:  # 接受
                self.play(dot.animate.set_color(GREEN), run_time=0.5)
            else:  # 拒絕
                self.play(dot.animate.set_color(RED), run_time=0.5)
        self.play(FadeOut(line_group),run_time=0.5)
        self.play(
            AnimationGroup(
                *[Flash(dot,color=GREEN,scale_factor=1.5) for dot in dots if dot.get_color() == GREEN],
                lag_ratio=0.1
            )
        )
        self.wait()
