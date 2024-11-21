from manim import *
class NL(Scene):

    def construct(self):

        sunbaby = ImageMobject("assets/sunbaby.png").scale(0.5)
        sunbaby.to_edge(DOWN+RIGHT)
        self.add(sunbaby)

        image = ImageMobject("assets/nl7788.webp")
        image.move_to(LEFT*2)
        self.add(image)
        dog = ImageMobject("assets/nldog.webp")
        dog.move_to(RIGHT*1.5,UP*5)
        self.add(dog)
        
        bat= ImageMobject("assets/bat.png").scale(1)
        
        bonk = ImageMobject("assets/bonk.png").scale(0.2)
        bonk.move_to(dog.get_center()+UP*0.5 )  # 设置初始位置
        
         

        bubble = RoundedRectangle(
            corner_radius=0.5,  # 圓角半徑
            height=2,           # 高度
            width=3,            # 寬度
            stroke_color=WHITE, # 邊框顏色
            stroke_width=2,     # 邊框寬度
            fill_color=WHITE,   # 填充顏色
            fill_opacity=1      # 填充不透明度（1表示完全不透明）
        )

        triangle = Triangle(fill_color=WHITE, fill_opacity=1, stroke_color=WHITE)
        triangle.scale(0.2)     # 調整尾巴大小
        triangle.rotate(PI)  # 旋轉尾巴方向
        triangle.next_to(bubble, DOWN, buff=0) # 將尾巴放在對話框下方

        chat_bubble = VGroup(bubble, triangle)
        text = Text("22222222 !", font="Microsoft YaHei", color=BLACK).scale(0.6)
        text.move_to(bubble.get_center())
        
        # 將整個對話框組（包含文字）放在狗的上方
        chat_group = VGroup(chat_bubble, text)
        chat_group.next_to(dog, UP, buff=0.5)  # buff=0.5 控制與狗的距離
        
        self.add(chat_bubble)
        # self.play()

        self.play(Write(text),
            Rotate(dog, angle=PI/12, rate_func=lambda t: np.sin(8 * 2 * PI * t)),
            run_time=3
        )

        bat.next_to(dog, UP + LEFT, buff=0.1).shift(RIGHT * 2+DOWN * 2)

        self.play(
          chat_group.animate.set_opacity(0),
          run_time=0.1
        )
        self.wait(0.2)
        self.play(
            bat.animate.rotate(-PI/4),
            run_time=0.25
        )
        self.play(
            FadeIn(bonk),
            run_time=0.3
        )

        self.play(
            bonk.animate.set_opacity(0),
            bat.animate.set_opacity(0),
            run_time=0.1
        )

        def update_rotation(mob, alpha):
            mob.rotate(alpha * PI * 6)  # 这里的4代表旋转的圈数


        self.play(
            dog.animate.shift(UP*5 + RIGHT*7),
            UpdateFromAlphaFunc(dog, update_rotation),
            run_time=1
        )

        
      
