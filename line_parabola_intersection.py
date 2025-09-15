from manim import *
import numpy as np
#案例 6：直线与抛物线交点轨迹问题
class LineParabolaIntersection(Scene):
    def construct(self):
        # 题目描述
        problem = Text("题目：已知抛物线y = x²，直线l: y = kx + 1，", font="PingFang SC")
        problem2 = Text("当k变化时，求直线l与抛物线交点的运动轨迹。", font="PingFang SC")
        VGroup(problem, problem2).arrange(DOWN, buff=0.5).to_corner(UP+LEFT)
        
        # 创建坐标系
        axes = Axes(
            x_range=[-3, 3, 1],
            y_range=[-1, 5, 1],
            axis_config={"color": GREY},
            tips=True
        )
        x_label = Text("x", font="PingFang SC").next_to(axes.x_axis.get_end(), RIGHT)
        y_label = Text("y", font="PingFang SC").next_to(axes.y_axis.get_end(), UP)
        labels = VGroup(x_label, y_label)
        
        # 绘制抛物线 y = x²
        parabola = axes.plot(lambda x: x**2, color=BLUE, x_range=[-2.5, 2.5])
        parabola_label = Text("y = x²", font="PingFang SC").next_to(parabola, RIGHT)
        
        # 初始直线 y = kx + 1 (k=0时)
        k = ValueTracker(0)  # 用于跟踪k值变化
        
        def get_line():
            """根据当前k值生成直线"""
            return axes.plot(
                lambda x: k.get_value() * x + 1,
                color=GREEN,
                x_range=[-2.5, 2.5]
            )
        
        line = get_line()
        line_label = Text("y = kx + 1", font="PingFang SC").next_to(line, LEFT)
        
        # 计算交点并创建交点对象
        def get_intersection_points():
            """计算直线与抛物线的交点"""
            k_val = k.get_value()
            # 解方程组: y = x² 和 y = kx + 1 → x² - kx - 1 = 0
            discriminant = k_val**2 + 4  # 判别式
            x1 = (k_val + np.sqrt(discriminant)) / 2
            x2 = (k_val - np.sqrt(discriminant)) / 2
            y1 = x1**2
            y2 = x2**2
            return [
                axes.coords_to_point(x1, y1),
                axes.coords_to_point(x2, y2)
            ]
        
        # 创建交点
        points = [Dot(point, color=RED) for point in get_intersection_points()]
        point_labels = [
            Text("P₁", font="PingFang SC").next_to(points[0], UP),
            Text("P₂", font="PingFang SC").next_to(points[1], UP)
        ]
        
        # k值显示
        k_display = Text("k = 0", font="PingFang SC").to_corner(UP+RIGHT)
        
        # 显示题目和坐标系
        self.play(Write(problem), Write(problem2))
        self.wait(2)
        self.play(Create(axes), Write(labels))
        self.wait(1)
        
        # 显示抛物线
        self.play(Create(parabola), Write(parabola_label))
        self.wait(2)
        
        # 显示初始直线和k值
        self.play(Create(line), Write(line_label), Write(k_display))
        self.wait(1)
        
        # 显示交点
        self.play(*[Create(p) for p in points], *[Write(l) for l in point_labels])
        self.wait(2)
        
        # 定义更新函数
        def update_line(line):
            new_line = get_line()
            line.become(new_line)
            return line
        
        def update_points(points):
            new_points = get_intersection_points()
            for i in range(2):
                points[i].move_to(new_points[i])
            return points
        
        def update_k_display(display):
            display.become(Text(f"k = {k.get_value():.1f}", font="PingFang SC").to_corner(UP+RIGHT))
            return display
        
        # 创建k值变化的动画（从-2到2）
        self.play(k.animate.set_value(2), run_time=6)
        self.play(k.animate.set_value(-2), run_time=12)
        self.play(k.animate.set_value(0), run_time=6)
        
        # 同步更新所有元素
        line.add_updater(update_line)
        points[0].add_updater(lambda p: p.move_to(get_intersection_points()[0]))
        points[1].add_updater(lambda p: p.move_to(get_intersection_points()[1]))
        k_display.add_updater(update_k_display)
        
        self.wait(2)
        
        # 显示结论
        conclusion = Text("结论：交点轨迹为抛物线 y = x² + 1", font="PingFang SC", color=RED)
        conclusion.to_corner(DOWN+RIGHT)
        self.play(Write(conclusion))
        
        # 绘制轨迹
        trajectory = axes.plot(lambda x: x**2 + 1, color=PURPLE, stroke_width=3)
        self.play(Create(trajectory))
        self.wait(3)

# 运行命令：manim -pqm line_parabola_intersection.py LineParabolaIntersection

# ===================== 知识点解析 =====================
# 1. 动态值跟踪（ValueTracker）
# - ValueTracker(initial_value)：跟踪一个数值的变化
#   * 这是Manim中实现参数化动画的核心工具
#   * get_value()：获取当前值
#   * set_value(new_value)：设置新值
#   * 配合animate可以创建平滑的数值变化动画
#   * 示例：k_tracker = ValueTracker(0) 跟踪斜率k的变化

# 2. 动态对象更新（add_updater）
# - add_updater(mobject, update_function)：为对象添加更新器
#   * 每次场景更新时自动调用更新函数
#   * 这是实现复杂动画的关键方法
#   * 注意：语法是 mobject.add_updater(update_function)
#   * 不是 self.add_updater(mobject, update_function)

# 3. 数学计算与动画结合
# - 在动画中嵌入数学计算，如求直线与抛物线的交点
# - 利用数学关系驱动动画对象的行为
# - 示例：根据k值计算直线方程，再求与抛物线的交点
# - 实时更新：每次k值变化时重新计算所有相关对象

# 4. 方程组求解与交点计算
# - 直线方程：y = kx + 1
# - 抛物线方程：y = x²
# - 联立求解：x² = kx + 1，即 x² - kx - 1 = 0
# - 使用求根公式计算交点坐标

# 5. 轨迹可视化
# - 可以先让点运动，再显示其运动轨迹
# - 使用不同颜色区分轨迹与原曲线
# - 轨迹方程：y = x² + 1（这是交点的运动轨迹）

# 6. 动画清理
# - 动画结束后使用remove_updater()移除更新器
# - 避免不必要的计算，提高性能
# - 示例：mobject.remove_updater(update_function)
