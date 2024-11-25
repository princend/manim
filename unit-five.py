from manim import *

class ParametricCurveExample(Scene):
    def construct(self):
        curve = ParametricFunction(
            lambda t: np.array([np.sin(t), np.cos(t), 0]),
            t_range=np.array([0, TAU/2]),
            color=BLUE,
            stroke_width=10
        )
        self.add(curve)
        self.wait(1)

class PolarPlotExample(Scene):
    def construct(self):
        plane = PolarPlane().add_coordinates()
        curve = ParametricFunction(
            lambda t: np.array([
                (2 + np.cos(3 * t)) * np.cos(t),
                (2 + np.cos(3 * t)) * np.sin(t),
                0
            ]),
            t_range=[0, TAU],
            color=RED
        )
        self.add(plane, curve)
        self.wait(1)