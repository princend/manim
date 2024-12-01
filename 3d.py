from manim import *

class SphereWithMaterial(Scene):
    def construct(self):
        sphere = Sphere(radius=1, resolution=(16, 16))
        sphere.set_color(BLUE)
        sphere.set_opacity(0.5)  # 設置透明度
        sphere.set_stroke(width=0)
        self.add(sphere)
        self.play(Create(sphere))
        self.wait()


