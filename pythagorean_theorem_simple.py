from manim import *
import numpy as np

#案例 4：实战 Demo - 勾股定理可视化（简化版）
class PythagoreanTheoremSimple(Scene):
    def construct(self):
        # 创建标题文本（使用英文避免字体问题）
        title = Text("Pythagorean Theorem", font_size=40)
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.to_corner(UP+LEFT))
        
        # 创建勾股定理公式（使用Text而不是MathTex）
        formula = Text("a² + b² = c²", font_size=36)
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
        a_label = Text("a").next_to(triangle.get_vertices()[0], LEFT)
        b_label = Text("b").next_to(triangle.get_vertices()[1], DOWN)
        c_label = Text("c").next_to(triangle.get_vertices()[2], UP)
        
        # 显示三角形和标记
        self.play(Create(triangle))
        self.play(Write(a_label), Write(b_label), Write(c_label))
        self.wait(2)
        
        # 创建以a、b、c为边的正方形
        square_a = Square(side_length=2, color=BLUE).next_to(triangle, LEFT, buff=0.5)
        square_a.rotate(-PI/2)
        label_a = Text("a²").move_to(square_a.get_center())
        
        square_b = Square(side_length=2, color=GREEN).next_to(triangle, DOWN, buff=0.5)
        label_b = Text("b²").move_to(square_b.get_center())
        
        square_c = Square(side_length=2*np.sqrt(2), color=RED).next_to(triangle, RIGHT+UP, buff=1)
        label_c = Text("c²").move_to(square_c.get_center())
        
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

# 运行命令：manim -pqm pythagorean_theorem_simple.py PythagoreanTheoremSimple
