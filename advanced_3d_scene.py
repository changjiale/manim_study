from manim import *


class Advanced3DScene(ThreeDScene):
    def construct(self):
        # 设置3D场景
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
        
        # 创建一个3D立方体
        cube = Cube(side_length=2, fill_opacity=0.7, fill_color=BLUE)
        
        # 创建一个球体
        sphere = Sphere(radius=1, fill_opacity=0.7, fill_color=RED)
        sphere.move_to(RIGHT * 3)
        
        # 创建一个圆柱体
        cylinder = Cylinder(radius=0.5, height=2, fill_opacity=0.7, fill_color=GREEN)
        cylinder.move_to(LEFT * 3)
        
        # 添加坐标轴
        axes = ThreeDAxes()
        
        # 显示所有对象
        self.add(axes, cube, sphere, cylinder)
        
        # 旋转动画
        self.play(
            Rotate(cube, angle=PI, axis=UP),
            Rotate(sphere, angle=PI, axis=RIGHT),
            Rotate(cylinder, angle=PI, axis=OUT),
            run_time=2
        )
        
        # 移动动画
        self.play(
            cube.animate.move_to(UP * 2),
            sphere.animate.move_to(DOWN * 2),
            cylinder.animate.move_to(ORIGIN),
            run_time=2
        )
        
        # 缩放动画
        self.play(
            cube.animate.scale(1.5),
            sphere.animate.scale(0.5),
            cylinder.animate.scale(2),
            run_time=2
        )
        
        # 相机旋转
        self.move_camera(phi=45 * DEGREES, theta=60 * DEGREES, run_time=2)
        
        # 最终旋转
        self.play(
            Rotate(cube, angle=2*PI, axis=UP),
            Rotate(sphere, angle=2*PI, axis=RIGHT),
            Rotate(cylinder, angle=2*PI, axis=OUT),
            run_time=3
        )
        self.wait(1)

# 运行命令：manim -pql advanced_3d_scene.py Advanced3DScene

# ===================== 知识点解析 =====================
# 1. 3D场景基础
# - ThreeDScene：3D场景的基类，继承自Scene
# - 必须继承ThreeDScene才能使用3D功能
# - 3D场景支持立体几何对象和3D变换

# 2. 相机控制
# - set_camera_orientation(phi, theta)：设置相机角度
#   * phi：俯仰角（0-90度），控制上下视角
#   * theta：偏航角（0-360度），控制左右视角
#   * DEGREES：角度转弧度的转换
# - move_camera(phi, theta, run_time)：动态改变相机角度
#   * 可以创建相机旋转动画

# 3. 3D坐标系
# - ThreeDAxes()：创建3D坐标系
# - 3D方向向量：
#   * OUT：指向屏幕外（z轴正方向）
#   * IN：指向屏幕内（z轴负方向）
#   * UP, DOWN, LEFT, RIGHT：与2D相同

# 4. 3D几何体
# - Sphere(radius, color)：创建球体
#   * radius：球体半径
# - Cube(side_length, color)：创建立方体
#   * side_length：边长
# - Cylinder(radius, height, color)：创建圆柱体
#   * radius：底面半径
#   * height：高度

# 5. 3D变换
# - shift(direction)：3D空间中的移动
#   * 可以使用3D方向向量：OUT, IN等
# - rotate(angle, axis)：绕指定轴旋转
#   * axis：旋转轴（X_AXIS, Y_AXIS, Z_AXIS）
#   * 示例：rotate(PI/2, axis=X_AXIS) 绕x轴旋转90度

# 6. 3D动画
# - Create()：创建3D对象
# - 所有2D动画效果在3D中同样适用
# - 3D对象可以同时进行多个变换

# 7. 3D渲染注意事项
# - 3D场景渲染时间通常比2D长
# - 复杂的3D对象可能影响性能
# - 建议先用低质量(-l)测试，再用高质量(-h)渲染