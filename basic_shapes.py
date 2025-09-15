from manim import *

#案例 1：基础形状与动画
class BasicShapes(Scene):
    # 所有动画逻辑都在construct方法中实现
    def construct(self):
        # 创建圆形：radius设置半径，color设置边框颜色，fill_opacity设置填充透明度
        circle = Circle(radius=1, color=BLUE, fill_opacity=0.5)
        
        # 创建正方形：side_length设置边长，shift()方法移动位置
        square = Square(side_length=2, color=GREEN).shift(RIGHT*3)
        
        # 创建三角形：rotate()方法旋转图形
        triangle = Triangle(color=RED).shift(LEFT*3)
        
        # 同时创建三个形状
        self.play(Create(circle), Create(square), Create(triangle), run_time=2)
        self.wait(1)
        
        # 多对象同时变换
        self.play(
            circle.animate.shift(UP*2).scale(0.5),
            square.animate.shift(DOWN*2).rotate(PI/4),
            triangle.animate.scale(1.5).rotate(-PI/2),
            run_time=1.5
        )
        self.wait(1)
        
        # 淡出所有对象
        self.play(FadeOut(circle), FadeOut(square), FadeOut(triangle))

# 运行命令：manim -pql basic_shapes.py BasicShapes

# ===================== 知识点解析 =====================
# 1. 核心类与方法
# - Scene：所有动画场景的基类，必须继承它来创建动画
# - construct(self)：动画的主方法，所有动画逻辑都写在这里
# - self.play(*animations, run_time)：执行动画，可同时传入多个动画
#   * 参数：*animations 是要执行的动画列表，run_time 控制动画持续时间（秒）
# - self.wait(duration)：暂停指定时间（秒），让观众看清当前画面

# 2. 基本形状
# - Circle(radius, color, fill_opacity)：创建圆形
#   * radius：半径大小
#   * color：边框颜色（内置颜色如BLUE, RED, GREEN等）
#   * fill_opacity：填充透明度（0-1之间）
# - Square(side_length, color)：创建正方形
#   * side_length：边长
# - Triangle(color)：创建三角形

# 3. 变换操作
# - shift(direction)：按指定方向移动
#   * 方向向量：UP(上)、DOWN(下)、LEFT(左)、RIGHT(右)
#   * 示例：RIGHT*3 表示向右移动3个单位
# - scale(factor)：缩放
#   * factor > 1：放大；factor < 1：缩小
# - rotate(angle)：旋转
#   * 角度单位：弧度（PI=180度，PI/2=90度）

# 4. 动画效果
# - Create(mobject)：创建绘制动画，模拟画图过程
# - FadeOut(mobject)：淡出动画，使对象逐渐消失
# - animate属性：用于创建平滑的状态过渡动画，可链式调用多个变换
