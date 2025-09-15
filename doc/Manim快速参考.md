# Manim 快速参考手册

## 🚀 快速开始

### 基本模板
```python
from manim import *

class MyScene(Scene):
    def construct(self):
        # 创建对象
        circle = Circle(radius=1, color=BLUE)
        
        # 播放动画
        self.play(Create(circle))
        self.wait(1)
```

### 运行命令
```bash
manim -pql filename.py SceneName
```

---

## 📐 基本形状

### 2D形状
```python
# 圆形
Circle(radius=1, color=BLUE, fill_opacity=0.5)

# 正方形
Square(side_length=2, color=GREEN)

# 三角形
Triangle(color=RED)

# 多边形
Polygon([-1, -1, 0], [1, -1, 0], [0, 1, 0], color=YELLOW)

# 点
Dot(point=[1, 1, 0], color=ORANGE)

# 线段
Line(start=[-1, -1, 0], end=[1, 1, 0], color=PURPLE)

# 箭头
Arrow(start=[-1, 0, 0], end=[1, 0, 0], color=BLUE)
```

### 3D形状
```python
# 球体
Sphere(radius=0.5, color=BLUE)

# 立方体
Cube(side_length=1, color=RED)

# 圆柱体
Cylinder(radius=0.3, height=1.5, color=GREEN)
```

---

## 🎬 动画效果

### 基础动画
```python
# 创建
self.play(Create(mobject))

# 淡入淡出
self.play(FadeIn(mobject))
self.play(FadeOut(mobject))

# 写入（适合文本）
self.play(Write(text))

# 变换
self.play(Transform(mobject1, mobject2))
```

### 变换动画
```python
# 移动
mobject.animate.shift(UP * 2)
mobject.animate.shift(RIGHT * 3)
mobject.animate.shift(DOWN * 1)
mobject.animate.shift(LEFT * 2)

# 缩放
mobject.animate.scale(1.5)    # 放大
mobject.animate.scale(0.5)    # 缩小

# 旋转
mobject.animate.rotate(PI/2)  # 旋转90度
mobject.animate.rotate(PI)    # 旋转180度

# 组合变换
mobject.animate.shift(UP).scale(0.5).rotate(PI/4)
```

### 高级动画
```python
# 路径动画
self.play(MoveAlongPath(mobject, path))

# 旋转动画
self.play(Rotate(mobject, angle=PI, axis=UP))

# 闪烁效果
self.play(Flash(mobject, color=YELLOW))
```

---

## 📊 坐标系与函数

### 创建坐标系
```python
# 2D坐标系
axes = Axes(
    x_range=[-3, 3, 1],
    y_range=[-1, 5, 1],
    axis_config={"color": GREY},
    tips=False
)

# 3D坐标系
axes_3d = ThreeDAxes()
```

### 绘制函数
```python
# 函数图像
parabola = axes.plot(lambda x: x**2, color=BLUE)
sine = axes.plot(lambda x: np.sin(x), color=RED)

# 隐函数
circle = axes.plot_implicit_curve(
    lambda x, y: x**2 + y**2 - 9, color=GREEN
)
```

### 坐标转换
```python
# 数学坐标 → 屏幕坐标
point = axes.coords_to_point(2, 4)

# 屏幕坐标 → 数学坐标
coords = axes.point_to_coords(point)
```

---

## 📝 文本与公式

### 普通文本
```python
# 英文文本
text = Text("Hello Manim", font_size=36)

# 中文文本
chinese_text = Text("数学动画", font="PingFang SC", font_size=40)

# 数学公式（简单）
formula = Text("x² + y² = r²", font="PingFang SC", font_size=48)
```

### 文本定位
```python
# 相对定位
text.next_to(mobject, RIGHT, buff=0.5)
text.next_to(mobject, UP, buff=1)

# 绝对定位
text.move_to(ORIGIN)
text.to_corner(UP+LEFT)
text.to_corner(DOWN+RIGHT)
```

---

## 🎯 对象定位

### 方向向量
```python
# 基本方向
UP, DOWN, LEFT, RIGHT

# 组合方向
UP+LEFT, UP+RIGHT, DOWN+LEFT, DOWN+RIGHT

# 3D方向
OUT, IN  # 屏幕外/内
```

### 定位方法
```python
# 移动到指定位置
mobject.move_to([x, y, z])
mobject.move_to(ORIGIN)

# 移动到角落
mobject.to_corner(UP+LEFT)
mobject.to_corner(DOWN+RIGHT)

# 相对于其他对象定位
mobject.next_to(other_mobject, RIGHT, buff=0.5)
mobject.next_to(other_mobject, UP, buff=1)
```

---

## 🔄 动态更新

### ValueTracker
```python
# 创建数值跟踪器
k_tracker = ValueTracker(0)

# 获取当前值
k = k_tracker.get_value()

# 设置新值
k_tracker.set_value(2)

# 动画数值变化
self.play(k_tracker.animate.set_value(5), run_time=2)
```

### 更新器
```python
# 定义更新函数
def update_mobject(mob):
    k = k_tracker.get_value()
    new_mob = create_mobject_with_k(k)
    mob.become(new_mob)

# 添加更新器
mobject.add_updater(update_mobject)

# 移除更新器
mobject.remove_updater(update_mobject)
```

### 基于Alpha的更新
```python
def update_function(mob, alpha):
    # alpha从0到1变化
    angle = alpha * 2 * PI
    x = 3 * np.cos(angle)
    y = 3 * np.sin(angle)
    mob.move_to(axes.coords_to_point(x, y))

# 使用UpdateFromAlphaFunc
self.play(
    UpdateFromAlphaFunc(mobject, update_function),
    run_time=4,
    rate_func=linear
)
```

---

## 🎨 颜色与样式

### 内置颜色
```python
# 基本颜色
RED, GREEN, BLUE, YELLOW, ORANGE, PURPLE, PINK, GRAY, WHITE, BLACK

# 深浅变化
RED_A, RED_B, RED_C, RED_D, RED_E
BLUE_A, BLUE_B, BLUE_C, BLUE_D, BLUE_E

# 特殊颜色
GOLD, MAROON, TEAL, LIGHT_BLUE, DARK_BLUE
```

### 样式属性
```python
# 颜色
mobject.set_color(RED)
mobject.set_fill(BLUE, opacity=0.5)
mobject.set_stroke(RED, width=3)

# 透明度
mobject.set_fill(opacity=0.3)
mobject.set_stroke(opacity=0.7)

# 边框
mobject.set_stroke(width=2)
mobject.set_stroke(color=RED, width=3)
```

---

## 🎭 对象组合

### VGroup
```python
# 创建对象组
group = VGroup(circle, square, triangle)

# 排列
group.arrange(RIGHT, buff=0.5)  # 水平排列
group.arrange(DOWN, buff=1)     # 垂直排列

# 组操作
group.shift(UP * 2)
group.scale(1.5)
group.rotate(PI/4)

# 组动画
self.play(group.animate.shift(UP * 2))
```

---

## 🎥 3D场景

### 3D场景基础
```python
class My3DScene(ThreeDScene):
    def construct(self):
        # 设置相机角度
        self.set_camera_orientation(phi=75*DEGREES, theta=30*DEGREES)
        
        # 创建3D对象
        sphere = Sphere(radius=0.5, color=BLUE)
        
        # 3D动画
        self.play(Create(sphere))
```

### 相机控制
```python
# 设置初始角度
self.set_camera_orientation(phi=45*DEGREES, theta=60*DEGREES)

# 动态改变角度
self.move_camera(phi=30*DEGREES, theta=90*DEGREES, run_time=2)
```

### 3D变换
```python
# 3D移动
mobject.shift(OUT * 2)  # 向屏幕外
mobject.shift(IN * 1)   # 向屏幕内

# 3D旋转
mobject.rotate(PI/2, axis=X_AXIS)  # 绕X轴
mobject.rotate(PI/2, axis=Y_AXIS)  # 绕Y轴
mobject.rotate(PI/2, axis=Z_AXIS)  # 绕Z轴
```

---

## ⚙️ 渲染命令

### 基本命令
```bash
# 低质量快速预览
manim -pql filename.py SceneName

# 中质量平衡
manim -pqm filename.py SceneName

# 高质量最终输出
manim -pqh filename.py SceneName

# 4K超高质量
manim -pqk filename.py SceneName
```

### 参数说明
```bash
-p    # 渲染完成后自动播放
-q    # 质量设置
  l   # 低质量 (480p) - 快速调试
  m   # 中质量 (720p) - 平衡质量与速度
  h   # 高质量 (1080p) - 最终输出
  k   # 4K质量 (2160p) - 超高质量
```

### 输出格式
```bash
# MP4视频（默认）
manim -pqm filename.py SceneName

# GIF动画
manim -pqm --format=gif filename.py SceneName

# PNG图片序列
manim -pqm --format=png filename.py SceneName
```

---

## 🐛 常见问题

### LaTeX问题
```python
# 问题：RuntimeError: latex failed
# 解决：使用Text替代MathTex
text = Text("x² + y² = r²", font="PingFang SC")
```

### 中文字体问题
```python
# 问题：中文显示为方块
# 解决：指定中文字体
text = Text("中文文本", font="PingFang SC")  # macOS
text = Text("中文文本", font="SimHei")      # Windows
```

### 性能问题
```bash
# 问题：渲染速度慢
# 解决：使用低质量预览
manim -pql filename.py SceneName
```

---

## 📚 学习案例

| 文件名 | 学习重点 | 难度 |
|--------|----------|------|
| `basic_shapes.py` | 基本形状、基础动画 | ⭐ |
| `text_and_formulas.py` | 文本处理、公式显示 | ⭐ |
| `coordinate_systems.py` | 坐标系、函数绘制 | ⭐⭐ |
| `pythagorean_theorem.py` | 数学可视化、对象定位 | ⭐⭐ |
| `circle_distance_problem.py` | 动态更新、数学计算 | ⭐⭐⭐ |
| `line_parabola_intersection.py` | ValueTracker、更新器 | ⭐⭐⭐ |
| `ellipse_tangent_problem.py` | 隐函数、切线计算 | ⭐⭐⭐⭐ |
| `advanced_3d_scene.py` | 3D对象、相机控制 | ⭐⭐⭐⭐ |

---

## 💡 学习建议

### 学习顺序
1. **基础阶段**：basic_shapes → text_and_formulas → coordinate_systems
2. **进阶阶段**：pythagorean_theorem → circle_distance_problem
3. **高级阶段**：line_parabola_intersection → ellipse_tangent_problem → advanced_3d_scene

### 实践建议
- 每个案例都要亲自运行
- 尝试修改参数和代码
- 创建自己的动画项目
- 参与社区讨论

---

## 🔗 有用链接

- [Manim官方文档](https://docs.manim.community/)
- [Manim GitHub](https://github.com/ManimCommunity/manim)
- [3Blue1Brown YouTube](https://www.youtube.com/c/3blue1brown)
- [Manim Discord社区](https://discord.gg/mMRrZQW)

---

*快速参考手册 - 随时查阅，快速上手！* 🚀
