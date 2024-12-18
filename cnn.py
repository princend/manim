from manim import *
import random

class NN(Scene):
    def construct(self):
        # 創建神經元
        input_image = ImageMobject("assets/mouse.png").scale(3).shift(LEFT * 4.5)
        conv1_layer = Group(ImageMobject("assets/feature1.png").scale(3),
                             ImageMobject("assets/feature2.png").scale(3),
                             ImageMobject("assets/feature3.png").scale(3),
                             ImageMobject("assets/feature4.png").scale(3),
                             ImageMobject("assets/feature5.png").scale(3))
        conv4_layer = Group(ImageMobject("assets/feature2_1.png").scale(3),
                             ImageMobject("assets/feature2_2.png").scale(3),
                             ImageMobject("assets/feature2_3.png").scale(3))
        hidden_layer = VGroup(*[Circle(radius=0.3, color=GRAY_A) for _ in range(6)])
        output_layer = Text("老鼠", font_size=36, color=WHITE)

        # 排列神經元位置
        conv1_layer.arrange(DOWN, buff=0.5)
        conv4_layer.arrange(DOWN, buff=0.5)
        hidden_layer.arrange(DOWN, buff=0.5)

        # 設置層的位置
        conv1_layer.move_to(LEFT * 2)
        conv4_layer.move_to(ORIGIN)
        hidden_layer.move_to(RIGHT * 2)
        output_layer.move_to(RIGHT * 5)

        # 創建連接線
        connections_input = VGroup(
            *[
                Line(input_image.get_right(), conv1_neuron.get_left())
                for conv1_neuron in conv1_layer
            ]
        )
        
        random_connections = VGroup(
            *[
                Line(conv1_neuron.get_right(), conv4_neuron.get_left())
                for conv1_neuron in random.sample(list(conv1_layer), len(conv1_layer))
                for conv4_neuron in random.sample(list(conv4_layer), k=2)
            ]
        )

        
        connections1 = VGroup(
            *[
                Line(conv4_neuron.get_right(), hidden_neuron.get_center())
                for conv4_neuron in conv4_layer
                for hidden_neuron in hidden_layer
            ]
        )

        connections2 = VGroup(
            *[
                Line(hidden_neuron.get_center(), output_layer.get_left())
                for hidden_neuron in hidden_layer
            ]
        )

        # 添加到場景
        self.play(FadeIn(input_image),run_time=0.5)
        self.play(FadeIn(conv1_layer),run_time=0.5)
        self.play(FadeIn(conv4_layer),run_time=0.5)
        self.play(Create(hidden_layer),run_time=0.5)
        self.play(Create(output_layer.set_opacity(0)),run_time=0.5)
        self.play(Create(connections_input),Create(random_connections),Create(connections1), Create(connections2),run_time=1)
        
        self.play(output_layer.animate.set_opacity(1),run_time=1)
        self.wait(1)
        input_text1 = Text("Conv 1-3", font_size=30)
        input_text = Text("Conv 4-6", font_size=30)
        hidden_text = Text("Flatten and FC", font_size=30)
        input_text1.next_to(conv1_layer, UP)
        input_text.next_to(conv4_layer, UP)
        hidden_text.next_to(hidden_layer, UP)
        self.play(Write(input_text1),run_time=1)
        self.play(Write(input_text),run_time=1)
        self.play(Write(hidden_text),run_time=1)
        self.wait(1)
