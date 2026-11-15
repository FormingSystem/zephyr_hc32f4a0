---
id: learning.zephyr-docs.api-file-reference.page-19
title: zephyr__dt-bindings__pinctrl__arm-mps4-pinctrl.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/arm-mps4-pinctrl_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第19章\_zephyr\_\_dt-bindings\_\_pinctrl\_\_arm-mps4-pinctrl.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/arm-mps4-pinctrl_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

查看此文件的源码。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 19.1\_宏定义（Macros）

<a id="r_a8afa19b922051b18516de109ef91cfb2"></a>

```c
#define MPS4_ALT_FUNC_POS 0
```

相关声明：[MPS4_ALT_FUNC_POS](#a8afa19b922051b18516de109ef91cfb2)。

<a id="r_a7499c07aa7f241ae37a8600ab3516025"></a>

```c
#define MPS4_ALT_FUNC_MASK 0x7
```

相关声明：[MPS4_ALT_FUNC_MASK](#a7499c07aa7f241ae37a8600ab3516025)。

<a id="r_a1b4bb85578599bcbe2d5abcd82ae5059"></a>

```c
#define MPS4_EXP_NUM_POS 3
```

相关声明：[MPS4_EXP_NUM_POS](#a1b4bb85578599bcbe2d5abcd82ae5059)。

<a id="r_a835b77789dd9e689e35f4fbdf8ae4b0c"></a>

```c
#define MPS4_EXP_NUM_MASK 0x1F8
```

相关声明：[MPS4_EXP_NUM_MASK](#a835b77789dd9e689e35f4fbdf8ae4b0c)。

<a id="r_aacc441eeb486384a97b6d495b7ede5b6"></a>

```c
#define MPS4_PINCTRL_FUNC_UART 0
```

相关声明：[MPS4_PINCTRL_FUNC_UART](#aacc441eeb486384a97b6d495b7ede5b6)。

<a id="r_abce528e0feff0ea28504196171437878"></a>

```c
#define MPS4_PINCTRL_FUNC_GPIO 1
```

相关声明：[MPS4_PINCTRL_FUNC_GPIO](#abce528e0feff0ea28504196171437878)。

<a id="r_acd848d6b9cd67310c7678c9c814d019d"></a>

```c
#define MPS4_PINCTRL_FUNC_I2C 2
```

相关声明：[MPS4_PINCTRL_FUNC_I2C](#acd848d6b9cd67310c7678c9c814d019d)。

<a id="r_af70280000f1f8d002f0eee7938595220"></a>

```c
#define MPS4_PINCTRL_FUNC_SPI 3
```

相关声明：[MPS4_PINCTRL_FUNC_SPI](#af70280000f1f8d002f0eee7938595220)。

<a id="r_aeea5b5140183c5d992cc3b786d43a9ba"></a>

```c
#define MPS4_PINMUX(alt_func, exp_num)
```

相关声明：[MPS4_PINMUX](#aeea5b5140183c5d992cc3b786d43a9ba)。

<a id="r_aad1ef19e8c46127baf5ddb680f4a9c2e"></a>

```c
#define UART3_RXD_EXP MPS4_PINMUX(MPS4_PINCTRL_FUNC_UART, 0)
```

相关声明：[UART3_RXD_EXP](#aad1ef19e8c46127baf5ddb680f4a9c2e)、[MPS4_PINMUX](#aeea5b5140183c5d992cc3b786d43a9ba)、[MPS4_PINCTRL_FUNC_UART](#aacc441eeb486384a97b6d495b7ede5b6)。

<a id="r_aab7f8b8584aa06a033aa1e93200eb0d6"></a>

```c
#define UART3_TXD_EXP MPS4_PINMUX(MPS4_PINCTRL_FUNC_UART, 1)
```

相关声明：[UART3_TXD_EXP](#aab7f8b8584aa06a033aa1e93200eb0d6)、[MPS4_PINMUX](#aeea5b5140183c5d992cc3b786d43a9ba)、[MPS4_PINCTRL_FUNC_UART](#aacc441eeb486384a97b6d495b7ede5b6)。

<a id="r_ae1f9ab03b508c087a9190d742b67fc2a"></a>

```c
#define SPI3_SS_EXP MPS4_PINMUX(MPS4_PINCTRL_FUNC_SPI, 10)
```

相关声明：[SPI3_SS_EXP](#ae1f9ab03b508c087a9190d742b67fc2a)、[MPS4_PINMUX](#aeea5b5140183c5d992cc3b786d43a9ba)、[MPS4_PINCTRL_FUNC_SPI](#af70280000f1f8d002f0eee7938595220)。

<a id="r_a95f2fe6603f5ab5de9c410dfaf87dc52"></a>

```c
#define SPI3_MOSI_EXP MPS4_PINMUX(MPS4_PINCTRL_FUNC_SPI, 11)
```

相关声明：[SPI3_MOSI_EXP](#a95f2fe6603f5ab5de9c410dfaf87dc52)、[MPS4_PINMUX](#aeea5b5140183c5d992cc3b786d43a9ba)、[MPS4_PINCTRL_FUNC_SPI](#af70280000f1f8d002f0eee7938595220)。

<a id="r_a14c932b34877e7b1f004bdf3edfdcd4b"></a>

```c
#define SPI3_MISO_EXP MPS4_PINMUX(MPS4_PINCTRL_FUNC_SPI, 12)
```

相关声明：[SPI3_MISO_EXP](#a14c932b34877e7b1f004bdf3edfdcd4b)、[MPS4_PINMUX](#aeea5b5140183c5d992cc3b786d43a9ba)、[MPS4_PINCTRL_FUNC_SPI](#af70280000f1f8d002f0eee7938595220)。

<a id="r_ac3801e4481859951369757ac96612165"></a>

```c
#define SPI3_SCK_EXP MPS4_PINMUX(MPS4_PINCTRL_FUNC_SPI, 13)
```

相关声明：[SPI3_SCK_EXP](#ac3801e4481859951369757ac96612165)、[MPS4_PINMUX](#aeea5b5140183c5d992cc3b786d43a9ba)、[MPS4_PINCTRL_FUNC_SPI](#af70280000f1f8d002f0eee7938595220)。

<a id="r_a8c2f848c26c691ce333e05fe17c9341d"></a>

```c
#define SBCON2_SDA_EXP MPS4_PINMUX(MPS4_PINCTRL_FUNC_I2C, 14)
```

相关声明：[SBCON2_SDA_EXP](#a8c2f848c26c691ce333e05fe17c9341d)、[MPS4_PINMUX](#aeea5b5140183c5d992cc3b786d43a9ba)、[MPS4_PINCTRL_FUNC_I2C](#acd848d6b9cd67310c7678c9c814d019d)。

<a id="r_a301bb93777a77d4fcbed8617edbe319a"></a>

```c
#define SBCON2_SCL_EXP MPS4_PINMUX(MPS4_PINCTRL_FUNC_I2C, 15)
```

相关声明：[SBCON2_SCL_EXP](#a301bb93777a77d4fcbed8617edbe319a)、[MPS4_PINMUX](#aeea5b5140183c5d992cc3b786d43a9ba)、[MPS4_PINCTRL_FUNC_I2C](#acd848d6b9cd67310c7678c9c814d019d)。

<a id="r_a960b6b4bf5810595c274fab5842189e4"></a>

```c
#define UART4_RXD_EXP MPS4_PINMUX(MPS4_PINCTRL_FUNC_UART, 16)
```

相关声明：[UART4_RXD_EXP](#a960b6b4bf5810595c274fab5842189e4)、[MPS4_PINMUX](#aeea5b5140183c5d992cc3b786d43a9ba)、[MPS4_PINCTRL_FUNC_UART](#aacc441eeb486384a97b6d495b7ede5b6)。

<a id="r_a8f2f8e4cb191c641dad8dff6c4753e38"></a>

```c
#define UART4_TXD_EXP MPS4_PINMUX(MPS4_PINCTRL_FUNC_UART, 17)
```

相关声明：[UART4_TXD_EXP](#a8f2f8e4cb191c641dad8dff6c4753e38)、[MPS4_PINMUX](#aeea5b5140183c5d992cc3b786d43a9ba)、[MPS4_PINCTRL_FUNC_UART](#aacc441eeb486384a97b6d495b7ede5b6)。

<a id="r_a525321e1403275e09014f3ff1fa88d78"></a>

```c
#define SPI4_SS_EXP MPS4_PINMUX(MPS4_PINCTRL_FUNC_SPI, 26)
```

相关声明：[SPI4_SS_EXP](#a525321e1403275e09014f3ff1fa88d78)、[MPS4_PINMUX](#aeea5b5140183c5d992cc3b786d43a9ba)、[MPS4_PINCTRL_FUNC_SPI](#af70280000f1f8d002f0eee7938595220)。

<a id="r_aa73c8c56e661787cc05b131f86a8478c"></a>

```c
#define SPI4_MOSI_EXP MPS4_PINMUX(MPS4_PINCTRL_FUNC_SPI, 27)
```

相关声明：[SPI4_MOSI_EXP](#aa73c8c56e661787cc05b131f86a8478c)、[MPS4_PINMUX](#aeea5b5140183c5d992cc3b786d43a9ba)、[MPS4_PINCTRL_FUNC_SPI](#af70280000f1f8d002f0eee7938595220)。

<a id="r_a9709eee41e54142558c4930f1b034043"></a>

```c
#define SPI4_MISO_EXP MPS4_PINMUX(MPS4_PINCTRL_FUNC_SPI, 28)
```

相关声明：[SPI4_MISO_EXP](#a9709eee41e54142558c4930f1b034043)、[MPS4_PINMUX](#aeea5b5140183c5d992cc3b786d43a9ba)、[MPS4_PINCTRL_FUNC_SPI](#af70280000f1f8d002f0eee7938595220)。

<a id="r_aa48a51e34a517797511e7214ad00b7de"></a>

```c
#define SPI4_SCK_EXP MPS4_PINMUX(MPS4_PINCTRL_FUNC_SPI, 29)
```

相关声明：[SPI4_SCK_EXP](#aa48a51e34a517797511e7214ad00b7de)、[MPS4_PINMUX](#aeea5b5140183c5d992cc3b786d43a9ba)、[MPS4_PINCTRL_FUNC_SPI](#af70280000f1f8d002f0eee7938595220)。

<a id="r_a1f600b98990e17441e52f65cc0dabddb"></a>

```c
#define SBCON3_SDA_EXP MPS4_PINMUX(MPS4_PINCTRL_FUNC_I2C, 30)
```

相关声明：[SBCON3_SDA_EXP](#a1f600b98990e17441e52f65cc0dabddb)、[MPS4_PINMUX](#aeea5b5140183c5d992cc3b786d43a9ba)、[MPS4_PINCTRL_FUNC_I2C](#acd848d6b9cd67310c7678c9c814d019d)。

<a id="r_a42708eb48f46a3dd04242b446389057b"></a>

```c
#define SBCON3_SCL_EXP MPS4_PINMUX(MPS4_PINCTRL_FUNC_I2C, 31)
```

相关声明：[SBCON3_SCL_EXP](#a42708eb48f46a3dd04242b446389057b)、[MPS4_PINMUX](#aeea5b5140183c5d992cc3b786d43a9ba)、[MPS4_PINCTRL_FUNC_I2C](#acd848d6b9cd67310c7678c9c814d019d)。

## 19.2\_详细说明（Detailed Documentation）

<a id="a7499c07aa7f241ae37a8600ab3516025"></a>

### `MPS4_ALT_FUNC_MASK`

```c
#define MPS4_ALT_FUNC_MASK 0x7
```

<a id="a8afa19b922051b18516de109ef91cfb2"></a>

### `MPS4_ALT_FUNC_POS`

```c
#define MPS4_ALT_FUNC_POS 0
```

<a id="a835b77789dd9e689e35f4fbdf8ae4b0c"></a>

### `MPS4_EXP_NUM_MASK`

```c
#define MPS4_EXP_NUM_MASK 0x1F8
```

<a id="a1b4bb85578599bcbe2d5abcd82ae5059"></a>

### `MPS4_EXP_NUM_POS`

```c
#define MPS4_EXP_NUM_POS 3
```

<a id="abce528e0feff0ea28504196171437878"></a>

### `MPS4_PINCTRL_FUNC_GPIO`

```c
#define MPS4_PINCTRL_FUNC_GPIO 1
```

<a id="acd848d6b9cd67310c7678c9c814d019d"></a>

### `MPS4_PINCTRL_FUNC_I2C`

```c
#define MPS4_PINCTRL_FUNC_I2C 2
```

<a id="af70280000f1f8d002f0eee7938595220"></a>

### `MPS4_PINCTRL_FUNC_SPI`

```c
#define MPS4_PINCTRL_FUNC_SPI 3
```

<a id="aacc441eeb486384a97b6d495b7ede5b6"></a>

### `MPS4_PINCTRL_FUNC_UART`

```c
#define MPS4_PINCTRL_FUNC_UART 0
```

<a id="aeea5b5140183c5d992cc3b786d43a9ba"></a>

### `MPS4_PINMUX`

```c
#define MPS4_PINMUX ( alt_func, exp_num )
```

展开值（Value）：

```c
(exp_num << MPS4_EXP_NUM_POS | \
alt_func << MPS4_ALT_FUNC_POS)
```

<a id="a301bb93777a77d4fcbed8617edbe319a"></a>

### `SBCON2_SCL_EXP`

```c
#define SBCON2_SCL_EXP MPS4_PINMUX(MPS4_PINCTRL_FUNC_I2C, 15)
```

<a id="a8c2f848c26c691ce333e05fe17c9341d"></a>

### `SBCON2_SDA_EXP`

```c
#define SBCON2_SDA_EXP MPS4_PINMUX(MPS4_PINCTRL_FUNC_I2C, 14)
```

<a id="a42708eb48f46a3dd04242b446389057b"></a>

### `SBCON3_SCL_EXP`

```c
#define SBCON3_SCL_EXP MPS4_PINMUX(MPS4_PINCTRL_FUNC_I2C, 31)
```

<a id="a1f600b98990e17441e52f65cc0dabddb"></a>

### `SBCON3_SDA_EXP`

```c
#define SBCON3_SDA_EXP MPS4_PINMUX(MPS4_PINCTRL_FUNC_I2C, 30)
```

<a id="a14c932b34877e7b1f004bdf3edfdcd4b"></a>

### `SPI3_MISO_EXP`

```c
#define SPI3_MISO_EXP MPS4_PINMUX(MPS4_PINCTRL_FUNC_SPI, 12)
```

<a id="a95f2fe6603f5ab5de9c410dfaf87dc52"></a>

### `SPI3_MOSI_EXP`

```c
#define SPI3_MOSI_EXP MPS4_PINMUX(MPS4_PINCTRL_FUNC_SPI, 11)
```

<a id="ac3801e4481859951369757ac96612165"></a>

### `SPI3_SCK_EXP`

```c
#define SPI3_SCK_EXP MPS4_PINMUX(MPS4_PINCTRL_FUNC_SPI, 13)
```

<a id="ae1f9ab03b508c087a9190d742b67fc2a"></a>

### `SPI3_SS_EXP`

```c
#define SPI3_SS_EXP MPS4_PINMUX(MPS4_PINCTRL_FUNC_SPI, 10)
```

<a id="a9709eee41e54142558c4930f1b034043"></a>

### `SPI4_MISO_EXP`

```c
#define SPI4_MISO_EXP MPS4_PINMUX(MPS4_PINCTRL_FUNC_SPI, 28)
```

<a id="aa73c8c56e661787cc05b131f86a8478c"></a>

### `SPI4_MOSI_EXP`

```c
#define SPI4_MOSI_EXP MPS4_PINMUX(MPS4_PINCTRL_FUNC_SPI, 27)
```

<a id="aa48a51e34a517797511e7214ad00b7de"></a>

### `SPI4_SCK_EXP`

```c
#define SPI4_SCK_EXP MPS4_PINMUX(MPS4_PINCTRL_FUNC_SPI, 29)
```

<a id="a525321e1403275e09014f3ff1fa88d78"></a>

### `SPI4_SS_EXP`

```c
#define SPI4_SS_EXP MPS4_PINMUX(MPS4_PINCTRL_FUNC_SPI, 26)
```

<a id="aad1ef19e8c46127baf5ddb680f4a9c2e"></a>

### `UART3_RXD_EXP`

```c
#define UART3_RXD_EXP MPS4_PINMUX(MPS4_PINCTRL_FUNC_UART, 0)
```

<a id="aab7f8b8584aa06a033aa1e93200eb0d6"></a>

### `UART3_TXD_EXP`

```c
#define UART3_TXD_EXP MPS4_PINMUX(MPS4_PINCTRL_FUNC_UART, 1)
```

<a id="a960b6b4bf5810595c274fab5842189e4"></a>

### `UART4_RXD_EXP`

```c
#define UART4_RXD_EXP MPS4_PINMUX(MPS4_PINCTRL_FUNC_UART, 16)
```

<a id="a8f2f8e4cb191c641dad8dff6c4753e38"></a>

### `UART4_TXD_EXP`

```c
#define UART4_TXD_EXP MPS4_PINMUX(MPS4_PINCTRL_FUNC_UART, 17)
```


## 19.3\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_configuration_reference/P006_arm-mps4-pinctrl.h_源码浏览.md)

<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="aarm-mps4-pinctrl_8h_html_a1b4bb85578599bcbe2d5abcd82ae5059"></a>
<a id="aarm-mps4-pinctrl_8h_html_a8afa19b922051b18516de109ef91cfb2"></a>

---

[上一章](P018_zephyr__dt-bindings__pinctrl__arm-mps3-pinctrl.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P020_zephyr__dt-bindings__pinctrl__arm-v2m_beetle-pinctrl.h_文件参考.md)
