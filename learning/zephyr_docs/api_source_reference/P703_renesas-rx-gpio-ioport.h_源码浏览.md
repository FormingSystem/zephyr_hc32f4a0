---
id: learning.zephyr-docs.api-source-reference.page-703
title: renesas-rx-gpio-ioport.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/renesas-rx-gpio-ioport_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第703章\_renesas-rx-gpio-ioport.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/renesas-rx-gpio-ioport_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/renesas-rx-gpio-ioport_8h.html)。

## 703.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00018"></a>
<a id="l00019"></a>
<a id="l00021"></a>
<a id="l00023"></a>
<a id="l00025"></a>
<a id="l00027"></a>
<a id="l00029"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="adt-util_8h_html"></a>

```c
/*
 * Copyright (c) 2026 Renesas Electronics Corporation
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_GPIO_RENESAS_RX_GPIO_IOPORT_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_GPIO_RENESAS_RX_GPIO_IOPORT_H_

#include <zephyr/dt-bindings/dt-util.h>

#define RENESAS_GPIO_DS_POS                   (8)
#define RENESAS_GPIO_DS_MSK                   GENMASK(RENESAS_GPIO_DS_POS + 1, RENESAS_GPIO_DS_POS)
#define RENESAS_GPIO_DS_LOW                   (0x0)
#define RENESAS_GPIO_DS_MIDDLE                BIT(RENESAS_GPIO_DS_POS)
#define RENESAS_GPIO_DS_HIGH_SPEED_HIGH_DRIVE BIT(RENESAS_GPIO_DS_POS + 1)
#define RENESAS_GPIO_DS_HIGH_DRIVE            GENMASK(RENESAS_GPIO_DS_POS + 1, RENESAS_GPIO_DS_POS)

#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_GPIO_RENESAS_RX_GPIO_IOPORT_H_ */
```

## 703.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2026 Renesas Electronics Corporation。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 33 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_GPIO_RENESAS_RX_GPIO_IOPORT_H_`。

## 703.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/renesas-rx-gpio-ioport_8h.html)
- [zephyr/dt-bindings/dt-util.h](../dt_bus_binding_reference/P005_设备树绑定工具头文件参考.md)
- [dt-util.h](../dt_bus_binding_reference/P005_设备树绑定工具头文件参考.md)

---

[上一章](P702_renesas-rtk0eg0019b01002bj.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P704_renesas-rza2m-gpio.h_源码浏览.md)
