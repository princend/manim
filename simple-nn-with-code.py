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
            relu = VGroup(
                Line(ORIGIN, RIGHT * 0.3, color=BLUE),  # x轴部分
                Line(RIGHT * 0.3, RIGHT * 0.6 + UP * 0.3, color=BLUE)  # y=x部分
            ).scale(0.5)
            relu.move_to(circle.get_center())
            relu_graphs.add(relu)  

        self.play(Create(input_layer),Create(hidden_layer),Create(output_layer),run_time=0.5)
        self.wait(0.1)
        self.play(Create(relu_graphs),run_time=0.3)
        self.wait(0.1)
        self.play(Create(connections1),Create(connections2),run_time=0.5)
        self.wait(0.25)

        nn = VGroup(input_layer,hidden_layer,output_layer,connections1,connections2,relu_graphs)
        self.play(nn.animate.scale(0.6).to_edge(LEFT*2),run_time=1)
        self.wait(0.5)
        nn_without_relu_graphs = VGroup(input_layer,hidden_layer,output_layer,connections1,connections2)
        
        for relu in relu_graphs:
            relu.set_opacity(0) 
        self.play(nn_without_relu_graphs.animate.rotate(-PI/2),run_time=0.5)
        self.wait(0.1)
        self.play(*[relu.animate.move_to(circle.get_center()) for relu, circle in zip(relu_graphs,VGroup(*input_layer,*hidden_layer))],run_time=0.1)
        self.wait(0.1)
        
        
        # self.play(*[hidden_relu.animate.move_to(hidden_circle.get_center()) for hidden_relu, hidden_circle in zip(hidden_relu_graphs,hidden_layer)],run_time=0.1)
        # self.wait(0.1)
        self.play(*[relu.animate.set_opacity(1) for relu in relu_graphs],
                  run_time=0.1)
        self.wait(0.5)
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
            height=code.height/9,
            color=RED
        )
        rectangle.move_to(code.get_top()).shift(DOWN*2.1)  # 将长方形移动到 Code 对象的中心
        # self.play(run_time=0.2)
        self.play(
            FadeIn(rectangle),
            *[circle.animate.set_color(RED) for circle in input_layer],
            run_time=0.5
        )
        self.wait(1)
        self.play(
            rectangle.animate.move_to(code.get_top()).shift(DOWN*3.2),
            *[circle.animate.set_color(YELLOW) for circle in input_layer],
            *[circle.animate.set_color(RED) for circle in hidden_layer],
            run_time=0.5
        )
        self.wait(1)
        self.play(
            rectangle.animate.move_to(code.get_top()).shift(DOWN*4.4),
            *[circle.animate.set_color(YELLOW) for circle in hidden_layer],
            *[circle.animate.set_color(RED) for circle in output_layer],
            run_time=0.5
        )
        self.wait(1)
        self.play(
            *[circle.animate.set_color(YELLOW) for circle in output_layer],
            FadeOut(rectangle),
            run_time=0.5
        )
        self.wait(1)



