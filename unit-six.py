from manim import *
class CameraMoveExample1(MovingCameraScene):
    def construct(self):
        square = Square(color=BLUE)
        self.add(square)
        self.play(self.camera.frame.animate.move_to(LEFT * 3))
        self.wait(1)

class CameraMoveExample2(MovingCameraScene):
    def construct(self):
        square = Square(color=BLUE)
        self.add(square)
        # 縮小相機（放大場景）
        self.play(self.camera.frame.animate.scale(0.5), run_time=2)
        self.wait(1)
        # 放大相機（縮小場景）
        self.play(self.camera.frame.animate.scale(2), run_time=2)
        self.wait(1)

class MoveCamera(ThreeDScene):  # 改用 ThreeDScene
    def construct(self):
        self.add(Cube())
        # 移動相機
        self.move_camera(phi=45 * DEGREES)  # 上下角度 控制相機的俯仰角（上下視角）。
        self.move_camera(theta=45 * DEGREES)  # 左右角度 控制相機的方位角（左右視角）。
        self.move_camera(gamma=90 * DEGREES)  # 控制相機的滾轉角（旋轉視角）。
        self.wait(1)

class ZoomCamera(ThreeDScene):
    def construct(self):
        self.add(Cube())
        self.move_camera(phi=45 * DEGREES)  # 上下角度
        self.move_camera(zoom=0.5)  # 縮放
        self.wait(1)

class ExampleLine3D(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        line = Line3D(start=np.array([0, 0, 0]), end=np.array([2, 2, 3]))
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
        self.add(axes, line)

class Sphere1(ThreeDScene):
    def construct(self):
        sphere = Sphere(radius=1, color=BLUE)
        self.add(sphere)
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
        self.begin_ambient_camera_rotation(rate=1)  # 開始自動旋轉
        self.wait(5)
        self.stop_ambient_camera_rotation()  # 停止旋轉


class CameraPanExample(MovingCameraScene):
    def construct(self):
        square = Square(color=BLUE).shift(LEFT * 3)
        circle = Circle(color=RED).shift(RIGHT * 3)

        self.add(square, circle)
        self.play(self.camera.frame.animate.move_to(square))  # 相機移動到方形
        self.play(FadeIn(square))
        self.play(self.camera.frame.animate.move_to(circle))  # 相機移動到圓形
        self.play(FadeIn(circle))


class ThreeDSceneExample(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        sphere = Sphere(radius=1, color=BLUE).move_to(UP * 2)

        self.add(axes, sphere)
        self.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES)
        self.play(Create(sphere))
        self.begin_ambient_camera_rotation(rate=1)  # 相機自動旋轉
        self.wait(3)
        self.stop_ambient_camera_rotation()
        self.begin_ambient_camera_rotation(rate=-1)  # 相機自動旋轉
        self.wait(3)
        self.stop_ambient_camera_rotation()
        self.begin_ambient_camera_rotation(rate=1,about="gamma")  # 相機自動旋轉
        self.wait(3)
        self.stop_ambient_camera_rotation()

class Exercise1(MovingCameraScene):
    def construct(self):
        square = Square(color=BLUE).shift(LEFT * 3)
        self.add(square)
        self.play(self.camera.frame.animate.move_to(square).scale(0.5))
        self.wait(1)

class Exercise2(ThreeDScene):
       def construct(self):
        axes = ThreeDAxes()
        cube = Cube(side_length=2).shift(LEFT*2)
        sphere = Sphere(radius=1.5).shift(RIGHT*3)
        self.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES, gamma=45 * DEGREES)
        self.add(axes, cube, sphere)
        self.begin_ambient_camera_rotation(rate=1)
        self.wait(3)
        self.stop_ambient_camera_rotation()