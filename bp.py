from manim import *

class BackpropagationScene(Scene):
    def construct(self):
        # 設定網絡層的顏色
        input_layer_color = BLUE
        hidden_layer_color = GREEN
        output_layer_color = YELLOW
        
        # 創建神經網絡層
        input_layer = VGroup(
            Circle(radius=0.5, color=input_layer_color).shift(LEFT*3),
            Circle(radius=0.5, color=input_layer_color).shift(LEFT*2),
            Circle(radius=0.5, color=input_layer_color).shift(LEFT)
        )

        hidden_layer = VGroup(
            Circle(radius=0.5, color=hidden_layer_color).shift(UP),
            Circle(radius=0.5, color=hidden_layer_color).shift(UP + RIGHT)
        )

        output_layer = VGroup(
            Circle(radius=0.5, color=output_layer_color).shift(DOWN)
        )

        # 顯示層
        self.play(FadeIn(input_layer), FadeIn(hidden_layer), FadeIn(output_layer))
        self.wait(1)

        # 連接每一層
        input_to_hidden = VGroup(
            Line(input_layer[0].get_center(), hidden_layer[0].get_center(), color=WHITE),
            Line(input_layer[1].get_center(), hidden_layer[0].get_center(), color=WHITE),
            Line(input_layer[2].get_center(), hidden_layer[1].get_center(), color=WHITE)
        )

        hidden_to_output = Line(hidden_layer[1].get_center(), output_layer[0].get_center(), color=WHITE)

        self.play(Create(input_to_hidden), Create(hidden_to_output))
        self.wait(1)

        # 模擬前向傳播
        forward_arrow = Arrow(input_layer[0].get_center(), hidden_layer[0].get_center(), color=RED)
        self.play(GrowArrow(forward_arrow))
        self.wait(1)
        forward_arrow2 = Arrow(input_layer[2].get_center(), hidden_layer[1].get_center(), color=RED)
        self.play(GrowArrow(forward_arrow2))
        self.wait(1)

        # 反向傳播
        backward_arrow = Arrow(output_layer[0].get_center(), hidden_layer[1].get_center(), color=BLUE)
        self.play(GrowArrow(backward_arrow))
        self.wait(1)
        backward_arrow2 = Arrow(hidden_layer[0].get_center(), input_layer[0].get_center(), color=BLUE)
        self.play(GrowArrow(backward_arrow2))
        self.wait(1)

        # 完成動畫
        self.play(FadeOut(input_layer), FadeOut(hidden_layer), FadeOut(output_layer), FadeOut(input_to_hidden), FadeOut(hidden_to_output), FadeOut(forward_arrow), FadeOut(forward_arrow2), FadeOut(backward_arrow), FadeOut(backward_arrow2))
        self.wait(1)
