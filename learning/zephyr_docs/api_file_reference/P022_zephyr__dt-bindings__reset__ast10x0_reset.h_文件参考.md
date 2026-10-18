---
id: learning.zephyr-docs.api-file-reference.page-22
title: zephyr__dt-bindings__reset__ast10x0_reset.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/ast10x0__reset_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第22章\_zephyr\_\_dt-bindings\_\_reset\_\_ast10x0\_reset.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/ast10x0__reset_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

查看此文件的源码。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 22.1\_宏定义（Macros）

<a id="r_a58f51601c877080d344167774969c9b4"></a>

```c
#define ASPEED_RESET_GRP_0_OFFSET (0)
```

相关声明：[ASPEED_RESET_GRP_0_OFFSET](#a58f51601c877080d344167774969c9b4)。

<a id="r_af60cf3c19df220966fcc6aeb553677a8"></a>

```c
#define ASPEED_RESET_GRP_1_OFFSET (32)
```

相关声明：[ASPEED_RESET_GRP_1_OFFSET](#af60cf3c19df220966fcc6aeb553677a8)。

<a id="r_a18a69d795a56e9077333b8d50fac36b0"></a>

```c
#define ASPEED_RESET_HACE (ASPEED_RESET_GRP_0_OFFSET + 4)
```

相关声明：[ASPEED_RESET_HACE](#a18a69d795a56e9077333b8d50fac36b0)、[ASPEED_RESET_GRP_0_OFFSET](#a58f51601c877080d344167774969c9b4)。

<a id="r_aa63cefb88f641936f49389acaff04cbc"></a>

```c
#define ASPEED_RESET_USB (ASPEED_RESET_GRP_0_OFFSET + 3)
```

相关声明：[ASPEED_RESET_USB](#aa63cefb88f641936f49389acaff04cbc)、[ASPEED_RESET_GRP_0_OFFSET](#a58f51601c877080d344167774969c9b4)。

<a id="r_a54fbdaa166cf43dadb6a4d9777b581c3"></a>

```c
#define ASPEED_RESET_SRAM (ASPEED_RESET_GRP_0_OFFSET + 0)
```

相关声明：[ASPEED_RESET_SRAM](#a54fbdaa166cf43dadb6a4d9777b581c3)、[ASPEED_RESET_GRP_0_OFFSET](#a58f51601c877080d344167774969c9b4)。

<a id="r_a19e6207b2212a0a58b8dc5c736748df1"></a>

```c
#define ASPEED_RESET_UART4 (ASPEED_RESET_GRP_1_OFFSET + 31)
```

相关声明：[ASPEED_RESET_UART4](#a19e6207b2212a0a58b8dc5c736748df1)、[ASPEED_RESET_GRP_1_OFFSET](#af60cf3c19df220966fcc6aeb553677a8)。

<a id="r_a31e0692dd65c0adbe937daebee4477e2"></a>

```c
#define ASPEED_RESET_UART3 (ASPEED_RESET_GRP_1_OFFSET + 30)
```

相关声明：[ASPEED_RESET_UART3](#a31e0692dd65c0adbe937daebee4477e2)、[ASPEED_RESET_GRP_1_OFFSET](#af60cf3c19df220966fcc6aeb553677a8)。

<a id="r_a67087547f237de76d2ab1e9c2fd774f1"></a>

```c
#define ASPEED_RESET_UART2 (ASPEED_RESET_GRP_1_OFFSET + 29)
```

相关声明：[ASPEED_RESET_UART2](#a67087547f237de76d2ab1e9c2fd774f1)、[ASPEED_RESET_GRP_1_OFFSET](#af60cf3c19df220966fcc6aeb553677a8)。

<a id="r_ab7429f58459c26d3cf637e4d9e764d67"></a>

```c
#define ASPEED_RESET_UART1 (ASPEED_RESET_GRP_1_OFFSET + 28)
```

相关声明：[ASPEED_RESET_UART1](#ab7429f58459c26d3cf637e4d9e764d67)、[ASPEED_RESET_GRP_1_OFFSET](#af60cf3c19df220966fcc6aeb553677a8)。

<a id="r_a2000c2cd1474abe2acf6716293f9a656"></a>

```c
#define ASPEED_RESET_JTAG_M0 (ASPEED_RESET_GRP_1_OFFSET + 26)
```

相关声明：[ASPEED_RESET_JTAG_M0](#a2000c2cd1474abe2acf6716293f9a656)、[ASPEED_RESET_GRP_1_OFFSET](#af60cf3c19df220966fcc6aeb553677a8)。

<a id="r_a76bc43a3b57f919db372e4a79dc79b6f"></a>

```c
#define ASPEED_RESET_ESPI (ASPEED_RESET_GRP_1_OFFSET + 25)
```

相关声明：[ASPEED_RESET_ESPI](#a76bc43a3b57f919db372e4a79dc79b6f)、[ASPEED_RESET_GRP_1_OFFSET](#af60cf3c19df220966fcc6aeb553677a8)。

<a id="r_ac8cad68c9911554194574d460d3f3814"></a>

```c
#define ASPEED_RESET_ADC (ASPEED_RESET_GRP_1_OFFSET + 23)
```

相关声明：[ASPEED_RESET_ADC](#ac8cad68c9911554194574d460d3f3814)、[ASPEED_RESET_GRP_1_OFFSET](#af60cf3c19df220966fcc6aeb553677a8)。

<a id="r_a8e20719b17e4f21c9673a7e740362b8e"></a>

```c
#define ASPEED_RESET_JTAG_M1 (ASPEED_RESET_GRP_1_OFFSET + 22)
```

相关声明：[ASPEED_RESET_JTAG_M1](#a8e20719b17e4f21c9673a7e740362b8e)、[ASPEED_RESET_GRP_1_OFFSET](#af60cf3c19df220966fcc6aeb553677a8)。

<a id="r_ae546e699360d23e89ddba7310d637c8a"></a>

```c
#define ASPEED_RESET_MAC (ASPEED_RESET_GRP_1_OFFSET + 20)
```

相关声明：[ASPEED_RESET_MAC](#ae546e699360d23e89ddba7310d637c8a)、[ASPEED_RESET_GRP_1_OFFSET](#af60cf3c19df220966fcc6aeb553677a8)。

<a id="r_a6eb1a65fee7f7d589e5c40acb06a59a7"></a>

```c
#define ASPEED_RESET_I3C3 (ASPEED_RESET_GRP_1_OFFSET + 11)
```

相关声明：[ASPEED_RESET_I3C3](#a6eb1a65fee7f7d589e5c40acb06a59a7)、[ASPEED_RESET_GRP_1_OFFSET](#af60cf3c19df220966fcc6aeb553677a8)。

<a id="r_a3e76867407846a68533e1ef13e5612e0"></a>

```c
#define ASPEED_RESET_I3C2 (ASPEED_RESET_GRP_1_OFFSET + 10)
```

相关声明：[ASPEED_RESET_I3C2](#a3e76867407846a68533e1ef13e5612e0)、[ASPEED_RESET_GRP_1_OFFSET](#af60cf3c19df220966fcc6aeb553677a8)。

<a id="r_a792d63822aaf04bcf8670471c6f5cb5c"></a>

```c
#define ASPEED_RESET_I3C1 (ASPEED_RESET_GRP_1_OFFSET + 9)
```

相关声明：[ASPEED_RESET_I3C1](#a792d63822aaf04bcf8670471c6f5cb5c)、[ASPEED_RESET_GRP_1_OFFSET](#af60cf3c19df220966fcc6aeb553677a8)。

<a id="r_a392ac704a9bbddcee588e9f52af8557e"></a>

```c
#define ASPEED_RESET_I3C0 (ASPEED_RESET_GRP_1_OFFSET + 8)
```

相关声明：[ASPEED_RESET_I3C0](#a392ac704a9bbddcee588e9f52af8557e)、[ASPEED_RESET_GRP_1_OFFSET](#af60cf3c19df220966fcc6aeb553677a8)。

<a id="r_a49e0d2e074659166bb20ad0a9a603435"></a>

```c
#define ASPEED_RESET_I3C (ASPEED_RESET_GRP_1_OFFSET + 7)
```

相关声明：[ASPEED_RESET_I3C](#a49e0d2e074659166bb20ad0a9a603435)、[ASPEED_RESET_GRP_1_OFFSET](#af60cf3c19df220966fcc6aeb553677a8)。

<a id="r_a49f53d3791ab6d0104837204c31eb1ad"></a>

```c
#define ASPEED_RESET_PWM_TACH (ASPEED_RESET_GRP_1_OFFSET + 5)
```

相关声明：[ASPEED_RESET_PWM_TACH](#a49f53d3791ab6d0104837204c31eb1ad)、[ASPEED_RESET_GRP_1_OFFSET](#af60cf3c19df220966fcc6aeb553677a8)。

<a id="r_a6cab61e115cc50636d3c5aa8b509f5c5"></a>

```c
#define ASPEED_RESET_PECI (ASPEED_RESET_GRP_1_OFFSET + 4)
```

相关声明：[ASPEED_RESET_PECI](#a6cab61e115cc50636d3c5aa8b509f5c5)、[ASPEED_RESET_GRP_1_OFFSET](#af60cf3c19df220966fcc6aeb553677a8)。

<a id="r_abb494d1ccc9ab01d50fc21bb7c2eb7de"></a>

```c
#define ASPEED_RESET_MII (ASPEED_RESET_GRP_1_OFFSET + 3)
```

相关声明：[ASPEED_RESET_MII](#abb494d1ccc9ab01d50fc21bb7c2eb7de)、[ASPEED_RESET_GRP_1_OFFSET](#af60cf3c19df220966fcc6aeb553677a8)。

<a id="r_a235bf82edd62f2f72fb9de4efa11c7f9"></a>

```c
#define ASPEED_RESET_I2C (ASPEED_RESET_GRP_1_OFFSET + 2)
```

相关声明：[ASPEED_RESET_I2C](#a235bf82edd62f2f72fb9de4efa11c7f9)、[ASPEED_RESET_GRP_1_OFFSET](#af60cf3c19df220966fcc6aeb553677a8)。

<a id="r_a93f2fc81c8a9cdfee97548fb48281bed"></a>

```c
#define ASPEED_RESET_LPC (ASPEED_RESET_GRP_1_OFFSET + 0)
```

相关声明：[ASPEED_RESET_LPC](#a93f2fc81c8a9cdfee97548fb48281bed)、[ASPEED_RESET_GRP_1_OFFSET](#af60cf3c19df220966fcc6aeb553677a8)。

## 22.2\_详细说明（Detailed Documentation）

<a id="ac8cad68c9911554194574d460d3f3814"></a>

### `ASPEED_RESET_ADC`

```c
#define ASPEED_RESET_ADC (ASPEED_RESET_GRP_1_OFFSET + 23)
```

<a id="a76bc43a3b57f919db372e4a79dc79b6f"></a>

### `ASPEED_RESET_ESPI`

```c
#define ASPEED_RESET_ESPI (ASPEED_RESET_GRP_1_OFFSET + 25)
```

<a id="a58f51601c877080d344167774969c9b4"></a>

### `ASPEED_RESET_GRP_0_OFFSET`

```c
#define ASPEED_RESET_GRP_0_OFFSET (0)
```

<a id="af60cf3c19df220966fcc6aeb553677a8"></a>

### `ASPEED_RESET_GRP_1_OFFSET`

```c
#define ASPEED_RESET_GRP_1_OFFSET (32)
```

<a id="a18a69d795a56e9077333b8d50fac36b0"></a>

### `ASPEED_RESET_HACE`

```c
#define ASPEED_RESET_HACE (ASPEED_RESET_GRP_0_OFFSET + 4)
```

<a id="a235bf82edd62f2f72fb9de4efa11c7f9"></a>

### `ASPEED_RESET_I2C`

```c
#define ASPEED_RESET_I2C (ASPEED_RESET_GRP_1_OFFSET + 2)
```

<a id="a49e0d2e074659166bb20ad0a9a603435"></a>

### `ASPEED_RESET_I3C`

```c
#define ASPEED_RESET_I3C (ASPEED_RESET_GRP_1_OFFSET + 7)
```

<a id="a392ac704a9bbddcee588e9f52af8557e"></a>

### `ASPEED_RESET_I3C0`

```c
#define ASPEED_RESET_I3C0 (ASPEED_RESET_GRP_1_OFFSET + 8)
```

<a id="a792d63822aaf04bcf8670471c6f5cb5c"></a>

### `ASPEED_RESET_I3C1`

```c
#define ASPEED_RESET_I3C1 (ASPEED_RESET_GRP_1_OFFSET + 9)
```

<a id="a3e76867407846a68533e1ef13e5612e0"></a>

### `ASPEED_RESET_I3C2`

```c
#define ASPEED_RESET_I3C2 (ASPEED_RESET_GRP_1_OFFSET + 10)
```

<a id="a6eb1a65fee7f7d589e5c40acb06a59a7"></a>

### `ASPEED_RESET_I3C3`

```c
#define ASPEED_RESET_I3C3 (ASPEED_RESET_GRP_1_OFFSET + 11)
```

<a id="a2000c2cd1474abe2acf6716293f9a656"></a>

### `ASPEED_RESET_JTAG_M0`

```c
#define ASPEED_RESET_JTAG_M0 (ASPEED_RESET_GRP_1_OFFSET + 26)
```

<a id="a8e20719b17e4f21c9673a7e740362b8e"></a>

### `ASPEED_RESET_JTAG_M1`

```c
#define ASPEED_RESET_JTAG_M1 (ASPEED_RESET_GRP_1_OFFSET + 22)
```

<a id="a93f2fc81c8a9cdfee97548fb48281bed"></a>

### `ASPEED_RESET_LPC`

```c
#define ASPEED_RESET_LPC (ASPEED_RESET_GRP_1_OFFSET + 0)
```

<a id="ae546e699360d23e89ddba7310d637c8a"></a>

### `ASPEED_RESET_MAC`

```c
#define ASPEED_RESET_MAC (ASPEED_RESET_GRP_1_OFFSET + 20)
```

<a id="abb494d1ccc9ab01d50fc21bb7c2eb7de"></a>

### `ASPEED_RESET_MII`

```c
#define ASPEED_RESET_MII (ASPEED_RESET_GRP_1_OFFSET + 3)
```

<a id="a6cab61e115cc50636d3c5aa8b509f5c5"></a>

### `ASPEED_RESET_PECI`

```c
#define ASPEED_RESET_PECI (ASPEED_RESET_GRP_1_OFFSET + 4)
```

<a id="a49f53d3791ab6d0104837204c31eb1ad"></a>

### `ASPEED_RESET_PWM_TACH`

```c
#define ASPEED_RESET_PWM_TACH (ASPEED_RESET_GRP_1_OFFSET + 5)
```

<a id="a54fbdaa166cf43dadb6a4d9777b581c3"></a>

### `ASPEED_RESET_SRAM`

```c
#define ASPEED_RESET_SRAM (ASPEED_RESET_GRP_0_OFFSET + 0)
```

<a id="ab7429f58459c26d3cf637e4d9e764d67"></a>

### `ASPEED_RESET_UART1`

```c
#define ASPEED_RESET_UART1 (ASPEED_RESET_GRP_1_OFFSET + 28)
```

<a id="a67087547f237de76d2ab1e9c2fd774f1"></a>

### `ASPEED_RESET_UART2`

```c
#define ASPEED_RESET_UART2 (ASPEED_RESET_GRP_1_OFFSET + 29)
```

<a id="a31e0692dd65c0adbe937daebee4477e2"></a>

### `ASPEED_RESET_UART3`

```c
#define ASPEED_RESET_UART3 (ASPEED_RESET_GRP_1_OFFSET + 30)
```

<a id="a19e6207b2212a0a58b8dc5c736748df1"></a>

### `ASPEED_RESET_UART4`

```c
#define ASPEED_RESET_UART4 (ASPEED_RESET_GRP_1_OFFSET + 31)
```

<a id="aa63cefb88f641936f49389acaff04cbc"></a>

### `ASPEED_RESET_USB`

```c
#define ASPEED_RESET_USB (ASPEED_RESET_GRP_0_OFFSET + 3)
```


## 22.3\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_reference/P042_ast10x0_reset.h_源码浏览.md)

<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P021_zephyr__dt-bindings__clock__ast10x0_clock.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P023_zephyr__drivers__mfd__aw9523b.h_文件参考.md)
