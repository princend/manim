from manim import *

class SimpleNeuralNetwork(Scene):
    def construct(self):

        # image = ImageMobject("image.png")
        # 創建神經元
        input_neurons = [Circle(radius=0.25) for _ in range(3)]
        hidden_neurons = [Circle(radius=0.25,color=BLUE) for _ in range(4)]
        output_neurons = [Circle(radius=0.25,color=YELLOW) for _ in range(2)]

        # 設置神經元位置
        for i, neuron in enumerate(input_neurons):
            neuron.move_to(LEFT * 3 + UP * (i - 1))
        
        for i, neuron in enumerate(hidden_neurons):
            neuron.move_to(UP * (i - 1.5))
        
        for i, neuron in enumerate(output_neurons):
            neuron.move_to(RIGHT * 3 + UP * (i - 0.5))

        # 創建連接線
        input_to_hidden_lines = [
            Line(input_neuron.get_center(), hidden_neuron.get_center())
            for input_neuron in input_neurons
            for hidden_neuron in hidden_neurons
        ]

        hidden_to_output_lines = [
            Line(hidden_neuron.get_center(), output_neuron.get_center())
            for hidden_neuron in hidden_neurons
            for output_neuron in output_neurons
        ]

        # 添加到場景中
        self.play(
            *[Create(neuron) for neuron in input_neurons  ],
            *[Create(line) for line in input_to_hidden_lines ],
            # *[Create(neuron) for neuron in  hidden_neurons ],
            # *[Create(line) for line in  hidden_to_output_lines],
            # *[Create(neuron) for neuron in   output_neurons],
        )

        self.play(
            # *[Create(neuron) for neuron in input_neurons  ],
            # *[Create(line) for line in input_to_hidden_lines ],
            *[Create(neuron) for neuron in  hidden_neurons ],
            *[Create(line) for line in  hidden_to_output_lines],
            # *[Create(neuron) for neuron in   output_neurons],
        )

        self.play(
            # *[Create(neuron) for neuron in input_neurons  ],
            # *[Create(line) for line in input_to_hidden_lines ],
            # *[Create(neuron) for neuron in  hidden_neurons ],
            # *[Create(line) for line in  hidden_to_output_lines],
            *[Create(neuron) for neuron in   output_neurons],
        )

        # 添加標籤
        input_label = Text("Input Layer",font_size=16).next_to(input_neurons[0], DOWN)
        hidden_label = Text("Hidden Layer",font_size=16).next_to(hidden_neurons[0], DOWN)
        output_label = Text("Output Layer",font_size=16).next_to(output_neurons[0], DOWN)

        self.play(Write(input_label), Write(hidden_label), Write(output_label))

        # 暫停以便觀察
        self.wait(2)
