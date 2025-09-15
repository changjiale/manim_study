from manim import *
import numpy as np
#案例 7：椭圆切线方程问题
class EllipseTangentProblem(Scene):
    def construct(self):
        # 题目描述
        problem = Text("题目：已知椭圆C：x²/4 + y²/9 = 1，", font="PingFang SC")
        problem2 = Text("点P是椭圆上的动点，求点P处切线方程的变化规律。", font="PingFang SC")
        VGroup(problem, problem2).arrange(DOWN, buff=0.5).to_corner(UP+LEFT)
        
        # 创建坐标系
        axes = Axes(
            x_range=[-3, 3, 1],
            y_range=[-5, 5, 1],
            axis_config={"color": GREY},
            tips=True
        )
        x_label = Text("x", font="PingFang SC").next_to(axes.x_axis.get_end(), RIGHT)
        y_label = Text("y", font="PingFang SC").next_to(axes.y_axis.get_end(), UP)
        labels = VGroup(x_label, y_label)
        
        # 绘制椭圆 x²/4 + y²/9 = 1
        ellipse = axes.plot_implicit_curve(
            lambda x, y: x**2/4 + y**2/9 - 1,
            color=BLUE
        )
        ellipse_label = Text("x²/4 + y²/9 = 1", font="PingFang SC").next_to(ellipse, RIGHT)
        
        # 椭圆上的动点P（初始位置在(2,0)）
        angle = ValueTracker(0)  # 用角度参数跟踪点的位置
        
        def get_p_point():
            """根据角度计算椭圆上点的坐标"""
            theta = angle.get_value()
            x = 2 * np.cos(theta)  # a=2
            y = 3 * np.sin(theta)  # b=3
            return axes.coords_to_point(x, y)
        
        point_p = Dot(get_p_point(), color=RED)
        label_p = Text("P(x,y)", font="PingFang SC").next_to(point_p, UP)
        
        # 点P处的切线
        def get_tangent_line():
            """计算椭圆在点P处的切线"""
            theta = angle.get_value()
            x0 = 2 * np.cos(theta)
            y0 = 3 * np.sin(theta)
            
            # 椭圆在点(x0,y0)处的切线方程：xx0/4 + yy0/9 = 1
            # 转换为y = kx + b形式（避免垂直情况）
            if y0 != 0:
                def tangent_func(x):
                    return (1 - x*x0/4) * 9 / y0
                return axes.plot(tangent_func, color=GREEN, x_range=[-3, 3])
            else:
                # 水平切线特殊情况
                return Line(
                    start=axes.coords_to_point(-3, y0),
                    end=axes.coords_to_point(3, y0),
                    color=GREEN
                )
        
        tangent_line = get_tangent_line()
        tangent_label = Text("切线", font="PingFang SC").next_to(tangent_line, RIGHT)
        
        # 切线方程显示
        def update_tangent_eq():
            theta = angle.get_value()
            x0 = 2 * np.cos(theta)
            y0 = 3 * np.sin(theta)
            if abs(x0) < 0.01:
                return Text("y = ±3", font="PingFang SC").to_corner(UP+RIGHT)
            elif abs(y0) < 0.01:
                return Text("x = ±2", font="PingFang SC").to_corner(UP+RIGHT)
            else:
                return Text(f"x·{x0:.1f}/4 + y·{y0:.1f}/9 = 1", font="PingFang SC").to_corner(UP+RIGHT)
        
        tangent_eq = update_tangent_eq()
        
        # 显示题目和坐标系
        self.play(Write(problem), Write(problem2))
        self.wait(2)
        self.play(Create(axes), Write(labels))
        self.wait(1)
        
        # 显示椭圆
        self.play(Create(ellipse), Write(ellipse_label))
        self.wait(2)
        
        # 显示点P和初始切线
        self.play(Create(point_p), Write(label_p))
        self.play(Create(tangent_line), Write(tangent_label), Write(tangent_eq))
        self.wait(2)
        
        # 定义更新函数
        def update_point(p):
            p.move_to(get_p_point())
            return p
        
        def update_tangent(line):
            new_line = get_tangent_line()
            line.become(new_line)
            return line
        
        def update_tangent_text(text):
            new_text = update_tangent_eq()
            text.become(new_text)
            return text
        
        # 添加更新器
        point_p.add_updater(update_point)
        tangent_line.add_updater(update_tangent)
        tangent_eq.add_updater(update_tangent_text)
        
        # 让点P沿椭圆运动一周
        self.play(angle.animate.increment_value(2*PI), run_time=10, rate_func=linear)
        
        # 移除更新器
        point_p.remove_updater(update_point)
        tangent_line.remove_updater(update_tangent)
        tangent_eq.remove_updater(update_tangent_text)
        
        # 显示结论
        conclusion = Text("结论：椭圆切线方程为xx₀/4 + yy₀/9 = 1", font="PingFang SC", color=RED)
        conclusion.to_corner(DOWN+RIGHT)
        self.play(Write(conclusion))
        self.wait(3)

# 运行命令：manim -pqm ellipse_tangent_problem.py EllipseTangentProblem

# ===================== 知识点解析 =====================
# 1. 椭圆绘制与参数化
# - 椭圆的隐函数形式：x²/a² + y²/b² = 1
# - 参数方程表示：x = a·cosθ, y = b·sinθ（便于动画）
#   * a = 2, b = 3 表示椭圆的长半轴和短半轴
#   * θ 是参数，从0到2π变化
# - 使用ValueTracker跟踪角度参数θ的变化
#   * angle = ValueTracker(0) 跟踪角度变化

# 2. 动态切线计算（高等数学应用）
# - 椭圆上点P的坐标：(2cosθ, 3sinθ)
# - 切线斜率：dy/dx = -2sinθ/(3cosθ) = -2tanθ/3
# - 切线方程：y - 3sinθ = -2tanθ/3(x - 2cosθ)
# - 特殊情况处理：
#   * 当cosθ = 0时，切线为水平线 y = ±3
#   * 当sinθ = 0时，切线为垂直线 x = ±2

# 3. 条件更新逻辑
# - 在更新器中加入条件判断，处理特殊情况
# - 根据点的位置动态调整显示内容
# - 使用if-else语句处理不同的数学情况

# 4. 角度动画控制
# - 使用angle.increment_value(2*PI)实现一周的旋转
# - rate_func=linear确保匀速运动
# - 2*PI表示360度，完成一个完整的椭圆

# 5. 更新器管理（性能优化）
# - add_updater()添加更新逻辑
# - remove_updater()在动画结束后移除更新器
# - 避免不必要的计算，提高渲染性能
# - 这是复杂动画的重要优化技巧

# 6. 数学可视化技巧
# - 将抽象的数学概念（切线）转化为直观的几何图形
# - 通过动画展示数学规律的变化
# - 结合数学计算和视觉呈现，增强理解
