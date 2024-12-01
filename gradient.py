from manim import *
import numpy as np


# Step 1: 定義 3D 曲面的數據生成函數
def generate_surface_data():
    x = np.linspace(-5, 5, 100)
    y = np.linspace(-5, 5, 100)
    X, Y = np.meshgrid(x, y)
    Z = X**2 + Y**2  # 示例：二次曲面
    return X, Y, Z

# Step 2: 使用 Manim 畫出 3D 曲面
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


        # 生成曲面數據
        X, Y, Z = generate_surface_data()
        
        # 將曲面數據轉換為點雲
        surface = Surface(
            lambda u, v: axes.c2p(u, v, u**2 + v**2),  # 將 Z 定義為 u^2 + v^2
            u_range=[-5, 5],
            v_range=[-5, 5],
            resolution=(30, 30),
            fill_opacity=0.7,
            checkerboard_colors=[BLUE_B, BLUE_B],
        )

        surface.shift(np.array((0.0, 0.0, -2.0)))
        # 設置相機角度
        self.set_camera_orientation(phi=75 * DEGREES, theta=45 * DEGREES)
        
        # 添加座標軸和曲面
        # self.add(axes, surface)
        self.add( surface)
        self.wait(3)
