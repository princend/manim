from manim import *

class SoftmaxOutputLayer(Scene):
    def construct(self):
        # Title
        title = Text("Softmax on Output Layer", font_size=48).to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Draw hidden layer neurons
        hidden_neurons = VGroup(
            *[Circle(radius=0.3, color=PURPLE).shift(DOWN * i) for i in range(4)]
        ).arrange(DOWN, buff=1).shift(LEFT * 5)

        hidden_labels = VGroup(
            *[MathTex(f"h_{i+1}", font_size=36).next_to(neuron, LEFT) for i, neuron in enumerate(hidden_neurons)]
        )

        self.play(FadeIn(hidden_neurons), Write(hidden_labels),run_time=0.5)
        self.wait(0.5)

        # Connections between hidden layer and output layer
        output_neurons = VGroup(
            *[Circle(radius=0.3, color=BLUE).shift(DOWN * i) for i in range(3)]
        ).arrange(DOWN, buff=1.5).shift(LEFT * 2)

        hidden_to_output_lines = VGroup(
            *[Line(h.get_center(), o.get_center(), color=GRAY) for h in hidden_neurons for o in output_neurons]
        )

        self.play(FadeIn(output_neurons), Create(hidden_to_output_lines),run_time=0.5)
        self.wait(0.5)

        output_labels = VGroup(
            *[MathTex(f"z_{i+1}", font_size=36).next_to(neuron, LEFT) for i, neuron in enumerate(output_neurons)]
        )

        self.play(Write(output_labels),run_time=0.5)
        self.wait(1)

        # Add exponentiation animation
        exp_neurons = VGroup(
            *[Circle(radius=0.3, color=GREEN).shift(neuron.get_center()) for neuron in output_neurons]
        )

        exp_labels = VGroup(
            *[MathTex(f"e^{{z_{i+1}}}", font_size=36).next_to(neuron, RIGHT) for i, neuron in enumerate(exp_neurons)]
        )

        step1_text = Text("Step 1: Exponentiation", font_size=32).to_edge(RIGHT, buff=1).shift(UP * 2)
        self.play(FadeIn(step1_text))
        self.play(Transform(output_neurons, exp_neurons), Write(exp_labels))
        self.wait(1)

        # Summation
        sum_text = Text("Step 2: Sum of exponentials", font_size=32).next_to(step1_text, DOWN, buff=0.8)
        self.play(FadeIn(sum_text))

        total_sum = MathTex(
            f"S = \sum e^{{z}}",
            font_size=36
        ).next_to(sum_text, DOWN)
        self.play(Write(total_sum))
        self.wait(1)

        # Normalize
        step3_text = Text("Step 3: Normalization", font_size=32).next_to(total_sum, DOWN ,buff=0.6)
        self.play(FadeIn(step3_text))

        norm_neurons = VGroup(
            *[Circle(radius=0.3, color=ORANGE).shift(neuron.get_center()) for neuron in output_neurons]
        )

        norm_labels = VGroup(
            *[MathTex(f"\\frac{{e^{{z_{i+1}}}}}{{S}}", font_size=36).next_to(neuron, RIGHT) for i, neuron in enumerate(norm_neurons)]
        )

        self.play(Transform(exp_neurons, norm_neurons), Transform(exp_labels, norm_labels))
        self.wait(1)

        # Highlight output probabilities
        # probabilities_text = Text("Output: Probabilities", font_size=32).to_edge(DOWN)
        # self.play(FadeIn(probabilities_text))
        # self.wait(3)

        # End Scene
        self.play(FadeOut(VGroup(title, hidden_neurons, hidden_labels, output_neurons, output_labels, hidden_to_output_lines, exp_neurons, exp_labels, total_sum, step1_text, sum_text, step3_text)))
