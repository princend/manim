from manim import *


class NN(Scene):
    def construct(self):
      
        neuron_image = ImageMobject("assets/neuron.webp")
        neuron_image.scale(0.5)
        neuron_image.set_opacity()
        self.add(neuron_image)

        self.wait(2)
        # 創建神經元
        input_layer = VGroup(*[Circle(radius=0.3) for _ in range(3)])
        hidden_layer = VGroup(*[Circle(radius=0.3) for _ in range(4)])
        output_layer = Circle(radius=0.3)

        # 排列神經元位置
        input_layer.arrange(DOWN, buff=0.5)
        hidden_layer.arrange(DOWN, buff=0.5)
        
        # 設置層的位置
        input_layer.move_to(LEFT * 4)
        hidden_layer.move_to(LEFT * 0)
        output_layer.move_to(RIGHT * 4)

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
        # self.add(input_layer, hidden_layer, output_layer)
        # self.add(connections1, connections2)
     