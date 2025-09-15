from manim import *
import numpy as np

#案例 4：实战 Demo - 勾股定理可视化
class PythagoreanTheorem(Scene):
    def construct(self):
        # 创建标题文本
        title = Text("勾股定理", font="PingFang SC", font_size=40)
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.to_corner(UP+LEFT))
        
        # 创建勾股定理公式
        formula = Text("a² + b² = c²", font="PingFang SC", font_size=36)
        formula.to_corner(UP+RIGHT)
        self.play(Write(formula))
        
        # 创建直角三角形（使用Polygon手动创建）
        triangle = Polygon(
            [-1, -1, 0],  # 左下角
            [1, -1, 0],   # 右下角
            [-1, 1, 0],   # 左上角
            color=WHITE
        )
        triangle.shift(DOWN*0.5)
        
        # 标记三角形的边
        a_label = Text("a", font="PingFang SC").next_to(triangle.get_vertices()[0], LEFT)
        b_label = Text("b", font="PingFang SC").next_to(triangle.get_vertices()[1], DOWN)
        c_label = Text("c", font="PingFang SC").next_to(triangle.get_vertices()[2], UP)
        
        # 显示三角形和标记
        self.play(Create(triangle))
        self.play(Write(a_label), Write(b_label), Write(c_label))
        self.wait(2)
        
        # 创建以a、b、c为边的正方形
        square_a = Square(side_length=2, color=BLUE).next_to(triangle, LEFT, buff=0.5)
        square_a.rotate(-PI/2)
        label_a = Text("a²", font="PingFang SC").move_to(square_a.get_center())
        
        square_b = Square(side_length=2, color=GREEN).next_to(triangle, DOWN, buff=0.5)
        label_b = Text("b²", font="PingFang SC").move_to(square_b.get_center())
        
        square_c = Square(side_length=2*np.sqrt(2), color=RED).next_to(triangle, RIGHT+UP, buff=1)
        label_c = Text("c²", font="PingFang SC").move_to(square_c.get_center())
        
        # 动画显示三个正方形
        self.play(Create(square_a), Write(label_a))
        self.wait(1)
        self.play(Create(square_b), Write(label_b))
        self.wait(1)
        self.play(Create(square_c), Write(label_c))
        self.wait(2)
        
        # 移动a²和b²到c²上方，展示面积相等
        self.play(
            square_a.animate.move_to(square_c.get_center() + LEFT*1),
            square_b.animate.move_to(square_c.get_center() + RIGHT*1),
            label_a.animate.move_to(square_c.get_center() + LEFT*1),
            label_b.animate.move_to(square_c.get_center() + RIGHT*1),
            run_time=2
        )
        self.wait(3)
        
        # 最终强调公式
        self.play(formula.animate.scale(1.5).move_to(ORIGIN))
        self.wait(2)

# 运行命令：manim -pqm pythagorean_theorem.py PythagoreanTheorem

# ===================== 知识点解析 =====================
# 1. 多边形创建
# - Polygon(*points, color)：创建多边形
#   * points：顶点坐标列表，格式为[x, y, z]
#   * 示例：Polygon([-1, -1, 0], [1, -1, 0], [-1, 1, 0]) 创建直角三角形
#   * 注意：RightTriangle不是Manim内置类，需要用Polygon手动创建
# - get_vertices()：返回多边形所有顶点的坐标列表
#   * 返回格式：[[x1,y1,z1], [x2,y2,z2], ...]

# 2. 对象定位与移动
# - next_to(mobject, direction, buff)：将对象放置在另一个对象的指定方向
#   * mobject：参考对象
#   * direction：方向（LEFT/RIGHT/UP/DOWN或组合如RIGHT+UP）
#   * buff：两个对象之间的距离（数值越大距离越远）
# - to_corner(direction)：将对象移动到屏幕角落
#   * UP+LEFT：左上角，UP+RIGHT：右上角
#   * DOWN+LEFT：左下角，DOWN+RIGHT：右下角
# - move_to(position)：将对象移动到指定位置
#   * ORIGIN：坐标原点（屏幕中心）
#   * 可使用相对位置：如square_c.get_center() + LEFT*1

# 3. 动画控制
# - scale(factor)：缩放对象
#   * factor > 1：放大，factor < 1：缩小
#   * 示例：scale(1.5)表示放大到原来的1.5倍
# - run_time：控制动画持续时间（秒）
#   * 数值越大动画越慢，数值越小动画越快

# 4. 数学计算与可视化
# - np.sqrt(2)：计算平方根（需要import numpy as np）
# - 数学公式的可视化：将抽象公式转化为具体的几何图形
# - 通过动画展示数学概念，如勾股定理的几何意义

# 5. 渲染控制
# - 命令参数：
#   * -l：低质量（480p），渲染快，适合调试
#   * -m：中质量（720p），平衡质量和速度
#   * -h：高质量（1080p），最终输出
#   * -p：渲染完成后自动播放
#   * 示例：manim -pqm 文件名.py 类名（高质量渲染并自动播放）
