from manim import *

class MomentumExplanation(Scene):
    def construct(self):
        # Create the cost function curve (representing the optimization landscape)
        cost_curve = FunctionGraph(lambda x: np.sin(x) * np.exp(-0.1 * x ** 2), x_range=[-3, 3])
        cost_curve.set_color(WHITE)
        self.play(Create(cost_curve))
        
        # Add labels for gradient descent and momentum
        grad_label = Tex("Negative of $\\frac{\\partial L}{\\partial w}$").shift(UP * 2.5)
        momentum_label = Tex("Momentum").shift(UP * 1.5)
        real_movement_label = Tex("Real Movement").shift(DOWN * 2.5)
        
        self.play(Write(grad_label), Write(momentum_label), Write(real_movement_label))
        
        # Show the movement without momentum (red arrows)
        grad_arrow1 = Arrow(start=LEFT * 2 + UP, end=LEFT * 2 + DOWN, color=RED)
        grad_arrow2 = Arrow(start=LEFT, end=LEFT + DOWN, color=RED)
        grad_arrow3 = Arrow(start=RIGHT, end=RIGHT + DOWN, color=RED)
        self.play(Create(grad_arrow1), Create(grad_arrow2), Create(grad_arrow3))
        
        # Show momentum (green dashed arrows)
        momentum_arrow1 = Arrow(start=LEFT * 2 + UP, end=LEFT * 2 + UP * 0.5, color=GREEN)
        momentum_arrow2 = Arrow(start=LEFT, end=LEFT + UP * 0.5, color=GREEN)
        momentum_arrow3 = Arrow(start=RIGHT, end=RIGHT + UP * 0.5, color=GREEN)
        self.play(Create(momentum_arrow1), Create(momentum_arrow2), Create(momentum_arrow3))
        
        # Show real movement (blue arrows)
        real_movement_arrow1 = Arrow(start=LEFT * 2 + UP, end=LEFT + UP * 0.5, color=BLUE)
        real_movement_arrow2 = Arrow(start=LEFT, end=LEFT + UP, color=BLUE)
        real_movement_arrow3 = Arrow(start=RIGHT, end=RIGHT + UP * 0.5, color=BLUE)
        self.play(Create(real_movement_arrow1), Create(real_movement_arrow2), Create(real_movement_arrow3))

        self.wait(2)

