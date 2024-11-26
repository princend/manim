---
title: Manim

---

# Manim

## 第一單元：基礎介紹與環境設置
### 1. 單元目標
* 了解 Manim 是什麼以及其應用場景。 
* 掌握如何安裝 Manim 並運行基礎腳本。
### 2. Manim 簡介
   :::info 
   什麼是 Manim?
   Manim 是一個用 Python 撰寫數學動畫的開源庫，專為展示數學概念、教學演示和數據可視化設計。 
   採用  v0.18.1 版本
   :::
*    名稱來源：Mathematical Animation Engine
*    用途：
        * 繪製數學函數與公式動畫。
        * 建立教學視頻或學術展示。
        * 視覺化數據或程式流程。

### 3.Manim 的特點： 
    * 靈活性：透過 Python 程式控制動畫。
    * 高精度渲染：生成高畫質影片。
    * 支援 2D 與 3D 場景。

### 4. 安裝環境
* 步驟一：準備安裝環境    
    * 確保已安裝 Python（版本 3.7 或以上）。
    * 安裝 pip 與 virtualenv（可選）。

* 步驟二：安裝 Manim    
    * 建議使用虛擬環境：
    ```python=   
    python -m venv manim-env
    source manim-env/bin/activate  # Windows 用 `manim-    nv\Scripts\activate`
    ```
    * 使用 pip 安裝：
	``` python= 
	pip install manim
	```
* 步驟三：檢查安裝
    * 測試 Manim 是否成功安裝：
    ```python=
    manim --version
    ```
* 步驟四：額外安裝工具（可選）
    * 安裝 FFmpeg（用於影片渲染）：
        * Windows: 可從 [FFmpeg](https://ffmpeg.org/download.html) 官網 下載。
    [FFmpeg安裝教學](https://blog.csdn.net/m0_53466575/article/details/136251866)
        * macOS: 使用 Homebrew 安裝：brew install ffmpeg。
    * 安裝 [ MiKTeX](https://miktex.org/howto/install-miktex)(用於Latex)
### 5. 初次運行 Manim
建立第一個 Manim 腳本    
* 建立檔案：helloworld.py
```python=
from manim import *

class HelloWorld(Scene):
    def construct(self):
        text = Text("Hello, Manim!")
        self.play(Write(text))

```
執行腳本
* 在終端執行以下命令：
```=
manim -pql helloworld.py HelloWorld
```
* 選項解釋：
    * -p：自動播放輸出視頻。
    * -ql：快速渲染（low quality）。
預期結果
* 螢幕上顯示「Hello, Manim!」的動畫。


### 6.單元練習
* 練習目標:建立自己的動畫腳本
* 練習內容:
    * 新建一個python檔案
    * 更改文字內容 使其影片顯示你更改過後的文字

---


## 第二單元：基本對象與場景


### 1. 單元目標
- 學習如何建立 Manim 的基本場景。
- 掌握常用對象（如圓形、方形、線條等）的創建與操作。


### 2. 場景 (Scene) 的基本結構

**Scene 是 Manim 的核心單位，用來定義動畫的內容與順序。**

#### Scene 的結構範例：
```python=
from manim import *

class BasicScene(Scene):
    def construct(self):
        square = Square()  # 創建一個方形
        self.add(square)  # 將方形添加到場景中
        self.wait(1)  # 等待 1 秒
```

**重要方法**：
- `add(obj)`：將對象添加到場景。
- `wait(time)`：暫停動畫 `time` 秒。
- `remove(obj)`：從場景中移除對象。
- `clear()`：清除場景中的所有對象。

---

### 3. 基本對象的創建與屬性調整

#### 常用幾何對象
- **圓形 (Circle)**：
    ```python=
    circle = Circle()  # 默認為單位圓
    circle.set_color(RED)  # 設置顏色為紅色
    ```

- **方形 (Square)**：
    ```python=
    square = Square()  # 默認邊長為 2
    square.set_fill(BLUE, opacity=0.5)  # 填充藍色，透明度 50%
    ```

- **多邊形 (Polygon)**：
    ```python=
    polygon = Polygon(
        [-1, 0, 0], [1, 0, 0], [0, 1, 0]
    )  # 創建一個三角形
    ```

#### 基本對象的常用屬性
1. **顏色**：
    - `set_color(color)`：設置對象顏色。
2. **位置**：
    - `move_to(position)`：移動對象到指定位置。
    - `next_to(position)`：移動對象到目標的旁邊
    - `shift(direction)`：按方向平移。
    - `to_corner(position)`：到角落。
    - `to_edge(postion)`:到邊緣。
3. **大小**：
    - `scale(factor)`：按比例縮放。
4. **透明度**：
    - `set_opacity(opacity)`：設置透明度（0~1）。



### 4. 操作與動畫效果

#### 添加對象的動畫
```python=
self.play(Create(circle))  # 以動畫方式創建圓形
```

#### 修改對象的動畫
```python=
self.play(square.animate.set_fill(GREEN, opacity=0.7))  # 動態改變填充
```

#### 移動對象的動畫
```python=
self.play(circle.animate.shift(RIGHT * 2))  # 圓形向右移動 2 單位
```


### 5. 常見組合操作

#### 對象的組合與對齊
- **組合對象 (VGroup)**：
    ```python=
    group = VGroup(circle, square)  # 將圓形和方形組合為一組
    group.arrange(RIGHT)  # 水平排列
    ```

- **對齊對象**：
    - `align_to(obj, direction)`：將對象對齊到某方向。
    - `next_to(obj, direction)`：將對象放置在另一對象旁邊。

---

### 6. 單元練習

**練習目標**：通過創建場景，掌握基本對象與動畫效果。  
**練習內容**：
1. 繪製一個藍色圓形和一個紅色方形，並讓它們從畫布兩側移動到畫布中心。
    ```python=
    from manim import *

    class PracticeScene(Scene):
        def construct(self):
            circle = Circle().set_color(BLUE).shift(LEFT * 3)
            square = Square().set_color(RED).shift(RIGHT * 3)
            self.play(circle.animate.move_to(ORIGIN), square.animate.move_to(ORIGIN))
            self.wait(1)
    ```
2. 嘗試將圓形和方形組合，並讓它們一起旋轉。
    ```python=
    group = VGroup(circle, square)
    self.play(Rotate(group, angle=PI/2))
    ```


### 7. 小結
- Manim 提供多種基本對象，易於定制與操作。
- 動畫方法（如 `play` 和 `animate`）讓對象的動態展示更簡單。
- 學習對象的屬性與動畫操作，是進一步學習 Manim 的基礎。


## 第三單元：動畫效果與過渡


### 1. 單元目標
- 學習如何讓對象以動畫方式呈現。
- 掌握基本動畫類型和過渡效果的應用。
- 理解如何組合與控制多個動畫的執行順序。


### 2. 動畫的基本概念

**什麼是動畫？**
- 動畫是對對象進行動態改變的過程，包括顯示、移動、縮放、旋轉等操作。

**執行動畫的方法：**
- 使用 `self.play(animation)` 指令。
- 動畫類型決定了對象的動態行為。


### 3. 常用動畫類型

#### 3.1 對象創建動畫
- **Create**: 逐步顯示對象的輪廓。
    ```python=
    self.play(Create(Circle()))
    ```

- **FadeIn/FadeOut**: 淡入或淡出對象。
    ```python=
    self.play(FadeIn(Square()))
    self.play(FadeOut(Square()))
    ```

- **Write**: 逐步顯示文字或公式。
    ```python=
    text = Text("Hello, Manim!")
    self.play(Write(text))
    ```


#### 3.2 對象變換動畫
- **Transform**: 將一個對象變換為另一個對象。
    ```python=
    square = Square()
    circle = Circle()
    self.play(Transform(square, circle))
    ```

- **ReplacementTransform**: 替換一個對象為另一個對象（更高效）。
    ```python=
    self.play(ReplacementTransform(square, circle))
    ```


#### 3.3 對象移動動畫
- **Shift**: 移動對象一段距離。
    ```python=
    self.play(circle.animate.shift(UP))
    ```

- **MoveTo**: 將對象移動到特定位置。
    ```python=
    self.play(square.animate.move_to(RIGHT * 2))
    ```

#### 3.4 對象旋轉與縮放動畫
- **Rotate**: 旋轉對象一定角度。
    ```python=
    self.play(Rotate(square, angle=PI/4))
    ```

- **Scale**: 按比例縮放對象。
    ```python=
    self.play(square.animate.scale(1.5))
    ```

### 4. 組合動畫與控制

#### 4.1 同步執行動畫
- **AnimationGroup**: 同步執行多個動畫。
    ```python=
    self.play(AnimationGroup(Create(circle), FadeIn(square)))
    ```

- **LaggedStart**: 多個動畫以延遲的方式依次開始。
    ```python=
    self.play(LaggedStart(Create(circle), Create(square)))
    ```

#### 4.2 動畫的延遲與運行時間
- 使用 `run_time` 控制動畫的持續時間。
    ```python=
    self.play(Create(circle), run_time=2)
    ```

- 使用 `rate_func` 控制動畫的速度曲線。
    ```python=
    self.play(Create(circle), rate_func=there_and_back)
    ```

### 5. 過渡效果

#### Scene 的切換過渡
- 使用 `self.next_section()` 來組織場景片段。

- **FadeTransition**: 淡入淡出過渡。
    ```python=
    self.play(FadeOut(square), FadeIn(circle))
    ```

- **SlideTransition**: 滑動過渡。
    ```python=
    self.play(Transform(square, circle))
    ```


### 6. 單元練習

**練習目標**：熟悉不同動畫效果與過渡的應用。

#### 練習內容
1. 創建一個圓形，讓它以動畫方式顯示，然後移動到畫布右上角：
    ```python=
    from manim import *

    class PracticeAnimation(Scene):
        def construct(self):
            circle = Circle()
            self.play(Create(circle))
            self.play(circle.animate.move_to(UP + RIGHT))
            self.wait(1)
    ```

2. 創建一個方形，並讓它逐漸旋轉與縮放：
    ```python=
    square = Square()
    self.play(Rotate(square, angle=2*PI))
    self.play(square.animate.scale(0.5))
    ```

3. 嘗試使用 `LaggedStart`，讓三個對象依次淡入：
    ```python=
    square = Square().shift(LEFT)
    circle = Circle().next_to(square,direction=RIGHT)
    triangle = Triangle().next_to(circle,direction=RIGHT)
    self.play(LaggedStart(FadeIn(square), FadeIn(circle), FadeIn(triangle)))
    ```



### 7. 小結
- Manim 提供了多種動畫類型，讓對象以不同方式呈現。
- 動畫的組合與時間控制可以創造流暢的過渡效果。
- 掌握動畫操作是設計複雜場景的基礎。

--- 
## 第四單元：文字與公式渲染
### 1. 單元目標
* 學習如何在 Manim 中添加與樣式化文字。
* 掌握數學公式的渲染與格式化技巧。
* 熟悉文字與公式的組合排版及動畫展示方法。
### 2. 添加文字
>基本文字對象
#### 使用 Text 類創建常規文字：
```python=
    from manim import *

    class TextExample(Scene):
    def construct(self):
        text = Text("Hello, Manim!")  # 創建文字對象
        self.add(text)  # 添加到場景中
        self.wait(1)
```
#### 文字樣式設置
##### 1.大小與顏色：
```python=  
text = Text("Styled Text", font_size=48, color=BLUE)
```
##### 2.字體選擇：    
```python=
text = Text("Custom Font", font="Times New Roman")
```
##### 3.文字對齊與排列：
- 水平對齊
```python=
text.align_to(LEFT)
```

- 排列多段文字
```python= 
text_group = VGroup(
    Text("Line 1"),
    Text("Line 2"),
    Text("Line 3")
).arrange(DOWN)  # 垂直排列

```

#### 文字樣式設置
##### 1.淡入與淡出：

```python=
self.play(FadeIn(text))
self.play(FadeOut(text))
```
##### 2.移動與縮放：
```python=
self.play(text.animate.shift(UP).scale(1.5))
```

### 3. 添加公式
> 基礎公式渲染

#### 使用 MathTex 類創建公式：
```python=
formula = MathTex("E = mc^2")
self.add(formula)

```

>多行公式渲染
#### 創建並排列多行公式：
```python=
multiline_formula = MathTex(
    "a^2 + b^2 = c^2",
    "\\sin^2\\theta + \\cos^2\\theta = 1"
).arrange(DOWN)  # 垂直排列
self.add(multiline_formula)

```
>公式樣式設置
##### 1.部分公式著色：
```python=
        formula = MathTex("E", "=", "mc^2")  # 將公式分成幾個部分
        self.add(formula)
        self.wait(1)
        formula.set_color_by_tex("mc^2", RED)  # 將 "mc^2" 設為紅色
        self.wait(1)
```
##### 2.大小調整：
```python=
formula.scale(1.5)  # 放大公式
```

### 4. 組合文字與公式
>文字與公式整合
#### 將文字與公式組合排列：
```python=
text_formula = VGroup(
    Text("The famous equation:"),
    MathTex("E = mc^2")
).arrange(DOWN)  # 垂直排列
self.add(text_formula)
```
>動畫應用
#### 同步動畫：
```python=
self.play(FadeIn(text_formula))
```
#### 分步動畫：
```python =
self.play(text_formula[0].animate.shift(LEFT))
self.play(text_formula[1].animate.shift(RIGHT))

```

### 5. 單元練習
**練習目標**:透過練習，熟悉文字與公式的基本操作以及動畫效果。
#### 練習內容
1. 創建文字與公式，讓其分別淡入並排列：
```python=
class PracticeTextFormula(Scene):
    def construct(self):
        text = Text("This is a formula:")
        formula = MathTex("a^2 + b^2 = c^2")
        group = VGroup(text, formula).arrange(DOWN)
        self.play(FadeIn(group))
        self.wait(1)

``` 
2. 突出公式中的關鍵部分：
```python=
formula = MathTex("a^2" , "+", "b^2" , "=", "c^2")
self.play(Write(formula[:2]))  # 顯示 "a^2 +"
self.play(Write(formula[2:4]))  # 顯示 "b^2 ="
self.play(Write(formula[4:]))  # 顯示 "c^2"
self.wait(1)
```

### 6.小結
* Manim 提供了靈活的文字與公式操作功能。
* 透過樣式設置與動畫效果，文字與公式可以變得更加生動。
* 熟悉這些操作是製作數學動畫的基礎技能。

---
## 第五單元：進階圖形與數據可視化
### 1.單元目標
* 掌握如何創建與操作進階圖形對象，例如曲線、圖表與自訂圖形。
* 學習如何將數據轉化為可視化的圖形。
* 理解如何使用動畫強調數據特徵，提升視覺效果。

### 2.創建進階圖形
>參數曲線
#### 基本曲線繪製：
```python=
from manim import *

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

```
* 調整曲線參數：
    * 變 t_range 控制曲線範圍。
    * 使用 stroke_width 調整線條粗細。

#### 極座標圖形:
* 使用 PolarPlane：
```python=
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

```
#### 自訂圖形
* 使用 VMobject 自訂繪製圖形:
```python=
class CustomShape(Scene):
    def construct(self):
        shape = VMobject()
        shape.set_points_as_corners([UP, RIGHT, DOWN, LEFT, UP])
        shape.set_color(YELLOW)
        self.add(shape)
```

### 3. 數據可視化
#### 條形圖
* 創建基本條形圖：
```python=
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
```
* 更新圖表數據：
```python=
self.play(chart.animate.change_bar_values([4, 6, 5, 7]))
```
#### 折線圖
* 創建基本折線圖：
```python=
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
```
* 更新圖表數據：
```python=
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
```

### 4.圖形與數據結合
>圖形強調與數據結合
#### 1.強調數據特徵：
##### 使用顏色區分：
```python=
bar = BarChart(
    values=[1, 2, 3, 4, 5],
    bar_names=["A", "B", "C", "D", "E"],
    y_range=[0, 6, 1],  # y軸範圍：[最小值, 最大值, 步長]
    bar_colors =[RED,RED,BLUE,BLUE,BLUE]  # 直接設置顏色
)
```
#### 2.動畫引導觀察重點：
##### 突出展示最大值：
```python=
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
self.play(max_value_bar.animate.set_color(RED).scale(1.2))
self.play(max_value_bar.animate.set_color(BLUE).scale(1/1.2))
self.wait(1)
```

### 5.單元練習
#### 練習目標:將所學的圖形與數據可視化知識應用到實際案例中。
#### 練習內容
##### 1.創建一個條形圖並實現隨機更新動畫：
```python=
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

```
        
##### 2.結合條形圖與數據標籤展示數據特徵：
```python=
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
        self.wait(1)
```
### 6.小結
* 學會如何創建進階圖形並結合數據展示。
* 熟悉使用動畫強調數據特徵。
* 圖形與數據結合是數據科學與教學演示中的重要技能。
 

---
## 第六單元：進階場景與相機控制
### 1.單元目標
* 學習如何操作 Manim 的相機，進行平移、縮放與旋轉。
* 掌握場景切換與多場景結合的技巧。
* 理解如何使用 3D 相機與場景創建立體效果。


### 2. 2D相機操作
#### 基礎相機操作
##### 1.移動相機
```python=
class CameraMoveExample1(MovingCameraScene):
    def construct(self):
        square = Square(color=BLUE)
        self.add(square)
        self.play(self.camera.frame.animate.move_to(LEFT * 3))
        self.wait(1)
```
##### 2.縮放
```python=
class CameraMoveExample2(MovingCameraScene):
    def construct(self):
        square = Square(color=BLUE)
        self.add(square)
        # 縮小相機（放大場景）
        self.play(self.camera.frame.animate.scale(0.5), run_time=2)
        self.wait(1)
        # 放大相機（縮小場景）
        self.play(self.camera.frame.animate.scale(2), run_time=2)
        self.wait(1)
```
### 3. 3D相機操作
#### 基礎相機操作
##### 1.移動相機：
```python=
class MoveCamera(ThreeDScene):  # 改用 ThreeDScene
    def construct(self):
        self.add(Cube())
        # 移動相機
        self.move_camera(phi=45 * DEGREES)  # 上下角度 控制相機的俯仰角（上下視角）。
        self.move_camera(theta=45 * DEGREES)  # 左右角度 控制相機的方位角（左右視角）。
        self.move_camera(gamma=90 * DEGREES)  # 控制相機的滾轉角（旋轉視角）。
        self.wait(1)
```
##### 2.縮放
```python=
class ZoomCamera(ThreeDScene):
    def construct(self):
        self.add(Cube())
        self.move_camera(phi=45 * DEGREES)  # 上下角度
        self.move_camera(zoom=0.5)  # 縮放
        self.wait(1)
```
### 4.添加 3D 對象
#### 創建3D對象並顯示:
```python=
class ExampleLine3D(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        line = Line3D(start=np.array([0, 0, 0]), end=np.array([2, 2, 3]))
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
        self.add(axes, line)
```
#### 使用相機環繞動畫：
```python=
class Sphere1(ThreeDScene):
    def construct(self):
        sphere = Sphere(radius=1, color=BLUE)
        self.add(sphere)
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
        self.begin_ambient_camera_rotation(rate=1)  # 開始自動旋轉
        self.wait(5)
        self.stop_ambient_camera_rotation()  # 停止旋轉
```

### 5.綜合案例
#### 案例 1：相機平移與動畫結合
```python=
class CameraPanExample(MovingCameraScene):
    def construct(self):
        square = Square(color=BLUE).shift(LEFT * 3)
        circle = Circle(color=RED).shift(RIGHT * 3)

        self.add(square, circle)
        self.play(self.camera.frame.animate.move_to(square))  # 相機移動到方形
        self.play(FadeIn(square))
        self.play(self.camera.frame.animate.move_to(circle))  # 相機移動到圓形
        self.play(FadeIn(circle))
```
#### 案例 2：3D 相機與對象展示
```python=
class ThreeDSceneExample(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        sphere = Sphere(radius=1, color=BLUE).move_to(UP * 2)

        self.add(axes, sphere)
        self.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES)
        self.play(Create(sphere))
        self.begin_ambient_camera_rotation(rate=1)  # 相機順時針自動旋轉
        self.wait(3)
        self.stop_ambient_camera_rotation()
        self.begin_ambient_camera_rotation(rate=-1)  # 相機逆時針自動旋轉
        self.wait(3)
        self.stop_ambient_camera_rotation()
        self.begin_ambient_camera_rotation(rate=1,about="gamma")  # 相機自動旋轉
        self.wait(3)
        self.stop_ambient_camera_rotation()
```
### 6. 單元練習
#### 練習目標
* 熟悉相機的基本與進階控制操作。
* 能靈活應用相機於多場景切換與 3D 展示。
#### 練習內容
##### 1. 相機平移與縮放：
* 創建一個圖形，並讓相機平滑地移動到不同位置。
```python=
class CameraZoomPractice(Scene):
    def construct(self):
        square = Square(color=BLUE).shift(LEFT * 3)
        self.add(square)
        self.play(self.camera.frame.animate.move_to(square).scale(0.5))
        self.wait(1)
```
##### 2.3D 場景探索：
* 創建一個立方體和球體，並讓相機在它們周圍旋轉：
```python=
class Rotate3DScene(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        cube = Cube(side_length=2).shift(LEFT*2)
        sphere = Sphere(radius=1.5).shift(RIGHT*3)

        self.add(axes, cube, sphere)
        self.
        self.begin_ambient_camera_rotation(rate=1)
        self.wait(3)
        self.stop_ambient_camera_rotation()
```

### 7. 小結
* 熟悉相機控制是提升場景表現力的核心技能。
* 3D 相機操作與場景切換拓展了動畫製作的可能性。
* 通過多場景展示，可以組織更清晰的教學內容。

---
## 第七單元：自訂類與模組化
### 1.單元目標
* 學會如何通過 Python 類來擴展 Manim 的功能。
* 理解如何模組化場景和動畫代碼，提升程式的可讀性與重用性。
* 能夠創建自訂的動畫效果與復雜的場景結構。

### 2.自訂類基礎
:::info 
**什麼是自訂類？**
自訂類允許我們：
* 封裝重複邏輯：將常用功能打包成獨立的類。
* 擴展功能：添加 Manim 原生物件沒有的特性。
* 提高代碼的組織性：簡化主場景文件的結構。
:::

#### 自訂類基本結構
##### 1.創建一個自訂類：
```python=
from manim import *

class CustomShape(VMobject):
    def __init__(self, color=BLUE, **kwargs):
        super().__init__(**kwargs)
        self.set_points_as_corners([UP, RIGHT, DOWN, LEFT, UP])
        self.set_color(color)
```
##### 2. 在場景中使用自訂類：
```python=
class CustomShapeScene(Scene):
    def construct(self):
        shape = CustomShape(color=YELLOW)
        self.play(Create(shape))
        self.wait(1)
```

#### 封裝自訂動畫
##### 1.自訂動畫方法：
```python=
class RotatingSquare(VGroup):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        square = Square(color=BLUE)
        self.add(square)
    ##翻轉
    def rotate_with_animation(self, scene):
        scene.play(self.animate.rotate(PI / 2))
```

##### 2.場景中使用動畫：
```python=
class AnimationExample(Scene):
    def construct(self):
        rotating_square = RotatingSquare()
        self.add(rotating_square)
        rotating_square.rotate_with_animation(self)
        self.wait(1)
```

### 3. 模組化代碼結構
:::info
**為什麼需要模組化？**
* 提升代碼重用性：將常用功能放入獨立模組中，方便調用。
* 降低場景文件的複雜度：將動畫邏輯分離到單獨文件或類中。
* 促進團隊協作：清晰的代碼結構便於多人維護。
:::

#### 模組化範例
##### 1.文件結構：
```bash=
project/
├── main.py         # 主場景文件
├── shapes.py       # 自訂圖形模組
└── animations.py   # 自訂動畫模組
```
##### 2.shapes.py 文件內容：
```python=
from manim import *

class CustomCircle(VMobject):
    def __init__(self, radius=1, color=BLUE, **kwargs):
        super().__init__(**kwargs)
        circle = Circle(radius=radius, color=color)
        self.add(circle)
```

##### 3.animations.py 文件內容：
```python=
from manim import *

class CustomCircle(VMobject):
    def __init__(self, radius=1, color=BLUE, **kwargs):
        super().__init__(**kwargs)
        circle = Circle(radius=radius, color=color)
        self.add(circle)
```

##### 4.main.py 文件內容：
```python=
from manim import *
from shapes import CustomCircle
from animations import bounce_animation

class ModularScene(Scene):
    def construct(self):
        circle = CustomCircle(radius=2, color=YELLOW)
        self.add(circle)
        bounce_animation(circle, self)
        self.wait(1)
```
### 4. 自訂模組與外部資源
#### 將自訂模組封裝成外部庫
##### 1.創建 Python 套件結構：
```bash=
mylibrary/
├── __init__.py      # 初始化模組
├── shapes.py        # 圖形模組
├── animations.py    # 動畫模組
├── setup.py         # 設定模組

``` 
##### 2. __ init __.py 文件內容：
```python=
from .shapes import CustomCircle
from .animations import bounce_animation
```

##### 3. setup.py 文件內容：
```python=
from setuptools import setup, find_packages

setup(
    name='mylibrary',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        # 在這裡添加你的依賴項，例如 'numpy', 'requests' 等
    ],
    author='Your Name',
    author_email='your.email@example.com',
    description='A brief description of your library',
    url='https://github.com/yourusername/mylibrary',  # 項目的主頁
)
```
##### 4.安裝自訂模組： 在項目中安裝自訂模組：
```bash=
pip install -e mylibrary/
```

##### 5.在場景中使用：
```python=
from mylibrary import CustomCircle, bounce_animation

class ModularExample(Scene):
    def construct(self):
        circle = CustomCircle(color=GREEN)
        self.add(circle)
        bounce_animation(circle, self)
        self.wait(1)
```

### 5.單元練習
#### 練習目標
* 能夠創建自訂類並封裝功能。
* 熟悉將代碼模組化，提升項目結構的清晰度。

#### 練習內容
* 自訂圖形類： 創建一個 CustomArrow 類，並能動態改變箭頭方向與顏色。
* 模組化動畫： 創建一個模組化的彈跳動畫，並將其應用於多個物件。
* 外部模組結構： 建立一個外部庫，封裝自己的自訂圖形與動畫。

### 6.小結
* 自訂類與模組化是實現復雜動畫的關鍵工具。
* 將代碼結構化可以提高項目可讀性與重用性。
* 自訂功能與模組化相結合，能夠應對更大規模的動畫需求。

## 資源與參考
- [官方網站](https://www.manim.community/)
- [中文教材](https://docs.manim.org.cn/)
- [中文教材(版本較舊)](https://github.com/cai-hust/manim-tutorial-CN)
- [英文YT簡介](https://www.youtube.com/watch?v=ENMyFGmq5OA&t=6s&ab_channel=TheoremofBeethoven)
- [中文YT簡介](https://www.youtube.com/watch?v=6xxu51H7b_8&ab_channel=geeker)
- [開發者YT頻道](https://www.youtube.com/@3blue1brown)