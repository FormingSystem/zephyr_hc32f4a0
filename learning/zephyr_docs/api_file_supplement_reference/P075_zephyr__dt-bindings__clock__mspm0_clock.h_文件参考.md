---
id: learning.zephyr-docs.api-file-supplement-reference.page-75
title: zephyr__dt-bindings__clock__mspm0_clock.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/mspm0__clock_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第75章\_zephyr\_\_dt-bindings\_\_clock\_\_mspm0\_clock.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/mspm0__clock_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

查看此文件的源码。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 75.1\_宏定义（Macros）

<a id="r_a546f50fc3a86ada7e34d3c5b78526e5e"></a>

```c
#define MSPM0_CLOCK(clk, bit)
```

相关声明：[MSPM0_CLOCK](#a546f50fc3a86ada7e34d3c5b78526e5e)。

<a id="r_a35877f69e306437ad9c8bea5ce455e11"></a>

```c
#define MSPM0_CLOCK_PERIPH_REG_MASK(X)
```

相关声明：[MSPM0_CLOCK_PERIPH_REG_MASK](#a35877f69e306437ad9c8bea5ce455e11)。

<a id="r_a7df45c402fe047a5b5742c1dda57c6b5"></a>

```c
#define MSPM0_CLOCK_SYSOSC MSPM0_CLOCK(0x0, 0x0)
```

相关声明：[MSPM0_CLOCK_SYSOSC](#a7df45c402fe047a5b5742c1dda57c6b5)、[MSPM0_CLOCK](#a546f50fc3a86ada7e34d3c5b78526e5e)。

<a id="r_a1eef26082f2c6a8bf57cfb33a8ae7bca"></a>

```c
#define MSPM0_CLOCK_LFCLK MSPM0_CLOCK(0x1, 0x2)
```

相关声明：[MSPM0_CLOCK_LFCLK](#a1eef26082f2c6a8bf57cfb33a8ae7bca)、[MSPM0_CLOCK](#a546f50fc3a86ada7e34d3c5b78526e5e)。

<a id="r_a3a35970f45fab5f68466339e14a5dcb1"></a>

```c
#define MSPM0_CLOCK_MFCLK MSPM0_CLOCK(0x2, 0x4)
```

相关声明：[MSPM0_CLOCK_MFCLK](#a3a35970f45fab5f68466339e14a5dcb1)、[MSPM0_CLOCK](#a546f50fc3a86ada7e34d3c5b78526e5e)。

<a id="r_a86b9a5c73fae48eace61eaddb94a7309"></a>

```c
#define MSPM0_CLOCK_BUSCLK MSPM0_CLOCK(0x3, 0x8)
```

相关声明：[MSPM0_CLOCK_BUSCLK](#a86b9a5c73fae48eace61eaddb94a7309)、[MSPM0_CLOCK](#a546f50fc3a86ada7e34d3c5b78526e5e)。

<a id="r_a9b1175ca378a2e7cfcda5f1ed0c0759a"></a>

```c
#define MSPM0_CLOCK_ULPCLK MSPM0_CLOCK(0x4, 0x8)
```

相关声明：[MSPM0_CLOCK_ULPCLK](#a9b1175ca378a2e7cfcda5f1ed0c0759a)、[MSPM0_CLOCK](#a546f50fc3a86ada7e34d3c5b78526e5e)。

<a id="r_aa8a1076dd4b533aa15b2ee838047546c"></a>

```c
#define MSPM0_CLOCK_MCLK MSPM0_CLOCK(0x5, 0x8)
```

相关声明：[MSPM0_CLOCK_MCLK](#aa8a1076dd4b533aa15b2ee838047546c)、[MSPM0_CLOCK](#a546f50fc3a86ada7e34d3c5b78526e5e)。

<a id="r_aa4b3c20657ab23b60f249d1f459829fd"></a>

```c
#define MSPM0_CLOCK_MFPCLK MSPM0_CLOCK(0x6, 0x0)
```

相关声明：[MSPM0_CLOCK_MFPCLK](#aa4b3c20657ab23b60f249d1f459829fd)、[MSPM0_CLOCK](#a546f50fc3a86ada7e34d3c5b78526e5e)。

<a id="r_abb0965a9382c3e85ec418ac911766094"></a>

```c
#define MSPM0_CLOCK_CANCLK MSPM0_CLOCK(0x7, 0x0)
```

相关声明：[MSPM0_CLOCK_CANCLK](#abb0965a9382c3e85ec418ac911766094)、[MSPM0_CLOCK](#a546f50fc3a86ada7e34d3c5b78526e5e)。

<a id="r_ad2a34eb409acbd0a2058434cdcf3c40c"></a>

```c
#define MSPM0_CLOCK_CLK_OUT MSPM0_CLOCK(0x8, 0x0)
```

相关声明：[MSPM0_CLOCK_CLK_OUT](#ad2a34eb409acbd0a2058434cdcf3c40c)、[MSPM0_CLOCK](#a546f50fc3a86ada7e34d3c5b78526e5e)。

<a id="r_ad252590d9958e7506c2554da23f9eab7"></a>

```c
#define MSPM0_CLOCK_HFCLK MSPM0_CLOCK(0x9, 0x2)
```

相关声明：[MSPM0_CLOCK_HFCLK](#ad252590d9958e7506c2554da23f9eab7)、[MSPM0_CLOCK](#a546f50fc3a86ada7e34d3c5b78526e5e)。

高频时钟引用（High Frequency Clock Reference）。

## 75.2\_详细说明（Detailed Documentation）

<a id="a546f50fc3a86ada7e34d3c5b78526e5e"></a>

### `MSPM0_CLOCK`

```c
#define MSPM0_CLOCK ( clk, bit )
```

展开值（Value）：

```c
((clk << 8) | bit)
```

<a id="a86b9a5c73fae48eace61eaddb94a7309"></a>

### `MSPM0_CLOCK_BUSCLK`

```c
#define MSPM0_CLOCK_BUSCLK MSPM0_CLOCK(0x3, 0x8)
```

<a id="abb0965a9382c3e85ec418ac911766094"></a>

### `MSPM0_CLOCK_CANCLK`

```c
#define MSPM0_CLOCK_CANCLK MSPM0_CLOCK(0x7, 0x0)
```

<a id="ad2a34eb409acbd0a2058434cdcf3c40c"></a>

### `MSPM0_CLOCK_CLK_OUT`

```c
#define MSPM0_CLOCK_CLK_OUT MSPM0_CLOCK(0x8, 0x0)
```

<a id="ad252590d9958e7506c2554da23f9eab7"></a>

### `MSPM0_CLOCK_HFCLK`

```c
#define MSPM0_CLOCK_HFCLK MSPM0_CLOCK(0x9, 0x2)
```

高频时钟引用（High Frequency Clock Reference）。

<a id="a1eef26082f2c6a8bf57cfb33a8ae7bca"></a>

### `MSPM0_CLOCK_LFCLK`

```c
#define MSPM0_CLOCK_LFCLK MSPM0_CLOCK(0x1, 0x2)
```

<a id="aa8a1076dd4b533aa15b2ee838047546c"></a>

### `MSPM0_CLOCK_MCLK`

```c
#define MSPM0_CLOCK_MCLK MSPM0_CLOCK(0x5, 0x8)
```

<a id="a3a35970f45fab5f68466339e14a5dcb1"></a>

### `MSPM0_CLOCK_MFCLK`

```c
#define MSPM0_CLOCK_MFCLK MSPM0_CLOCK(0x2, 0x4)
```

<a id="aa4b3c20657ab23b60f249d1f459829fd"></a>

### `MSPM0_CLOCK_MFPCLK`

```c
#define MSPM0_CLOCK_MFPCLK MSPM0_CLOCK(0x6, 0x0)
```

<a id="a35877f69e306437ad9c8bea5ce455e11"></a>

### `MSPM0_CLOCK_PERIPH_REG_MASK`

```c
#define MSPM0_CLOCK_PERIPH_REG_MASK ( X)
```

展开值（Value）：

```c
(X & 0xFF)
```

<a id="a7df45c402fe047a5b5742c1dda57c6b5"></a>

### `MSPM0_CLOCK_SYSOSC`

```c
#define MSPM0_CLOCK_SYSOSC MSPM0_CLOCK(0x0, 0x0)
```

<a id="a9b1175ca378a2e7cfcda5f1ed0c0759a"></a>

### `MSPM0_CLOCK_ULPCLK`

```c
#define MSPM0_CLOCK_ULPCLK MSPM0_CLOCK(0x4, 0x8)
```


## 75.3\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_configuration_reference/P059_mspm0_clock.h_源码浏览.md)

<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P074_zephyr__mpipe__mpipe_transform_client.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P076_zephyr__drivers__clock_control__mspm0_clock_control.h_文件参考.md)
