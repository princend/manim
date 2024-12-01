from manim import *

class Convert3Dto2DExample(ThreeDScene):
    def construct(self):
        # 建立 3D 物件
        axes = ThreeDAxes()
        sphere = Sphere(radius=1).set_color(BLUE).shift(UP)

        # 添加 3D 物件到場景
        self.add(axes, sphere)

        # 設置相機角度，讓場景看起來像 2D
        self.set_camera_orientation(phi=90 * DEGREES, theta=0 * DEGREES)

        # 播放動畫
        self.play(Create(axes), Create(sphere))
        self.wait()
