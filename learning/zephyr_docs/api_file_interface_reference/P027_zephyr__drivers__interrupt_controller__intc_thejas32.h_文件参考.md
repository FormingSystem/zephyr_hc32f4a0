---
id: learning.zephyr-docs.api-file-interface-reference.page-27
title: zephyr__drivers__interrupt_controller__intc_thejas32.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/intc__thejas32_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第27章\_zephyr\_\_drivers\_\_interrupt\_controller\_\_intc\_thejas32.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/intc__thejas32_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

C-DAC THEJAS32中断控制器（Interrupt Controller）的驱动。

<a id="details"></a>

```c
#include <stdint.h>
```

查看此文件的源码。

C-DAC THEJAS32中断控制器（Interrupt Controller）的驱动。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 27.1\_函数（Functions）

<a id="r_a21f7b9f44b60ee4b83afa3cb7c03ce1e"></a>

```c
void thejas32_intc_irq_enable (uint32_t irq)
```

相关声明：[thejas32_intc_irq_enable](#a21f7b9f44b60ee4b83afa3cb7c03ce1e)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

启用中断源（interrupt source）。

<a id="r_ae81206dbe469ac478fb89330e4a2cb05"></a>

```c
void thejas32_intc_irq_disable (uint32_t irq)
```

相关声明：[thejas32_intc_irq_disable](#ae81206dbe469ac478fb89330e4a2cb05)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

禁用中断源。

<a id="r_a0a4623b59f2f106493c9046da20f7799"></a>

```c
int thejas32_intc_irq_is_enabled (uint32_t irq)
```

相关声明：[thejas32_intc_irq_is_enabled](#a0a4623b59f2f106493c9046da20f7799)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

检查中断源是否已启用。

## 27.2\_详细说明（Detailed Documentation）

<a id="ae81206dbe469ac478fb89330e4a2cb05"></a>

### `thejas32_intc_irq_disable()`

```c
void thejas32_intc_irq_disable ( uint32_t irq)
```

禁用中断源。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `irq` | 采用多级编码（multi-level encoded）的中断 ID。 |

<a id="a21f7b9f44b60ee4b83afa3cb7c03ce1e"></a>

### `thejas32_intc_irq_enable()`

```c
void thejas32_intc_irq_enable ( uint32_t irq)
```

启用中断源（interrupt source）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `irq` | 采用多级编码（multi-level encoded）的中断 ID。 |

<a id="a0a4623b59f2f106493c9046da20f7799"></a>

### `thejas32_intc_irq_is_enabled()`

```c
int thejas32_intc_irq_is_enabled ( uint32_t irq)
```

检查中断源是否已启用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `irq` | 采用多级编码（multi-level encoded）的中断 ID。 |

**返回（Returns）**：返回值：中断已启用时为非零值，否则为 0。


## 27.3\_原页交叉引用（Cross References）

- [stdint.h](../api_source_device_reference/P036_stdint.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P403_intc_thejas32.h_源码浏览.md)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)

<a id="header-details"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P026_zephyr__drivers__interrupt_controller__intc_rz_icu.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P028_zephyr__dt-bindings__interrupt-controller__ite-intc.h_文件参考.md)
