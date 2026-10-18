---
id: learning.zephyr-docs.api-protocol-topic-reference.page-14
title: 瑞萨（Renesas）RZ 时钟生成电路（CGC）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__renesas__rz.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第14章\_瑞萨（Renesas）RZ 时钟生成电路（CGC）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__renesas__rz.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

<a id="details"></a>



<a id="header-files"></a>
<a id="files"></a>

## 14.1\_文件（Files）

<a id="r_renesas_5Frz_5Fcgc_2Eh"></a>

```c
file renesas_rz_cgc.h
```

相关声明：[renesas_rz_cgc.h](../api_file_interface_reference/P050_zephyr__drivers__clock_control__renesas_rz_cgc.h_文件参考.md)。

Renesas RZ设备的时钟源分频器与倍频器辅助接口（Clock Source Divider and Multiplier Helpers）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 14.2\_宏定义（Macros）

<a id="r_gae05eccc27dccf3896e0eb771ca328902"></a>

```c
#define RZ_CGC_SUBCLK_DIV(subclk)
```

相关声明：[RZ_CGC_SUBCLK_DIV](#gae05eccc27dccf3896e0eb771ca328902)。

根据子时钟（sub-clock）的设备树 `div` 属性确定分频常量（divider constant）。

<a id="r_gafaf026fec58c9ba14630f8d9257a847a"></a>

```c
#define RZ_CGC_SUBCLK_MUL(subclk)
```

相关声明：[RZ_CGC_SUBCLK_MUL](#gafaf026fec58c9ba14630f8d9257a847a)。

根据子时钟的设备树 `mul` 属性确定倍频常量（multiplier constant）。

<a id="r_ga2a2bff8417f805667752f2ea509907ae"></a>

```c
#define RZ_CGC_DIV_CKIO(n)
```

相关声明：[RZ_CGC_DIV_CKIO](#ga2a2bff8417f805667752f2ea509907ae)。

CKIO 时钟分频器辅助宏。

<a id="r_ga99b067cbcd645b89f1262ba3311cb9ef"></a>

```c
#define RZ_CGC_MUL_CPU0CLK(n)
```

相关声明：[RZ_CGC_MUL_CPU0CLK](#ga99b067cbcd645b89f1262ba3311cb9ef)。

CPU0 时钟倍频器（clock multiplier）辅助宏。

<a id="r_gac303412a881625281bce2f3f9a20f352"></a>

```c
#define RZ_CGC_MUL_CPU1CLK(n)
```

相关声明：[RZ_CGC_MUL_CPU1CLK](#gac303412a881625281bce2f3f9a20f352)。

CPU1 时钟倍频器辅助宏。

## 14.3\_详细说明（Detailed Documentation）

<a id="ga2a2bff8417f805667752f2ea509907ae"></a>

### `RZ_CGC_DIV_CKIO`

```c
#define RZ_CGC_DIV_CKIO ( n)
```

```c
#include <zephyr/drivers/clock_control/renesas_rz_cgc.h>
```

展开值（Value）：

```c
UTIL_CAT(BSP_CLOCKS_CKIO_ICLK_DIV, n)
```

CKIO 时钟分频器辅助宏。

<a id="ga99b067cbcd645b89f1262ba3311cb9ef"></a>

### `RZ_CGC_MUL_CPU0CLK`

```c
#define RZ_CGC_MUL_CPU0CLK ( n)
```

```c
#include <zephyr/drivers/clock_control/renesas_rz_cgc.h>
```

展开值（Value）：

```c
UTIL_CAT(BSP_CLOCKS_FSELCPU0_ICLK_MUL, n)
```

CPU0 时钟倍频器（clock multiplier）辅助宏。

<a id="gac303412a881625281bce2f3f9a20f352"></a>

### `RZ_CGC_MUL_CPU1CLK`

```c
#define RZ_CGC_MUL_CPU1CLK ( n)
```

```c
#include <zephyr/drivers/clock_control/renesas_rz_cgc.h>
```

展开值（Value）：

```c
UTIL_CAT(BSP_CLOCKS_FSELCPU1_ICLK_MUL, n)
```

CPU1 时钟倍频器辅助宏。

<a id="gae05eccc27dccf3896e0eb771ca328902"></a>

### `RZ_CGC_SUBCLK_DIV`

```c
#define RZ_CGC_SUBCLK_DIV ( subclk)
```

```c
#include <zephyr/drivers/clock_control/renesas_rz_cgc.h>
```

展开值（Value）：

```c
UTIL_CAT(RZ_CGC_DIV_, DT_NODE_FULL_NAME_UPPER_TOKEN(subclk))                               \
(DT_PROP(subclk, div))
```

根据子时钟（sub-clock）的设备树 `div` 属性确定分频常量（divider constant）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `subclk` | 子时钟（sub-clock）的设备树节点标识符。 |

<a id="gafaf026fec58c9ba14630f8d9257a847a"></a>

### `RZ_CGC_SUBCLK_MUL`

```c
#define RZ_CGC_SUBCLK_MUL ( subclk)
```

```c
#include <zephyr/drivers/clock_control/renesas_rz_cgc.h>
```

展开值（Value）：

```c
UTIL_CAT(RZ_CGC_MUL_, DT_NODE_FULL_NAME_UPPER_TOKEN(subclk))                               \
(DT_PROP(subclk, mul))
```

根据子时钟的设备树 `mul` 属性确定倍频常量（multiplier constant）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `subclk` | 子时钟（sub-clock）的设备树节点标识符。 |


## 14.4\_原页交叉引用（Cross References）

- [renesas_rz_cgc.h](../api_file_interface_reference/P050_zephyr__drivers__clock_control__renesas_rz_cgc.h_文件参考.md)
- [UTIL_CAT](../util_reference/P006_内部宏工具头文件参考.md#a7e7766e792d1638bfbbc9d0f328d3d0d)
- [DT_NODE_FULL_NAME_UPPER_TOKEN](../dt_identity_reference/P001_设备树节点标识宏.md#gab966ae50efe46cc3a54f086f508edb3b)
- [DT_PROP](../dt_property_reference/P001_设备树属性读取宏.md#ga8e1fd9ebacd85d2013df027d041d506b)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="autil__internal_8h_html_a7e7766e792d1638bfbbc9d0f328d3d0d"></a>
<a id="agroup__devicetree-generic-id_html_gab966ae50efe46cc3a54f086f508edb3b"></a>
<a id="agroup__devicetree-generic-prop_html_ga8e1fd9ebacd85d2013df027d041d506b"></a>

---

[上一章](P013_瑞萨（Renesas）RX 时钟生成电路（CGC）.md) · [返回大纲](大纲.md) · [下一章](P015_动态主机配置协议第 6 版（DHCPv6）.md)
