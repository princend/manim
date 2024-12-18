from manim import *
import numpy as np

class AdamOptimization(Scene):
    def construct(self):
        # 標題
        title = Text("Adam Optimization").scale(0.8).to_edge(UP)
        self.play(Write(title))

        # 等高線圖 (模擬損失函數)
        contours = VGroup(
            *[Circle(radius=r, color=BLUE_B).shift(UP * 0.5 + RIGHT * 0.5)
            for r in [0.5, 1.0, 1.5, 2.0, 2.5]]
        )
        self.play(Create(contours))

        # 起始點
        start_point = LEFT * 3 + DOWN * 2
        dot = Dot(point=start_point, color=YELLOW)
        self.play(FadeIn(dot))

        # Adam 優化軌跡模擬 (用數據模擬軌跡點)
        adam_path = self.generate_adam_path(start_point)
        trajectory = VMobject(color=ORANGE)
        trajectory.set_points_smoothly(adam_path)

        # 動畫展示軌跡
        self.play(Create(trajectory), run_time=5, rate_func=linear)
        self.wait(2)

    def generate_adam_path(self, start_point):
        """
        模擬 Adam 優化器的軌跡 (非真實計算，但符合其收斂特性)
        """
        path = [np.array([start_point[0], start_point[1], 0])]  # 确保是三维向量
        current_point = np.array([start_point[0], start_point[1], 0])

        # 确保 current_point 是二维向量
        if current_point.shape != (2,):
            current_point = current_point[:2]

        # 模擬步長衰減和動量
        alpha = 0.5  # 初始學習率
        beta1 = 0.9  # 一階動量衰減
        beta2 = 0.999  # 二階動量衰減
        epsilon = 1e-8
        m = np.array([0.0, 0.0])  # 一階動量
        v = np.array([0.0, 0.0])  # 二階動量

        for t in range(1, 20):  # 迭代 20 次模擬更新
            # 模擬梯度 (越靠近中心梯度越小)
            grad = -current_point[:2] / (np.linalg.norm(current_point[:2]) + epsilon)

            # 更新動量項
            m[:2] = beta1 * m[:2] + (1 - beta1) * grad
            v[:2] = beta2 * v[:2] + (1 - beta2) * (grad ** 2)

            # 動量校正
            m_hat = m / (1 - beta1 ** t)
            v_hat = v / (1 - beta2 ** t)

            # 更新��數
            step = alpha * m_hat[:2] / (np.sqrt(v_hat[:2]) + epsilon)
            current_point[:2] += step  # 更新 x 和 y

            # 加入軌跡點
            path.append(np.array([current_point[0], current_point[1], 0]))  # 确保是三维向量

        return path
