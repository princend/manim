from manim import *

# config.frame_width = 1920
# config.frame_height = 1080

class MarkovChainOptimized(Scene):
    def construct(self):
        # 定義狀態和其位置
        rice='飯'
        noodle="麵"
        hamburger="漢堡"
        states = {
            "飯": LEFT * 4+UP*2,
            "麵": RIGHT * 4+UP*2,
            "漢堡": DOWN * 3,
        }
        
        circles = {name: Circle(radius=1, color=color).move_to(pos)
                   for (name, pos), color in zip(states.items(), [BLUE, RED, YELLOW])}
        labels = {name: Text(name).move_to(circle.get_center())
                  for name, circle in circles.items()}

        self.play(*[Create(circle) for circle in circles.values()])
        self.play(*[Write(label) for label in labels.values()])


        # 添加箭頭和標籤
        arrows_and_probs = [
            #(start,end,   prob,offset ,custom_radius,arrow_color)
            (rice, noodle, 0.8, 2.5*DOWN, 2.5,BLUE),  
            (rice, hamburger, 0.2, DOWN * 1.8, 2.0,BLUE),  
            (noodle, rice, 0.3, 3*UP, 2.5,RED),
            (noodle, hamburger, 0.7, 0.5*RIGHT+UP*2.5, 2.5,RED),
            (hamburger, noodle, 0.9, DOWN * 1.8, 2.0,YELLOW), 
            (hamburger, rice, 0.1, 0.75*LEFT+3*UP, 2.5,YELLOW),
        ]

        arrows = []
        probs = []
        for start, end, prob, offset, custom_radius ,arrow_color in arrows_and_probs:
            start_pos = circles[start].get_center()
            end_pos = circles[end].get_center()
            
            # 計算從圓周開始和結束的位置
            direction = end_pos - start_pos
            angle = np.arctan2(direction[1], direction[0])
            
            start_point = circles[start].point_at_angle(angle)
            end_point = circles[end].point_at_angle(angle + PI)

            if start == end:
                # 自回圈的箭頭，避免太靠近，並將箭頭放在圓外
                loop_start_angle = 3 * PI / 3
                loop_end_angle = PI / 4
                loop_start = circles[start].point_at_angle(loop_start_angle)
                loop_end = circles[end].point_at_angle(loop_end_angle)
                
                # 調整半徑，使箭頭位於圓外
                arrow = CurvedArrow(circles[start].get_left(),loop_end,angle=-TAU/4)
                # arrow = ArcBetweenPoints(
                #     loop_start, loop_end, radius=-1  # 調整自回圈的半徑
                # ).add_tip(tip_length=0.2)
            else:
                # 普通箭頭，避免箭頭重疊
                radius = max(custom_radius, np.linalg.norm(end_point - start_point) / 2 + 0.5)
                
                arrow = CurvedArrow(
                    start_point, end_point, radius=radius+1,color=arrow_color
                )
                

           
            prob_label = Text(str(prob), font_size=24).next_to(
                (start_pos + end_pos) / 2, offset
            )
            arrows.append(arrow)
            probs.append(prob_label)
        
        rice_arrows:list[CurvedArrow]=[arrows[0],arrows[1]]
        rice_probs=[ probs[0], probs[1]]
        noodle_arrows=[arrows[2],arrows[3]]
        noodle_probs=[ probs[2], probs[3]]
        hamburger_arrows=[arrows[4],arrows[5]]
        hamburger_probs=[ probs[4], probs[5]]
        
        self.play(*[Create(arrow) for arrow in rice_arrows])
        self.play(*[Write(prob) for prob in rice_probs])
        self.play(*[Create(arrow) for arrow in noodle_arrows])
        self.play(*[Write(prob) for prob in noodle_probs])
        self.play(*[Create(arrow) for arrow in hamburger_arrows])
        self.play(*[Write(prob) for prob in hamburger_probs])
        
        circles_values=  [circle for circle in circles.values()]
        labels_values= [label for label in labels.values()]
        
        all_objects = Group(*circles_values, *labels_values,  *rice_arrows, *rice_probs, *noodle_arrows, *noodle_probs, *hamburger_arrows, *hamburger_probs)

        self.play(all_objects.animate.scale(0.5))  
        self.play(all_objects.animate.shift(LEFT*4))
        self.wait(1)
        
        

        # self.play(*[Write(prob) for prob in probs])
        # self.play(*[Create(arrow) for arrow in arrows])
        # 顯示轉移矩陣
        matrix = MathTable(
            [["0", "0.8", "0.2"],
             ["0.3", "0", "0.7"],
             ["0.1", "0.9", "0"]],
            row_labels=[Text(rice, font_size=20), Text(noodle, font_size=20), Text(hamburger, font_size=20)],
            col_labels=[Text(rice, font_size=20), Text(noodle, font_size=20), Text(hamburger, font_size=20)],
            top_left_entry=Text("轉移矩陣", font_size=20),
        ).shift(RIGHT*2.5)  # 矩陣移到右側

        self.play(Create(matrix),matrix.animate.scale(0.8))
        self.wait(3)