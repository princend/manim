from manim import *
import numpy as np


class PdfToCdf(Scene):
    def construct(self):
        # 创建坐标系
        axes = Axes(
            x_range=[-4, 4, 1],
            y_range=[0, 1.1, 0.1],  # CDF的y范围应该是0到1
            axis_config={"color": WHITE, "include_numbers": True},
        ).scale(0.9)

        # 定义PDF函数
        # pdf = axes.plot(
        #     lambda x: 0.5 * np.exp(-0.5 * x**2), color=BLUE, x_range=[-4, 4]
        # )

        # 计算CDF
        cdf = axes.plot(
            lambda x: 0.5 * (1 + np.math.erf(x / np.sqrt(2))),
            color=GREEN,
            x_range=[-4, 4],
        )

        # 创建PDF和CDF标签
        # pdf_label = axes.get_graph_label(pdf, label="PDF", x_val=-3, direction=UP)
        cdf_label = axes.get_graph_label(cdf, label="CDF", x_val=3, direction=UP)

        # 动画
        self.play(Create(axes), Write(cdf_label))
        # self.play(Create(pdf), Write(pdf_label))
        self.wait(0.5)

        # integral_formula = MathTex(
        #     r"\text{CDF}(x) = \int_{-\infty}^{x} \text{PDF}(t) \, dt"
        # ).to_corner(UL).scale(0.8)

        # self.play(Write(integral_formula))

        self.play(Create(cdf))
        self.wait(1)

        # 添加逆采样过程的LaTeX公式
        cdf_definition = (
            MathTex(r"CDF(x) = \int_{-\infty}^x f(t) \, dt").to_corner(UL).scale(0.8)
        )

        # 从均匀分布中生成随机数
        uniform_distribution = (
            MathTex(r"u \sim U(0, 1)", color=BLUE).next_to(cdf_definition, DOWN).scale(
                0.8
            )
        )

        # 计算逆累积分布函数得到样本
        inverse_cdf = (
            MathTex(r"x = CDF^{-1}(u)", color=RED).next_to(uniform_distribution, DOWN).scale(
                0.8
            )
        )

        self.play(Write(cdf_definition))
        self.play(Write(uniform_distribution))
        self.play(Write(inverse_cdf))
        self.wait(1)

        # 使用逆采样方法
        samples = self.inverse_transform_sampling(
            lambda x: 0.5 * (1 + np.math.erf(x / np.sqrt(2)))
        )

        cdf_func = lambda x: 0.5 * (1 + np.math.erf(x / np.sqrt(2)))

        self.wait(0.5)
        # 收集样本数据
        for index, sample in enumerate(samples):
            x_value = sample
            y_value = cdf_func(sample)
            x_dot = Dot(axes.c2p(x_value, y_value), color=BLUE).scale(1)
            y_dot = Dot(axes.c2p(x_value, 0), color=RED).scale(1.5)

            # 创建垂直线
            vertical_line = DashedLine(
                start=axes.c2p(x_value, 0), end=axes.c2p(x_value, y_value), color=WHITE
            )

            # 显示点
            self.play(Create(x_dot), run_time=0.1)
            self.play(Create(vertical_line), run_time=0.1)
            self.play(Create(y_dot), run_time=0.1)
            self.wait(0.5)

            # 显示点对应的x值

            x_value_text = (
                Text(f"= {x_value:+.2f}", font_size=20, color=RED)
                .to_edge(RIGHT)
                .shift(DOWN * index * 0.5)
                .shift(LEFT * 1.5)
            )

            x_text = (
                Text(f"x{index+1}", font_size=20, color=RED)
                .shift(DOWN * index * 0.5 + RIGHT * 2)
                .next_to(x_value_text, LEFT)
            )

            self.play(Write(x_text), Write(x_value_text))
            self.wait(0.5)

        # 创建表格
        # table = Table(table_data, col_labels=[Text("Sample Index"), Text("x Value")], include_outer_lines=True)
        # table.to_corner(UL).scale(0.5)  # 将表格放置在左上角

        # 显示表格
        # self.play(Create(table))
        self.wait(1)

        # 计算 CDF 的反函数

    # 逆采样函数
    def inverse_transform_sampling(self, cdf_func, num_samples=5):
        # 从均匀分布中采样
        uniform_samples = np.random.uniform(0, 1, num_samples)
        # 使用 CDF 的反函数来获取样本
        samples = np.array([self.inverse_cdf(u, cdf_func) for u in uniform_samples])
        return samples

    def inverse_cdf(self, u, cdf_func):
        from scipy.optimize import bisect

        # 调试输出
        a, b = -4, 4
        fa = cdf_func(a) - u
        fb = cdf_func(b) - u
        # print(f"f(a) = {fa}, f(b) = {fb}")

        if fa * fb >= 0:
            raise ValueError("f(a) and f(b) must have different signs")

        return bisect(lambda x: cdf_func(x) - u, a, b)
