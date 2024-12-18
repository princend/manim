from manim import *


class ConvolutionalLayerDemo(Scene):
    def construct(self):
        input_matrix = [[1, 2, 1], [0, 1, 4], [8, 1, 6]]

        input_grid = self.create_grid(input_matrix, LEFT * 3 + UP * 0.25)
        self.play(Create(input_grid))
        arrow = Arrow(color=WHITE,buff=3).next_to(input_grid, RIGHT*4)
        text = Text("Max Pooled", font_size=16).next_to(arrow, UP*0.5).shift(LEFT*0.15)
        self.play(Write(arrow),Write(text))
        self.perform_convolution(input_matrix, input_grid)
        self.wait(2)

    def create_grid(self, matrix, position):
        """Create a grid representation of a matrix."""
        rows, cols = len(matrix), len(matrix[0])
        grid = VGroup()

        for i in range(rows):
            for j in range(cols):
                cell = Square(side_length=0.5)
                cell.move_to(position + RIGHT * j * 0.5 + DOWN * i * 0.5)
                value = Text(str(matrix[i][j]), font_size=24)
                value.move_to(cell.get_center())
                grid.add(VGroup(cell, value))
        return grid

    def perform_convolution(self, input_matrix, input_grid):
        """Perform convolution operation and animate the process."""
        input_rows, input_cols = len(input_matrix), len(input_matrix[0])
     
        output_matrix = [[2, 4], [8, 6]]
        arr = [[0, 1, 3, 4], [1, 2, 4, 5], [3, 4, 6, 7], [4, 5, 7, 8]]
        output_grid = self.create_grid(output_matrix, RIGHT * 2.5)
       
        for i in range(4):
            highlights = VGroup()
            highlights.add(input_grid[arr[i][0]].copy().set_fill(ORANGE, opacity=0.5))
            highlights.add(input_grid[arr[i][1]].copy().set_fill(ORANGE, opacity=0.5))
            highlights.add(input_grid[arr[i][2]].copy().set_fill(ORANGE, opacity=0.5))
            highlights.add(input_grid[arr[i][3]].copy().set_fill(ORANGE, opacity=0.5))

            self.play(
                FadeIn(highlights),
                run_time=0.5,
            )
            self.play(Create(output_grid[i]), run_time=0.5)
            self.play(
                FadeOut(highlights),
                run_time=0.5,
            )
       
