from manim import *
class ImagePractice(Scene):
    def construct(self):
        image = ImageMobject("assets/sunbaby.png")
        self.play(FadeIn(image))
        
        small_image = image.copy().scale(0.75)
        large_image = image.copy().scale(1.5)
        
        for _ in range(4):
            self.play(Transform(image, large_image, run_time=0.75))
            self.play(Transform(image, small_image, run_time=0.75))
        self.wait(1)
