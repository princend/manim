from manim import *

class SaddlePointAndGradient(ThreeDScene):
    def construct(self):
        # 建立 3D 坐標系統
        axes = ThreeDAxes(
            x_range=[-2, 2, 0.5],
            y_range=[-2, 2, 0.5],
            z_range=[-4, 4, 2],
            tips=True,
        )

        # 定義 z = x^2 - y^2 函數
        surface = Surface(
            lambda u, v: axes.c2p(u, v, u**2 - v**2),
            u_range=[-2, 2],
            v_range=[-2, 2],
            fill_opacity=0.7,
            checkerboard_colors=[BLUE_B, BLUE_B],
        ).scale(0.75)


        # 鞍點位置
        saddle_point = Dot3D(point=axes.c2p(0, 0, 0), color=RED, radius=0.08)

        # 梯度下降路徑
        current_point = np.array([-1.5, 0])  # 初始點
        path_points = [axes.c2p(current_point[0], current_point[1], current_point[0]**2 - current_point[1]**2)]


        moving_dot = Dot3D(point=path_points[0], color=RED, radius=0.1)
        self.add(moving_dot)
        grad_text = Text(f"梯度:({current_point[0]:+.2f}, {current_point[1]:+.2f})", font_size=16)
        grad_text.add_updater(lambda m: m.become(Text(f"梯度:({current_point[0]:+.2f}, {current_point[1]:+.2f})", font_size=16).to_corner(UR).shift(np.array([-0.75, 0, 0]))))
        self.add_fixed_in_frame_mobjects(grad_text)
        self.add(grad_text)
        trace = TracedPath(moving_dot.get_center, stroke_color=YELLOW, stroke_width=2)
        self.add(trace)

        # 添加標籤
        saddle_label = Text("Saddle Point").next_to(saddle_point, UP)
        path_label = Text("Gradient Descent").move_to(axes.c2p(-1.5, 0, 2))

        # 將元件添加到場景
        self.set_camera_orientation(phi=75 * DEGREES, theta=45 * DEGREES)
        self.add(surface)
        
        learning_rate = 0.05  # 学习率
        for _ in range(50):  # 迭代次數
            grad = 2 * current_point   # 梯度計算
            next_point = current_point - learning_rate * grad
            path_points.append(axes.c2p(next_point[0], next_point[1], next_point[0]**2 - next_point[1]**2))
            current_point = next_point
            grad_text.become(Text(f"梯度:({current_point[0]:+.2f}, {current_point[1]:+.2f})", font_size=16))
            self.play(moving_dot.animate.move_to(path_points[-1]), run_time=0.1)
        self.wait(0.5)
        # 相機動畫和顯示梯度下降
        self.begin_ambient_camera_rotation(rate=2,about='theta')
        self.wait(PI)
        self.stop_ambient_camera_rotation(about='theta')
        self.wait(1)   
        self.begin_ambient_camera_rotation(rate=-1,about='phi')
        self.wait(1)
        self.stop_ambient_camera_rotation(about='phi')
        self.wait(1)
        self.begin_ambient_camera_rotation(rate=1,about='phi')
        self.wait(1)    
        self.stop_ambient_camera_rotation(about='phi')
        self.wait(2)   