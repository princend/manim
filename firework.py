from manim import *
import numpy as np
import random


class Fireworks(Scene):
    def create_firework(self, position, num_particles=50, colors=[RED, ORANGE, YELLOW]):
        particles = VGroup()
        animations = []
        for _ in range(num_particles):
            direction = random.uniform(0, 2 * PI)
            distance = random.uniform(1, 3)
            end_position = position + distance * np.array(
                [np.cos(direction), np.sin(direction), 0]
            )
            particle = Dot(point=position, color=random.choice(colors))
            particle.set_width(random.uniform(0.05, 0.2))  # 设置随机宽度
            particles.add(particle)
            # 创建动画并添加到动画列表中
            animations.append(particle.animate.move_to(end_position).set_opacity(0))
        return particles, animations

    def animate_firework(self, particles, animations, duration=1):
        return AnimationGroup(*animations, run_time=duration)

    def construct(self):
        # 背景顏色
        # self.camera.background_color = DARK_BLUE
        firework5, animations5 = self.create_firework(
            2 * LEFT + 1 * UP,
            num_particles=100,
            colors=[RED, ORANGE, YELLOW, BLUE, GREEN, PURPLE],
        )
        firework6, animations6 = self.create_firework(
            2 * RIGHT + 2 * DOWN,
            num_particles=100,
            colors=[RED, ORANGE, YELLOW, BLUE, GREEN, PURPLE],
        )
        firework7, animations7 = self.create_firework(
            3 * LEFT + 3 * DOWN,
            num_particles=100,
            colors=[RED, ORANGE, YELLOW, BLUE, GREEN, PURPLE],
        )
        firework8, animations8 = self.create_firework(
            4 * RIGHT + 2 * UP,
            num_particles=100,
            colors=[RED, ORANGE, YELLOW, BLUE, GREEN, PURPLE],
        )

        # 動畫1: 創建煙火
        firework1, animations1 = self.create_firework(ORIGIN)
        self.add(firework1)
        self.play(self.animate_firework(firework1, animations1))

        # 等待片刻
        self.wait(0.5)

        # 動畫2: 另一個煙火
        firework2, animations2 = self.create_firework(
            2 * RIGHT + UP, colors=[BLUE, GREEN, PURPLE]
        )
        self.add(firework2)
        self.play(self.animate_firework(firework2, animations2))

        self.wait(0.5)

        # 動畫3和動畫4: 同時創建兩個煙火
        firework3, animations3 = self.create_firework(
            2 * LEFT + 1 * UP, colors=[RED, ORANGE, YELLOW, BLUE, GREEN, PURPLE]
        )
        firework4, animations4 = self.create_firework(
            2 * RIGHT + 2 * DOWN, colors=[RED, ORANGE, YELLOW, BLUE, GREEN, PURPLE]
        )

        self.add(firework3, firework4)
        self.play(
            self.animate_firework(firework3, animations3),
            self.animate_firework(firework4, animations4),
        )
        self.wait(0.5)
        # self.add(firework3, firework4)
        # self.play(
        #     self.animate_firework(firework3, animations3),
        #     self.animate_firework(firework4, animations4)
        # )

        # self.wait(0.1)
        self.add(firework5, firework6, firework7, firework8)
        # self.add(firework5, firework6, firework7, firework8)
        # self.wait(0.1)
        self.play(
            self.animate_firework(firework5, animations5),
            self.animate_firework(firework6, animations6),
            self.animate_firework(firework7, animations7),
            self.animate_firework(firework8, animations8)
        )

        self.wait(0.1)

        # 添加 "2025 Happy New Year" 文字
        year_text = Text("2025", font_size=48, color=WHITE)
        year_text.shift(UP * 0.5)
        new_year_text = Text("Happy New Year", font_size=48, color=WHITE)
        new_year_text.next_to(year_text, DOWN)
        self.play(FadeIn(year_text), FadeIn(new_year_text))
        self.wait(2)
