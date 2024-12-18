from manim import *


class AutoencoderAnimation(Scene):
    def construct(self):
        # 輸入 (Input)
        input_rect = Rectangle(
            height=2, width=1, fill_color=GREEN, fill_opacity=0.7
        ).to_edge(LEFT)
        input_text = Text("Input (x)", font_size=25).next_to(input_rect, UP*3)
        # input_data = MathTex("4").next_to(input_rect, RIGHT)  # 假設輸入是數字 4

        # 編碼器 (Encoder)
        encoder_rect = Polygon(
            [-4, 2, 0], [-2, 1, 0], [-2, -1, 0], [-4, -2, 0],color=GREEN
        ).next_to(input_rect, RIGHT).shift(RIGHT*1.4)
        encoder_text = Text("Encoder (gφ)", font_size=25).next_to(encoder_rect, UP * 3)
        encoder_arrow = Arrow(input_rect.get_right(), encoder_rect.get_left(), buff=1.5)

        # 瓶頸 (Bottleneck / Latent Space)
        bottleneck_rect = Square(
            side_length=0.5, fill_color=RED, fill_opacity=0.7
        ).next_to(encoder_rect, RIGHT).shift(RIGHT*1.4)
        bottleneck_text = Text("Bottleneck (z)", font_size=25).next_to(
            bottleneck_rect, UP * 3
        )
        bottleneck_arrow = Arrow(encoder_rect.get_right(), bottleneck_rect.get_left(), buff=1.5)

        # 解碼器 (Decoder)
        decoder_rect = Polygon([2, 1, 0], [4, 2, 0], [4, -2, 0], [2, -1, 0]).next_to(
            bottleneck_rect, RIGHT
        ).shift(RIGHT*1.4)
        decoder_text = Text("Decoder (fθ)", font_size=25).next_to(
            decoder_rect, UP * 3
        )
        decoder_arrow = Arrow(bottleneck_rect.get_right(), decoder_rect.get_left(), buff=1.5)

        # 重建的輸出 (Reconstructed Output)
        output_rect = Rectangle(
            height=2, width=1, fill_color=BLUE, fill_opacity=0.7
        ).next_to(decoder_rect, RIGHT).shift(RIGHT*1.4)
        output_text = Text("Reconstructed\nInput (x')", font_size=25).next_to(
            output_rect, UP * 3
        )
        output_arrow = Arrow(decoder_rect.get_right(), output_rect.get_left(), buff=1.5)
        # output_data = MathTex("4").next_to(output_rect, RIGHT)  # 理論上應與輸入相同

        # 動畫
        self.play(Write(input_text), Create(input_rect))
        self.wait(0.5)
        self.play(Write(encoder_text), Create(encoder_arrow), Create(encoder_rect))
        self.wait(0.5)
        self.play(
            Write(bottleneck_text), Create(bottleneck_arrow), Create(bottleneck_rect)
        )
        self.wait(0.5)
        self.play(Write(decoder_text), Create(decoder_arrow), Create(decoder_rect))
        self.wait(0.5)
        self.play(
            Write(output_text),
            Create(output_arrow),
            Create(output_rect)
            # Write(output_data),
        )
        self.wait(1)

        # 額外說明 (Optional)
        bottleneck_explanation = Text(
            "Compressed\nRepresentation", font_size=20
        ).next_to(bottleneck_rect, DOWN * 2)
        self.play(Write(bottleneck_explanation))
        self.wait(2)

        self.play(*[FadeOut(mob) for mob in self.mobjects])
