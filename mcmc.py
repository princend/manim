from manim import *
import numpy as np

# class MCMCVisualization(Scene):
#     def construct(self):
#         # 目標分佈（正態分佈）
#         target_distribution = FunctionGraph(lambda x: np.exp(-x**2), x_range=[-3, 3])
#         self.play(Create(target_distribution))
        
#         # MCMC樣本點
#         sample_points = VGroup()
#         for i in range(5):
#             point = Dot(point=[i-2, np.exp(-(i-2)**2), 0])
#             sample_points.add(point)
        
#         self.play(FadeIn(sample_points))
#         self.wait(1)


# class MetropolisHastings(Scene):
#     def construct(self):
#         # 當前狀態
#         current_state = Dot(point=[0, np.exp(-0**2), 0], color=BLUE)
#         candidate_state = Dot(point=[1, np.exp(-1**2), 0], color=GREEN)
        
#         # 顯示當前狀態和候選狀態
#         self.play(FadeIn(current_state))
#         self.play(FadeIn(candidate_state))
        
#         # 顯示接受或拒絕
#         self.play(Transform(current_state, candidate_state))
#         self.wait(1)

# class MCMCConvergence(Scene):
#     def construct(self):
#         # 目標分佈
#         target_distribution = FunctionGraph(lambda x: np.exp(-x**2), x_range=[-3, 3])
#         self.play(Create(target_distribution))
        
#         # 模擬抽樣過程
#         sample_points = VGroup()
#         for i in range(10):
#             point = Dot(point=[np.random.uniform(-3, 3), np.exp(-np.random.uniform(-3, 3)**2), 0], color=BLUE)
#             sample_points.add(point)
        
#         self.play(FadeIn(sample_points))
#         self.wait(1)

# config.disable_caching = True
# from manim import *

class MCMCMetropolisHastings(Scene):
    def construct(self):
        config.disable_caching = True  # 禁用快取
        axes = Axes(x_range=[-4, 4, 1], y_range=[0, 1, 0.1], tips=False)
        target_graph = axes.plot(lambda x: np.exp(-0.5 * x**2), color=BLUE)
        
        self.play(Create(axes), Create(target_graph))
        
        current_x = 0
        current_dot = Dot(axes.coords_to_point(current_x, np.exp(-0.5 * current_x**2)), color=YELLOW)
        self.play(FadeIn(current_dot))

        sample_dots = VGroup()
        for _ in range(10):
            candidate_x = np.random.normal(current_x, 1)
            candidate_dot = Dot(axes.coords_to_point(candidate_x, np.exp(-0.5 * candidate_x**2)), color=GREEN)
            acceptance_ratio = min(1, np.exp(-0.5 * candidate_x**2) / np.exp(-0.5 * current_x**2))

            self.play(FadeIn(candidate_dot), run_time=0.5)
            if np.random.rand() < acceptance_ratio:
                self.play(Transform(current_dot, candidate_dot))
                current_x = candidate_x
                sample_dots.add(candidate_dot.copy().set_color(RED))
            else:
                self.play(FadeOut(candidate_dot), run_time=0.5)

        self.play(FadeIn(sample_dots))
        self.wait(2)
