from manim import *

class CrossEntropyLoss(Scene):
    def construct(self):
        # Title
        title = MathTex("\\text{Cross-Entropy Loss}", font_size=48).to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Equation for cross-entropy loss
        eq = MathTex(
            "L = -\\sum_{i=1}^N y_i \\log(\\hat{y}_i)",
            font_size=48
        ).to_edge(UP, buff=1.5)
        self.play(Write(eq))
        self.wait(2)

        # Explain components of the equation
        explanation = VGroup(
            MathTex("1.\\ y_i: \\text{True label (one-hot encoded)}", font_size=28),
            MathTex("2.\\ \\hat{y}_i: \\text{Predicted probability}", font_size=28),
            MathTex("3.\\ \\log(\\hat{y}_i): \\text{Logarithm of predicted probability}", font_size=28),
            MathTex("4.\\ \\sum: \\text{Summation over all classes}", font_size=28),
            MathTex("5.\\ -L: \\text{Negative to minimize loss}", font_size=28)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).to_edge(LEFT, buff=0.5).shift(DOWN)

        self.play(FadeIn(explanation, shift=RIGHT))
        self.wait(2)

        # Example of true labels and predicted probabilities
        true_label = MathTex("y = [1, 0, 0]", font_size=32).shift(UP*0.5)
        pred_probs = MathTex("\\hat{y} = [0.7, 0.2, 0.1]", font_size=32).next_to(true_label, DOWN, buff=0.5)
        
                # Highlight the correct class calculation
        focus_text = MathTex(
            "L = -(1 \\cdot \\log(0.7) + 0 \\cdot \\log(0.2) + 0 \\cdot \\log(0.1))",
            font_size=32
        ).next_to(pred_probs, DOWN, buff=0.5)
        
        result = MathTex("L = -\\log(0.7) = 0.357", font_size=32).next_to(focus_text, DOWN, buff=0.5)
        
        example = VGroup(true_label, pred_probs, focus_text, result)
        
        example.to_edge(RIGHT)
        self.play(Write(true_label), Write(pred_probs))
        self.wait(1)


        self.play(Write(focus_text))
        self.wait(1)

        # Show the final computed loss
        self.play(Write(result))
        self.wait(2)

        # End Scene
        self.play(FadeOut(VGroup(title, eq, explanation, true_label, pred_probs, focus_text, result)))
