from manim import *

class StyledTable(Scene):
    def construct(self):
        text = MathTex("Target Encoding",color=WHITE).scale(2.5)
        self.play(Write(text))
        self.wait(0.5)
        self.play(FadeOut(text))
        class1="實驗班"
        class2="普通班"
        # 表格數據
        data = [
            ["1", class1, "90"],
            ["2", class1, "85"],
            ["3", class2, "80"],
            ["4", class2, "75"],
            ["5", class1, "95"],
            ["6", class1, "90"],
            ["7", class2, "85"],
        ]
        # 創建表格
        table = Table(
            data,
            col_labels=[Text("同學"), Text("班級"), Text("成績")],
            element_to_mobject=Text,  # 使用 Text 標籤
            line_config={"stroke_width": 2},  # 自訂表格線條
        ).scale(0.5).to_edge(LEFT*2).shift(UP*0.5)
        # 修改某些欄位的樣式
        table.get_entries((2, 2)).set_color(BLUE)  # 將第 2 行第 3 列的元素設為紅色
        table.get_entries((2, 3)).set_color(BLUE)  # 將第 2 行第 3 列的元素設為紅色
        table.get_entries((3, 2)).set_color(BLUE)  # 將第 2 行第 3 列的元素設為紅色
        table.get_entries((3, 3)).set_color(BLUE)  # 將第 2 行第 3 列的元素設為紅色
        table.get_entries((6, 2)).set_color(BLUE)  # 將第 2 行第 3 列的元素設為紅色
        table.get_entries((6, 3)).set_color(BLUE)  # 將第 2 行第 3 列的元素設為紅色
        table.get_entries((7, 2)).set_color(BLUE)  # 將第 2 行第 3 列的元素設為紅色
        table.get_entries((7, 3)).set_color(BLUE)  # 將第 2 行第 3 列的元素設為紅色
        self.play(Create(table))
        self.wait(0.5)
        class1_mean_text = Text("實驗班成績均值:").next_to(table, RIGHT, buff=1.5).shift(UP*2.75)
        self.play(Write(class1_mean_text))
        class1_mean_formula = MathTex(r"\frac{90 + 85 + 95 + 90}{4} = 90", color=BLUE).next_to(class1_mean_text, DOWN, buff=1)
        self.play(Create(class1_mean_formula))
        self.wait(0.5)
        class2_mean_text = Text("普通班成績均值:").next_to(class1_mean_formula, DOWN, buff=1)
        self.play(Write(class2_mean_text))
        class2_mean_formula = MathTex(r"\frac{80 + 75 + 85}{3} = 80", color=WHITE).next_to(class2_mean_text, DOWN, buff=1)
        self.play(Create(class2_mean_formula))
        self.wait(0.5)
        entries2_2 = table.get_entries((2, 2))
        entries3_2 = table.get_entries((3, 2))
        entries4_2 = table.get_entries((4, 2))
        entries5_2 = table.get_entries((5, 2))
        entries6_2 = table.get_entries((6, 2))
        entries7_2 = table.get_entries((7, 2))
        entries8_2 = table.get_entries((8, 2))
       

        self.play(
            FadeOut(entries2_2),
            FadeOut(entries3_2),
            FadeOut(entries4_2),
            FadeOut(entries5_2),
            FadeOut(entries6_2),
            FadeOut(entries7_2),
            FadeOut(entries8_2),
            run_time=0.5
        )
        self.wait(0.1)
        self.play(Write(Text("90",color=BLUE).scale(0.5).move_to(entries2_2.get_center())),
                  Write(Text("90",color=BLUE).scale(0.5).move_to(entries3_2.get_center())),
                  Write(Text("80",color=WHITE).scale(0.5).move_to(entries4_2.get_center())),
                  Write(Text("80",color=WHITE).scale(0.5).move_to(entries5_2.get_center())),
                  Write(Text("90",color=BLUE).scale(0.5).move_to(entries6_2.get_center())),
                  Write(Text("90",color=BLUE).scale(0.5).move_to(entries7_2.get_center())),
                  Write(Text("80",color=WHITE).scale(0.5).move_to(entries8_2.get_center())),
                  run_time=0.5)
        self.wait()
        self.wait(0.5)
