from manim import *

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

        # 初始點
        current_point = np.array([-1.5, 0])  # 初始位置
        path_points = [axes.c2p(current_point[0], current_point[1], current_point[0]**2 - current_point[1]**2)]

        # 梯度下降點
        moving_dot = Dot3D(point=path_points[0], color=RED, radius=0.1)

        # 路徑追踪
        trace = TracedPath(moving_dot.get_center, stroke_color=YELLOW, stroke_width=2)

        # 場景設置
        self.set_camera_orientation(phi=75 * DEGREES, theta=45 * DEGREES)
        self.add(surface, trace)

        # 固定數值模擬
        # points = [
        #     [-1.5, 0, 2.25],
        #     [-1.4, 0.5, 1.25],
        #     [-0.5, 1.0, 0.25],
        #     [0.0, 1.5, -2.25],  # 穿過鞍點
        #     [0.5, 1.8, -3.15],
        #     [1.0, 2.0, -4.0],  # 繼續向下降
        # ]
        points=[]

# 生成40個點


# 初始部分：從 -1.5 開始，緩慢接近鞍點
        current_point = np.array([-1.5, 0])
        learning_rate = 0.05
        noise_scale = 0.01  # 隨機擾動範圍

# 前 15 個步驟：緩慢接近鞍點
        for _ in range(50):
            grad = 2 * current_point  # 梯度計算
            noise = np.random.uniform(-noise_scale, noise_scale, size=current_point.shape)  # 隨機擾動
            current_point = current_point - learning_rate * grad + noise  # 更新位置
            points.append(current_point.tolist())

# 中間 10 個步驟：在鞍點附近波動
        # for _ in range(5):
        #     noise = np.random.uniform(-noise_scale, noise_scale, size=current_point.shape)  # 隨機擾動
        #     current_point = current_point + noise  # 隨機移動
        #     points.append(current_point.tolist())

# 後 15 個步驟：快速向下掉落


        # for _ in range(15):
        #     grad = 2 * current_point  # 梯度計算
        #     noise = np.random.uniform(-noise_scale, noise_scale, size=current_point.shape)  # 隨機擾動
        #     current_point = current_point - learning_rate * grad + noise  # 更新位置
        #     points.append(current_point.tolist())


        # addedPoints = [
        #     [0, 0.0, 0.0],
        #     [0, 0.1, -0.2],
        #     [0, 0.2, -0.4],
        #     [0, 0.3, -0.6],
        #     [0, 0.4, -0.8],
        #     [0, 0.5, -1.0],
        #     [0, 0.6, -1.2],
        #     [0, 0.7, -1.4],
        #     [0, 0.8, -1.6],
        #     [0, 0.9, -1.8],
        #     [0, 1.0, -2.0],
        #     [0, 1.1, -2.2],
        #     [0, 1.2, -2.4],
        #     [0, 1.8, -3.15],
        #     [0, 2.0, -4.0]  # 保持不變
        # ]

        addedPoints = [
            [0, 0.0, 0.0],
            [0, pow(0.01,0.5), -0.01],
            [0, pow(0.02,0.5), -0.02],
            [0, pow(0.03,0.5), -0.03],
            [0, pow(0.05,0.5), -0.05],
            [0, pow(0.08,0.5), -0.08],
            [0, pow(0.1,0.5), -0.1],
            [0, pow(0.2,0.5), -0.2],
            [0, pow(0.4,0.5), -0.4],
            [0, pow(0.6,0.5), -0.6],
            [0, pow(0.8,0.5), -0.8],
            [0, pow(1.0,0.5), -1.0],
            [0, pow(1.2,0.5), -1.2],
            [0, pow(1.4,0.5), -1.4],
            [0, pow(1.6,0.5), -1.6],
            # [0, pow(1.8,0.5), -1.8],
            [0, pow(2.0,0.5), -2.0],
            # [0, pow(2.2,0.5), -2.2],
            [0, pow(2.4,0.5), -2.4],
            [0, pow(3.15,0.5), -3.15],
            [0, pow(4,0.5), -4.0]  # 保持不變
        ]

        for point in addedPoints:
            points.append(point)
        # 動畫展示
        for p in points:
            path_points.append(axes.c2p(p[0], p[1], p[0]**2 - p[1]**2))
            self.play(moving_dot.animate.move_to(path_points[-1]), run_time=0.1)
            
        # self.wait(1)   
        # self.begin_ambient_camera_rotation(rate=2,about='theta')
        # self.wait(PI)
        # self.stop_ambient_camera_rotation(about='theta')
        
        # 停止展示
        self.wait(2)
