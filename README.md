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
   :::
*    名稱來源：Mathematical Animation Engine
*    用途：
        * 繪製數學函數與公式動畫。
        * 建立教學視頻或學術展示。
        * 視覺化數據或程式流程。

### * Manim 的特點：    
    * 靈活性：透過 Python 程式控制動畫。
    * 高精度渲染：生成高畫質影片。
    * 支援 2D 與 3D 場景。

### 3. 安裝環境
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
### 4. 初次運行 Manim
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


### 5.單元練習
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
    - `shift(direction)`：按方向平移。
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
### 分步動畫：
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