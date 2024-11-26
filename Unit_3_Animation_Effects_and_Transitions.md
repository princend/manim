
# 第三單元：動畫效果與過渡

---

## 1. 單元目標
- 學習如何讓對象以動畫方式呈現。
- 掌握基本動畫類型和過渡效果的應用。
- 理解如何組合與控制多個動畫的執行順序。

---

## 2. 動畫的基本概念

**什麼是動畫？**
- 動畫是對對象進行動態改變的過程，包括顯示、移動、縮放、旋轉等操作。

**執行動畫的方法：**
- 使用 `self.play(animation)` 指令。
- 動畫類型決定了對象的動態行為。

---

## 3. 常用動畫類型

### 3.1 對象創建動畫
- **Create**: 逐步顯示對象的輪廓。
    ```python
    self.play(Create(Circle()))
    ```

- **FadeIn/FadeOut**: 淡入或淡出對象。
    ```python
    self.play(FadeIn(Square()))
    self.play(FadeOut(Square()))
    ```

- **Write**: 逐步顯示文字或公式。
    ```python
    text = Text("Hello, Manim!")
    self.play(Write(text))
    ```

---

### 3.2 對象變換動畫
- **Transform**: 將一個對象變換為另一個對象。
    ```python
    square = Square()
    circle = Circle()
    self.play(Transform(square, circle))
    ```

- **ReplacementTransform**: 替換一個對象為另一個對象（更高效）。
    ```python
    self.play(ReplacementTransform(square, circle))
    ```

---

### 3.3 對象移動動畫
- **Shift**: 移動對象一段距離。
    ```python
    self.play(circle.animate.shift(UP))
    ```

- **MoveTo**: 將對象移動到特定位置。
    ```python
    self.play(square.animate.move_to(RIGHT * 2))
    ```

---

### 3.4 對象旋轉與縮放動畫
- **Rotate**: 旋轉對象一定角度。
    ```python
    self.play(Rotate(square, angle=PI/4))
    ```

- **Scale**: 按比例縮放對象。
    ```python
    self.play(square.animate.scale(1.5))
    ```

---

## 4. 組合動畫與控制

### 4.1 同步執行動畫
- **AnimationGroup**: 同步執行多個動畫。
    ```python
    self.play(AnimationGroup(Create(circle), FadeIn(square)))
    ```

- **LaggedStart**: 多個動畫以延遲的方式依次開始。
    ```python
    self.play(LaggedStart(Create(circle), Create(square)))
    ```

### 4.2 動畫的延遲與運行時間
- 使用 `run_time` 控制動畫的持續時間。
    ```python
    self.play(Create(circle), run_time=2)
    ```

- 使用 `rate_func` 控制動畫的速度曲線。
    ```python
    self.play(Create(circle), rate_func=there_and_back)
    ```

---

## 5. 過渡效果

### Scene 的切換過渡
- 使用 `self.next_section()` 來組織場景片段。

- **FadeTransition**: 淡入淡出過渡。
    ```python
    self.play(FadeOut(square), FadeIn(circle))
    ```

- **SlideTransition**: 滑動過渡。
    ```python
    self.play(Transform(square, circle))
    ```

---

## 6. 單元練習

**練習目標**：熟悉不同動畫效果與過渡的應用。

### 練習內容
1. 創建一個圓形，讓它以動畫方式顯示，然後移動到畫布右上角：
    ```python
    from manim import *

    class PracticeAnimation(Scene):
        def construct(self):
            circle = Circle()
            self.play(Create(circle))
            self.play(circle.animate.move_to(UP + RIGHT))
            self.wait(1)
    ```

2. 創建一個方形，並讓它逐漸旋轉與縮放：
    ```python
    square = Square()
    self.play(Rotate(square, angle=PI), square.animate.scale(0.5))
    ```

3. 嘗試使用 `LaggedStart`，讓三個對象依次淡入：
    ```python
    square = Square().shift(LEFT)
    circle = Circle()
    triangle = Triangle().shift(RIGHT)
    self.play(LaggedStart(FadeIn(square), FadeIn(circle), FadeIn(triangle)))
    ```

---

## 7. 小結
- Manim 提供了多種動畫類型，讓對象以不同方式呈現。
- 動畫的組合與時間控制可以創造流暢的過渡效果。
- 掌握動畫操作是設計複雜場景的基礎。
