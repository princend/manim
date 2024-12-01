from manim import *
import numpy as np


class Plot3DSurface(ThreeDScene):
    def construct(self):
        # 創建座標軸
        axes = ThreeDAxes(
            x_range=[-6, 6, 1],
            y_range=[-6, 6, 1],
            z_range=[0, 50, 10],
            x_length=8,
            y_length=8,
            z_length=4,
        )
        
        # 將曲面數據轉換為點雲
        surface = Surface(
            lambda u, v: axes.c2p(u, v, u**2 + v**2),  # 將 Z 定義為 u^2 + v^2
            u_range=[-5, 5],
            v_range=[-5, 5],
            resolution=(30, 30),
            fill_opacity=0.7,
            checkerboard_colors=[BLUE_B, BLUE_B],
            stroke_width=0,
        )

        
        # 設置相機角度
        self.set_camera_orientation(phi=75 * DEGREES, theta=135 * DEGREES)
        # self.move_camera(phi=60 * DEGREES, theta=30 * DEGREES,frame_center=surface.get_center())
        self.move_camera(frame_center=surface.get_center())

        # 添加座標軸和曲面
        self.add( surface)

                # 初始化梯度下降
        learning_rate = 0.05
        current_point = np.array([5.0, 5.0])  # 初始點

        dot = Dot3D(axes.c2p(current_point[0], current_point[1], current_point[0]**2 + current_point[1]**2), color=RED)
        self.add(dot)

        trace= TracedPath(dot.get_center,stroke_color=ORANGE,stroke_width=2)
        self.add(trace)

        # grad_text = Text(f"梯度:{2 * current_point}", font_size=16)
        grad_text = Text(f"梯度:({current_point[0]:.2f}, {current_point[1]:.2f})", font_size=16)
        grad_text.add_updater(lambda m: m.to_corner(UR))
        self.add_fixed_in_frame_mobjects(grad_text)
        self.add(grad_text)
        for _ in range(50):  # 迭代次數
            grad = 2 * current_point  # 梯度計算 因為目標函數是 f(x,y) = x^2 + y^2 所以計算偏導數梯度向量為 ∇f(x,y)=(2x,2y)，要乘以2
            next_point = current_point - learning_rate * grad
            next_dot_position = axes.c2p(next_point[0], next_point[1], next_point[0]**2 + next_point[1]**2)
            self.play(dot.animate.move_to(next_dot_position), run_time=0.1)
            
        #     # 更新梯度顯示文本
            grad_text.become(Text(f"梯度:({current_point[0]:.2f}, {current_point[1]:.2f})", font_size=16))
            
            current_point = next_point

        self.wait(1)
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
        
        
