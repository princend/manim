from manim import *
import numpy as np

class SaddlePointAndSGD(ThreeDScene):
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

        # 初始點
        current_point = np.array([-1.5, 0])  # 初始位置
        path_points = [axes.c2p(current_point[0], current_point[1], current_point[0]**2 - current_point[1]**2)]

        # 梯度下降點
        moving_dot = Dot3D(point=path_points[0], color=RED, radius=0.1)

        # 梯度顯示
        grad_text = Text(f"梯度:({current_point[0]:+.2f}, {current_point[1]:+.2f})", font_size=16)
        grad_text.add_updater(lambda m: m.become(Text(f"梯度:({current_point[0]:+.2f}, {current_point[1]:+.2f})", font_size=16).to_corner(UR).shift(np.array([-0.75, 0, 0]))))
        self.add_fixed_in_frame_mobjects(grad_text)

        # 路徑追踪
        trace = TracedPath(moving_dot.get_center, stroke_color=YELLOW, stroke_width=2)

        # 場景設置
        self.set_camera_orientation(phi=75 * DEGREES, theta=45 * DEGREES)
        self.add(surface, trace, grad_text)

        # 學習率與隨機性參數
        base_learning_rate = 0.05  # 基礎學習率
        noise_scale = 0.01  # 隨機擾動範圍


        # 進行梯度下降（SGD）
        for _ in range(30):  # 迭代次數
            grad = 2 * current_point  # 梯度計算
            learning_rate = base_learning_rate  # 初始化學習率

            # 當接近鞍點時，額外加強方向或增強隨機性
            if np.linalg.norm(current_point) < 0.5:
                grad[1] += -2 * np.sign(current_point[1])  # 加強 y 軸方向的推動
                noise_scale = 0.5  # 增強隨機擾動
                learning_rate = 0.2  # 增加學習率

            # 引入隨機擾動
            noise = np.random.uniform(-noise_scale, noise_scale, size=current_point.shape)
            next_point = current_point - learning_rate * grad + noise  # 更新位置
            z_value = next_point[0]**2 - next_point[1]**2

            # 確保點更新到正確位置
            path_points.append(axes.c2p(next_point[0], next_point[1], z_value))
            current_point = next_point

            # 更新動畫
            grad_text.become(Text(f"梯度:({current_point[0]:+.2f}, {current_point[1]:+.2f})", font_size=16))
            self.play(moving_dot.animate.move_to(path_points[-1]), run_time=0.1)

        self.wait(1)   

        self.begin_ambient_camera_rotation(rate=2,about='theta')
        self.wait(PI)
        self.stop_ambient_camera_rotation(about='theta')
        # 鏡頭動畫
        self.wait(2)
