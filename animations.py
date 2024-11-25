from manim import *

def bounce_animation(mobject, scene):
    scene.play(mobject.animate.shift(UP * 2))
    scene.play(mobject.animate.shift(DOWN * 2))
