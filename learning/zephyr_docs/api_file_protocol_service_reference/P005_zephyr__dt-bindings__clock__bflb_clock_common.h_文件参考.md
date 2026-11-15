---
id: learning.zephyr-docs.api-file-protocol-service-reference.page-5
title: zephyr__dt-bindings__clock__bflb_clock_common.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/bflb__clock__common_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第5章\_zephyr\_\_dt-bindings\_\_clock\_\_bflb\_clock\_common.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/bflb__clock__common_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

查看此文件的源码。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 5.1\_宏定义（Macros）

<a id="r_af2d6e2a7c386b50358a9cf50fc8808b3"></a>

```c
#define BFLB_CLKID_CLK_ROOT 0
```

相关声明：[BFLB_CLKID_CLK_ROOT](#af2d6e2a7c386b50358a9cf50fc8808b3)。

根时钟（Root Clock）。

<a id="r_a48bf5d6a4379c03c7817503d7fe66c8b"></a>

```c
#define BFLB_CLKID_CLK_RC32M 1
```

相关声明：[BFLB_CLKID_CLK_RC32M](#a48bf5d6a4379c03c7817503d7fe66c8b)。

32 MHz RC 振荡器时钟（RC Oscillator Clock）。

<a id="r_a059c42552c94b942f53c644207776326"></a>

```c
#define BFLB_CLKID_CLK_CRYSTAL 2
```

相关声明：[BFLB_CLKID_CLK_CRYSTAL](#a059c42552c94b942f53c644207776326)。

使用晶体（Crystal）作为时钟。

<a id="r_a81f8f15faf5025212dbe96417515c358"></a>

```c
#define BFLB_CLKID_CLK_BCLK 3
```

相关声明：[BFLB_CLKID_CLK_BCLK](#a81f8f15faf5025212dbe96417515c358)。

总线时钟（Bus Clock）。

<a id="r_a5b8eca0197f839af7776f5d02c6eab13"></a>

```c
#define BFLB_CLKID_CLK_F32K 4
```

相关声明：[BFLB_CLKID_CLK_F32K](#a5b8eca0197f839af7776f5d02c6eab13)。

F32K 时钟（Clock）。

<a id="r_a14b75b51b81786bb7ae26070e5e41e22"></a>

```c
#define BFLB_CLKID_CLK_XTAL32K 5
```

相关声明：[BFLB_CLKID_CLK_XTAL32K](#a14b75b51b81786bb7ae26070e5e41e22)。

XTAL32K 时钟（Clock）。

<a id="r_ad2b0e7bd97598e50d10ce66d5b52a360"></a>

```c
#define BFLB_CLKID_CLK_RC32K 6
```

相关声明：[BFLB_CLKID_CLK_RC32K](#ad2b0e7bd97598e50d10ce66d5b52a360)。

RC32K 时钟（Clock）。

<a id="r_acc4f8e38984a2ec63e470b919b6d8aef"></a>

```c
#define BFLB_CLKID_CLK_PRIVATE 7
```

相关声明：[BFLB_CLKID_CLK_PRIVATE](#acc4f8e38984a2ec63e470b919b6d8aef)。

SoC 专用时钟 ID 条目（SoC-specific Clock ID Entries）的起始位置。

<a id="r_a66a85ae5e3c9b8986554ffab7cd3410a"></a>

```c
#define BFLB_FORCE_ROOT_RC32M 32
```

相关声明：[BFLB_FORCE_ROOT_RC32M](#a66a85ae5e3c9b8986554ffab7cd3410a)。

传给时钟 API，将根时钟（Root Clock）切换为 RC32M。

<a id="r_a54b4470e00cf413ff590b144a7196542"></a>

```c
#define BFLB_FORCE_ROOT_CRYSTAL 33
```

相关声明：[BFLB_FORCE_ROOT_CRYSTAL](#a54b4470e00cf413ff590b144a7196542)。

传给时钟 API，将根时钟（Root Clock）切换为晶体（Crystal）。

<a id="r_ab8f04871f9bb53ca5d410c66413b21de"></a>

```c
#define BFLB_FORCE_ROOT_PLL 34
```

相关声明：[BFLB_FORCE_ROOT_PLL](#ab8f04871f9bb53ca5d410c66413b21de)。

传给时钟 API，将根时钟（Root Clock）切换为 DTS 配置的 PLL。

<a id="r_a4f6aa90fc9b6f55cd305e3c27d43732d"></a>

```c
#define BFLB_RC32M_FREQUENCY (DT_FREQ_M(32))
```

相关声明：[BFLB_RC32M_FREQUENCY](#a4f6aa90fc9b6f55cd305e3c27d43732d)。

RC32M 的固定频率（Constant Frequency）。

<a id="r_ab7b933509a8737fb0eadba3db5a59de1"></a>

```c
#define BFLB_F32K_FREQUENCY 32768U
```

相关声明：[BFLB_F32K_FREQUENCY](#ab7b933509a8737fb0eadba3db5a59de1)。

F32K 的固定频率（Constant Frequency）。

## 5.2\_详细说明（Detailed Documentation）

<a id="a81f8f15faf5025212dbe96417515c358"></a>

### `BFLB_CLKID_CLK_BCLK`

```c
#define BFLB_CLKID_CLK_BCLK 3
```

总线时钟（Bus Clock）。

<a id="a059c42552c94b942f53c644207776326"></a>

### `BFLB_CLKID_CLK_CRYSTAL`

```c
#define BFLB_CLKID_CLK_CRYSTAL 2
```

使用晶体（Crystal）作为时钟。

<a id="a5b8eca0197f839af7776f5d02c6eab13"></a>

### `BFLB_CLKID_CLK_F32K`

```c
#define BFLB_CLKID_CLK_F32K 4
```

F32K 时钟（Clock）。

<a id="acc4f8e38984a2ec63e470b919b6d8aef"></a>

### `BFLB_CLKID_CLK_PRIVATE`

```c
#define BFLB_CLKID_CLK_PRIVATE 7
```

SoC 专用时钟 ID 条目（SoC-specific Clock ID Entries）的起始位置。

<a id="ad2b0e7bd97598e50d10ce66d5b52a360"></a>

### `BFLB_CLKID_CLK_RC32K`

```c
#define BFLB_CLKID_CLK_RC32K 6
```

RC32K 时钟（Clock）。

<a id="a48bf5d6a4379c03c7817503d7fe66c8b"></a>

### `BFLB_CLKID_CLK_RC32M`

```c
#define BFLB_CLKID_CLK_RC32M 1
```

32 MHz RC 振荡器时钟（RC Oscillator Clock）。

<a id="af2d6e2a7c386b50358a9cf50fc8808b3"></a>

### `BFLB_CLKID_CLK_ROOT`

```c
#define BFLB_CLKID_CLK_ROOT 0
```

根时钟（Root Clock）。

<a id="a14b75b51b81786bb7ae26070e5e41e22"></a>

### `BFLB_CLKID_CLK_XTAL32K`

```c
#define BFLB_CLKID_CLK_XTAL32K 5
```

XTAL32K 时钟（Clock）。

<a id="ab7b933509a8737fb0eadba3db5a59de1"></a>

### `BFLB_F32K_FREQUENCY`

```c
#define BFLB_F32K_FREQUENCY 32768U
```

F32K 的固定频率（Constant Frequency）。

<a id="a54b4470e00cf413ff590b144a7196542"></a>

### `BFLB_FORCE_ROOT_CRYSTAL`

```c
#define BFLB_FORCE_ROOT_CRYSTAL 33
```

传给时钟 API，将根时钟（Root Clock）切换为晶体（Crystal）。

<a id="ab8f04871f9bb53ca5d410c66413b21de"></a>

### `BFLB_FORCE_ROOT_PLL`

```c
#define BFLB_FORCE_ROOT_PLL 34
```

传给时钟 API，将根时钟（Root Clock）切换为 DTS 配置的 PLL。

<a id="a66a85ae5e3c9b8986554ffab7cd3410a"></a>

### `BFLB_FORCE_ROOT_RC32M`

```c
#define BFLB_FORCE_ROOT_RC32M 32
```

传给时钟 API，将根时钟（Root Clock）切换为 RC32M。

<a id="a4f6aa90fc9b6f55cd305e3c27d43732d"></a>

### `BFLB_RC32M_FREQUENCY`

```c
#define BFLB_RC32M_FREQUENCY (DT_FREQ_M(32))
```

RC32M 的固定频率（Constant Frequency）。


## 5.3\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_reference/P065_bflb_clock_common.h_源码浏览.md)

<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P004_zephyr__dt-bindings__clock__bflb_bl61x_clock.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P006_zephyr__net__capture.h_文件参考.md)
