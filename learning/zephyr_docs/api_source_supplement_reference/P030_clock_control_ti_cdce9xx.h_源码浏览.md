---
id: learning.zephyr-docs.api-source-supplement-reference.page-30
title: clock_control_ti_cdce9xx.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/clock__control__ti__cdce9xx_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第30章\_clock\_control\_ti\_cdce9xx.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/clock__control__ti__cdce9xx_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/clock__control__ti__cdce9xx_8h.html)。

## 30.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00011"></a>
<a id="l00012"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00022"></a>
<a id="l00023"></a>
<a id="l00024"></a>
<a id="l00025"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="l00034"></a>
<a id="l00035"></a>
<a id="l00036"></a>
<a id="l00037"></a>
<a id="l00038"></a>
<a id="l00039"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="l00044"></a>
<a id="l00045"></a>
<a id="aclock__control_8h_html"></a>

```c
/*
 * Copyright (c) 2026 Carl Zeiss Meditec AG
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DRIVERS_CLOCK_CONTROL_CLOCK_CONTROL_TI_CDCE9XX_H_
#define ZEPHYR_INCLUDE_DRIVERS_CLOCK_CONTROL_CLOCK_CONTROL_TI_CDCE9XX_H_

#include <zephyr/drivers/clock_control.h>


#ifdef __cplusplus
extern "C" {
#endif

/* Keep the order, the driver relies on it. */
#define CLOCK_CONTROL_TI_CDCE9XX_ALL (CLOCK_CONTROL_SUBSYS_ALL)
#define CLOCK_CONTROL_TI_CDCE9XX_Y1  ((clock_control_subsys_t)1)
#define CLOCK_CONTROL_TI_CDCE9XX_Y2  ((clock_control_subsys_t)2)
#define CLOCK_CONTROL_TI_CDCE9XX_Y3  ((clock_control_subsys_t)3)
#define CLOCK_CONTROL_TI_CDCE9XX_Y4  ((clock_control_subsys_t)4)
#define CLOCK_CONTROL_TI_CDCE9XX_Y5  ((clock_control_subsys_t)5)
#define CLOCK_CONTROL_TI_CDCE9XX_Y6  ((clock_control_subsys_t)6)
#define CLOCK_CONTROL_TI_CDCE9XX_Y7  ((clock_control_subsys_t)7)
#define CLOCK_CONTROL_TI_CDCE9XX_Y8  ((clock_control_subsys_t)8)
#define CLOCK_CONTROL_TI_CDCE9XX_Y9  ((clock_control_subsys_t)9)

#ifdef __cplusplus
}
#endif


#endif /* ZEPHYR_INCLUDE_DRIVERS_CLOCK_CONTROL_CLOCK_CONTROL_TI_CDCE9XX_H_ */
```

## 30.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2026 Carl Zeiss Meditec AG。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 27 行

保持此顺序，驱动程序依赖它。

### 注释 3：原第 45 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_CLOCK_CONTROL_CLOCK_CONTROL_TI_CDCE9XX_H_`。

## 30.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/clock__control__ti__cdce9xx_8h.html)
- [zephyr/drivers/clock_control.h](../timer_reference/P095_时钟控制头文件参考.md)
- [clock_control.h](../timer_reference/P095_时钟控制头文件参考.md)

---

[上一章](P029_clock_control_rts5912.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P031_cobs.h_源码浏览.md)
