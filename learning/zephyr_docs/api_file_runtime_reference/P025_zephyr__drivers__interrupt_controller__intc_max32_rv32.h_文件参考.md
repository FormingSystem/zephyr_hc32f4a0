---
id: learning.zephyr-docs.api-file-runtime-reference.page-25
title: zephyr__drivers__interrupt_controller__intc_max32_rv32.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/intc__max32__rv32_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第25章\_zephyr\_\_drivers\_\_interrupt\_controller\_\_intc\_max32\_rv32.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/intc__max32__rv32_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

MAX32 RV32中断控制器（Interrupt Controller）的API。

查看此文件的源码。

<a id="details"></a>

MAX32 RV32 中断控制器 API（Interrupt Controller API）。本 API 用于与 MAX32 RV32 中断控制器交互。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 25.1\_函数（Functions）

<a id="r_aded0ce31f6ebff4efe19773abddb71f6"></a>

```c
void intc_max32_rv32_irq_clear_pending (int source)
```

相关声明：[intc_max32_rv32_irq_clear_pending](#aded0ce31f6ebff4efe19773abddb71f6)。

清除控制器（Controller）中处于挂起状态的中断线（Pending Interrupt Line）。

## 25.2\_详细说明（Detailed Documentation）

<a id="aded0ce31f6ebff4efe19773abddb71f6"></a>

### `intc_max32_rv32_irq_clear_pending()`

```c
void intc_max32_rv32_irq_clear_pending ( int source)
```

清除控制器（Controller）中处于挂起状态的中断线（Pending Interrupt Line）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `source` | 需要清除挂起状态（Pending Status）的中断请求编号（IRQ Number）。 |


## 25.3\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_reference/P394_intc_max32_rv32.h_源码浏览.md)

<a id="header-details"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P024_zephyr__input__input_keymap.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P026_zephyr__posix__sys__ioctl.h_文件参考.md)
