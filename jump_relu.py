from manim import *

class JumpReLU(Scene):
    def construct(self):
        # 創建座標軸
        axes = Axes(
            x_range=[-2, 3, 1],
            y_range=[-1, 3, 1],
            axis_config={"include_numbers": True},
            tips=False
        )
        
        # 添加座標標籤
        labels = axes.get_axis_labels(x_label="z", y_label="J(z)")
        
        # 定義 JumpReLU 函數
        kappa = 1  # 閥值點
        left_segment = axes.plot(
            lambda z: 0,
            x_range=[-2, kappa],
            color=ORANGE,
            use_smoothing=False
        )
        right_segment = axes.plot(
            lambda z: z,
            x_range=[kappa, 3],
            color=ORANGE,
            use_smoothing=False
        )
        
        # 添加閥值點
        open_dot = Circle(radius=0.1, color=WHITE).move_to(axes.c2p(kappa, 0)).set_stroke(width=2)  # 空心點
        filled_dot = Dot(axes.c2p(kappa, kappa), color=WHITE).scale(1.5)  # 實心點
        
        formula = MathTex(
            r"J(z) := zH(z-k) \\ = \begin{cases} 0, & if z \leq k \\ z , & z > k \end{cases}"
        ).scale(0.8)
        formula.to_corner(UL)  # 放置在左上角
        
        # 動畫繪製
        self.play(Create(axes), Write(labels))
        self.play(Write(formula))
        self.play(Create(left_segment))
        self.play(Create(right_segment))
        self.play(Create(open_dot), Create(filled_dot))
        
        # 保持畫面
        self.wait()
