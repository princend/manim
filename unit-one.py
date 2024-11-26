from manim import *

class HelloWorld(Scene):
    def construct(self):
        text = Text("Hello, Manim!")
        self.play(Write(text))

