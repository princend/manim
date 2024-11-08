from manim import *

class MarkovChainOptimized(Scene):
    def construct(self):
        # 定義狀態和其位置
        states = {
            "單身": LEFT * 4,
            "交往": RIGHT * 4,
            "結婚": DOWN * 3,
        }
        
        circles = {name: Circle(radius=1, color=color).move_to(pos)
                   for (name, pos), color in zip(states.items(), [BLUE, RED, YELLOW])}
        labels = {name: Text(name).move_to(circle.get_center())
                  for name, circle in circles.items()}

        self.play(*[Create(circle) for circle in circles.values()])
        self.play(*[Write(label) for label in labels.values()])

        # 添加箭頭和標籤
        arrows_and_probs = [
            ("單身", "交往", 0.8, 0.5*UP, 2.5),  
            ("交往", "單身", 0.2, 0.5*DOWN, 2.5),
            ("單身", "單身", 0.2, UP * 1.8, 2.0),  # 自回
            ("交往", "交往", 0.6, UP * 1.8, 2.0),  # 自回
            ("交往", "結婚", 0.2, 0.5*RIGHT, 2.5),
            ("結婚", "結婚", 0.9, DOWN * 1.8, 2.0),  # 自回
            ("結婚", "單身", 0.1, 0.5*LEFT, 2.5),
        ]

        arrows = []
        probs = []
        for start, end, prob, offset, custom_radius in arrows_and_probs:
            start_pos = circles[start].get_center()
            end_pos = circles[end].get_center()
            
            # 計算從圓周開始和結束的位置
            direction = end_pos - start_pos
            angle = np.arctan2(direction[1], direction[0])
            
            start_point = circles[start].point_at_angle(angle)
            end_point = circles[end].point_at_angle(angle + PI)

            if start == end:
                # 自回圈的箭頭，避免太靠近，並將箭頭放在圓外
                loop_start_angle = 3 * PI / 4
                loop_end_angle = PI / 4
                loop_start = circles[start].point_at_angle(loop_start_angle)
                loop_end = circles[end].point_at_angle(loop_end_angle)
                
                # 調整半徑，使箭頭位於圓外
                arrow = ArcBetweenPoints(
                    loop_start, loop_end, radius=-4.5  # 調整自回圈的半徑
                ).add_tip(tip_length=0.2)
            else:
                # 普通箭頭，避免箭頭重疊
                radius = max(custom_radius, np.linalg.norm(end_point - start_point) / 2 + 0.5)
                arrow = CurvedArrow(
                    start_point, end_point, radius=radius
                )

            prob_label = Text(str(prob), font_size=24).next_to(
                (start_pos + end_pos) / 2, offset
            )
            arrows.append(arrow)
            probs.append(prob_label)

        self.play(*[Create(arrow) for arrow in arrows])
        self.play(*[Write(prob) for prob in probs])

        # 顯示轉移矩陣
        matrix = MathTable(
            [["0.2", "0.8", "0.0"],
             ["0.2", "0.6", "0.2"],
             ["0.1", "0.0", "0.9"]],
            row_labels=[Text("單身"), Text("交往"), Text("結婚")],
            col_labels=[Text("單身"), Text("交往"), Text("結婚")],
            top_left_entry=Text("轉移矩陣", font_size=24),
        ).shift(RIGHT*5)  # 矩陣移到右側

        self.play(Create(matrix))
        self.wait(3)
