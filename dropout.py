from manim import *

class DropoutIllustration(Scene):
    def construct(self):
        # Title
        title = MathTex("\\text{Dropout: Preventing Overfitting}", font_size=40).to_edge(UP)
        dropout_label = MathTex("\\text{Randomly deactivate neurons}", font_size=28).next_to(title, DOWN)
        self.play(Write(title),run_time=0.5)
        self.play(Write(dropout_label),run_time=0.5)
        self.wait(1)

        # Neural Network Layers
        input_layer = VGroup(*[Circle(color=BLUE).shift(UP * i) for i in range(3)]).arrange(DOWN, buff=0.7).scale(0.5).shift(LEFT * 3)
        hidden_layer = VGroup(*[Circle(color=GREEN).shift(UP * i) for i in range(5)]).arrange(DOWN, buff=0.7).scale(0.5)
        output_layer = VGroup(*[Circle(color=RED).shift(UP * i) for i in range(2)]).arrange(DOWN, buff=1).scale(0.5).shift(RIGHT * 3)

        # Connections
        connections_input_hidden = VGroup(
            *[Line(start=i.get_center(), end=j.get_center(), color=GRAY) 
              for i in input_layer for j in hidden_layer]
        )
        connections_hidden_output = VGroup(
            *[Line(start=i.get_center(), end=j.get_center(), color=GRAY) 
              for i in hidden_layer for j in output_layer]
        )
        
        network = VGroup(input_layer, hidden_layer, output_layer, connections_input_hidden, connections_hidden_output)
        network.scale(0.8)
        # Display Network
        self.play(FadeIn(input_layer), FadeIn(hidden_layer), FadeIn(output_layer))
        self.play(Create(connections_input_hidden), Create(connections_hidden_output))
        self.wait(2)

        # Highlight Dropout in Hidden Layer
        self.play(FadeOut(hidden_layer[1], scale=0.5), FadeOut(hidden_layer[3], scale=0.5), 
                  FadeOut(connections_input_hidden[1::5]), FadeOut(connections_input_hidden[3::5]),
                #   FadeOut(connections_hidden_output[1::5]), FadeOut(connections_hidden_output[3::5]),
                  FadeOut(connections_hidden_output[2]),
                  FadeOut(connections_hidden_output[7]),
                  FadeOut(connections_hidden_output[3]),
                  FadeOut(connections_hidden_output[6]),
                  )

        self.wait(2)
        # Restore Hidden Layer
        # self.play(FadeIn(hidden_layer[1], scale=1.2), FadeIn(hidden_layer[3], scale=1.2), 
        #           FadeIn(connections_input_hidden[1::5]), FadeIn(connections_input_hidden[3::5]),
        #           FadeIn(connections_hidden_output[2]), FadeIn(connections_hidden_output[3]),
        #           FadeIn(connections_hidden_output[6]), FadeIn(connections_hidden_output[7]))

        # self.wait(2)
        # # End Scene
        # self.play(FadeOut(dropout_label),FadeOut(VGroup(title, input_layer, hidden_layer, output_layer, connections_input_hidden, connections_hidden_output)))
        self.play(FadeOut(VGroup(title, dropout_label, input_layer, hidden_layer[0],hidden_layer[2],hidden_layer[4], 
                                 output_layer,
                                 connections_input_hidden[0], connections_input_hidden[2], connections_input_hidden[4], connections_input_hidden[5], connections_input_hidden[7], connections_input_hidden[9],connections_input_hidden[10],connections_input_hidden[12],connections_input_hidden[14],
                                 connections_hidden_output[0], connections_hidden_output[1], connections_hidden_output[4], connections_hidden_output[5], connections_hidden_output[8], connections_hidden_output[9])))
        
