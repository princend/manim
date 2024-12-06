from manim import *


class PdfToCdf(Scene):
    def construct(self):
        # 创建坐标系
        axes = Axes(
            x_range=[-4, 4, 1],
            y_range=[0, 1.1, 0.1],  # CDF的y范围应该是0到1
            axis_config={"color": WHITE, "include_numbers": True},
        ).scale(0.9)

        # 定义PDF函数
        pdf = axes.plot(
            lambda x: 0.5 * np.exp(-0.5 * x**2), color=BLUE, x_range=[-4, 4]
        )

        # 计算CDF
        cdf = axes.plot(
            lambda x: 0.5 * (1 + np.math.erf(x / np.sqrt(2))),
            color=GREEN,
            x_range=[-4, 4],
        )

        # 创建PDF和CDF标签
        pdf_label = axes.get_graph_label(pdf, label="PDF", x_val=-3, direction=UP)
        cdf_label = axes.get_graph_label(cdf, label="CDF", x_val=3, direction=UP)

        # 动画
        self.play(Create(axes))
        self.play(Create(pdf), Write(pdf_label))
        self.wait(0.5)
        
        integral_formula = MathTex(
            r"\text{CDF}(x) = \int_{-\infty}^{x} \text{PDF}(t) \, dt"
        ).to_corner(UL).scale(0.8)
        
        self.play(Write(integral_formula))
        self.play(Transform(pdf, cdf), Transform(pdf_label, cdf_label))
        self.wait(2)
