from manim import *

class ManimConstantsDemo(Scene):
    def construct(self):
        # 定義常用的定位常數和位置
        positions = {
            # "IN": IN,
            # "OUT": OUT,
            "ORIGIN": ORIGIN,
            "UP": UP,
            "DOWN": DOWN,
            "RIGHT": RIGHT,
            "LEFT": LEFT,
            "UL": UL,
            "UR": UR,
            "DL": DL,
            "DR": DR,
        }

        # 用於存放所有對象的群組
        elements = VGroup()

        # 對每個位置進行標註
        for label, position in positions.items():
            dot = Dot(position, color=YELLOW,radius=0.05)  # 在對應位置添加一個藍色點
            text = Text(label).scale(0.25).next_to(dot, RIGHT)  # 在點旁標註文字
            elements.add(dot, text)

        # 在場景中創建所有標註
        self.play(LaggedStart(*[Create(element) for element in elements]))
        self.wait(2)

        # 添加坐標原點的說明
        # origin_label = Text("ORIGIN (0, 0)", color=YELLOW).scale(0.7).next_to(ORIGIN, DOWN)
        # self.play(Write(origin_label))
        self.wait(2)
