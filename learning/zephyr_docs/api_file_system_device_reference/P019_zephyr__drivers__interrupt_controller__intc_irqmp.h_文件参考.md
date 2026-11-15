---
id: learning.zephyr-docs.api-file-system-device-reference.page-19
title: zephyr__drivers__interrupt_controller__intc_irqmp.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/intc__irqmp_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第19章\_zephyr\_\_drivers\_\_interrupt\_controller\_\_intc\_irqmp.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/intc__irqmp_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

GRLIB IRQMP中断控制器（Interrupt Controller）的驱动API。

查看此文件的源码。

<a id="details"></a>

GRLIB IRQMP中断控制器（Interrupt Controller）的驱动API。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 19.1\_函数（Functions）

<a id="r_af4d923ff11d417610c0d786784ef092b"></a>

```c
void intc_irqmp_irq_enable (unsigned int source)
```

相关声明：[intc_irqmp_irq_enable](#af4d923ff11d417610c0d786784ef092b)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)。

启用中断源（interrupt source）。

<a id="r_a6075fec44da0b8a67d90dd61477a8c3b"></a>

```c
void intc_irqmp_irq_disable (unsigned int source)
```

相关声明：[intc_irqmp_irq_disable](#a6075fec44da0b8a67d90dd61477a8c3b)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)。

禁用中断源。

<a id="r_af8642128f51648d5023d558f9762eafc"></a>

```c
int intc_irqmp_irq_is_enabled (unsigned int source)
```

相关声明：[intc_irqmp_irq_is_enabled](#af8642128f51648d5023d558f9762eafc)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)。

获取中断源（interrupt source）的使能状态。

<a id="r_a612b61d005749401a85ace84d5052d37"></a>

```c
int intc_irqmp_get_source (int irl)
```

相关声明：[intc_irqmp_get_source](#a612b61d005749401a85ace84d5052d37)。

获取处理器中断请求对应的中断源。

## 19.2\_详细说明（Detailed Documentation）

<a id="a612b61d005749401a85ace84d5052d37"></a>

### `intc_irqmp_get_source()`

```c
int intc_irqmp_get_source ( int irl)
```

获取处理器中断请求对应的中断源。

确认中断请求级别（interrupt request level）`irl`，并返回实际中断源，同时考虑 IRQMP 扩展中断。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `irl` | 处理器中断请求级别。 |

**返回（Returns）**：返回值：中断源编号。

<a id="a6075fec44da0b8a67d90dd61477a8c3b"></a>

### `intc_irqmp_irq_disable()`

```c
void intc_irqmp_irq_disable ( unsigned int source)
```

禁用中断源。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `source` | 中断源编号。 |

<a id="af4d923ff11d417610c0d786784ef092b"></a>

### `intc_irqmp_irq_enable()`

```c
void intc_irqmp_irq_enable ( unsigned int source)
```

启用中断源（interrupt source）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `source` | 中断源编号。 |

<a id="af8642128f51648d5023d558f9762eafc"></a>

### `intc_irqmp_irq_is_enabled()`

```c
int intc_irqmp_irq_is_enabled ( unsigned int source)
```

获取中断源（interrupt source）的使能状态。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `source` | 中断源编号。 |

**返回（Returns）**：返回值：中断源已启用时返回 1，否则返回 0。


## 19.3\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_reference/P393_intc_irqmp.h_源码浏览.md)
- [unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)

<a id="header-details"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P018_zephyr__input__input.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P020_zephyr__kernel__internal__mm.h_文件参考.md)
