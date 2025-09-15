# Manim 学习项目

## 📚 项目简介

这是一个完整的Manim学习项目，包含了从基础到高级的8个学习案例，以及详细的学习文档和参考手册。适合从零开始学习Manim的初学者。

## 🎯 学习目标

通过系统化的学习，掌握Manim的核心概念和高级技巧，能够创建高质量的数学动画。

## 📖 学习资源

### 📚 学习文档
1. **[Manim学习指南.md](./doc/Manim学习指南.md)** - 完整的学习文档，包含所有核心概念
2. **[Manim快速参考.md](./doc/Manim快速参考.md)** - 随时查阅的参考手册
3. **[学习路径规划.md](./doc/学习路径规划.md)** - 4周学习计划，循序渐进

### 🎬 学习案例（按难度排序）

| 案例 | 文件名 | 学习重点 | 难度 | 状态 |
|------|--------|----------|------|------|
| 1 | `basic_shapes.py` | 基本形状、基础动画、变换操作 | ⭐ | ✅ |
| 2 | `text_and_formulas.py` | 文本处理、公式显示、对象组合 | ⭐ | ✅ |
| 3 | `coordinate_systems.py` | 坐标系创建、函数绘制、坐标转换 | ⭐⭐ | ✅ |
| 4 | `pythagorean_theorem.py` | 数学可视化、对象定位、动画控制 | ⭐⭐ | ✅ |
| 5 | `circle_distance_problem.py` | 动态更新、数学计算、复杂动画 | ⭐⭐⭐ | ✅ |
| 6 | `line_parabola_intersection.py` | ValueTracker、更新器、轨迹可视化 | ⭐⭐⭐ | ✅ |
| 7 | `ellipse_tangent_problem.py` | 隐函数、切线计算、条件逻辑 | ⭐⭐⭐⭐ | ✅ |
| 8 | `advanced_3d_scene.py` | 3D对象、相机控制、3D变换 | ⭐⭐⭐⭐ | ✅ |

## 🚀 快速开始

### 1. 环境准备
```bash
# 激活conda环境
conda activate manim_study

# 验证Manim安装
manim --version
```

### 2. 运行第一个案例
```bash
# 运行基础形状案例
manim -pql basic_shapes.py BasicShapes
```

### 3. 学习建议
1. 按照学习路径规划逐步学习
2. 每个案例都要亲自运行和修改
3. 遇到问题时查阅快速参考手册
4. 记录学习进度和心得

## 📅 学习计划

### 第1周：基础入门
- 掌握基本形状和动画
- 理解文本处理和对象定位
- 完成案例1-2

### 第2周：坐标系与函数
- 掌握坐标系创建和函数绘制
- 理解数学概念可视化
- 完成案例3-4

### 第3周：动态动画与数学应用
- 掌握动态更新和复杂动画
- 理解数学计算与动画结合
- 完成案例5-6

### 第4周：高级技巧与3D场景
- 掌握高级动画技巧
- 理解3D场景和相机控制
- 完成案例7-8

## 🎨 案例特色

### 中文支持
- 所有案例都支持中文显示
- 使用PingFang SC字体确保中文显示效果
- 避免了LaTeX依赖问题

### 详细注释
- 每个案例都有详尽的中文注释
- 包含知识点解析和学习重点
- 适合初学者理解

### 循序渐进
- 从简单到复杂的学习路径
- 每个案例都建立在之前的基础上
- 逐步掌握Manim的核心概念

## 🔧 技术特点

### 环境兼容
- 解决了LaTeX依赖问题
- 使用Text替代MathTex
- 确保在macOS上正常运行

### 代码质量
- 所有案例都经过测试验证
- 修复了常见的语法错误
- 优化了动画性能

### 学习友好
- 详细的错误解决方案
- 常见问题FAQ
- 完整的学习资源

## 📁 项目结构

```
manim_study/
├── 项目说明.md                    # 项目说明（本文件）
├── Manim学习指南.md               # 完整学习文档
├── Manim快速参考.md               # 快速参考手册
├── 学习路径规划.md                # 学习计划
├── basic_shapes.py                # 案例1：基础形状
├── text_and_formulas.py           # 案例2：文本与公式
├── coordinate_systems.py          # 案例3：坐标系与函数
├── pythagorean_theorem.py         # 案例4：勾股定理
├── circle_distance_problem.py     # 案例5：圆上动点距离
├── line_parabola_intersection.py  # 案例6：直线与抛物线交点
├── ellipse_tangent_problem.py     # 案例7：椭圆切线问题
├── advanced_3d_scene.py           # 案例8：3D场景
└── media/                         # 渲染输出文件
    ├── videos/                    # 视频文件
    ├── images/                    # 图片文件
    └── texts/                     # 文本文件
```

## 🎯 学习成果

完成所有案例后，您将能够：

- ✅ 创建各种几何形状动画
- ✅ 处理中文文本和数学公式
- ✅ 绘制函数图像和数学曲线
- ✅ 实现动态点运动和轨迹可视化
- ✅ 创建3D场景和立体动画
- ✅ 解决常见的技术问题
- ✅ 独立开发新的动画项目

## 🔗 有用链接

- [Manim官方文档](https://docs.manim.community/)
- [Manim GitHub仓库](https://github.com/ManimCommunity/manim)
- [3Blue1Brown YouTube频道](https://www.youtube.com/c/3blue1brown)
- [Manim Discord社区](https://discord.gg/mMRrZQW)

## 📝 学习记录

建议在学习过程中记录：
- 学习进度和完成情况
- 遇到的问题和解决方案
- 学习心得和体会
- 创新想法和项目计划

## 🎉 开始学习

现在就开始您的Manim学习之旅吧！

1. 首先阅读 **[Manim学习指南.md](./Manim学习指南.md)**
2. 按照 **[学习路径规划.md](./学习路径规划.md)** 逐步学习
3. 遇到问题时查阅 **[Manim快速参考.md](./Manim快速参考.md)**
4. 记录学习进度和心得

**记住**：学习Manim是一个循序渐进的过程，扎实的基础是成功的关键！

祝您学习愉快！🎬✨

---

*项目创建时间：2024年*  
*Manim版本：Community v0.19.0*  
*适用平台：macOS, Windows, Linux*
