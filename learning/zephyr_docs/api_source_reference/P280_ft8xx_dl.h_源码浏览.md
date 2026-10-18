---
id: learning.zephyr-docs.api-source-reference.page-280
title: ft8xx_dl.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/ft8xx__dl_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第280章\_ft8xx\_dl.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/ft8xx__dl_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/ft8xx__dl_8h.html)。

## 280.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00011"></a>
<a id="l00012"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00018"></a>
<a id="l00019"></a>
<a id="l00020"></a>
<a id="l00027"></a>
<a id="l00029"></a>
<a id="l00031"></a>
<a id="l00036"></a>
<a id="l00038"></a>
<a id="l00040"></a>
<a id="l00042"></a>
<a id="l00044"></a>
<a id="l00046"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="l00076"></a>
<a id="l00077"></a>
<a id="foldopen00101"></a>
<a id="l00101"></a>
<a id="l00102"></a>
<a id="l00103"></a>
<a id="foldopen00113"></a>
<a id="l00113"></a>
<a id="l00114"></a>
<a id="l00115"></a>
<a id="l00116"></a>
<a id="l00117"></a>
<a id="foldopen00128"></a>
<a id="l00128"></a>
<a id="l00129"></a>
<a id="l00130"></a>
<a id="l00131"></a>
<a id="l00132"></a>
<a id="l00138"></a>
<a id="l00139"></a>
<a id="l00147"></a>
<a id="l00148"></a>
<a id="l00162"></a>
<a id="l00163"></a>
<a id="l00183"></a>
<a id="l00184"></a>
<a id="foldopen00197"></a>
<a id="l00197"></a>
<a id="l00198"></a>
<a id="l00199"></a>
<a id="l00200"></a>
<a id="foldopen00216"></a>
<a id="l00216"></a>
<a id="l00217"></a>
<a id="l00218"></a>
<a id="l00219"></a>
<a id="l00220"></a>
<a id="l00221"></a>
<a id="l00225"></a>
<a id="l00226"></a>
<a id="l00227"></a>
<a id="l00228"></a>
<a id="l00229"></a>
<a id="l00230"></a>
<a id="astdint_8h_html"></a>

```c
/*
 * Copyright (c) 2020 Hubert Miś
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DRIVERS_MISC_FT8XX_FT8XX_DL_H_
#define ZEPHYR_INCLUDE_DRIVERS_MISC_FT8XX_FT8XX_DL_H_

#include <stdint.h>

#ifdef __cplusplus
extern "C" {
#endif


#define FT8XX_BITMAPS      1U
#define FT8XX_POINTS       2U
#define FT8XX_LINES        3U
#define FT8XX_LINE_STRIP   4U
#define FT8XX_EDGE_STRIP_R 5U
#define FT8XX_EDGE_STRIP_L 6U
#define FT8XX_EDGE_STRIP_A 7U
#define FT8XX_EDGE_STRIP_B 8U
#define FT8XX_RECTS        9U

#define FT8XX_BEGIN(prim) (0x1f000000 | ((prim) & 0x0f))

#define FT8XX_CLEAR(c, s, t) (0x26000000 | \
                ((c) ? 0x04 : 0) | ((s) ? 0x02 : 0) | ((t) ? 0x01 : 0))

#define FT8XX_CLEAR_COLOR_RGB(red, green, blue) (0x02000000 | \
                (((uint32_t)(red) & 0xff) << 16) | \
                (((uint32_t)(green) & 0xff) << 8) | \
                ((uint32_t)(blue) & 0xff))

#define FT8XX_COLOR_RGB(red, green, blue) (0x04000000 | \
                (((uint32_t)(red) & 0xff) << 16) | \
                (((uint32_t)(green) & 0xff) << 8) | \
                ((uint32_t)(blue) & 0xff))

#define FT8XX_DISPLAY() 0

#define FT8XX_END() 0x21000000

#define FT8XX_LINE_WIDTH(width) (0x0e000000 | ((uint32_t)(width) & 0xfff))

#define FT8XX_TAG(s) (0x03000000 | (uint8_t)(s))

#define FT8XX_VERTEX2F(x, y) (0x40000000 | \
                (((int32_t)(x) & 0x7fff) << 15) | \
                ((int32_t)(y) & 0x7fff))

#define FT8XX_VERTEX2II(x, y, handle, cell) (0x80000000 | \
                (((uint32_t)(x) & 0x01ff) << 21) | \
                (((uint32_t)(y) & 0x01ff) << 12) | \
                (((uint32_t)(handle) & 0x1f) << 7) | \
                ((uint32_t)(cell) & 0x7f))


#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_DRIVERS_MISC_FT8XX_FT8XX_DL_H_ */
```

## 280.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2020 Hubert Miś。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 230 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_MISC_FT8XX_FT8XX_DL_H_`。

## 280.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/ft8xx__dl_8h.html)
- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html)

---

[上一章](P279_ft8xx_copro.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P281_ft8xx_memory.h_源码浏览.md)
