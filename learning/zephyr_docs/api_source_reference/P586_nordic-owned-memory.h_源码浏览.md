---
id: learning.zephyr-docs.api-source-reference.page-586
title: nordic-owned-memory.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/nordic-owned-memory_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第586章\_nordic-owned-memory.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/nordic-owned-memory_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/nordic-owned-memory_8h.html)。

## 586.1\_原始可见代码（Source Code）

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
<a id="l00015"></a>
<a id="l00017"></a>
<a id="l00019"></a>
<a id="l00021"></a>
<a id="l00023"></a>
<a id="l00025"></a>
<a id="l00026"></a>
<a id="l00030"></a>
<a id="l00036"></a>
<a id="l00037"></a>
<a id="l00038"></a>
<a id="l00039"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="l00044"></a>
<a id="l00045"></a>
<a id="l00046"></a>
<a id="l00047"></a>
<a id="l00048"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="adt-util_8h_html"></a>

```c
/*
 * Copyright (c) 2024 Nordic Semiconductor ASA
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_RESERVED_MEMORY_NORDIC_OWNED_MEMORY_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_RESERVED_MEMORY_NORDIC_OWNED_MEMORY_H_

#include <zephyr/dt-bindings/dt-util.h>


#define NRF_PERM_R BIT(0)
#define NRF_PERM_W BIT(1)
#define NRF_PERM_X BIT(2)
#define NRF_PERM_S BIT(3)
#define NRF_PERM_NSC BIT(4)



#define NRF_PERM_RW   (NRF_PERM_R | NRF_PERM_W)
#define NRF_PERM_RX   (NRF_PERM_R | NRF_PERM_X)
#define NRF_PERM_RS   (NRF_PERM_R | NRF_PERM_S)
#define NRF_PERM_WX   (NRF_PERM_W | NRF_PERM_X)
#define NRF_PERM_WS   (NRF_PERM_W | NRF_PERM_S)
#define NRF_PERM_XS   (NRF_PERM_X | NRF_PERM_S)
#define NRF_PERM_RWX  (NRF_PERM_R | NRF_PERM_W | NRF_PERM_X)
#define NRF_PERM_RWS  (NRF_PERM_R | NRF_PERM_W | NRF_PERM_S)
#define NRF_PERM_RXS  (NRF_PERM_R | NRF_PERM_X | NRF_PERM_S)
#define NRF_PERM_WXS  (NRF_PERM_W | NRF_PERM_X | NRF_PERM_S)
#define NRF_PERM_RWXS (NRF_PERM_R | NRF_PERM_W | NRF_PERM_X | NRF_PERM_S)


#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_RESERVED_MEMORY_NORDIC_OWNED_MEMORY_H_ */
```

## 586.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2024 Nordic Semiconductor ASA。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 53 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_RESERVED_MEMORY_NORDIC_OWNED_MEMORY_H_`。

## 586.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/nordic-owned-memory_8h.html)
- [zephyr/dt-bindings/dt-util.h](../dt_bus_binding_reference/P005_设备树绑定工具头文件参考.md)
- [dt-util.h](../dt_bus_binding_reference/P005_设备树绑定工具头文件参考.md)

---

[上一章](P585_nordic-nrf-gpio.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P587_nordic-owner-id-nrf54h20.h_源码浏览.md)
