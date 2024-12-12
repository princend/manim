from manim import *


class MSEAnimation(Scene):
    def construct(self):

        title = Text("Mean Squared Error (MSE)", font_size=48, color=BLUE)
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.to_edge(UP), run_time=0.5)

        axes = (
            Axes(
                x_range=[0, 5, 1],  # x 轴范围
                y_range=[-3, 3, 1],  # y 轴范围
                axis_config={"color": WHITE},
                x_axis_config={"numbers_to_include": np.arange(1, 5)},
                y_axis_config={"numbers_to_include": np.arange(-3, 4)},
                x_length=5,  # 设置 x 轴长度
                y_length=5,  # 设置 y 轴长度
            )
            .scale(0.75)
            .to_edge(LEFT)
            .shift(RIGHT)
        )

        self.play(Create(axes), run_time=0.5)
        self.wait(0.5)

        differences = [0, 0.5, 0, 1.5]  # 计算的差异
        dots = VGroup(
            *[
                Dot(axes.c2p(i + 1, diff), color=RED)
                for i, diff in enumerate(differences)
            ]
        )

        self.play(FadeIn(dots), run_time=0.5)
        self.wait(0.5)

        # 添加一条斜线模拟回归
        regression_line = axes.plot(lambda x: 0.5 * x - 1, x_range=[0, 5], color=GREEN)
        self.play(Create(regression_line), run_time=0.5)
        self.wait(0.5)

        # 为每个点绘制垂直线到回归线
        vertical_lines = VGroup(
            *[
                DashedLine(
                    start=axes.c2p(i + 1, diff),
                    end=axes.c2p(i + 1, 0.5 * (i + 1) - 1),  # 回归线上的点
                    color=YELLOW,
                )
                for i, diff in enumerate(differences)
            ]
        )

        self.play(Create(vertical_lines), run_time=1)
        self.wait(1)
        # 顯示公式
        # 计算 MSE 的公式
        mse_formula = (
            MathTex(
                "MSE = ",
                "\\frac{1}{n}",
                "\\sum_{i=1}^{n} ",
                "(y_i - \\hat{y}_i)^2",
                font_size=36,
            )
            .to_edge(RIGHT)
            .shift(UP * 2 + LEFT * 2)
        )  # 将公式移到场景右边

        mse_formula.set_color_by_tex("\\frac{1}{n}", RED)
        mse_formula.set_color_by_tex("(y_i - \\hat{y}_i)^2", YELLOW)

        # 逐步显示公式
        self.play(
            Write(mse_formula[0:2]), run_time=0.5
        )  # 显示 "MSE = " 和 "\\frac{1}{n}"
        self.wait(0.5)
        self.play(Write(mse_formula[2:]), run_time=0.5)  # 显示其余部分
        self.wait(0.5)

        # 计算 MSE 的过程
        mse_calculation_1 = MathTex(
            "= \\frac{1}{4}", "((0.5)^2 + (0.5)^2 + (-0.5)^2 + (0.5)^2)", font_size=36
        ).next_to(mse_formula, DOWN, buff=0.5)

        mse_calculation_2 = MathTex(
            "= \\frac{1}{4} (0.25 + 0.25 + 0.25 + 0.25)", font_size=36
        ).next_to(mse_calculation_1, DOWN, aligned_edge=LEFT)

        mse_calculation_3 = MathTex("= \\frac{1}{4} (1)", font_size=36).next_to(
            mse_calculation_2, DOWN, aligned_edge=LEFT
        )

        mse_calculation_4 = (
            MathTex("= 0.25", font_size=36)
            .next_to(mse_calculation_3, RIGHT, aligned_edge=LEFT)
            .shift(RIGHT * 0.5)
        )

        # 逐步显示计算过程
        self.play(Write(mse_calculation_1), run_time=0.5)
        self.wait(0.5)
        self.play(Write(mse_calculation_2), run_time=0.5)
        self.wait(0.5)
        self.play(Write(mse_calculation_3), run_time=0.5)
        self.wait(0.5)
        self.play(Write(mse_calculation_4), run_time=0.5)
        self.wait(0.5)
        # 移除所有现有物件
        all_objects = VGroup(
            title,
            axes,
            dots,
            regression_line,
            vertical_lines,
            mse_formula,
            mse_calculation_1,
            mse_calculation_2,
            mse_calculation_3,
            mse_calculation_4,
        )
        self.play(FadeOut(all_objects))
        self.wait(0.5)

        # 创建MSE和MAE的图形
        error_axes = Axes(
            x_range=[-10, 10, 5],
            y_range=[0, 100, 20],  # 调整y轴范围以适应MSE的值
            axis_config={"color": WHITE},
            x_axis_config={"numbers_to_include": np.arange(-10, 11, 5)},
            y_axis_config={"numbers_to_include": np.arange(0, 101, 20)},
            x_length=8,
            y_length=6,
        ).scale(0.8)

        title_mse = Text("MSE", font_size=48, color=BLUE)
        title_mse.to_edge(UP).shift(LEFT * 1.5)
        title_vs = Text("vs", font_size=48, color=WHITE).next_to(
            title_mse, RIGHT, buff=0.5
        )
        title_mae = Text("MAE", font_size=48, color=RED).next_to(
            title_vs, RIGHT, buff=0.5
        )

        # 绘制MAE的V形图
        mae_graph = error_axes.plot(lambda x: abs(x), x_range=[-10, 10], color=RED)

        # 绘制MSE的抛物线
        mse_graph = error_axes.plot(lambda x: x**2, x_range=[-10, 10], color=BLUE)

        # 添加图例
        mae_dot = Dot(color=BLUE)
        mse_dot = Dot(color=RED)
        mae_text = Text("MSE", font_size=24, color=BLUE)
        mse_text = Text("MAE", font_size=24, color=RED)

        legend = VGroup(mae_dot, mae_text, mse_dot, mse_text).arrange(RIGHT, buff=0.2)
        legend.to_corner(UR).shift(LEFT*0.5 + DOWN)

        error_group = VGroup(error_axes, mae_graph, mse_graph)
        error_group.move_to(ORIGIN)

        # 显示图形
        self.play(Write(title_mse), Write(title_vs), Write(title_mae), run_time=0.5)
        self.play(Create(error_axes), run_time=0.5)
        self.play(Create(mae_graph), run_time=0.5)
        self.play(Create(mse_graph), run_time=0.5)
        self.play(Create(legend), run_time=0.5)
        self.wait(2)
