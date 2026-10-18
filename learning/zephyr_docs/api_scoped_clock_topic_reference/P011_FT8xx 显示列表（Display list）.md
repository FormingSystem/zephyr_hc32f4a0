---
id: learning.zephyr-docs.api-scoped-clock-topic-reference.page-11
title: FT8xx 显示列表（Display list）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__dl.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第11章\_FT8xx 显示列表（Display list）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__dl.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

FT8xx 显示列表命令。

<a id="details"></a>

FT8xx 显示列表命令。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 11.1\_宏定义（Macros）

<a id="r_ga28f7596c367f67f73d701b792300aa09"></a>

```c
#define FT8XX_BITMAPS 1U
```

相关声明：[位图（FT8XX_BITMAPS）。](#ga28f7596c367f67f73d701b792300aa09)。

矩形像素阵列（Rectangular Pixel Arrays），支持多种颜色格式。

<a id="r_ga1d6f49b3817f9927fa1cd3cd42820490"></a>

```c
#define FT8XX_POINTS 2U
```

相关声明：[点（FT8XX_POINTS）。](#ga1d6f49b3817f9927fa1cd3cd42820490)。

抗锯齿点（Anti-aliased Points），点半径为 1–256 像素。

<a id="r_ga62bcf30c7a9eae4c468e1c7de144ad01"></a>

```c
#define FT8XX_LINES 3U
```

相关声明：[线段（FT8XX_LINES）。](#ga62bcf30c7a9eae4c468e1c7de144ad01)。

抗锯齿线（Anti-aliased Lines），宽度为 0–4095 个 1/16 像素单位。

<a id="r_gac1b1188c36a4078e7db50d3c5aee7d25"></a>

```c
#define FT8XX_LINE_STRIP 4U
```

相关声明：[折线（FT8XX_LINE_STRIP）。](#gac1b1188c36a4078e7db50d3c5aee7d25)。

首尾连接的抗锯齿线（Anti-aliased Lines）。

<a id="r_ga0b3ce2828323978e9648bfd07caa1065"></a>

```c
#define FT8XX_EDGE_STRIP_R 5U
```

相关声明：[右侧边带（FT8XX_EDGE_STRIP_R）。](#ga0b3ce2828323978e9648bfd07caa1065)。

向右延伸的边缘带（Edge Strips）。

<a id="r_ga97229abf592bba4039f19a98451cdc5b"></a>

```c
#define FT8XX_EDGE_STRIP_L 6U
```

相关声明：[左侧边带（FT8XX_EDGE_STRIP_L）。](#ga97229abf592bba4039f19a98451cdc5b)。

向左延伸的边缘带（Edge Strips）。

<a id="r_gaf5ad60bbe137dbf64281ad8d0be051e0"></a>

```c
#define FT8XX_EDGE_STRIP_A 7U
```

相关声明：[上侧边带（FT8XX_EDGE_STRIP_A）。](#gaf5ad60bbe137dbf64281ad8d0be051e0)。

向上延伸的边缘带（Edge Strips）。

<a id="r_ga9aff3a3c58e12b990130271e845662a8"></a>

```c
#define FT8XX_EDGE_STRIP_B 8U
```

相关声明：[下侧边带（FT8XX_EDGE_STRIP_B）。](#ga9aff3a3c58e12b990130271e845662a8)。

向下延伸的边缘带（Edge Strips）。

<a id="r_ga05077568fea624ed7e3f9e3f6e8d72b8"></a>

```c
#define FT8XX_RECTS 9U
```

相关声明：[矩形（FT8XX_RECTS）。](#ga05077568fea624ed7e3f9e3f6e8d72b8)。

圆角矩形（Round-cornered Rectangles），可使用 `FT8XX_LINE_WIDTH` 调整圆角曲率。

<a id="r_ga25324ac604e037baf26cdd37341bee44"></a>

```c
#define FT8XX_BEGIN(prim)
```

相关声明：[FT8XX_BEGIN](#ga25324ac604e037baf26cdd37341bee44)。

开始绘制图形图元（Graphics Primitive）。

<a id="r_gab0fb60eec6f4c3b68d47f61886e7b933"></a>

```c
#define FT8XX_CLEAR(c, s, t)
```

相关声明：[FT8XX_CLEAR](#gab0fb60eec6f4c3b68d47f61886e7b933)。

将缓冲区清除为预设值（Preset Values）。

<a id="r_ga180b0ed70243277462cf303bc788e094"></a>

```c
#define FT8XX_CLEAR_COLOR_RGB(red, green, blue)
```

相关声明：[FT8XX_CLEAR_COLOR_RGB](#ga180b0ed70243277462cf303bc788e094)。

指定红、绿、蓝通道的清除值（Clear Values）。

<a id="r_ga3bc794705028fc7e8e1b742db180055d"></a>

```c
#define FT8XX_COLOR_RGB(red, green, blue)
```

相关声明：[FT8XX_COLOR_RGB](#ga3bc794705028fc7e8e1b742db180055d)。

设置当前红、绿、蓝颜色（Current Color）。

<a id="r_ga135472b1cdf30d4bd69372e36c9960ce"></a>

```c
#define FT8XX_DISPLAY()
```

相关声明：[FT8XX_DISPLAY](#ga135472b1cdf30d4bd69372e36c9960ce)。

结束显示列表（Display List）。

<a id="r_ga8a9d0eb6521459eb7ce50b397de194d9"></a>

```c
#define FT8XX_END()
```

相关声明：[FT8XX_END](#ga8a9d0eb6521459eb7ce50b397de194d9)。

结束图形图元（Graphics Primitive）的绘制。

<a id="r_ga1d22204625ef070a6b8d16af7ad97578"></a>

```c
#define FT8XX_LINE_WIDTH(width)
```

相关声明：[FT8XX_LINE_WIDTH](#ga1d22204625ef070a6b8d16af7ad97578)。

指定使用 `FT8XX_LINES` 图元绘制的线宽（Line Width）。

<a id="r_gab0721051bb3f3cb9f555f696f36dfbbf"></a>

```c
#define FT8XX_TAG(s)
```

相关声明：[FT8XX_TAG](#gab0721051bb3f3cb9f555f696f36dfbbf)。

为后续图形对象附加标签值（Tag Value）。

<a id="r_ga2648ab069991c02b2e8de62bf13913ab"></a>

```c
#define FT8XX_VERTEX2F(x, y)
```

相关声明：[FT8XX_VERTEX2F](#ga2648ab069991c02b2e8de62bf13913ab)。

在指定坐标（Coordinate）开始图形图元（Graphics Primitives）操作。

<a id="r_ga560836cd8c85599f24e5623a3e286b12"></a>

```c
#define FT8XX_VERTEX2II(x, y, handle, cell)
```

相关声明：[FT8XX_VERTEX2II](#ga560836cd8c85599f24e5623a3e286b12)。

在指定坐标（Coordinates）开始图形图元（Graphics Primitive）操作。

## 11.2\_详细说明（Detailed Documentation）

<a id="ga25324ac604e037baf26cdd37341bee44"></a>

### `FT8XX_BEGIN`

```c
#define FT8XX_BEGIN ( prim)
```

```c
#include <zephyr/drivers/misc/ft8xx/ft8xx_dl.h>
```

展开值（Value）：

```c
(0x1f000000 | ((prim) & 0x0f))
```

开始绘制图形图元（Graphics Primitive）。

有效图元（Primitives）定义如下：

- 位图（FT8XX_BITMAPS）。
- 点（FT8XX_POINTS）。
- 线段（FT8XX_LINES）。
- 折线（FT8XX_LINE_STRIP）。
- 右侧边带（FT8XX_EDGE_STRIP_R）。
- 左侧边带（FT8XX_EDGE_STRIP_L）。
- 上侧边带（FT8XX_EDGE_STRIP_A）。
- 下侧边带（FT8XX_EDGE_STRIP_B）。
- 矩形（FT8XX_RECTS）。

要绘制的图元（Primitive）由 FT8XX_BEGIN 命令选择。选定后持续有效，直到另一个 FT8XX_BEGIN 命令选择新图元。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `prim` | 图形图元（Graphics Primitive）。 |

**说明（Note）**：注意（Note）：执行 FT8XX_VERTEX2II 或 FT8XX_VERTEX2F 之前，不会进行图元绘制（Primitive Drawing）。

<a id="ga28f7596c367f67f73d701b792300aa09"></a>

### `FT8XX_BITMAPS`

```c
#define FT8XX_BITMAPS 1U
```

```c
#include <zephyr/drivers/misc/ft8xx/ft8xx_dl.h>
```

矩形像素阵列（Rectangular Pixel Arrays），支持多种颜色格式。

<a id="gab0fb60eec6f4c3b68d47f61886e7b933"></a>

### `FT8XX_CLEAR`

```c
#define FT8XX_CLEAR ( c, s, t )
```

```c
#include <zephyr/drivers/misc/ft8xx/ft8xx_dl.h>
```

展开值（Value）：

```c
(0x26000000 | \
((c) ? 0x04 : 0) | ((s) ? 0x02 : 0) | ((t) ? 0x01 : 0))
```

将缓冲区清除为预设值（Preset Values）。

c 为 true 时，将 FT8xx 颜色缓冲区（Color Buffer）清除为预设值；为 false 时保持其值不变。RGB 通道的预设值由 FT8XX_CLEAR_COLOR_RGB 命令定义，透明度通道（Alpha Channel）的预设值由 FT8XX_CLEAR_COLOR_A 定义。

s 为 true 时，将 FT8xx 模板缓冲区（Stencil Buffer）清除为预设值；为 false 时保持其值不变。预设值由 FT8XX_CLEAR_STENCIL 命令定义。

t 为 true 时，将 FT8xx 标签缓冲区（Tag Buffer）清除为预设值；为 false 时保持其值不变。预设值由 FT8XX_CLEAR_TAG 命令定义。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `c` | 清除颜色缓冲区（Color Buffer）。 |
| `s` | 清除模板缓冲区（Stencil Buffer）。 |
| `t` | 清除标签缓冲区（Tag Buffer）。 |

<a id="ga180b0ed70243277462cf303bc788e094"></a>

### `FT8XX_CLEAR_COLOR_RGB`

```c
#define FT8XX_CLEAR_COLOR_RGB ( red, green, blue )
```

```c
#include <zephyr/drivers/misc/ft8xx/ft8xx_dl.h>
```

展开值（Value）：

```c
(0x02000000 | \
(((uint32_t)(red) & 0xff) << 16) | \
(((uint32_t)(green) & 0xff) << 8) | \
((uint32_t)(blue) & 0xff))
```

指定红、绿、蓝通道的清除值（Clear Values）。

设置后续 FT8XX_CLEAR 使用的颜色值（Color Values）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `red` | 清除颜色缓冲区时使用的红色值（Red Value）。 |
| `green` | 清除颜色缓冲区时使用的绿色值（Green Value）。 |
| `blue` | 清除颜色缓冲区时使用的蓝色值（Blue Value）。 |

<a id="ga3bc794705028fc7e8e1b742db180055d"></a>

### `FT8XX_COLOR_RGB`

```c
#define FT8XX_COLOR_RGB ( red, green, blue )
```

```c
#include <zephyr/drivers/misc/ft8xx/ft8xx_dl.h>
```

展开值（Value）：

```c
(0x04000000 | \
(((uint32_t)(red) & 0xff) << 16) | \
(((uint32_t)(green) & 0xff) << 8) | \
((uint32_t)(blue) & 0xff))
```

设置当前红、绿、蓝颜色（Current Color）。

设置 FT8xx 颜色缓冲区（Color Buffer）的红、绿、蓝值，应用于后续绘制操作。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `red` | 当前颜色的红色值（Red Value）。 |
| `green` | 当前颜色的绿色值（Green Value）。 |
| `blue` | 当前颜色的蓝色值（Blue Value）。 |

<a id="ga135472b1cdf30d4bd69372e36c9960ce"></a>

### `FT8XX_DISPLAY`

```c
#define FT8XX_DISPLAY ( )
```

```c
#include <zephyr/drivers/misc/ft8xx/ft8xx_dl.h>
```

展开值（Value）：

```c
0
```

结束显示列表（Display List）。

FT8xx 会忽略此命令之后的所有命令。

<a id="gaf5ad60bbe137dbf64281ad8d0be051e0"></a>

### `FT8XX_EDGE_STRIP_A`

```c
#define FT8XX_EDGE_STRIP_A 7U
```

```c
#include <zephyr/drivers/misc/ft8xx/ft8xx_dl.h>
```

向上延伸的边缘带（Edge Strips）。

<a id="ga9aff3a3c58e12b990130271e845662a8"></a>

### `FT8XX_EDGE_STRIP_B`

```c
#define FT8XX_EDGE_STRIP_B 8U
```

```c
#include <zephyr/drivers/misc/ft8xx/ft8xx_dl.h>
```

向下延伸的边缘带（Edge Strips）。

<a id="ga97229abf592bba4039f19a98451cdc5b"></a>

### `FT8XX_EDGE_STRIP_L`

```c
#define FT8XX_EDGE_STRIP_L 6U
```

```c
#include <zephyr/drivers/misc/ft8xx/ft8xx_dl.h>
```

向左延伸的边缘带（Edge Strips）。

<a id="ga0b3ce2828323978e9648bfd07caa1065"></a>

### `FT8XX_EDGE_STRIP_R`

```c
#define FT8XX_EDGE_STRIP_R 5U
```

```c
#include <zephyr/drivers/misc/ft8xx/ft8xx_dl.h>
```

向右延伸的边缘带（Edge Strips）。

<a id="ga8a9d0eb6521459eb7ce50b397de194d9"></a>

### `FT8XX_END`

```c
#define FT8XX_END ( )
```

```c
#include <zephyr/drivers/misc/ft8xx/ft8xx_dl.h>
```

展开值（Value）：

```c
0x21000000
```

结束图形图元（Graphics Primitive）的绘制。

建议每个 FT8XX_BEGIN 都有对应的 FT8XX_END。不过，熟悉该机制的用户可以省略 FT8XX_END，以节省显示列表 RAM（Display List RAM）中的额外图形指令。

<a id="gac1b1188c36a4078e7db50d3c5aee7d25"></a>

### `FT8XX_LINE_STRIP`

```c
#define FT8XX_LINE_STRIP 4U
```

```c
#include <zephyr/drivers/misc/ft8xx/ft8xx_dl.h>
```

首尾连接的抗锯齿线（Anti-aliased Lines）。

<a id="ga1d22204625ef070a6b8d16af7ad97578"></a>

### `FT8XX_LINE_WIDTH`

```c
#define FT8XX_LINE_WIDTH ( width)
```

```c
#include <zephyr/drivers/misc/ft8xx/ft8xx_dl.h>
```

展开值（Value）：

```c
(0x0e000000 | ((uint32_t)(width) & 0xfff))
```

指定使用 `FT8XX_LINES` 图元绘制的线宽（Line Width）。

设置所绘制线条的宽度（Line Width）。这里的宽度是线条中心到最外侧绘制像素的距离，以 1/16 像素为单位；按此单位计，有效范围为 16–4095。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `width` | 线宽（Line Width），以 1/16 像素为单位。 |

**说明（Note）**：注意（Note）：FT8XX_LINE_WIDTH 命令会影响 FT8XX_LINES、FT8XX_LINE_STRIP、FT8XX_RECTS 以及 FT8XX_EDGE_STRIP_A /B/R/L 图元（Primitives）。

<a id="ga62bcf30c7a9eae4c468e1c7de144ad01"></a>

### `FT8XX_LINES`

```c
#define FT8XX_LINES 3U
```

```c
#include <zephyr/drivers/misc/ft8xx/ft8xx_dl.h>
```

抗锯齿线（Anti-aliased Lines），宽度为 0–4095 个 1/16 像素单位。

宽度（Width）从线条中心量到边界。

<a id="ga1d6f49b3817f9927fa1cd3cd42820490"></a>

### `FT8XX_POINTS`

```c
#define FT8XX_POINTS 2U
```

```c
#include <zephyr/drivers/misc/ft8xx/ft8xx_dl.h>
```

抗锯齿点（Anti-aliased Points），点半径为 1–256 像素。

<a id="ga05077568fea624ed7e3f9e3f6e8d72b8"></a>

### `FT8XX_RECTS`

```c
#define FT8XX_RECTS 9U
```

```c
#include <zephyr/drivers/misc/ft8xx/ft8xx_dl.h>
```

圆角矩形（Round-cornered Rectangles），可使用 `FT8XX_LINE_WIDTH` 调整圆角曲率。

<a id="gab0721051bb3f3cb9f555f696f36dfbbf"></a>

### `FT8XX_TAG`

```c
#define FT8XX_TAG ( s)
```

```c
#include <zephyr/drivers/misc/ft8xx/ft8xx_dl.h>
```

展开值（Value）：

```c
(0x03000000 | (uint8_t)(s))
```

为后续图形对象附加标签值（Tag Value）。

FT8xx 标签缓冲区（Tag Buffer）的初始值由 FT8XX_CLEAR_TAG 命令指定，并通过 FT8XX_CLEAR 命令生效。FT8XX_TAG 命令可以指定绘制到屏幕上的图形对象所使用的标签缓冲区值。除非使用 FT8XX_TAG_MASK 命令禁用，否则此标签值（Tag Value）会赋给后续所有对象。后续图形对象绘制完成后，便成功附加了该标签值。触摸带标签的图形对象时，FT800_REG_TOUCH_TAG 或 FT810_REG_TOUCH_TAG 寄存器将更新为被触摸对象的标签值。如果一个显示列表中没有 FT8XX_TAG 命令，则该列表渲染的所有图形对象被触摸时，都会在上述寄存器中报告标签值 255。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `s` | 标签值（Tag Value），范围为 1–255。 |

<a id="ga2648ab069991c02b2e8de62bf13913ab"></a>

### `FT8XX_VERTEX2F`

```c
#define FT8XX_VERTEX2F ( x, y )
```

```c
#include <zephyr/drivers/misc/ft8xx/ft8xx_dl.h>
```

展开值（Value）：

```c
(0x40000000 | \
(((int32_t)(x) & 0x7fff) << 15) | \
((int32_t)(y) & 0x7fff))
```

在指定坐标（Coordinate）开始图形图元（Graphics Primitives）操作。

坐标范围为 -16384 至 +16383，以 1/16 像素为单位。负 x 坐标表示相对于 (0, 0) 位于左侧虚拟屏幕的坐标，负 y 坐标表示位于上方虚拟屏幕的坐标。在负坐标位置绘制时，绘制结果不可见。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `x` | 有符号 x 坐标（Signed X-coordinate），精度为 1/16 像素。 |
| `y` | 有符号 y 坐标（Signed Y-coordinate），精度为 1/16 像素。 |

<a id="ga560836cd8c85599f24e5623a3e286b12"></a>

### `FT8XX_VERTEX2II`

```c
#define FT8XX_VERTEX2II ( x, y, handle, cell )
```

```c
#include <zephyr/drivers/misc/ft8xx/ft8xx_dl.h>
```

展开值（Value）：

```c
(0x80000000 | \
(((uint32_t)(x) & 0x01ff) << 21) | \
(((uint32_t)(y) & 0x01ff) << 12) | \
(((uint32_t)(handle) & 0x1f) << 7) | \
((uint32_t)(cell) & 0x7f))
```

在指定坐标（Coordinates）开始图形图元（Graphics Primitive）操作。

handle 的有效范围为 0–31，其中 16–31 的位图句柄（Bitmap Handles）专供 FT8xx 内建字体使用。

单元编号（Cell Number）是具有相同位图布局与格式的位图索引。例如，对于句柄 31，单元 65 表示最大内建字体中的字符 "A"。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `x` | x 坐标（X-coordinate），单位为像素，范围为 0–511。 |
| `y` | y 坐标（Y-coordinate），单位为像素，范围为 0–511。 |
| `handle` | 位图句柄（Bitmap Handle）。 |
| `cell` | 单元编号（Cell Number）。 |


## 11.3\_原页交叉引用（Cross References）

- [zephyr/drivers/misc/ft8xx/ft8xx_dl.h](../api_file_display_management_reference/P009_zephyr__drivers__misc__ft8xx__ft8xx_dl.h_文件参考.md)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [FT800_REG_TOUCH_TAG](../api_service_topic_reference/P010_FT8xx 内存映射（Memory map）.md#gga3c885b333acd851fed4d74886656d2c6a245e5594218702bc2c30c1b50ec44329)
- [FT810_REG_TOUCH_TAG](../api_service_topic_reference/P010_FT8xx 内存映射（Memory map）.md#gga495a8c0706389e9b3677846d772eb352a97ef048be3e5f39cc5ce6e7f12326a23)
- [int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a0c18914b3041c2f583aba76f418399c2"></a>

---

[上一章](P010_FT8xx 协处理器（Co-processor）.md) · [返回大纲](大纲.md) · [下一章](P012_FT8xx 参考 API.md)
