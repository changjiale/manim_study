from manim import *
import numpy as np
#案例 3：坐标系与函数可视化
class FunctionVisualization(Scene):
    def construct(self):
        # 创建坐标系
        axes = Axes(
            x_range=[-3, 3, 1],
            y_range=[-1, 5, 1],
            axis_config={"color": GREY},
            tips=False
        )
        
        # 获取坐标轴标签
        x_label = Text("x", font="PingFang SC").next_to(axes.x_axis.get_end(), RIGHT)
        y_label = Text("f(x)", font="PingFang SC").next_to(axes.y_axis.get_end(), UP)
        labels = VGroup(x_label, y_label)
        
        # 绘制函数图像
        parabola = axes.plot(lambda x: x**2, color=BLUE, x_range=[-2, 2])
        sine = axes.plot(lambda x: np.sin(x) + 2, color=RED)
        
        # 为函数添加标签
        parabola_label = Text("x²", font="PingFang SC").next_to(parabola, RIGHT)
        sine_label = Text("sin(x) + 2", font="PingFang SC").next_to(sine, RIGHT)
        
        # 动画序列
        self.play(Create(axes), Write(labels))
        self.wait(0.5)
        self.play(Create(parabola), Write(parabola_label))
        self.wait(1)
        self.play(Create(sine), Write(sine_label))
        self.wait(1)
        
        # 突出显示交点
        intersection = Dot(axes.coords_to_point(0, 0), color=YELLOW)
        self.play(Create(intersection), Flash(intersection, color=YELLOW))
        self.wait(2)

# 运行命令：manim -pql coordinate_systems.py FunctionVisualization

# ===================== 知识点解析 =====================
# 1. 坐标系创建
# - Axes()：创建坐标系
#   * x_range/y_range：设置坐标轴范围和刻度间隔，格式为[min, max, step]
#     - 示例：[0, 10, 2] 表示从0到10，每隔2个单位一个刻度
#   * axis_config：设置坐标轴样式（颜色、线宽等）
#   * tips：是否显示轴末端的箭头（True/False）
#   * 注意：避免使用numbers_to_include，因为会触发LaTeX依赖

# 2. 坐标轴标签（手动创建）
# - 由于get_axis_labels()有LaTeX依赖，这里手动创建标签
# - axes.x_axis.get_end()：获取x轴的终点位置
# - axes.y_axis.get_end()：获取y轴的终点位置
# - next_to(mobject, direction)：将标签放置在轴的末端

# 3. 函数绘制
# - axes.plot(function, color, x_range)：绘制函数图像
#   * function：函数表达式（可使用lambda表达式或已定义函数）
#     - 示例：lambda x: x**2 表示二次函数
#     - 示例：lambda x: np.sin(x) + 2 表示正弦函数向上平移2
#   * color：曲线颜色（BLUE, RED, GREEN等）
#   * x_range：指定函数绘制的x范围（可选）

# 4. 函数标签（手动创建）
# - 由于get_graph_label()有LaTeX依赖，这里手动创建标签
# - next_to(graph, direction)：将标签放置在函数图像旁边
# - 可以精确控制标签的位置和样式

# 5. 点与标记
# - Dot(point, color)：创建点对象
#   * point：点的坐标（使用axes.coords_to_point()转换）
#   * color：点的颜色
# - axes.coords_to_point(x, y)：将数学坐标(x,y)转换为Manim屏幕坐标
#   * 这是坐标系的核心功能，连接数学和视觉
# - Flash(mobject, color)：创建闪烁效果，突出显示重要元素
#   * 常用于强调关键点或重要概念
