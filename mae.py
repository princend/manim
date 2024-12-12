from manim import *

class MAEAnimation(Scene):
    def construct(self):
        
        title = Text("Mean Absolute Error (MAE)", font_size=48, color=BLUE)
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.to_edge(UP),run_time=0.5)
        
        axes = Axes(
            x_range=[0, 5, 1],  # x 轴范围
            y_range=[-3, 3, 1],  # y 轴范围
            axis_config={"color": WHITE},
            x_axis_config={"numbers_to_include": np.arange(1, 5)},
            y_axis_config={"numbers_to_include": np.arange(-3, 4)},
            x_length=5,  # 设置 x 轴长度
            y_length=5   # 设置 y 轴长度
        ).scale(0.75).to_edge(LEFT).shift(RIGHT)

        self.play(Create(axes),run_time=0.5)
        self.wait(0.5)

       
        
        differences = [0, 0.5, 0, 1.5]  # 计算的差异
        dots = VGroup(*[
            Dot(axes.c2p(i + 1, diff), color=RED) for i, diff in enumerate(differences)
        ])
        
        self.play(FadeIn(dots),run_time=0.5)
        self.wait(0.5)
        
         # 添加一条斜线模拟回归
        regression_line = axes.plot(lambda x: 0.5 * x - 1, x_range=[0, 5], color=GREEN)
        self.play(Create(regression_line),run_time=0.5)
        self.wait(0.5)
        
        # 为每个点绘制垂直线到回归线
        vertical_lines = VGroup(*[
            DashedLine(
                start=axes.c2p(i + 1, diff),
                end=axes.c2p(i + 1, 0.5 * (i + 1) - 1),  # 回归线上的点
                color=YELLOW
            ) for i, diff in enumerate(differences)
        ])
        
        self.play(Create(vertical_lines),run_time=1)
        self.wait(1)
        # 顯示公式
        # 计算 MAE 的公式
        mae_formula = MathTex(
            "MAE = ", 
            "\\frac{1}{n}", 
            "\\sum_{i=1}^{n} ", 
            "| y_i - \\hat{y}_i |",
            font_size=36
        ).to_edge(RIGHT).shift(UP*2+LEFT*2)  # 将公式移到场景右边

        mae_formula.set_color_by_tex("\\frac{1}{n}", RED)
        mae_formula.set_color_by_tex("| y_i - \\hat{y}_i |", YELLOW)

        # 逐步显示公式
        self.play(Write(mae_formula[0:2]),run_time=0.5)  # 显示 "MAE = " 和 "\\frac{1}{n}"
        self.wait(0.5)
        self.play(Write(mae_formula[2:]),run_time=0.5)  # 显示其余部分
        self.wait(0.5)
        
       
        # 计算 MAE 的过程
        mae_calculation_1 = MathTex(
            "= \\frac{1}{4}", 
            "(|0.5| + |0.5| + |-0.5| + |0.5|)",
            font_size=36
        ).next_to(mae_formula, DOWN, buff=0.5)

        mae_calculation_2 = MathTex(
            "= \\frac{1}{4} (0.5 + 0.5 + 0.5 + 0.5)",
            font_size=36
        ).next_to(mae_calculation_1, DOWN, aligned_edge=LEFT)

        mae_calculation_3 = MathTex(
            "= \\frac{2}{4}",
            font_size=36
        ).next_to(mae_calculation_2, DOWN, aligned_edge=LEFT)

        mae_calculation_4 = MathTex(
            "= 0.5",
            font_size=36
        ).next_to(mae_calculation_3, RIGHT, aligned_edge=LEFT).shift(RIGHT*0.25)

        # 逐步显示计算过程
        self.play(Write(mae_calculation_1),run_time=0.5)
        self.wait(0.5)
        self.play(Write(mae_calculation_2),run_time=0.5)
        self.wait(0.5)
        self.play(Write(mae_calculation_3),run_time=0.5)
        self.wait(0.5)
        self.play(Write(mae_calculation_4),run_time=0.5)
        self.wait(0.5)
        
