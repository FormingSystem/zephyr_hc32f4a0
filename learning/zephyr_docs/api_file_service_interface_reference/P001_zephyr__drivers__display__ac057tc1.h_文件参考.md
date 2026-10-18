---
id: learning.zephyr-docs.api-file-service-interface-reference.page-1
title: zephyr__drivers__display__ac057tc1.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/ac057tc1_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第1章\_zephyr\_\_drivers\_\_display\_\_ac057tc1.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/ac057tc1_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

AC057TC1七色电子墨水显示器（E-Ink Display）的调色板定义。

<a id="details"></a>

```c
#include <zephyr/drivers/display.h>
```

查看此文件的源码。

AC057TC1七色电子墨水显示器（E-Ink Display）的调色板定义。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 1.1\_宏定义（Macros）

<a id="define-members-0"></a>

### AC057TC1 颜色定义（Color Definitions）

显示器支持 7 种颜色，通过 3 位索引（3-bit Indices）`0–6` 映射。

`display_capabilities` 中的调色板（Color Palette）提供这些颜色的 ARGB8888 表示，供用户界面（UI）渲染使用，例如 LVGL。

控制器渲染时直接使用索引值（Index Values）；从 ARGB8888 转换到硬件颜色表示的方式由应用程序决定。

<a id="r_gaddc8c85260f4711008145f4dc9adfda5"></a>

```c
#define AC057TC1_COLOR_BLACK 0x00
```

相关声明：[AC057TC1_COLOR_BLACK](https://docs.zephyrproject.org/latest/doxygen/html/group__ac057tc1__display__interface.html#gaddc8c85260f4711008145f4dc9adfda5)。

黑色索引（Black color index）。

<a id="r_gab14e0c1ddc7cdf1ade0007aa1ddc48e0"></a>

```c
#define AC057TC1_COLOR_WHITE 0x01
```

相关声明：[AC057TC1_COLOR_WHITE](https://docs.zephyrproject.org/latest/doxygen/html/group__ac057tc1__display__interface.html#gab14e0c1ddc7cdf1ade0007aa1ddc48e0)。

白色索引（White color index）。

<a id="r_gad6815dcf9640db77784760fd497d4470"></a>

```c
#define AC057TC1_COLOR_GREEN 0x02
```

相关声明：[AC057TC1_COLOR_GREEN](https://docs.zephyrproject.org/latest/doxygen/html/group__ac057tc1__display__interface.html#gad6815dcf9640db77784760fd497d4470)。

绿色索引（Green color index）。

<a id="r_ga4c7ec1517bcf0a759e4d90a50de90322"></a>

```c
#define AC057TC1_COLOR_BLUE 0x03
```

相关声明：[AC057TC1_COLOR_BLUE](https://docs.zephyrproject.org/latest/doxygen/html/group__ac057tc1__display__interface.html#ga4c7ec1517bcf0a759e4d90a50de90322)。

蓝色索引（Blue color index）。

<a id="r_ga59e811b002e9625d53ef4865a65a09d1"></a>

```c
#define AC057TC1_COLOR_RED 0x04
```

相关声明：[AC057TC1_COLOR_RED](https://docs.zephyrproject.org/latest/doxygen/html/group__ac057tc1__display__interface.html#ga59e811b002e9625d53ef4865a65a09d1)。

红色索引（Red color index）。

<a id="r_ga610ac37a47780ed653c2436a95ffc124"></a>

```c
#define AC057TC1_COLOR_YELLOW 0x05
```

相关声明：[AC057TC1_COLOR_YELLOW](https://docs.zephyrproject.org/latest/doxygen/html/group__ac057tc1__display__interface.html#ga610ac37a47780ed653c2436a95ffc124)。

黄色索引（Yellow color index）。

<a id="r_gae55d18fa0a1a32ae917d7da3f2af9298"></a>

```c
#define AC057TC1_COLOR_ORANGE 0x06
```

相关声明：[AC057TC1_COLOR_ORANGE](https://docs.zephyrproject.org/latest/doxygen/html/group__ac057tc1__display__interface.html#gae55d18fa0a1a32ae917d7da3f2af9298)。

橙色索引（Orange Color Index）。

<a id="r_ga3d612bff27859fad0baa5f6286b3999a"></a>

```c
#define AC057TC1_COLOR_PALETTE_SIZE 7
```

相关声明：[AC057TC1_COLOR_PALETTE_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__ac057tc1__display__interface.html#ga3d612bff27859fad0baa5f6286b3999a)。

调色板（Palette）中的颜色数量。


## 1.2\_原页交叉引用（Cross References）

- [zephyr/drivers/display.h](../api_source_supplement_reference/P041_display.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P002_ac057tc1.h_源码浏览.md)
- [display_capabilities](../hardware/P216_显示能力结构.md)
- [AC057TC1_COLOR_BLACK](https://docs.zephyrproject.org/latest/doxygen/html/group__ac057tc1__display__interface.html#gaddc8c85260f4711008145f4dc9adfda5)
- [AC057TC1_COLOR_WHITE](https://docs.zephyrproject.org/latest/doxygen/html/group__ac057tc1__display__interface.html#gab14e0c1ddc7cdf1ade0007aa1ddc48e0)
- [AC057TC1_COLOR_GREEN](https://docs.zephyrproject.org/latest/doxygen/html/group__ac057tc1__display__interface.html#gad6815dcf9640db77784760fd497d4470)
- [AC057TC1_COLOR_BLUE](https://docs.zephyrproject.org/latest/doxygen/html/group__ac057tc1__display__interface.html#ga4c7ec1517bcf0a759e4d90a50de90322)
- [AC057TC1_COLOR_RED](https://docs.zephyrproject.org/latest/doxygen/html/group__ac057tc1__display__interface.html#ga59e811b002e9625d53ef4865a65a09d1)
- [AC057TC1_COLOR_YELLOW](https://docs.zephyrproject.org/latest/doxygen/html/group__ac057tc1__display__interface.html#ga610ac37a47780ed653c2436a95ffc124)
- [AC057TC1_COLOR_ORANGE](https://docs.zephyrproject.org/latest/doxygen/html/group__ac057tc1__display__interface.html#gae55d18fa0a1a32ae917d7da3f2af9298)
- [AC057TC1_COLOR_PALETTE_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__ac057tc1__display__interface.html#ga3d612bff27859fad0baa5f6286b3999a)

<a id="header-details"></a>

---

[返回大纲](大纲.md) · [下一章](P002_zephyr__drivers__mfd__ad559x.h_文件参考.md)
