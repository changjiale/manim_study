from manim import *
#案例 2：文本与数学公式
class TextAndFormulas(Scene):
    def construct(self):
        # 创建普通文本：font设置字体（支持中文），font_size设置大小
        text = Text("Manim 文本示例", font="PingFang SC", font_size=36)
        
        # 创建数学公式：使用Text替代MathTex避免LaTeX依赖
        formula1 = Text("e^(iπ) + 1 = 0", font="PingFang SC", font_size=48)
        formula2 = Text("∑(1/n²) = π²/6", font="PingFang SC", font_size=40)
        
        # 组合对象并排列
        VGroup(text, formula1, formula2).arrange(DOWN, buff=1)
        
        # 文本写入动画
        self.play(Write(text))
        self.wait(0.5)
        self.play(Write(formula1))
        self.wait(1)
        self.play(Write(formula2))
        self.wait(2)
        
        # 为公式添加括号和说明文字
        brace = Brace(formula2, LEFT)
        text = Text("欧拉级数", font="PingFang SC").next_to(brace, LEFT)
        
        self.play(Create(brace), Write(text))
        self.wait(2)

# 运行命令：manim -pql text_and_formulas.py TextAndFormulas

# ===================== 知识点解析 =====================
# 1. 文本处理
# - Text(content, font, font_size)：创建普通文本
#   * content：文本内容（支持中文）
#   * font：字体（支持中文需指定中文字体如"PingFang SC"、"Heiti SC"）
#   * font_size：字体大小（数值越大字体越大）
# - Write(mobject)：文本写入动画，模拟手写效果
#   * 比Create()更适合文本，有逐字显示的效果

# 2. 数学公式显示
# - 注意：由于LaTeX配置问题，这里使用Text替代MathTex
# - Text可以显示简单的数学符号：²、π、∑等
# - 如果需要复杂公式，建议使用MathTex（需要LaTeX环境）
#   * MathTex使用LaTeX语法，如：r"\sum_{n=1}^\infty \frac{1}{n^2}"
#   * 特殊字符前需加反斜杠，如：\sum(求和)、\pi(π)、\infty(∞)

# 3. 对象组合与排列
# - VGroup(*mobjects)：将多个对象组合成一个组
#   * 组合后可作为一个整体进行操作（移动、缩放等）
#   * 示例：VGroup(text, formula1, formula2)
# - arrange(direction, buff)：自动排列组内对象
#   * direction：排列方向（DOWN：垂直排列，RIGHT：水平排列）
#   * buff：对象之间的间距（数值越大间距越大）

# 4. 公式标注
# - Brace(mobject, direction)：创建括号标注
#   * mobject：要标注的对象
#   * direction：括号方向（LEFT/RIGHT/UP/DOWN）
# - next_to(mobject, direction, buff)：手动定位文本
#   * 比get_text()更灵活，可以精确控制位置
