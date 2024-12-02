from gradient_descent_lr1 import Plot3DSurface
from manim import *

class GradientDescent(Plot3DSurface):
    def construct(self):
        self.draw_gradient_descent()

    def draw_gradient_descent(self,learning_rate=0.05):
        self.draw_gradient(learning_rate)
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