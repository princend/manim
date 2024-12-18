from manim import *

class BatchNormalizationDiagram(Scene):
    def construct(self):
        # 標題
        title = Text("Batch Normalization", font_size=48).to_edge(UP)
        self.play(Write(title))

        # 輸入 x^1, x^2, x^3
        input_x = VGroup(
            self.create_input_block("x^1"),
            self.create_input_block("x^2"),
            self.create_input_block("x^3")
        ).arrange(DOWN, buff=1).shift(LEFT * 4)

        self.play(FadeIn(input_x))

        # 權重 W^1
        weights = VGroup(
            self.create_weight_block("W^1"),
            self.create_weight_block("W^1"),
            self.create_weight_block("W^1")
        ).arrange(DOWN, buff=1).next_to(input_x, RIGHT, buff=0.5)

        self.play(FadeIn(weights))

        # 產生 z^1, z^2, z^3
        z_values = VGroup(
            self.create_output_block("z^1"),
            self.create_output_block("z^2"),
            self.create_output_block("z^3")
        ).arrange(DOWN, buff=1).next_to(weights, RIGHT, buff=0.5)

        z_values_box = SurroundingRectangle(z_values, color=RED, buff=0.2)
         
        self.play(FadeIn(z_values))
     

  


        # 箭頭連接
        self.connect_blocks(input_x, weights)
        self.connect_blocks(weights, z_values)
        
        self.play(FadeIn(z_values_box))
        # μ 和 σ 計算
        mu_sigma_box = self.create_mu_sigma_block().next_to(z_values_box, DOWN*1.5).shift(RIGHT*0.65)
        self.play(FadeIn(mu_sigma_box))
        
        self.connect_mu_sigma(z_values_box, mu_sigma_box)
        # self.connect_blocks(mu_sigma_box, z_tilde_values)
        
        # z 標準化後輸出
        z_tilde_values = VGroup(
            self.create_output_block("\\tilde{z}^1"),
            self.create_output_block("\\tilde{z}^2"),
            self.create_output_block("\\tilde{z}^3")
        ).arrange(DOWN, buff=1).shift(RIGHT * 4)

        formula = MathTex(r"\tilde{z}^i = \frac{z^i - \mu}{\sigma}").scale(0.8).to_corner(UR).shift(DOWN*0.5+LEFT*0.5)
        self.play(Write(formula))
        self.wait(1)
        arrow_z_to_z_tilde = Arrow(z_values[0].get_right(), z_tilde_values[0].get_left(), buff=0.1)
        arrow_mu_to_z_tilde = Arrow(mu_sigma_box.get_top(), z_tilde_values[0].get_left(), buff=0.1)
        self.play(GrowArrow(arrow_z_to_z_tilde,stroke_width =0.5),GrowArrow(arrow_mu_to_z_tilde ,stroke_width =0.5))
        self.wait(0.5) 
        self.play(FadeIn(z_tilde_values[0]))   
        arrow_z_to_z_tilde = Arrow(z_values[1].get_right(), z_tilde_values[1].get_left(), buff=0.1)
        arrow_mu_to_z_tilde = Arrow(mu_sigma_box.get_top(), z_tilde_values[1].get_left(), buff=0.1)
        self.play(GrowArrow(arrow_z_to_z_tilde,stroke_width =0.5),GrowArrow(arrow_mu_to_z_tilde ,stroke_width =0.5))
        self.wait(0.5)    
        self.play(FadeIn(z_tilde_values[1]))   
        arrow_z_to_z_tilde = Arrow(z_values[2].get_right(), z_tilde_values[2].get_left(), buff=0.1)
        arrow_mu_to_z_tilde = Arrow(mu_sigma_box.get_top(), z_tilde_values[2].get_left(), buff=0.1)
        self.play(GrowArrow(arrow_z_to_z_tilde,stroke_width =0.5),GrowArrow(arrow_mu_to_z_tilde ,stroke_width =0.5))
        self.play(FadeIn(z_tilde_values[2]))   
        self.wait(2)    
        
    def create_input_block(self, label):
        return VGroup(
            Rectangle(width=0.8, height=0.5, color=BLACK, fill_opacity=1),
            MathTex(label, color=WHITE).scale(0.8)
        ).arrange().set_z_index(1)

    def create_weight_block(self, label):
        return VGroup(
            Rectangle(width=1, height=0.5, color=BLUE, fill_opacity=0.5),
            MathTex(label).scale(0.8)
        )

    def create_output_block(self, label):
        return VGroup(
            Rectangle(width=0.8, height=0.5, color=BLUE, fill_opacity=0.7),
            MathTex(label).scale(0.8)
        )

    def create_mu_sigma_block(self):
        mu_box = VGroup(
            Rectangle(width=0.8, height=0.5, color=YELLOW, fill_opacity=0.7),
            MathTex("\\mu").scale(0.8)
        )
        
        sigma_box = VGroup(
            Rectangle(width=0.8, height=0.5, color=GREEN, fill_opacity=0.7),
            MathTex("\\sigma").scale(0.8)
        )
        return VGroup(mu_box, sigma_box).arrange(RIGHT, buff=0.5)

    def connect_blocks(self, start_blocks, end_blocks):
        group=VGroup()
        for start, end in zip(start_blocks, end_blocks):
            arrow = Arrow(start.get_right(), end.get_left(), buff=0.1)
            group.add(arrow)
        self.play(*[GrowArrow(arrow) for arrow in group])

    def connect_mu_sigma(self, z_values_box, mu_sigma_block):
        arrow_mu=Arrow(z_values_box.get_bottom(), mu_sigma_block[0].get_top())    
        arrow_sigma = Arrow(mu_sigma_block[0].get_right(), mu_sigma_block[1].get_left(),buff=1.2)
        self.play(GrowArrow(arrow_mu))
        self.wait(0.5)
        self.play(GrowArrow(arrow_sigma))
