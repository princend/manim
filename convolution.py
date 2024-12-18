from manim import *


class ConvolutionalLayerDemo(Scene):
    def construct(self):
        input_matrix = [[1, 1, 1], [1, 0, 1], [0, 0, 1]]

        kernel = [[1, 0], [0, 1]]

        input_grid = self.create_grid(input_matrix, LEFT * 3 + UP * 0.25)
        self.play(Create(input_grid))
        text = Text("Image", font_size=24).next_to(input_grid, DOWN * 0.5)
        self.play(Write(text))
        self.dot = (
            Dot()
            .move_to((input_grid.get_center() + ORIGIN) / 2)
            .shift(RIGHT * 0.25 + DOWN * 0.1)
        )

        kernel_grid = self.create_grid(kernel, ORIGIN)
        text2 = Text("Kernel", font_size=24).next_to(kernel_grid, DOWN * 0.5)
        self.play(Create(kernel_grid))
        self.play(Write(text2))
        self.play(Create(self.dot))
        self.perform_convolution(input_matrix, kernel, input_grid, kernel_grid)

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

    def perform_convolution(self, input_matrix, kernel, input_grid, kernel_grid):
        """Perform convolution operation and animate the process."""
        input_rows, input_cols = len(input_matrix), len(input_matrix[0])
        kernel_size = len(kernel)
        output_rows, output_cols = (
            input_rows - kernel_size + 1,
            input_cols - kernel_size + 1,
        )

        output_matrix = [[1, 2], [1, 1]]
        arr = [[0, 1, 3, 4], [1, 2, 4, 5], [3, 4, 6, 7], [4, 5, 7, 8]]
        output_grid = self.create_grid(output_matrix, RIGHT * 3)

        for i in range(4):
            highlights = VGroup()
            highlights.add(input_grid[arr[i][0]].copy().set_fill(ORANGE, opacity=0.5))
            highlights.add(input_grid[arr[i][1]].copy().set_fill(ORANGE, opacity=0.5))
            highlights.add(input_grid[arr[i][2]].copy().set_fill(ORANGE, opacity=0.5))
            highlights.add(input_grid[arr[i][3]].copy().set_fill(ORANGE, opacity=0.5))
            kernel_highlights = VGroup()
            kernel_highlights.add(kernel_grid[0].copy().set_fill(ORANGE, opacity=0.5))
            kernel_highlights.add(kernel_grid[1].copy().set_fill(ORANGE, opacity=0.5))
            kernel_highlights.add(kernel_grid[2].copy().set_fill(ORANGE, opacity=0.5))
            kernel_highlights.add(kernel_grid[3].copy().set_fill(ORANGE, opacity=0.5))
            dot_highlights = VGroup()
            dot_highlights.add(self.dot.copy().set_fill(ORANGE, opacity=0.5))
            self.play(
                FadeIn(highlights),
                FadeIn(kernel_highlights),
                FadeIn(dot_highlights),
                run_time=0.5,
            )
            self.play(Create(output_grid[i]), run_time=0.5)
            self.play(
                FadeOut(highlights),
                FadeOut(kernel_highlights),
                FadeOut(dot_highlights),
                run_time=0.5,
            )
        text3 = Text("Convolved", font_size=24).next_to(output_grid, DOWN * 0.5)
        text4 = Text("Feature", font_size=24).next_to(text3, DOWN * 0.5)
        self.play(Write(text3))
        self.play(Write(text4))
