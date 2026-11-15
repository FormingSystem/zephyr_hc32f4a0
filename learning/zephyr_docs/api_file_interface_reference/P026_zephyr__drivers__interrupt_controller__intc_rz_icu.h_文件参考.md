---
id: learning.zephyr-docs.api-file-interface-reference.page-26
title: zephyr__drivers__interrupt_controller__intc_rz_icu.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/intc__rz__icu_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第26章\_zephyr\_\_drivers\_\_interrupt\_controller\_\_intc\_rz\_icu.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/intc__rz__icu_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Renesas RZ中断控制器（Interrupt Controller）的API。

<a id="details"></a>

```c
#include <bsp_api.h>
```

查看此文件的源码。

Renesas RZ 中断控制器（Interrupt Controller）API。用于支持可选中断（selectable interrupts）的 Renesas RZ 中断控制单元（Interrupt Controller Unit）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 26.1\_函数（Functions）

<a id="r_a10ad39137e6677fef333b8ef183fd5b0"></a>

```c
int icu_connect_irq_event (int irq, elc_event_t event)
```

相关声明：[icu_connect_irq_event](#a10ad39137e6677fef333b8ef183fd5b0)。

将中断 ID 连接到事件编号（event number）。

## 26.2\_详细说明（Detailed Documentation）

<a id="a10ad39137e6677fef333b8ef183fd5b0"></a>

### `icu_connect_irq_event()`

```c
int icu_connect_irq_event ( int irq, elc_event_t event )
```

将中断 ID 连接到事件编号（event number）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `irq` | 中断标识符（interrupt ID）。 |
| `event` | 事件编号（event number）。 |

**返回（Returns）**：返回值：成功时返回 0，出错时返回负值。


## 26.3\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_reference/P401_intc_rz_icu.h_源码浏览.md)

<a id="header-details"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P025_zephyr__input__input_touch.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P027_zephyr__drivers__interrupt_controller__intc_thejas32.h_文件参考.md)
