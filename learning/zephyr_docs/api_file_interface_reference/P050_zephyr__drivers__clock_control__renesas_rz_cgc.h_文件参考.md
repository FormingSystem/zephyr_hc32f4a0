---
id: learning.zephyr-docs.api-file-interface-reference.page-50
title: zephyr__drivers__clock_control__renesas_rz_cgc.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/renesas__rz__cgc_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第50章\_zephyr\_\_drivers\_\_clock\_control\_\_renesas\_rz\_cgc.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/renesas__rz__cgc_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Renesas RZ设备的时钟源分频器与倍频器辅助接口（Clock Source Divider and Multiplier Helpers）。

<a id="details"></a>

```c
#include <zephyr/drivers/clock_control.h>
```

查看此文件的源码。

Renesas RZ设备的时钟源分频器与倍频器辅助接口（Clock Source Divider and Multiplier Helpers）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 50.1\_宏定义（Macros）

<a id="r_gae05eccc27dccf3896e0eb771ca328902"></a>

```c
#define RZ_CGC_SUBCLK_DIV(subclk)
```

相关声明：[RZ_CGC_SUBCLK_DIV](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__renesas__rz.html#gae05eccc27dccf3896e0eb771ca328902)。

根据子时钟（sub-clock）的设备树 `div` 属性确定分频常量（divider constant）。

<a id="r_gafaf026fec58c9ba14630f8d9257a847a"></a>

```c
#define RZ_CGC_SUBCLK_MUL(subclk)
```

相关声明：[RZ_CGC_SUBCLK_MUL](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__renesas__rz.html#gafaf026fec58c9ba14630f8d9257a847a)。

根据子时钟的设备树 `mul` 属性确定倍频常量（multiplier constant）。

<a id="r_ga2a2bff8417f805667752f2ea509907ae"></a>

```c
#define RZ_CGC_DIV_CKIO(n)
```

相关声明：[RZ_CGC_DIV_CKIO](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__renesas__rz.html#ga2a2bff8417f805667752f2ea509907ae)。

CKIO 时钟分频器辅助宏。

<a id="r_ga99b067cbcd645b89f1262ba3311cb9ef"></a>

```c
#define RZ_CGC_MUL_CPU0CLK(n)
```

相关声明：[RZ_CGC_MUL_CPU0CLK](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__renesas__rz.html#ga99b067cbcd645b89f1262ba3311cb9ef)。

CPU0 时钟倍频器（clock multiplier）辅助宏。

<a id="r_gac303412a881625281bce2f3f9a20f352"></a>

```c
#define RZ_CGC_MUL_CPU1CLK(n)
```

相关声明：[RZ_CGC_MUL_CPU1CLK](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__renesas__rz.html#gac303412a881625281bce2f3f9a20f352)。

CPU1 时钟倍频器辅助宏。


## 50.2\_原页交叉引用（Cross References）

- [zephyr/drivers/clock_control.h](../timer_reference/P096_时钟控制完整头文件.md)
- [查看此文件的源码。](../api_source_reference/P713_renesas_rz_cgc.h_源码浏览.md)
- [RZ_CGC_SUBCLK_DIV](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__renesas__rz.html#gae05eccc27dccf3896e0eb771ca328902)
- [RZ_CGC_SUBCLK_MUL](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__renesas__rz.html#gafaf026fec58c9ba14630f8d9257a847a)
- [RZ_CGC_DIV_CKIO](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__renesas__rz.html#ga2a2bff8417f805667752f2ea509907ae)
- [RZ_CGC_MUL_CPU0CLK](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__renesas__rz.html#ga99b067cbcd645b89f1262ba3311cb9ef)
- [RZ_CGC_MUL_CPU1CLK](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__renesas__rz.html#gac303412a881625281bce2f3f9a20f352)

<a id="header-details"></a>

---

[上一章](P049_zephyr__drivers__clock_control__renesas_rx_cgc.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P051_zephyr__sensing__sensing_sensor.h_文件参考.md)
