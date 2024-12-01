from manim import *

class SimpleNN(Scene):
    def construct(self):
        input_layer = VGroup(*[Circle(radius=0.3,color=YELLOW) for _ in range(3)])
        hidden_layer = VGroup(*[Circle(radius=0.3,color=YELLOW) for _ in range(4)])
        output_layer = Circle(radius=0.3,color=YELLOW)

        input_layer.arrange(DOWN, buff=0.5)
        hidden_layer.arrange(DOWN, buff=0.5)
        
        input_layer.move_to(LEFT * 4)
        hidden_layer.move_to(LEFT * 0)
        output_layer.move_to(RIGHT * 4)

        connections1 = VGroup(*[
            Line(input_neuron.get_right(), hidden_neuron.get_left())
            for input_neuron in input_layer
            for hidden_neuron in hidden_layer
        ])

        connections2 = VGroup(*[
            Line(hidden_neuron.get_right(), output_layer.get_left())
            for hidden_neuron in hidden_layer
        ])

        relu_graphs = VGroup()
        for circle in VGroup(*input_layer,*hidden_layer):
            activation = VGroup(
                Line(LEFT * 0.1, RIGHT * 0.3, color=WHITE),  # x轴部分
                Line(RIGHT * 0.3, RIGHT * 0.6 + UP * 0.3, color=WHITE)  # y=x部分
            ).scale(0.5)
            activation.move_to(circle.get_center())
            relu_graphs.add(activation)  
        
        ### 其實是tanh
        sigmoid = ParametricFunction(
            lambda t: np.array([t, np.tanh(t), 0]),  # 使用tanh函数
            t_range=np.array([-2, 2]),  # 调整t的范围
            color=WHITE
        ).scale(0.1)
        
        sigmoid.move_to(output_layer.get_center())

        self.play(Create(input_layer),Create(hidden_layer),Create(output_layer),run_time=0.5)
        self.wait(0.1)
        self.play(Create(relu_graphs),Create(sigmoid),run_time=0.3)
        self.wait(0.1)
        self.play(Create(connections1),Create(connections2),run_time=0.5)
        self.wait(0.25)

        nn = VGroup(input_layer,hidden_layer,output_layer,connections1,connections2,relu_graphs,sigmoid)
        self.play(nn.animate.scale(0.8).to_edge(LEFT),run_time=1)
        self.wait(0.5)
        nn_without_relu_graphs = VGroup(input_layer,hidden_layer,output_layer,connections1,connections2)
        
        for activation in VGroup(*relu_graphs,*sigmoid):
            activation.set_opacity(0) 
        self.play(nn_without_relu_graphs.animate.rotate(-PI/2),
                  run_time=0.5)
        self.wait(0.1)
        self.play(*[activation.animate.move_to(circle.get_center()) for activation, circle in zip(VGroup(*relu_graphs,sigmoid),VGroup(*input_layer,*hidden_layer,*output_layer))],run_time=0.1)
        self.wait(0.1)
        self.play(*[activation.animate.set_opacity(1) for activation in VGroup(*relu_graphs,sigmoid)],
                  run_time=0.1)
        self.wait(0.1)
        code = Code(
            file_name="simple_nn.py",
            language="Python",
            tab_width=1,
            font="Monospace",
            font_size=42,
            line_spacing=2,
            stroke_width=2,
            background="window",
        )
        code.width = 7

        code.next_to(nn,RIGHT*3)
        self.play(Write(code))
        self.wait(0.1)
        rectangle = Rectangle(
            width=code.width,
            height=code.height/6,
            color=RED
        )
        rectangle.move_to(code.get_top()).shift(DOWN*2.3)  # 将长方形移动到 Code 对象的中心

        self.play(
            FadeIn(rectangle),
            *[circle.animate.set_color(RED) for circle in input_layer],
            *[activation.animate.set_color(RED) for activation in VGroup(*relu_graphs[:3])],
            run_time=0.5
        )
        self.wait(1)
        self.play(
            rectangle.animate.move_to(code.get_top()).shift(DOWN*4.0),
            *[circle.animate.set_color(YELLOW) for circle in input_layer],
            *[activation.animate.set_color(WHITE) for activation in VGroup(*relu_graphs[:3])],
            *[circle.animate.set_color(RED) for circle in hidden_layer],
            *[activation.animate.set_color(RED) for activation in VGroup(*relu_graphs[3:])],
            run_time=0.5
        )
        self.wait(1)
        self.play(
            rectangle.animate.move_to(code.get_top()).shift(DOWN*5.7),
            *[circle.animate.set_color(YELLOW) for circle in hidden_layer],
            *[activation.animate.set_color(WHITE) for activation in VGroup(*relu_graphs[3:])],
            *[circle.animate.set_color(RED) for circle in output_layer],
            sigmoid.animate.set_color(RED),
            run_time=0.5
        )
        self.wait(1)
        self.play(
            *[circle.animate.set_color(YELLOW) for circle in output_layer],
            sigmoid.animate.set_color(WHITE),
            FadeOut(rectangle),
            run_time=0.5
        )
        self.wait(1)



