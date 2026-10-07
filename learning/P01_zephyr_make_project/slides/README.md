---
id: zephyr-download-slides
title: 演示资料维护
kind: reference
status: maintained
domains: [zephyr, tools]
---

<!-- SPDX-License-Identifier: Apache-2.0 -->

# 第1章\_演示资料维护

每个独立主题占用一个连续的三位章号。Windows 主线为 P001—P007，Linux 分支保留平台后缀。MD 与 PPT 同名对应，正文按所在章号从 x.1 开始，PPT 页码在每份文稿内独立计数。

| 章号 | 正式 PPT | 页数 | 完整正文 |
| --- | --- | --- | --- |
| P001 | [准备UCRT64环境与下载Zephyr_Windows](P001_准备UCRT64环境与下载Zephyr_Windows.pptx) | 41 | [MD](../P001_准备UCRT64环境与下载Zephyr_Windows.md) |
| P002 | [主机工具与Python环境_Windows](P002_主机工具与Python环境_Windows.pptx) | 16 | [MD](../P002_主机工具与Python环境_Windows.md) |
| P003 | [Zephyr的CMake接口体系_Windows](P003_Zephyr的CMake接口体系_Windows.pptx) | 56 | [MD](../P003_Zephyr的CMake接口体系_Windows.md) |
| P004 | [SDK准备与编译器选型_Windows](P004_SDK准备与编译器选型_Windows.pptx) | 45 | [MD](../P004_SDK准备与编译器选型_Windows.md) |
| P005 | [CMSIS与HAL选择下载_Windows](P005_CMSIS与HAL选择下载_Windows.pptx) | 22 | [MD](../P005_CMSIS与HAL选择下载_Windows.md) |
| P006 | [源码模块接入Zephyr工程_Windows](P006_源码模块接入Zephyr工程_Windows.pptx) | 14 | [MD](../P006_源码模块接入Zephyr工程_Windows.md) |
| P007 | [编译示例与新增开发板_Windows](P007_编译示例与新增开发板_Windows.pptx) | 51 | [MD](../P007_编译示例与新增开发板_Windows.md) |
| Linux-P001 | [官方环境安装与源码准备_Linux](P001_官方环境安装与源码准备_Linux.pptx) | 21 | [MD](../P001_官方环境安装与源码准备_Linux.md) |

## 1.1\_文件与命令位置

正式 PPT 放在 slides，正文放在其上一级。同名文件配对阅读，学习顺序见 [专题大纲](../大纲.md)。主机与 Python 是 P002，通用 CMake 接口是 P003，SDK 是 P004，源码依赖下载是 P005，模块接入是 P006，编译与新增板是 P007。

命令分别在 commands/P001_Windows 至 commands/P007_Windows，Linux 使用 commands/P001_Linux。每个 PPT 的“完整命令”相对链接指向对应目录；分发时保留 slides 与 commands 的相邻位置。实验仍在 G:/zephyr_practice/zephyr-main，资料目录不作为实验源码根。

P007 中原有 build/learning-tools/p003 和 labs/p003 是实验目录标识，不随资料章号迁移；正文已注明用途，读者继续复用。

## 1.2\_封面、页脚署名与页码

正式文稿统一采用本系列的芯片背景封面，Linux P001 标明 Ubuntu 22.04 LTS。封面保留主讲人 `lizhaojun`，正文和封面均在左下角显示横向页脚署名 `lizhaojun`。按 2026-10-06 的最新约定，取消正文上的斜向大水印。

页脚署名位于幻灯片母版，形状名为 `Footer signature lizhaojun`。在 PowerPoint 的“视图 → 幻灯片母版”中编辑，并检查各套正文及封面母版；使用相应版式新增页面时自动继承。普通幻灯片不重复添加署名，也不勾选“隐藏背景图形”。封面中的主讲人仍为独立可编辑文字 `Presenter lizhaojun`。

在 1280 × 720 页面坐标中，署名框为左 64、上 676、宽 150、高 28，横向左对齐、垂直居中，Microsoft YaHei 13.5 pt，无填充和边框。白底正文使用 `#646173`，深色封面使用 `#D4CDE8`，文字不透明，保证可读性。该框及其周围留白为非正文区域，图片、表格、代码和链接均不得占用。母版对象仍位于普通页面内容后方，依靠预留页脚区域避免遮挡，而非强制覆盖正文。

仅对署名文字启用“不检查拼写”，不关闭正文或应用的拼写检查。检查每页署名清晰、没有重复、没有被图片或文本遮挡。

正文自动页码保留右下角，形状名 `PageNumber`，Microsoft YaHei 13.5 pt，右对齐，框为左 1140、上 676、宽 76、高 28。署名和页码分居页脚两端。封面不显示页码，正文显示实际幻灯片序号。

<a id="semantic-colors"></a>

### 1.2.1\_变量、文件、接口和命令的颜色

沿用已有手工标注的分类，浅色页面采用深橙色 `#B84E00` 表示变量、参数及配置字段，蓝色 `#0070C0` 表示文件和路径，深绿色 `#087B3D` 表示接口函数，紫色 `#A02B93` 表示终端命令。普通说明保持深色 `#29263B`，链接保留原有下划线样式。P003 的第 2、18 页提供颜色图例；颜色只辅助辨认，文字仍须明确对象类型。

按上下文区分目录、工具与函数；文件中的 `cmake-ext` 是配置字段，不能把其中的 cmake 当命令着色。完整路径作为一个对象处理。正文、代码及图示中的同类对象使用一致颜色。代码着色使用原文本框内的富文本片段，保留完整可复制的操作单元；不得拆散文本框或改变代码内容。

维护时先读取当前 PPT 的手工配色和版式，保留后再同步原生包，禁止用单色旧生成器覆盖。上述色值针对浅色画布，深色画布需另核对对比度；配套 MD 继续使用阅读器的行内代码和语法高亮，不强行写入这些固定颜色。

### 1.2.2\_行距与段间留白

正文、代码、表格和图内多行文字采用多倍行距 1.2。段间留白独立设置，正文逻辑段落间可从 12 pt 段后距起按页校准；代码空行与换行保持原样。调整后保留字号与配色，检查文字框、图节点和页脚的间隔，不缩字或恢复单倍来强行塞入内容。封面、标题和单行页脚沿用现有版式。

Windows P001—P007 与 Linux P001 的 8 份正式 PPT 已按此规则整理。规则适用于可编辑文字，现有截图和图片内的文字保留原样。维护时核对保存后的段落属性与原生渲染；不能只把视觉上多出的空白当作 1.2 倍行距已生效。配套 MD 不强制写入行距样式。

## 1.3\_保存、同步与重建

在 PowerPoint 保存正式文件后，在本 slides 目录运行以下资料维护命令（PowerShell，Python 3.10+）。示例同步和重建 SDK 章：

```powershell
# 当前位置：learning/P01_zephyr_make_project/slides；资料维护，不是实验命令。
python build.py --deck P004 sync
python build.py --deck P004 build --output P004-review.pptx
```

可选 --deck 为 P001、P002、P003、P004、P005、P006、P007、Linux-P001。P001 原生源在 src；P002—P007 分别在 p02—p07 的 src，Linux P001 在 p01_linux/src。每个目录同级的 source.json 保存页序。它们只承担 PPT 重建，不是实验目录。

先同步再重建；默认拒绝覆盖候选输出，明确使用 --force 才覆盖。--input 可同步另存文件，须先核对是否包含最新手工修改。旧分册编号和生成入口已退出正式使用。

## 1.4\_结构与原生检查

sync/build 检查母版与版式登记、布局 ID、备注母版和自动页码。在本目录运行 `python test_build.py` 做结构回归。修改后还需 PowerPoint 正常打开与渲染检查，不能用 ZIP 有效代替原生验收。
