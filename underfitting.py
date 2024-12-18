from manim import *

class TrainingTestingCurve(Scene):
    def construct(self):
        # 建立坐標軸
        axes = Axes(
            x_range=[0, 10, 1],
            y_range=[0, 5, 1],
            axis_config={"color": WHITE},
            x_length=10,
            y_length=6
        )
        axes_labels = axes.get_axis_labels(x_label="d^{*}_{VC}", y_label="Error")
        self.play(Create(axes), Write(axes_labels))

        # 訓練誤差曲線（Training）
        training_curve = axes.plot(
            lambda x: 5 / (x + 1),  # 訓練誤差遞減
            color=BLUE,
            x_range=[0.1, 9]
        )
        training_label = MathTex("Training", color=BLUE).scale(0.7).move_to(axes.c2p(7, 1))
        
        # 測試誤差曲線（Testing：非線性，快速下降後平緩上升）
        testing_curve = axes.plot(
            lambda x: (2 / (x + 0.5)) + 0.2 * x+2,  # 非線性：指數衰減 + 緩慢上升
            color=PURPLE,
            x_range=[0.1, 9]
        )
        testing_label = MathTex("Testing", color=PURPLE).scale(0.7).move_to(axes.c2p(7, 3))

        # VC 維度最小誤差線
        vc_line = DashedLine(
            start=axes.c2p(2.5, 0),
            end=axes.c2p(2.5, 5),
            color=MAROON
        )
        vc_label = MathTex(r"d^{*}_{VC}", color=MAROON).scale(0.7).next_to(vc_line, DOWN)

        # 背景區域顏色
        left_bg = Rectangle(width=2.5, height=6, color=ORANGE, fill_opacity=0.15)
        
        left_bg.move_to(axes.c2p(1.25, 2.5))
        underfitting_text = Text("underfitting", color=ORANGE).scale(0.5)
        underfitting_text.move_to(left_bg.get_center())
        
        right_bg = Rectangle(width=6.5, height=6, color=YELLOW, fill_opacity=0.15)
        right_bg.move_to(axes.c2p(5.75, 2.5))
        overfitting_text = Text("overfitting", color=YELLOW).scale(0.5)
        overfitting_text.move_to(right_bg.get_center())
        # 顯示動畫
        
        self.play(Create(training_curve), Write(training_label))
        self.play(Create(testing_curve), Write(testing_label))
        self.play(Create(vc_line), Write(vc_label))
        self.wait(0.5)
        for i in range(2):
            if i == 0:
                self.play(Write(underfitting_text),FadeIn(left_bg),run_time=0.3)
            else:
                self.play(FadeIn(left_bg),run_time=0.3)
            self.wait(0.2)
            self.play(FadeOut(left_bg),run_time=0.3)
            self.wait(0.2)
        self.play(FadeIn(left_bg),run_time=0.3)
        self.play(FadeOut(left_bg),FadeOut(underfitting_text))
        self.wait(0.5)
        for i in range(2):
            if i == 0:
                self.play(Write(overfitting_text),FadeIn(right_bg),run_time=0.3)
            else:
                self.play(FadeIn(right_bg),run_time=0.3)
            self.wait(0.2)
            self.play(FadeOut(right_bg),run_time=0.3)
            self.wait(0.2)
        self.play(FadeIn(right_bg),run_time=0.3)
        self.play(FadeOut(right_bg),FadeOut(overfitting_text))
        self.wait(2)
        # self.play(Wiggle(right_bg))
        # self.wait(0.5)
        # self.play(FadeOut(right_bg))
