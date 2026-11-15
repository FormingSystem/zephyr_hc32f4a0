---
id: learning.zephyr-docs.api-source-supplement-reference.page-136
title: nxp-s32-xspi.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/nxp-s32-xspi_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第136章\_nxp-s32-xspi.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/nxp-s32-xspi_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/nxp-s32-xspi_8h.html)。

## 136.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00008"></a>
<a id="l00009"></a>
<a id="l00010"></a>
<a id="l00011"></a>
<a id="l00012"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="adt-util_8h_html"></a>

```c
/*
 * Copyright 2025 NXP
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_XSPI_NXP_S32_XSPI_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_XSPI_NXP_S32_XSPI_H_

#include <zephyr/dt-bindings/dt-util.h>

/* The XSPI secure attribute and secure policy references */
#define NXP_S32_XSPI_NON_SECURE BIT(0)
#define NXP_S32_XSPI_SECURE     BIT(1)
#define NXP_S32_XSPI_PRIVILEGE  BIT(2)

#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_XSPI_NXP_S32_XSPI_H_ */
```

## 136.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：2025 NXP。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 12 行

XSPI 安全属性（Secure attribute）和安全策略（Secure policy）的引用。

### 注释 3：原第 17 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_XSPI_NXP_S32_XSPI_H_`。

## 136.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/nxp-s32-xspi_8h.html)
- [zephyr/dt-bindings/dt-util.h](../dt_bus_binding_reference/P005_设备树绑定工具头文件参考.md)
- [dt-util.h](../dt_bus_binding_reference/P005_设备树绑定工具头文件参考.md)

---

[上一章](P135_nxp-s32-qspi.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P137_nxp-siul2-pinctrl.h_源码浏览.md)
