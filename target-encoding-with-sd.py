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
            ["1", class1, "60"],
            ["2", class1, "65"],
            ["3", class2, "85"],
            ["4", class2, "45"],
            ["5", class1, "70"],
            ["6", class1, "65"],
            ["7", class2, "65"],
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
        class1_mean_formula = MathTex(r"\frac{60 + 65 + 70 + 65}{4} = 65", color=BLUE).next_to(class1_mean_text, DOWN, buff=1)
        self.play(Create(class1_mean_formula))
        self.wait(0.5)
        class2_mean_text = Text("普通班成績均值:").next_to(class1_mean_formula, DOWN, buff=1)
        self.play(Write(class2_mean_text))
        class2_mean_formula = MathTex(r"\frac{85 + 45 + 65}{3} = 65", color=WHITE).next_to(class2_mean_text, DOWN, buff=1)
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
        mean_group=VGroup(Text("65",color=RED).scale(0.5).move_to(entries2_2.get_center()),
                          Text("65",color=RED).scale(0.5).move_to(entries3_2.get_center()),
                          Text("65",color=RED).scale(0.5).move_to(entries4_2.get_center()),
                          Text("65",color=RED).scale(0.5).move_to(entries5_2.get_center()),
                          Text("65",color=RED).scale(0.5).move_to(entries6_2.get_center()),
                          Text("65",color=RED).scale(0.5).move_to(entries7_2.get_center()),
                          Text("65",color=RED).scale(0.5).move_to(entries8_2.get_center()),
                          )
        self.wait(0.1)
        self.play(Write(mean_group),run_time=0.5)
        
        self.wait(0.1)
    
        self.play(FadeOut(VGroup(class1_mean_text,class1_mean_formula,class2_mean_text,class2_mean_formula)),run_time=0.5)
        self.wait(0.5)
        hint_text = Text(f"目標均值編碼\n無法區分\n實驗班及普通班",color=RED).next_to(table,RIGHT,buff=1)
        self.play(Write(hint_text))
        self.wait(0.5)
        self.play(FadeOut(hint_text))
        self.wait(0.5)

        class1_std_text = Text("實驗班成績標準差:",color=BLUE).next_to(table, RIGHT, buff=1.5).shift(UP*2.75)
        self.play(Write(class1_std_text))
        class1_std_formula = MathTex(r"\sqrt{\frac{(60-65)^2 + (65-65)^2 + (70-65)^2 + (65-65)^2}{4}} = 3.54", color=BLUE).scale(0.6).next_to(class1_std_text, DOWN, buff=1)
        self.play(Create(class1_std_formula))
        self.wait(0.5)
        class2_std_text = Text("普通班成績標準差:").next_to(class1_std_formula, DOWN, buff=1)
        self.play(Write(class2_std_text))
        class2_std_formula = MathTex(r"\sqrt{\frac{(85-65)^2 + (45-65)^2 + (65-65)^2}{3}} = 16.33", color=WHITE).scale(0.6).next_to(class2_std_text, DOWN, buff=1)
        self.play(Create(class2_std_formula))
        self.wait(0.5)
        self.play(FadeOut(mean_group),run_time=0.5)
        self.play(Write(Text("3.54",color=BLUE).scale(0.5).move_to(entries2_2.get_center())),
                  Write(Text("3.54",color=BLUE).scale(0.5).move_to(entries3_2.get_center())),
                  Write(Text("16.33",color=WHITE).scale(0.5).move_to(entries4_2.get_center())),
                  Write(Text("16.33",color=WHITE).scale(0.5).move_to(entries5_2.get_center())),
                  Write(Text("3.54",color=BLUE).scale(0.5).move_to(entries6_2.get_center())),
                  Write(Text("3.54",color=BLUE).scale(0.5).move_to(entries7_2.get_center())),
                  Write(Text("16.33",color=WHITE).scale(0.5).move_to(entries8_2.get_center())),
                  run_time=0.5)
        image_file = "assets/mizunehehe.webp"
        hehe_mobject = ImageMobject(image_file)
        checkmark = Tex(r"\checkmark", color=GREEN).scale(3)
        checkmark.move_to(table.get_center()) 
        hehe_mobject.next_to(checkmark,RIGHT)
         # 調整位置
        self.play(Write(checkmark),FadeIn(hehe_mobject))
        self.wait(2)
        

