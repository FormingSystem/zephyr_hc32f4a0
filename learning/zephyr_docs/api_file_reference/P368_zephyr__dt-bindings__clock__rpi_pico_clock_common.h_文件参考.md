---
id: learning.zephyr-docs.api-file-reference.page-368
title: zephyr__dt-bindings__clock__rpi_pico_clock_common.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/rpi__pico__clock__common_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第368章\_zephyr\_\_dt-bindings\_\_clock\_\_rpi\_pico\_clock\_common.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/rpi__pico__clock__common_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

查看此文件的源码。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 368.1\_宏定义（Macros）

<a id="r_a466e4913a0890f6d06decf7fe912a8d6"></a>

```c
#define RPI_PICO_PLL_SYS 0
```

相关声明：[RPI_PICO_PLL_SYS](#a466e4913a0890f6d06decf7fe912a8d6)。

<a id="r_a32863224d85037e237d6ba1d6f526349"></a>

```c
#define RPI_PICO_PLL_USB 1
```

相关声明：[RPI_PICO_PLL_USB](#a32863224d85037e237d6ba1d6f526349)。

<a id="r_ac641d50669b0c5a5932ba47754f997f2"></a>

```c
#define RPI_PICO_PLL_COUNT 2
```

相关声明：[RPI_PICO_PLL_COUNT](#ac641d50669b0c5a5932ba47754f997f2)。

<a id="r_ac64aeeb93c3df085cdba8088c7e71643"></a>

```c
#define RPI_PICO_GPIN_0 0
```

相关声明：[RPI_PICO_GPIN_0](#ac64aeeb93c3df085cdba8088c7e71643)。

<a id="r_a6f6f6655d1e43da01b19f676da7eba9f"></a>

```c
#define RPI_PICO_GPIN_1 1
```

相关声明：[RPI_PICO_GPIN_1](#a6f6f6655d1e43da01b19f676da7eba9f)。

<a id="r_a0c1f6d136e18501a33806da47b4fbd74"></a>

```c
#define RPI_PICO_GPIN_COUNT 2
```

相关声明：[RPI_PICO_GPIN_COUNT](#a0c1f6d136e18501a33806da47b4fbd74)。

<a id="r_ad69d8a2bad53c6d014daaf080459785f"></a>

```c
#define RPI_PICO_CLKID_CLK_GPOUT0 0
```

相关声明：[RPI_PICO_CLKID_CLK_GPOUT0](#ad69d8a2bad53c6d014daaf080459785f)。

<a id="r_a4ff53626cd36bd222c4fd03fa2a1cd7c"></a>

```c
#define RPI_PICO_CLKID_CLK_GPOUT1 1
```

相关声明：[RPI_PICO_CLKID_CLK_GPOUT1](#a4ff53626cd36bd222c4fd03fa2a1cd7c)。

<a id="r_ad56ce5dde45a27c349e97060fe81b877"></a>

```c
#define RPI_PICO_CLKID_CLK_GPOUT2 2
```

相关声明：[RPI_PICO_CLKID_CLK_GPOUT2](#ad56ce5dde45a27c349e97060fe81b877)。

<a id="r_adc9f3183caef9040a3e217b8ad373aa4"></a>

```c
#define RPI_PICO_CLKID_CLK_GPOUT3 3
```

相关声明：[RPI_PICO_CLKID_CLK_GPOUT3](#adc9f3183caef9040a3e217b8ad373aa4)。

<a id="r_a3209f2d463248e9eaecf91bfad06221c"></a>

```c
#define RPI_PICO_CLKID_CLK_REF 4
```

相关声明：[RPI_PICO_CLKID_CLK_REF](#a3209f2d463248e9eaecf91bfad06221c)。

<a id="r_aa6925acbb797026caccb78c0bb0c64c5"></a>

```c
#define RPI_PICO_CLKID_CLK_SYS 5
```

相关声明：[RPI_PICO_CLKID_CLK_SYS](#aa6925acbb797026caccb78c0bb0c64c5)。

<a id="r_aa0e2c91d4ad02985c075c9206d1be314"></a>

```c
#define RPI_PICO_CLKID_CLK_PERI 6
```

相关声明：[RPI_PICO_CLKID_CLK_PERI](#aa0e2c91d4ad02985c075c9206d1be314)。

<a id="r_afa64692c1c8e8c28970fd9c88a8a1adf"></a>

```c
#define RPI_PICO_CLKID_PLL_SYS 10
```

相关声明：[RPI_PICO_CLKID_PLL_SYS](#afa64692c1c8e8c28970fd9c88a8a1adf)。

<a id="r_aec02ce9014d772f07ba4e25d825e61a0"></a>

```c
#define RPI_PICO_CLKID_PLL_USB 11
```

相关声明：[RPI_PICO_CLKID_PLL_USB](#aec02ce9014d772f07ba4e25d825e61a0)。

<a id="r_ace2c7bd1defff7594766ad67416ed524"></a>

```c
#define RPI_PICO_CLKID_XOSC 12
```

相关声明：[RPI_PICO_CLKID_XOSC](#ace2c7bd1defff7594766ad67416ed524)。

<a id="r_a942f1316a463d6a10d4edf88176915f2"></a>

```c
#define RPI_PICO_CLKID_ROSC 13
```

相关声明：[RPI_PICO_CLKID_ROSC](#a942f1316a463d6a10d4edf88176915f2)。

<a id="r_af74becbd25d5e91d0034236b30c13b73"></a>

```c
#define RPI_PICO_CLKID_ROSC_PH 14
```

相关声明：[RPI_PICO_CLKID_ROSC_PH](#af74becbd25d5e91d0034236b30c13b73)。

<a id="r_a5da8c9643f9505364e73f1ea44555939"></a>

```c
#define RPI_PICO_CLKID_GPIN0 15
```

相关声明：[RPI_PICO_CLKID_GPIN0](#a5da8c9643f9505364e73f1ea44555939)。

<a id="r_a668080f8aaa30b302a2eb92c11320533"></a>

```c
#define RPI_PICO_CLKID_GPIN1 16
```

相关声明：[RPI_PICO_CLKID_GPIN1](#a668080f8aaa30b302a2eb92c11320533)。

<a id="r_a4b34aea0ef551dbdc54a321ebb891866"></a>

```c
#define RPI_PICO_ROSC_RANGE_RESET 0xAA0
```

相关声明：[RPI_PICO_ROSC_RANGE_RESET](#a4b34aea0ef551dbdc54a321ebb891866)。

<a id="r_ac095e9944a07e06b48bc2bce646afac1"></a>

```c
#define RPI_PICO_ROSC_RANGE_LOW 0xFA4
```

相关声明：[RPI_PICO_ROSC_RANGE_LOW](#ac095e9944a07e06b48bc2bce646afac1)。

<a id="r_afeca2ad3fbf43ff038e7d8b334de8217"></a>

```c
#define RPI_PICO_ROSC_RANGE_MEDIUM 0xFA5
```

相关声明：[RPI_PICO_ROSC_RANGE_MEDIUM](#afeca2ad3fbf43ff038e7d8b334de8217)。

<a id="r_a109f4ccc6aca6fc3fdf31be5817e779c"></a>

```c
#define RPI_PICO_ROSC_RANGE_HIGH 0xFA7
```

相关声明：[RPI_PICO_ROSC_RANGE_HIGH](#a109f4ccc6aca6fc3fdf31be5817e779c)。

<a id="r_ab8e87bc64fecf6db1ff6124be82b9120"></a>

```c
#define RPI_PICO_ROSC_RANGE_TOOHIGH 0xFA6
```

相关声明：[RPI_PICO_ROSC_RANGE_TOOHIGH](#ab8e87bc64fecf6db1ff6124be82b9120)。

<a id="r_a610d24203e8b6b6d69a37ee38c26b2d2"></a>

```c
#define RPI_PICO_CLOCK_COUNT 10
```

相关声明：[RPI_PICO_CLOCK_COUNT](#a610d24203e8b6b6d69a37ee38c26b2d2)。

## 368.2\_详细说明（Detailed Documentation）

<a id="ad69d8a2bad53c6d014daaf080459785f"></a>

### `RPI_PICO_CLKID_CLK_GPOUT0`

```c
#define RPI_PICO_CLKID_CLK_GPOUT0 0
```

<a id="a4ff53626cd36bd222c4fd03fa2a1cd7c"></a>

### `RPI_PICO_CLKID_CLK_GPOUT1`

```c
#define RPI_PICO_CLKID_CLK_GPOUT1 1
```

<a id="ad56ce5dde45a27c349e97060fe81b877"></a>

### `RPI_PICO_CLKID_CLK_GPOUT2`

```c
#define RPI_PICO_CLKID_CLK_GPOUT2 2
```

<a id="adc9f3183caef9040a3e217b8ad373aa4"></a>

### `RPI_PICO_CLKID_CLK_GPOUT3`

```c
#define RPI_PICO_CLKID_CLK_GPOUT3 3
```

<a id="aa0e2c91d4ad02985c075c9206d1be314"></a>

### `RPI_PICO_CLKID_CLK_PERI`

```c
#define RPI_PICO_CLKID_CLK_PERI 6
```

<a id="a3209f2d463248e9eaecf91bfad06221c"></a>

### `RPI_PICO_CLKID_CLK_REF`

```c
#define RPI_PICO_CLKID_CLK_REF 4
```

<a id="aa6925acbb797026caccb78c0bb0c64c5"></a>

### `RPI_PICO_CLKID_CLK_SYS`

```c
#define RPI_PICO_CLKID_CLK_SYS 5
```

<a id="a5da8c9643f9505364e73f1ea44555939"></a>

### `RPI_PICO_CLKID_GPIN0`

```c
#define RPI_PICO_CLKID_GPIN0 15
```

<a id="a668080f8aaa30b302a2eb92c11320533"></a>

### `RPI_PICO_CLKID_GPIN1`

```c
#define RPI_PICO_CLKID_GPIN1 16
```

<a id="afa64692c1c8e8c28970fd9c88a8a1adf"></a>

### `RPI_PICO_CLKID_PLL_SYS`

```c
#define RPI_PICO_CLKID_PLL_SYS 10
```

<a id="aec02ce9014d772f07ba4e25d825e61a0"></a>

### `RPI_PICO_CLKID_PLL_USB`

```c
#define RPI_PICO_CLKID_PLL_USB 11
```

<a id="a942f1316a463d6a10d4edf88176915f2"></a>

### `RPI_PICO_CLKID_ROSC`

```c
#define RPI_PICO_CLKID_ROSC 13
```

<a id="af74becbd25d5e91d0034236b30c13b73"></a>

### `RPI_PICO_CLKID_ROSC_PH`

```c
#define RPI_PICO_CLKID_ROSC_PH 14
```

<a id="ace2c7bd1defff7594766ad67416ed524"></a>

### `RPI_PICO_CLKID_XOSC`

```c
#define RPI_PICO_CLKID_XOSC 12
```

<a id="a610d24203e8b6b6d69a37ee38c26b2d2"></a>

### `RPI_PICO_CLOCK_COUNT`

```c
#define RPI_PICO_CLOCK_COUNT 10
```

<a id="ac64aeeb93c3df085cdba8088c7e71643"></a>

### `RPI_PICO_GPIN_0`

```c
#define RPI_PICO_GPIN_0 0
```

<a id="a6f6f6655d1e43da01b19f676da7eba9f"></a>

### `RPI_PICO_GPIN_1`

```c
#define RPI_PICO_GPIN_1 1
```

<a id="a0c1f6d136e18501a33806da47b4fbd74"></a>

### `RPI_PICO_GPIN_COUNT`

```c
#define RPI_PICO_GPIN_COUNT 2
```

<a id="ac641d50669b0c5a5932ba47754f997f2"></a>

### `RPI_PICO_PLL_COUNT`

```c
#define RPI_PICO_PLL_COUNT 2
```

<a id="a466e4913a0890f6d06decf7fe912a8d6"></a>

### `RPI_PICO_PLL_SYS`

```c
#define RPI_PICO_PLL_SYS 0
```

<a id="a32863224d85037e237d6ba1d6f526349"></a>

### `RPI_PICO_PLL_USB`

```c
#define RPI_PICO_PLL_USB 1
```

<a id="a109f4ccc6aca6fc3fdf31be5817e779c"></a>

### `RPI_PICO_ROSC_RANGE_HIGH`

```c
#define RPI_PICO_ROSC_RANGE_HIGH 0xFA7
```

<a id="ac095e9944a07e06b48bc2bce646afac1"></a>

### `RPI_PICO_ROSC_RANGE_LOW`

```c
#define RPI_PICO_ROSC_RANGE_LOW 0xFA4
```

<a id="afeca2ad3fbf43ff038e7d8b334de8217"></a>

### `RPI_PICO_ROSC_RANGE_MEDIUM`

```c
#define RPI_PICO_ROSC_RANGE_MEDIUM 0xFA5
```

<a id="a4b34aea0ef551dbdc54a321ebb891866"></a>

### `RPI_PICO_ROSC_RANGE_RESET`

```c
#define RPI_PICO_ROSC_RANGE_RESET 0xAA0
```

<a id="ab8e87bc64fecf6db1ff6124be82b9120"></a>

### `RPI_PICO_ROSC_RANGE_TOOHIGH`

```c
#define RPI_PICO_ROSC_RANGE_TOOHIGH 0xFA6
```


## 368.3\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_supplement_reference/P168_rpi_pico_clock_common.h_源码浏览.md)

<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P367_zephyr__dt-bindings__pinctrl__rpi-pico-rp2350b-pinctrl.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P369_zephyr__dt-bindings__clock__rpi_pico_rp2040_clock.h_文件参考.md)
