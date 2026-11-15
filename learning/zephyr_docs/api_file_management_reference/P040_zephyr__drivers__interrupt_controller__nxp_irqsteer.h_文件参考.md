---
id: learning.zephyr-docs.api-file-management-reference.page-40
title: zephyr__drivers__interrupt_controller__nxp_irqsteer.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/nxp__irqsteer_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第40章\_zephyr\_\_drivers\_\_interrupt\_controller\_\_nxp\_irqsteer.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/nxp__irqsteer_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

NXP IRQSTEER中断聚合器（Interrupt Aggregator）的驱动API。

<a id="details"></a>

```c
#include <zephyr/types.h>
```

查看此文件的源码。

NXP IRQSTEER中断聚合器（Interrupt Aggregator）的驱动API。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 40.1\_函数（Functions）

<a id="r_a804052418d11f36a4070ea82be29d9cc"></a>

```c
void nxp_irqstr_irq_enable (uint32_t irq)
```

相关声明：[nxp_irqstr_irq_enable](#a804052418d11f36a4070ea82be29d9cc)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

启用多级中断请求（multi-level IRQ）线。

<a id="r_a965f25329c0731f6932eeee7d3ee292c"></a>

```c
void nxp_irqstr_irq_disable (uint32_t irq)
```

相关声明：[nxp_irqstr_irq_disable](#a965f25329c0731f6932eeee7d3ee292c)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

禁用多级 IRQ 线。

<a id="r_a4fda601d90bcf144c9671f0ef23db22a"></a>

```c
int nxp_irqstr_irq_is_enabled (unsigned int irq)
```

相关声明：[nxp_irqstr_irq_is_enabled](#a4fda601d90bcf144c9671f0ef23db22a)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)。

获取多级 IRQ 线的使能状态。

<a id="r_a9906ded93b7efe994d60b3b66c443352"></a>

```c
void nxp_irqstr_irq_priority_set (unsigned int irq, unsigned int prio, unsigned int flags)
```

相关声明：[nxp_irqstr_irq_priority_set](#a9906ded93b7efe994d60b3b66c443352)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)、[标志（Flags）。](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)。

设置多级 IRQ 父中断线的优先级（priority）。

## 40.2\_详细说明（Detailed Documentation）

<a id="a965f25329c0731f6932eeee7d3ee292c"></a>

### `nxp_irqstr_irq_disable()`

```c
void nxp_irqstr_irq_disable ( uint32_t irq)
```

禁用多级 IRQ 线。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `irq` | 采用多级编码的 IRQ 编号。 |

<a id="a804052418d11f36a4070ea82be29d9cc"></a>

### `nxp_irqstr_irq_enable()`

```c
void nxp_irqstr_irq_enable ( uint32_t irq)
```

启用多级中断请求（multi-level IRQ）线。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `irq` | 采用多级编码的 IRQ 编号。 |

<a id="a4fda601d90bcf144c9671f0ef23db22a"></a>

### `nxp_irqstr_irq_is_enabled()`

```c
int nxp_irqstr_irq_is_enabled ( unsigned int irq)
```

获取多级 IRQ 线的使能状态。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `irq` | 采用多级编码的 IRQ 编号。 |

**返回（Returns）**：返回值：IRQ 线已启用时返回 1，否则返回 0。

<a id="a9906ded93b7efe994d60b3b66c443352"></a>

### `nxp_irqstr_irq_priority_set()`

```c
void nxp_irqstr_irq_priority_set ( unsigned int irq, unsigned int prio, unsigned int flags )
```

设置多级 IRQ 父中断线的优先级（priority）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `irq` | 采用多级编码的 IRQ 编号。 |
| `prio` | 中断优先级。 |
| `flags` | 架构专有的 IRQ 配置标志。 |


## 40.3\_原页交叉引用（Cross References）

- [zephyr/types.h](../api_source_compiler_device_reference/P014_types.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P620_nxp_irqsteer.h_源码浏览.md)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)
- [标志（Flags）。](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)

<a id="header-details"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P039_zephyr__dt-bindings__reserved-memory__nordic-owned-memory.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P041_zephyr__bluetooth__mesh__proxy.h_文件参考.md)
