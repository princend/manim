
# 第二單元：基本對象與場景

---

## 1. 單元目標
- 學習如何建立 Manim 的基本場景。
- 掌握常用對象（如圓形、方形、線條等）的創建與操作。

---

## 2. 場景 (Scene) 的基本結構

**Scene 是 Manim 的核心單位，用來定義動畫的內容與順序。**

### Scene 的結構範例：
```python
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

## 3. 基本對象的創建與屬性調整

### 常用幾何對象
- **圓形 (Circle)**：
    ```python
    circle = Circle()  # 默認為單位圓
    circle.set_color(RED)  # 設置顏色為紅色
    ```

- **方形 (Square)**：
    ```python
    square = Square()  # 默認邊長為 2
    square.set_fill(BLUE, opacity=0.5)  # 填充藍色，透明度 50%
    ```

- **多邊形 (Polygon)**：
    ```python
    polygon = Polygon(
        [-1, 0, 0], [1, 0, 0], [0, 1, 0]
    )  # 創建一個三角形
    ```

### 基本對象的常用屬性
1. **顏色**：
    - `set_color(color)`：設置對象顏色。
2. **位置**：
    - `move_to(position)`：移動對象到指定位置。
    - `shift(direction)`：按方向平移。
3. **大小**：
    - `scale(factor)`：按比例縮放。
4. **透明度**：
    - `set_opacity(opacity)`：設置透明度（0~1）。

---

## 4. 操作與動畫效果

### 添加對象的動畫
```python
self.play(Create(circle))  # 以動畫方式創建圓形
```

### 修改對象的動畫
```python
self.play(square.animate.set_fill(GREEN, opacity=0.7))  # 動態改變填充
```

### 移動對象的動畫
```python
self.play(circle.animate.shift(RIGHT * 2))  # 圓形向右移動 2 單位
```

---

## 5. 常見組合操作

### 對象的組合與對齊
- **組合對象 (VGroup)**：
    ```python
    group = VGroup(circle, square)  # 將圓形和方形組合為一組
    group.arrange(RIGHT)  # 水平排列
    ```

- **對齊對象**：
    - `align_to(obj, direction)`：將對象對齊到某方向。
    - `next_to(obj, direction)`：將對象放置在另一對象旁邊。

---

## 6. 單元練習

**練習目標**：通過創建場景，掌握基本對象與動畫效果。  
**練習內容**：
1. 繪製一個藍色圓形和一個紅色方形，並讓它們從畫布兩側移動到畫布中心。
    ```python
    from manim import *

    class PracticeScene(Scene):
        def construct(self):
            circle = Circle().set_color(BLUE).shift(LEFT * 3)
            square = Square().set_color(RED).shift(RIGHT * 3)
            self.play(circle.animate.move_to(ORIGIN), square.animate.move_to(ORIGIN))
            self.wait(1)
    ```
2. 嘗試將圓形和方形組合，並讓它們一起旋轉。
    ```python
    group = VGroup(circle, square)
    self.play(Rotate(group, angle=PI/2))
    ```

---

## 7. 小結
- Manim 提供多種基本對象，易於定制與操作。
- 動畫方法（如 `play` 和 `animate`）讓對象的動態展示更簡單。
- 學習對象的屬性與動畫操作，是進一步學習 Manim 的基礎。
