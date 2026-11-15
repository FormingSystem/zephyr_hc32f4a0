---
id: learning.zephyr-docs.api-file-reference.page-17
title: zephyr__dt-bindings__pinctrl__arm-mps2-pinctrl.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/arm-mps2-pinctrl_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第17章\_zephyr\_\_dt-bindings\_\_pinctrl\_\_arm-mps2-pinctrl.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/arm-mps2-pinctrl_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

查看此文件的源码。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 17.1\_宏定义（Macros）

<a id="r_ad565796e43c28185243be8c71f910e3f"></a>

```c
#define MPS2_ALT_FUNC_POS 0
```

相关声明：[MPS2_ALT_FUNC_POS](#ad565796e43c28185243be8c71f910e3f)。

<a id="r_a6ba3abb5ab20065ea59cb44a2b12f09e"></a>

```c
#define MPS2_ALT_FUNC_MASK 0x3
```

相关声明：[MPS2_ALT_FUNC_MASK](#a6ba3abb5ab20065ea59cb44a2b12f09e)。

<a id="r_a8fc17b69bcffa4039b207b6a4ab7475d"></a>

```c
#define MPS2_EXP_NUM_POS 2
```

相关声明：[MPS2_EXP_NUM_POS](#a8fc17b69bcffa4039b207b6a4ab7475d)。

<a id="r_a98780dae8c8964bbcce2007cf5186b64"></a>

```c
#define MPS2_EXP_NUM_MASK 0x3F
```

相关声明：[MPS2_EXP_NUM_MASK](#a98780dae8c8964bbcce2007cf5186b64)。

<a id="r_a793e19909cf9cdd9fb1aa0a34f835c65"></a>

```c
#define MPS2_PINCTRL_FUNC_UART 0
```

相关声明：[MPS2_PINCTRL_FUNC_UART](#a793e19909cf9cdd9fb1aa0a34f835c65)。

<a id="r_af7cfe8556e424a3018d0e62e62f1b210"></a>

```c
#define MPS2_PINCTRL_FUNC_GPIO 1
```

相关声明：[MPS2_PINCTRL_FUNC_GPIO](#af7cfe8556e424a3018d0e62e62f1b210)。

<a id="r_a33857f12895ab4ffb8bac15a226d9e44"></a>

```c
#define MPS2_PINCTRL_FUNC_I2C 2
```

相关声明：[MPS2_PINCTRL_FUNC_I2C](#a33857f12895ab4ffb8bac15a226d9e44)。

<a id="r_a459cfc88b65ae738b2a94be1fbe6df46"></a>

```c
#define MPS2_PINCTRL_FUNC_SPI 3
```

相关声明：[MPS2_PINCTRL_FUNC_SPI](#a459cfc88b65ae738b2a94be1fbe6df46)。

<a id="r_affba791a0c60352a28b3d8f122534540"></a>

```c
#define MPS2_PINMUX(alt_func, exp_num)
```

相关声明：[MPS2_PINMUX](#affba791a0c60352a28b3d8f122534540)。

<a id="r_aad1ef19e8c46127baf5ddb680f4a9c2e"></a>

```c
#define UART3_RXD_EXP MPS2_PINMUX(MPS2_PINCTRL_FUNC_UART, 0)
```

相关声明：[UART3_RXD_EXP](#aad1ef19e8c46127baf5ddb680f4a9c2e)、[MPS2_PINMUX](#affba791a0c60352a28b3d8f122534540)、[MPS2_PINCTRL_FUNC_UART](#a793e19909cf9cdd9fb1aa0a34f835c65)。

<a id="r_aab7f8b8584aa06a033aa1e93200eb0d6"></a>

```c
#define UART3_TXD_EXP MPS2_PINMUX(MPS2_PINCTRL_FUNC_UART, 4)
```

相关声明：[UART3_TXD_EXP](#aab7f8b8584aa06a033aa1e93200eb0d6)、[MPS2_PINMUX](#affba791a0c60352a28b3d8f122534540)、[MPS2_PINCTRL_FUNC_UART](#a793e19909cf9cdd9fb1aa0a34f835c65)。

<a id="r_a301bb93777a77d4fcbed8617edbe319a"></a>

```c
#define SBCON2_SCL_EXP MPS2_PINMUX(MPS2_PINCTRL_FUNC_I2C, 5)
```

相关声明：[SBCON2_SCL_EXP](#a301bb93777a77d4fcbed8617edbe319a)、[MPS2_PINMUX](#affba791a0c60352a28b3d8f122534540)、[MPS2_PINCTRL_FUNC_I2C](#a33857f12895ab4ffb8bac15a226d9e44)。

<a id="r_a8c2f848c26c691ce333e05fe17c9341d"></a>

```c
#define SBCON2_SDA_EXP MPS2_PINMUX(MPS2_PINCTRL_FUNC_I2C, 15)
```

相关声明：[SBCON2_SDA_EXP](#a8c2f848c26c691ce333e05fe17c9341d)、[MPS2_PINMUX](#affba791a0c60352a28b3d8f122534540)、[MPS2_PINCTRL_FUNC_I2C](#a33857f12895ab4ffb8bac15a226d9e44)。

<a id="r_ac3801e4481859951369757ac96612165"></a>

```c
#define SPI3_SCK_EXP MPS2_PINMUX(MPS2_PINCTRL_FUNC_SPI, 11)
```

相关声明：[SPI3_SCK_EXP](#ac3801e4481859951369757ac96612165)、[MPS2_PINMUX](#affba791a0c60352a28b3d8f122534540)、[MPS2_PINCTRL_FUNC_SPI](#a459cfc88b65ae738b2a94be1fbe6df46)。

<a id="r_ae1f9ab03b508c087a9190d742b67fc2a"></a>

```c
#define SPI3_SS_EXP MPS2_PINMUX(MPS2_PINCTRL_FUNC_SPI, 12)
```

相关声明：[SPI3_SS_EXP](#ae1f9ab03b508c087a9190d742b67fc2a)、[MPS2_PINMUX](#affba791a0c60352a28b3d8f122534540)、[MPS2_PINCTRL_FUNC_SPI](#a459cfc88b65ae738b2a94be1fbe6df46)。

<a id="r_a95f2fe6603f5ab5de9c410dfaf87dc52"></a>

```c
#define SPI3_MOSI_EXP MPS2_PINMUX(MPS2_PINCTRL_FUNC_SPI, 13)
```

相关声明：[SPI3_MOSI_EXP](#a95f2fe6603f5ab5de9c410dfaf87dc52)、[MPS2_PINMUX](#affba791a0c60352a28b3d8f122534540)、[MPS2_PINCTRL_FUNC_SPI](#a459cfc88b65ae738b2a94be1fbe6df46)。

<a id="r_a14c932b34877e7b1f004bdf3edfdcd4b"></a>

```c
#define SPI3_MISO_EXP MPS2_PINMUX(MPS2_PINCTRL_FUNC_SPI, 14)
```

相关声明：[SPI3_MISO_EXP](#a14c932b34877e7b1f004bdf3edfdcd4b)、[MPS2_PINMUX](#affba791a0c60352a28b3d8f122534540)、[MPS2_PINCTRL_FUNC_SPI](#a459cfc88b65ae738b2a94be1fbe6df46)。

<a id="r_af8e71afd57806fbe85b504ac68879fa6"></a>

```c
#define SPI2_SS_EXP MPS2_PINMUX(MPS2_PINCTRL_FUNC_SPI, 16)
```

相关声明：[SPI2_SS_EXP](#af8e71afd57806fbe85b504ac68879fa6)、[MPS2_PINMUX](#affba791a0c60352a28b3d8f122534540)、[MPS2_PINCTRL_FUNC_SPI](#a459cfc88b65ae738b2a94be1fbe6df46)。

<a id="r_af0e38d71c2b6d7cb6f1238e17e8fff6f"></a>

```c
#define SPI2_MISO_EXP MPS2_PINMUX(MPS2_PINCTRL_FUNC_SPI, 17)
```

相关声明：[SPI2_MISO_EXP](#af0e38d71c2b6d7cb6f1238e17e8fff6f)、[MPS2_PINMUX](#affba791a0c60352a28b3d8f122534540)、[MPS2_PINCTRL_FUNC_SPI](#a459cfc88b65ae738b2a94be1fbe6df46)。

<a id="r_a32eff7bbffdfc00975ff1b5f3281eaa1"></a>

```c
#define SPI2_MOSI_EXP MPS2_PINMUX(MPS2_PINCTRL_FUNC_SPI, 18)
```

相关声明：[SPI2_MOSI_EXP](#a32eff7bbffdfc00975ff1b5f3281eaa1)、[MPS2_PINMUX](#affba791a0c60352a28b3d8f122534540)、[MPS2_PINCTRL_FUNC_SPI](#a459cfc88b65ae738b2a94be1fbe6df46)。

<a id="r_a6fbdf386063229b64599d3c2071ebffd"></a>

```c
#define SPI2_SCK_EXP MPS2_PINMUX(MPS2_PINCTRL_FUNC_SPI, 19)
```

相关声明：[SPI2_SCK_EXP](#a6fbdf386063229b64599d3c2071ebffd)、[MPS2_PINMUX](#affba791a0c60352a28b3d8f122534540)、[MPS2_PINCTRL_FUNC_SPI](#a459cfc88b65ae738b2a94be1fbe6df46)。

<a id="r_a960b6b4bf5810595c274fab5842189e4"></a>

```c
#define UART4_RXD_EXP MPS2_PINMUX(MPS2_PINCTRL_FUNC_UART, 26)
```

相关声明：[UART4_RXD_EXP](#a960b6b4bf5810595c274fab5842189e4)、[MPS2_PINMUX](#affba791a0c60352a28b3d8f122534540)、[MPS2_PINCTRL_FUNC_UART](#a793e19909cf9cdd9fb1aa0a34f835c65)。

<a id="r_a8f2f8e4cb191c641dad8dff6c4753e38"></a>

```c
#define UART4_TXD_EXP MPS2_PINMUX(MPS2_PINCTRL_FUNC_UART, 30)
```

相关声明：[UART4_TXD_EXP](#a8f2f8e4cb191c641dad8dff6c4753e38)、[MPS2_PINMUX](#affba791a0c60352a28b3d8f122534540)、[MPS2_PINCTRL_FUNC_UART](#a793e19909cf9cdd9fb1aa0a34f835c65)。

<a id="r_a42708eb48f46a3dd04242b446389057b"></a>

```c
#define SBCON3_SCL_EXP MPS2_PINMUX(MPS2_PINCTRL_FUNC_I2C, 31)
```

相关声明：[SBCON3_SCL_EXP](#a42708eb48f46a3dd04242b446389057b)、[MPS2_PINMUX](#affba791a0c60352a28b3d8f122534540)、[MPS2_PINCTRL_FUNC_I2C](#a33857f12895ab4ffb8bac15a226d9e44)。

<a id="r_a1f600b98990e17441e52f65cc0dabddb"></a>

```c
#define SBCON3_SDA_EXP MPS2_PINMUX(MPS2_PINCTRL_FUNC_I2C, 41)
```

相关声明：[SBCON3_SDA_EXP](#a1f600b98990e17441e52f65cc0dabddb)、[MPS2_PINMUX](#affba791a0c60352a28b3d8f122534540)、[MPS2_PINCTRL_FUNC_I2C](#a33857f12895ab4ffb8bac15a226d9e44)。

<a id="r_a525321e1403275e09014f3ff1fa88d78"></a>

```c
#define SPI4_SS_EXP MPS2_PINMUX(MPS2_PINCTRL_FUNC_SPI, 38)
```

相关声明：[SPI4_SS_EXP](#a525321e1403275e09014f3ff1fa88d78)、[MPS2_PINMUX](#affba791a0c60352a28b3d8f122534540)、[MPS2_PINCTRL_FUNC_SPI](#a459cfc88b65ae738b2a94be1fbe6df46)。

<a id="r_aa73c8c56e661787cc05b131f86a8478c"></a>

```c
#define SPI4_MOSI_EXP MPS2_PINMUX(MPS2_PINCTRL_FUNC_SPI, 39)
```

相关声明：[SPI4_MOSI_EXP](#aa73c8c56e661787cc05b131f86a8478c)、[MPS2_PINMUX](#affba791a0c60352a28b3d8f122534540)、[MPS2_PINCTRL_FUNC_SPI](#a459cfc88b65ae738b2a94be1fbe6df46)。

<a id="r_a9709eee41e54142558c4930f1b034043"></a>

```c
#define SPI4_MISO_EXP MPS2_PINMUX(MPS2_PINCTRL_FUNC_SPI, 40)
```

相关声明：[SPI4_MISO_EXP](#a9709eee41e54142558c4930f1b034043)、[MPS2_PINMUX](#affba791a0c60352a28b3d8f122534540)、[MPS2_PINCTRL_FUNC_SPI](#a459cfc88b65ae738b2a94be1fbe6df46)。

<a id="r_aa48a51e34a517797511e7214ad00b7de"></a>

```c
#define SPI4_SCK_EXP MPS2_PINMUX(MPS2_PINCTRL_FUNC_SPI, 44)
```

相关声明：[SPI4_SCK_EXP](#aa48a51e34a517797511e7214ad00b7de)、[MPS2_PINMUX](#affba791a0c60352a28b3d8f122534540)、[MPS2_PINCTRL_FUNC_SPI](#a459cfc88b65ae738b2a94be1fbe6df46)。

## 17.2\_详细说明（Detailed Documentation）

<a id="a6ba3abb5ab20065ea59cb44a2b12f09e"></a>

### `MPS2_ALT_FUNC_MASK`

```c
#define MPS2_ALT_FUNC_MASK 0x3
```

<a id="ad565796e43c28185243be8c71f910e3f"></a>

### `MPS2_ALT_FUNC_POS`

```c
#define MPS2_ALT_FUNC_POS 0
```

<a id="a98780dae8c8964bbcce2007cf5186b64"></a>

### `MPS2_EXP_NUM_MASK`

```c
#define MPS2_EXP_NUM_MASK 0x3F
```

<a id="a8fc17b69bcffa4039b207b6a4ab7475d"></a>

### `MPS2_EXP_NUM_POS`

```c
#define MPS2_EXP_NUM_POS 2
```

<a id="af7cfe8556e424a3018d0e62e62f1b210"></a>

### `MPS2_PINCTRL_FUNC_GPIO`

```c
#define MPS2_PINCTRL_FUNC_GPIO 1
```

<a id="a33857f12895ab4ffb8bac15a226d9e44"></a>

### `MPS2_PINCTRL_FUNC_I2C`

```c
#define MPS2_PINCTRL_FUNC_I2C 2
```

<a id="a459cfc88b65ae738b2a94be1fbe6df46"></a>

### `MPS2_PINCTRL_FUNC_SPI`

```c
#define MPS2_PINCTRL_FUNC_SPI 3
```

<a id="a793e19909cf9cdd9fb1aa0a34f835c65"></a>

### `MPS2_PINCTRL_FUNC_UART`

```c
#define MPS2_PINCTRL_FUNC_UART 0
```

<a id="affba791a0c60352a28b3d8f122534540"></a>

### `MPS2_PINMUX`

```c
#define MPS2_PINMUX ( alt_func, exp_num )
```

展开值（Value）：

```c
(exp_num << MPS2_EXP_NUM_POS | \
alt_func << MPS2_ALT_FUNC_POS)
```

<a id="a301bb93777a77d4fcbed8617edbe319a"></a>

### `SBCON2_SCL_EXP`

```c
#define SBCON2_SCL_EXP MPS2_PINMUX(MPS2_PINCTRL_FUNC_I2C, 5)
```

<a id="a8c2f848c26c691ce333e05fe17c9341d"></a>

### `SBCON2_SDA_EXP`

```c
#define SBCON2_SDA_EXP MPS2_PINMUX(MPS2_PINCTRL_FUNC_I2C, 15)
```

<a id="a42708eb48f46a3dd04242b446389057b"></a>

### `SBCON3_SCL_EXP`

```c
#define SBCON3_SCL_EXP MPS2_PINMUX(MPS2_PINCTRL_FUNC_I2C, 31)
```

<a id="a1f600b98990e17441e52f65cc0dabddb"></a>

### `SBCON3_SDA_EXP`

```c
#define SBCON3_SDA_EXP MPS2_PINMUX(MPS2_PINCTRL_FUNC_I2C, 41)
```

<a id="af0e38d71c2b6d7cb6f1238e17e8fff6f"></a>

### `SPI2_MISO_EXP`

```c
#define SPI2_MISO_EXP MPS2_PINMUX(MPS2_PINCTRL_FUNC_SPI, 17)
```

<a id="a32eff7bbffdfc00975ff1b5f3281eaa1"></a>

### `SPI2_MOSI_EXP`

```c
#define SPI2_MOSI_EXP MPS2_PINMUX(MPS2_PINCTRL_FUNC_SPI, 18)
```

<a id="a6fbdf386063229b64599d3c2071ebffd"></a>

### `SPI2_SCK_EXP`

```c
#define SPI2_SCK_EXP MPS2_PINMUX(MPS2_PINCTRL_FUNC_SPI, 19)
```

<a id="af8e71afd57806fbe85b504ac68879fa6"></a>

### `SPI2_SS_EXP`

```c
#define SPI2_SS_EXP MPS2_PINMUX(MPS2_PINCTRL_FUNC_SPI, 16)
```

<a id="a14c932b34877e7b1f004bdf3edfdcd4b"></a>

### `SPI3_MISO_EXP`

```c
#define SPI3_MISO_EXP MPS2_PINMUX(MPS2_PINCTRL_FUNC_SPI, 14)
```

<a id="a95f2fe6603f5ab5de9c410dfaf87dc52"></a>

### `SPI3_MOSI_EXP`

```c
#define SPI3_MOSI_EXP MPS2_PINMUX(MPS2_PINCTRL_FUNC_SPI, 13)
```

<a id="ac3801e4481859951369757ac96612165"></a>

### `SPI3_SCK_EXP`

```c
#define SPI3_SCK_EXP MPS2_PINMUX(MPS2_PINCTRL_FUNC_SPI, 11)
```

<a id="ae1f9ab03b508c087a9190d742b67fc2a"></a>

### `SPI3_SS_EXP`

```c
#define SPI3_SS_EXP MPS2_PINMUX(MPS2_PINCTRL_FUNC_SPI, 12)
```

<a id="a9709eee41e54142558c4930f1b034043"></a>

### `SPI4_MISO_EXP`

```c
#define SPI4_MISO_EXP MPS2_PINMUX(MPS2_PINCTRL_FUNC_SPI, 40)
```

<a id="aa73c8c56e661787cc05b131f86a8478c"></a>

### `SPI4_MOSI_EXP`

```c
#define SPI4_MOSI_EXP MPS2_PINMUX(MPS2_PINCTRL_FUNC_SPI, 39)
```

<a id="aa48a51e34a517797511e7214ad00b7de"></a>

### `SPI4_SCK_EXP`

```c
#define SPI4_SCK_EXP MPS2_PINMUX(MPS2_PINCTRL_FUNC_SPI, 44)
```

<a id="a525321e1403275e09014f3ff1fa88d78"></a>

### `SPI4_SS_EXP`

```c
#define SPI4_SS_EXP MPS2_PINMUX(MPS2_PINCTRL_FUNC_SPI, 38)
```

<a id="aad1ef19e8c46127baf5ddb680f4a9c2e"></a>

### `UART3_RXD_EXP`

```c
#define UART3_RXD_EXP MPS2_PINMUX(MPS2_PINCTRL_FUNC_UART, 0)
```

<a id="aab7f8b8584aa06a033aa1e93200eb0d6"></a>

### `UART3_TXD_EXP`

```c
#define UART3_TXD_EXP MPS2_PINMUX(MPS2_PINCTRL_FUNC_UART, 4)
```

<a id="a960b6b4bf5810595c274fab5842189e4"></a>

### `UART4_RXD_EXP`

```c
#define UART4_RXD_EXP MPS2_PINMUX(MPS2_PINCTRL_FUNC_UART, 26)
```

<a id="a8f2f8e4cb191c641dad8dff6c4753e38"></a>

### `UART4_TXD_EXP`

```c
#define UART4_TXD_EXP MPS2_PINMUX(MPS2_PINCTRL_FUNC_UART, 30)
```


## 17.3\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_runtime_reference/P001_arm-mps2-pinctrl.h_源码浏览.md)

<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="aarm-mps2-pinctrl_8h_html_a8fc17b69bcffa4039b207b6a4ab7475d"></a>
<a id="aarm-mps2-pinctrl_8h_html_ad565796e43c28185243be8c71f910e3f"></a>

---

[上一章](P016_zephyr__arch__arch_inlines.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P018_zephyr__dt-bindings__pinctrl__arm-mps3-pinctrl.h_文件参考.md)
