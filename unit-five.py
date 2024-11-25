from manim import *
import random

class ParametricCurveExample(Scene):
    def construct(self):
        curve = ParametricFunction(
            lambda t: np.array([np.sin(t), np.cos(t), 0]),
            t_range=np.array([0, TAU/2]),
            color=BLUE,
            stroke_width=10
        )
        self.add(curve)
        self.wait(1)

class PolarPlotExample(Scene):
    def construct(self):
        plane = PolarPlane().add_coordinates()
        curve = ParametricFunction(
            lambda t: np.array([
                (2 + np.cos(3 * t)) * np.cos(t),
                (2 + np.cos(3 * t)) * np.sin(t),
                0
            ]),
            t_range=[0, TAU],
            color=RED
        )
        self.add(plane, curve)
        self.wait(1)

class CustomShape(Scene):
    def construct(self):
        shape = VMobject()
        shape.set_points_as_corners([UP, RIGHT, DOWN, LEFT, UP])
        shape.set_color(YELLOW)
        self.add(shape)

from manim import *

class BarChartExample(Scene):
    def construct(self):
        chart = BarChart(
            values=[3, 5, 7, 6],
            bar_names=["A", "B", "C", "D"],
            y_range=[0, 8, 2],
            bar_colors=[BLUE, GREEN, RED, YELLOW]
        )
        self.add(chart)
        self.wait(1)
        self.play(chart.animate.change_bar_values([4, 6, 5, 7]))

class LineChartExample(Scene):
    def construct(self):
        # 創建座標軸
        axes = Axes(
            x_range=[0, 5, 1],  # x軸範圍：[最小值, 最大值, 步長]
            y_range=[0, 10, 2],  # y軸範圍：[最小值, 最大值, 步長]
            axis_config={"include_numbers": True}
        )
        
        # 定義數據點
        points = [[1, 2], [2, 4], [3, 6], [4, 8]]
        
        # 創建折線
        line_graph = VMobject()
        dots = VGroup()
        
        # 將數據點轉換為座標系中的點並連接
        line_points = []
        for x, y in points:
            point = axes.c2p(x, y)  # 將座標轉換為畫布上的點
            line_points.append(point)
            # 添加點
            dot = Dot(point, color=BLUE)
            dots.add(dot)
        
        line_graph.set_points_as_corners(line_points)
        line_graph.set_color(BLUE)
        
        # 添加到場景
        self.add(axes, line_graph, dots)
        self.wait(1)
        # 添加新的點
        new_point = [5, 10]
        new_dot = Dot(axes.c2p(new_point[0], new_point[1]), color=BLUE)
        
        # 更新折線
        new_line_points = line_points + [axes.c2p(new_point[0], new_point[1])]
        new_line = VMobject()
        new_line.set_points_as_corners(new_line_points)
        new_line.set_color(BLUE)

        # 播放動畫
        self.play(
            Transform(line_graph, new_line),
            Create(new_dot)
        )
        self.wait(1)

class Practice1(Scene):
    def construct(self):
        # 創建柱狀圖
        bar = BarChart(
            values=[1, 2, 3, 4, 5],
            bar_names=["A", "B", "C", "D", "E"],
            y_range=[0, 6, 1],  # y軸範圍：[最小值, 最大值, 步長]
            bar_colors =[RED,RED,BLUE,BLUE,BLUE]  # 直接設置顏色
        )
        
        # 添加到場景
        self.add(bar)
        self.wait(1)
    
class Practice2(Scene):
    def construct(self):
        # 創建柱狀圖
        chart = BarChart(
            values=[1, 2, 5, 4, 3],
            bar_names=["A", "B", "C", "D", "E"],
            y_range=[0, 6, 1],  # y軸範圍：[最小值, 最大值, 步長]
            bar_colors=[BLUE] * 5  # 所有柱子初始為藍色
        )
        
        # 添加到場景
        self.add(chart)
        self.wait(1)
        
        # 找出最高的柱子並改變其顏色和大小
        max_value_bar = chart.bars[np.argmax(chart.values)]
        self.play(
            max_value_bar.animate.set_color(RED).scale(1.2),
        )
        self.play(  
            max_value_bar.animate.set_color(BLUE).scale(1/1.2)
        )
        self.wait(1)


class RandomBarChart(Scene):
    def construct(self):
        chart = BarChart(
            values=[2, 4, 6, 8],
            bar_names=["A", "B", "C", "D"],
            y_range=[0, 10, 2]
        )
        self.add(chart)
        self.wait(1)

        # 隨機更新
        new_values = [random.randint(1, 9) for _ in range(4)]
        self.play(chart.animate.change_bar_values(new_values))
        self.wait(1)

class BarChartWithLabels(Scene):
    def construct(self):
        chart = BarChart(
            values=[3, 5, 7, 6],
            bar_names=["A", "B", "C", "D"]
        )
        self.add(chart)

        # 添加數據標籤
        for bar, value in zip(chart.bars, chart.values):
            label = Text(str(value), font_size=24).next_to(bar, UP)
            self.add(label)

        # 突出最大值
        max_bar = chart.bars[np.argmax(chart.values)]
        self.play(max_bar.animate.set_color(RED).scale(1.2))
        self.play(max_bar.animate.set_color(RED).scale(1/1.2))
        self.wait(1)