from manim import *
import numpy as np
#案例 5：圆上动点与定点距离问题
class CircleDistanceProblem(Scene):
    def construct(self):
        # 题目描述
        problem = Text("题目：已知圆O：x² + y² = 9，点A(5, 0)，", font="PingFang SC", font_size=24)
        problem2 = Text("点P是圆O上的动点，求PA的最大值和最小值。", font="PingFang SC", font_size=24)
        VGroup(problem, problem2).arrange(DOWN, buff=0.5).to_corner(UP+LEFT)
        
        # 创建坐标系
        axes = Axes(
            x_range=[-6, 6, 1],
            y_range=[-6, 6, 1],
            axis_config={"color": GREY},
            tips=True
        )
        x_label = Text("x", font="PingFang SC").next_to(axes.x_axis.get_end(), RIGHT)
        y_label = Text("y", font="PingFang SC").next_to(axes.y_axis.get_end(), UP)
        labels = VGroup(x_label, y_label)
        
        # 绘制圆O: x² + y² = 9 (半径3，圆心在原点)
        circle = axes.plot_implicit_curve(
            lambda x, y: x**2 + y**2 - 9,
            color=BLUE
        )
        circle_label = Text("x² + y² = 9", font="PingFang SC").next_to(circle, RIGHT)
        
        # 定点A(5,0)
        point_a = Dot(axes.coords_to_point(5, 0), color=RED)
        label_a = Text("A(5,0)", font="PingFang SC").next_to(point_a, UP)
        
        # 圆心O
        center_o = Dot(axes.coords_to_point(0, 0), color=GREEN)
        label_o = Text("O(0,0)", font="PingFang SC").next_to(center_o, UP+LEFT)
        
        # 初始动点P
        point_p = Dot(axes.coords_to_point(3, 0), color=YELLOW)
        label_p = Text("P(x,y)", font="PingFang SC").next_to(point_p, UP)
        
        # 线段PA和PO
        line_pa = Line(point_p, point_a, color=ORANGE)
        line_po = Line(point_p, center_o, color=GREEN)
        
        # 距离标记
        pa_value = Text("PA = ?", font="PingFang SC").next_to(line_pa, UP+RIGHT, buff=0.2)
        
        # 显示题目和坐标系
        self.play(Write(problem), Write(problem2))
        self.wait(2)
        self.play(Create(axes), Write(labels))
        self.wait(1)
        
        # 显示圆、圆心和定点
        self.play(Create(circle), Write(circle_label))
        self.play(Create(center_o), Write(label_o))
        self.play(Create(point_a), Write(label_a))
        self.wait(2)
        
        # 显示动点P和线段
        self.play(Create(point_p), Write(label_p))
        self.play(Create(line_po), Create(line_pa), Write(pa_value))
        self.wait(2)
        
        # 让点P沿圆周运动，同时更新线段和距离值
        def update_p(point, alpha):
            # 计算角度（从0到2π）
            angle = alpha * 2 * PI
            # 计算圆上点的坐标
            x = 3 * np.cos(angle)
            y = 3 * np.sin(angle)
            # 更新点位置
            point.move_to(axes.coords_to_point(x, y))
            return point
        
        def update_lines(line_pa, line_po, point_p, point_a, center_o):
            line_pa.become(Line(point_p, point_a, color=ORANGE))
            line_po.become(Line(point_p, center_o, color=GREEN))
            # 计算实际距离并更新文本
            x, y = axes.point_to_coords(point_p.get_center())
            distance = np.sqrt((x-5)**2 + y**2)
            pa_value.become(Text(f"PA = {distance:.2f}").next_to(line_pa, UP+RIGHT, buff=0.2))
            return line_pa, line_po, pa_value
        
        # 创建动画
        def update_all(mobject, alpha):
            # 更新点P位置
            angle = alpha * 2 * PI
            x = 3 * np.cos(angle)
            y = 3 * np.sin(angle)
            point_p.move_to(axes.coords_to_point(x, y))
            
            # 更新线段
            line_pa.become(Line(point_p, point_a, color=ORANGE))
            line_po.become(Line(point_p, center_o, color=GREEN))
            
            # 更新距离显示
            distance = np.sqrt((x-5)**2 + y**2)
            pa_value.become(Text(f"PA = {distance:.2f}", font="PingFang SC").next_to(line_pa, UP+RIGHT, buff=0.2))
            label_p.next_to(point_p, UP)
        
        self.play(
            UpdateFromAlphaFunc(VGroup(point_p, line_pa, line_po, pa_value, label_p), update_all),
            run_time=8,  # 8秒完成一周运动
            rate_func=linear  # 匀速运动
        )
        self.wait(2)
        
        # 显示结论
        conclusion = Text("结论：PA的最大值为8，最小值为2", font="PingFang SC", color=RED, font_size=24)
        conclusion.to_corner(DOWN+RIGHT)
        self.play(Write(conclusion))
        self.wait(3)

# 运行命令：manim -pqm circle_distance_problem.py CircleDistanceProblem

# ===================== 知识点解析 =====================
# 1. 隐函数曲线绘制
# - axes.plot_implicit_curve(function, color)：绘制隐函数曲线
#   * function：隐函数表达式，形式为f(x,y)=0
#   * 示例：lambda x,y: x**2 + y**2 - 9 表示圆x²+y²=9
#   * 注意：函数返回0的点会被绘制出来

# 2. 点的动态更新（重要概念）
# - UpdateFromAlphaFunc(mobject, update_function)：根据alpha值更新对象
#   * alpha值从0到1，表示动画进度（0=开始，1=结束）
#   * update_function(mobject, alpha)：定义对象如何随alpha变化
#   * 这是创建复杂动画的核心方法
#   * 示例：alpha * 2 * PI 表示从0到2π的角度变化

# 3. 多对象联动更新
# - 在update_function中同时更新多个对象
#   * 点P的位置：根据角度计算坐标
#   * 线段PA和PO：根据新的点位置重新绘制
#   * 距离显示：实时计算并更新文本
#   * 标签位置：跟随点P移动

# 4. 坐标转换（坐标系核心功能）
# - axes.coords_to_point(x, y)：将数学坐标(x,y)转换为Manim屏幕坐标
#   * 输入：数学坐标（如(3, 0)）
#   * 输出：屏幕上的像素位置
# - axes.point_to_coords(point)：将Manim屏幕坐标转换为数学坐标
#   * 输入：屏幕上的点对象
#   * 输出：数学坐标(x, y)

# 5. 数学计算与动画结合
# - np.cos(angle), np.sin(angle)：三角函数计算
# - np.sqrt((x-5)**2 + y**2)：距离公式计算
# - 实时更新：每次动画帧都重新计算所有相关值

# 6. 动画速率控制
# - rate_func=linear：匀速运动
# - 其他常用速率函数：
#   * smooth：平滑加速减速
#   * rush_into：先快后慢
#   * rush_from：先慢后快
#   * ease_in_out：缓入缓出
