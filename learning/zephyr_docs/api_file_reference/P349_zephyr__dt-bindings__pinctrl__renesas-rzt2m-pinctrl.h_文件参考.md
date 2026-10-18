---
id: learning.zephyr-docs.api-file-reference.page-349
title: zephyr__dt-bindings__pinctrl__renesas-rzt2m-pinctrl.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/renesas-rzt2m-pinctrl_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第349章\_zephyr\_\_dt-bindings\_\_pinctrl\_\_renesas-rzt2m-pinctrl.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/renesas-rzt2m-pinctrl_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

查看此文件的源码。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 349.1\_宏定义（Macros）

<a id="r_a3f45a2e9a92ee5884dd6020bfb77f683"></a>

```c
#define RZT2M_PINMUX(port, pin, func)
```

相关声明：[RZT2M_PINMUX](#a3f45a2e9a92ee5884dd6020bfb77f683)。

<a id="r_ade0a78ce111ddccc167c5b3a6ef1b7b0"></a>

```c
#define UART0TX_P16_5 RZT2M_PINMUX(16, 5, 1)
```

相关声明：[UART0TX_P16_5](#ade0a78ce111ddccc167c5b3a6ef1b7b0)、[RZT2M_PINMUX](#a3f45a2e9a92ee5884dd6020bfb77f683)。

<a id="r_a3881268da0d5cdb51afb0114281dcb02"></a>

```c
#define UART0RX_P16_6 RZT2M_PINMUX(16, 6, 2)
```

相关声明：[UART0RX_P16_6](#a3881268da0d5cdb51afb0114281dcb02)、[RZT2M_PINMUX](#a3f45a2e9a92ee5884dd6020bfb77f683)。

<a id="r_a5c55cbae38d8df4f6678f379cb4e5ed2"></a>

```c
#define UART3TX_P18_0 RZT2M_PINMUX(18, 0, 4)
```

相关声明：[UART3TX_P18_0](#a5c55cbae38d8df4f6678f379cb4e5ed2)、[RZT2M_PINMUX](#a3f45a2e9a92ee5884dd6020bfb77f683)。

<a id="r_a86e9102e5f4f409facbffd2e4347071d"></a>

```c
#define UART3RX_P17_7 RZT2M_PINMUX(17, 7, 4)
```

相关声明：[UART3RX_P17_7](#a86e9102e5f4f409facbffd2e4347071d)、[RZT2M_PINMUX](#a3f45a2e9a92ee5884dd6020bfb77f683)。

## 349.2\_详细说明（Detailed Documentation）

<a id="a3f45a2e9a92ee5884dd6020bfb77f683"></a>

### `RZT2M_PINMUX`

```c
#define RZT2M_PINMUX ( port, pin, func )
```

展开值（Value）：

```c
((port << 16) | (pin << 8) | func)
```

<a id="a3881268da0d5cdb51afb0114281dcb02"></a>

### `UART0RX_P16_6`

```c
#define UART0RX_P16_6 RZT2M_PINMUX(16, 6, 2)
```

<a id="ade0a78ce111ddccc167c5b3a6ef1b7b0"></a>

### `UART0TX_P16_5`

```c
#define UART0TX_P16_5 RZT2M_PINMUX(16, 5, 1)
```

<a id="a86e9102e5f4f409facbffd2e4347071d"></a>

### `UART3RX_P17_7`

```c
#define UART3RX_P17_7 RZT2M_PINMUX(17, 7, 4)
```

<a id="a5c55cbae38d8df4f6678f379cb4e5ed2"></a>

### `UART3TX_P18_0`

```c
#define UART3TX_P18_0 RZT2M_PINMUX(18, 0, 4)
```


## 349.3\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_reference/P706_renesas-rzt2m-pinctrl.h_源码浏览.md)

<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P348_zephyr__dt-bindings__gpio__renesas-rtk0eg0019b01002bj.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P350_zephyr__dt-bindings__memory-controller__renesas,ra-sdram.h_文件参考.md)
