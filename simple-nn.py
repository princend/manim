from manim import *


class NN(Scene):
    def construct(self):
        sunbaby = ImageMobject("assets/sunbaby.png").scale(0.5)
        sunbaby.to_edge(DOWN+RIGHT)
        self.add(sunbaby)
        neuron_image = ImageMobject("assets/neuron.jpg")
        neuron_image.scale(2)
        neuron_text = Text("神經元 Neuron", font_size=60)
        neuron_text.next_to(neuron_image, UP)
        self.play(Write(neuron_text))
        self.play(FadeIn(neuron_image))
        self.wait(1)
        self.play(FadeOut(neuron_text),neuron_image.animate.scale(0.2))


        created_neuron_circle = Circle(radius=0.3,color=YELLOW,fill_color=BLACK,fill_opacity=0)
        self.play(Create(created_neuron_circle.set_opacity(0.5)),neuron_image.animate.set_opacity(0),run_time=1)
        self.remove(neuron_image)
        self.play(created_neuron_circle.animate.set_opacity(1),run_time=0.5)

        # 創建神經元
        input_layer = VGroup(*[Circle(radius=0.3,color=YELLOW) for _ in range(3)])
        # self.play(Create(input_layer[0].set_opacity(1)))
        
        hidden_layer = VGroup(*[Circle(radius=0.3,color=YELLOW) for _ in range(4)])
        output_layer = Circle(radius=0.3,color=YELLOW)

        # 排列神經元位置
        input_layer.arrange(DOWN, buff=0.5)
        hidden_layer.arrange(DOWN, buff=0.5)
        
        # 設置層的位置
        input_layer.move_to(LEFT * 4)
        hidden_layer.move_to(LEFT * 0)
        output_layer.move_to(RIGHT * 4)
        self.play(created_neuron_circle.animate.move_to(input_layer[0].get_center()))
        # 創建連接線
        connections1 = VGroup(*[
            Line(input_neuron.get_center(), hidden_neuron.get_center())
            for input_neuron in input_layer
            for hidden_neuron in hidden_layer
        ])

        connections2 = VGroup(*[
            Line(hidden_neuron.get_center(), output_layer.get_center())
            for hidden_neuron in hidden_layer
        ])

        # 添加到場景
        
        self.play(Create(input_layer))
        self.play(Create(hidden_layer))
        self.play(Create(output_layer))
        self.play(Create(connections1),Create(connections2))
        self.wait(0.5)
        input_text = Text("輸入層", font_size=36)
        hidden_text = Text("隱藏層", font_size=36)
        output_text = Text("輸出層", font_size=36)
        input_text.next_to(input_layer, UP)
        hidden_text.next_to(hidden_layer, UP)
        output_text.next_to(output_layer, UP)
        self.play(Write(input_text))
        self.play(Write(hidden_text))
        self.play(Write(output_text))
        self.wait(1)
        self.remove(sunbaby)

