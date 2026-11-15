---
id: learning.zephyr-docs.api-file-reference.page-18
title: zephyr__dt-bindings__pinctrl__arm-mps3-pinctrl.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/arm-mps3-pinctrl_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第18章\_zephyr\_\_dt-bindings\_\_pinctrl\_\_arm-mps3-pinctrl.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/arm-mps3-pinctrl_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

查看此文件的源码。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 18.1\_宏定义（Macros）

<a id="r_a92d23b008eed86044d67552ec703f2ab"></a>

```c
#define MPS3_ALT_FUNC_POS 0
```

相关声明：[MPS3_ALT_FUNC_POS](#a92d23b008eed86044d67552ec703f2ab)。

<a id="r_af29520fbd24c4ed2559ff1dcefa9c901"></a>

```c
#define MPS3_ALT_FUNC_MASK 0x7
```

相关声明：[MPS3_ALT_FUNC_MASK](#af29520fbd24c4ed2559ff1dcefa9c901)。

<a id="r_a271fc39e2ac01cf6973857666445b92a"></a>

```c
#define MPS3_EXP_NUM_POS 3
```

相关声明：[MPS3_EXP_NUM_POS](#a271fc39e2ac01cf6973857666445b92a)。

<a id="r_a38ff399b3140635abe0858e73ad02b5a"></a>

```c
#define MPS3_EXP_NUM_MASK 0x1F8
```

相关声明：[MPS3_EXP_NUM_MASK](#a38ff399b3140635abe0858e73ad02b5a)。

<a id="r_a67c22b434c59a2eee7c6b60e2b70ae59"></a>

```c
#define MPS3_PINCTRL_FUNC_UART 0
```

相关声明：[MPS3_PINCTRL_FUNC_UART](#a67c22b434c59a2eee7c6b60e2b70ae59)。

<a id="r_a89a852a0ee4d66c8031b09f6db24331a"></a>

```c
#define MPS3_PINCTRL_FUNC_GPIO 1
```

相关声明：[MPS3_PINCTRL_FUNC_GPIO](#a89a852a0ee4d66c8031b09f6db24331a)。

<a id="r_a23b4c2379a045e9c16bd53d4c5226252"></a>

```c
#define MPS3_PINCTRL_FUNC_I2C 2
```

相关声明：[MPS3_PINCTRL_FUNC_I2C](#a23b4c2379a045e9c16bd53d4c5226252)。

<a id="r_a9a5e1735229d515e14606ba2c5347195"></a>

```c
#define MPS3_PINCTRL_FUNC_SPI 3
```

相关声明：[MPS3_PINCTRL_FUNC_SPI](#a9a5e1735229d515e14606ba2c5347195)。

<a id="r_a7ba2947efe4589c519c8a4531def43a9"></a>

```c
#define MPS3_PINCTRL_FUNC_PMOD 4
```

相关声明：[MPS3_PINCTRL_FUNC_PMOD](#a7ba2947efe4589c519c8a4531def43a9)。

<a id="r_ad10638589bc1eaa0bc10ef0529cb816c"></a>

```c
#define MPS3_PINMUX(alt_func, exp_num)
```

相关声明：[MPS3_PINMUX](#ad10638589bc1eaa0bc10ef0529cb816c)。

<a id="r_a34c7b3c59e141cc0dbae7e0edc2ad129"></a>

```c
#define PMOD1_IO1_EXP MPS3_PINMUX(MPS3_PINCTRL_FUNC_PMOD, 0)
```

相关声明：[PMOD1_IO1_EXP](#a34c7b3c59e141cc0dbae7e0edc2ad129)、[MPS3_PINMUX](#ad10638589bc1eaa0bc10ef0529cb816c)、[MPS3_PINCTRL_FUNC_PMOD](#a7ba2947efe4589c519c8a4531def43a9)。

<a id="r_a4424b55dd5454cd7fa120a23cd5df6f4"></a>

```c
#define PMOD1_IO0_EXP MPS3_PINMUX(MPS3_PINCTRL_FUNC_PMOD, 1)
```

相关声明：[PMOD1_IO0_EXP](#a4424b55dd5454cd7fa120a23cd5df6f4)、[MPS3_PINMUX](#ad10638589bc1eaa0bc10ef0529cb816c)、[MPS3_PINCTRL_FUNC_PMOD](#a7ba2947efe4589c519c8a4531def43a9)。

<a id="r_a02b3cca65f1c7756a3ffe36b7987222b"></a>

```c
#define PMOD1_SS_EXP MPS3_PINMUX(MPS3_PINCTRL_FUNC_PMOD, 3)
```

相关声明：[PMOD1_SS_EXP](#a02b3cca65f1c7756a3ffe36b7987222b)、[MPS3_PINMUX](#ad10638589bc1eaa0bc10ef0529cb816c)、[MPS3_PINCTRL_FUNC_PMOD](#a7ba2947efe4589c519c8a4531def43a9)。

<a id="r_a0695f557cb8f855300365e2be11bc9bb"></a>

```c
#define PMOD0_IO2_EXP MPS3_PINMUX(MPS3_PINCTRL_FUNC_PMOD, 7)
```

相关声明：[PMOD0_IO2_EXP](#a0695f557cb8f855300365e2be11bc9bb)、[MPS3_PINMUX](#ad10638589bc1eaa0bc10ef0529cb816c)、[MPS3_PINCTRL_FUNC_PMOD](#a7ba2947efe4589c519c8a4531def43a9)。

<a id="r_a585aef742cc326eee64903f1fcef6883"></a>

```c
#define PMOD0_IO3_EXP MPS3_PINMUX(MPS3_PINCTRL_FUNC_PMOD, 8)
```

相关声明：[PMOD0_IO3_EXP](#a585aef742cc326eee64903f1fcef6883)、[MPS3_PINMUX](#ad10638589bc1eaa0bc10ef0529cb816c)、[MPS3_PINCTRL_FUNC_PMOD](#a7ba2947efe4589c519c8a4531def43a9)。

<a id="r_a91e253309b1e5b615c204836c13900da"></a>

```c
#define PMOD1_SCK_EXP MPS3_PINMUX(MPS3_PINCTRL_FUNC_PMOD, 9)
```

相关声明：[PMOD1_SCK_EXP](#a91e253309b1e5b615c204836c13900da)、[MPS3_PINMUX](#ad10638589bc1eaa0bc10ef0529cb816c)、[MPS3_PINCTRL_FUNC_PMOD](#a7ba2947efe4589c519c8a4531def43a9)。

<a id="r_a4b78ddad746105930ae289c4afd4d4ca"></a>

```c
#define PMOD0_SS_EXP MPS3_PINMUX(MPS3_PINCTRL_FUNC_PMOD, 10)
```

相关声明：[PMOD0_SS_EXP](#a4b78ddad746105930ae289c4afd4d4ca)、[MPS3_PINMUX](#ad10638589bc1eaa0bc10ef0529cb816c)、[MPS3_PINCTRL_FUNC_PMOD](#a7ba2947efe4589c519c8a4531def43a9)。

<a id="r_a1957ed3aa96ccfb786632620782c0f49"></a>

```c
#define PMOD0_IO0_EXP MPS3_PINMUX(MPS3_PINCTRL_FUNC_PMOD, 11)
```

相关声明：[PMOD0_IO0_EXP](#a1957ed3aa96ccfb786632620782c0f49)、[MPS3_PINMUX](#ad10638589bc1eaa0bc10ef0529cb816c)、[MPS3_PINCTRL_FUNC_PMOD](#a7ba2947efe4589c519c8a4531def43a9)。

<a id="r_a4284a74f7ee7d951f316a5fa721f5b4c"></a>

```c
#define PMOD0_IO1_EXP MPS3_PINMUX(MPS3_PINCTRL_FUNC_PMOD, 12)
```

相关声明：[PMOD0_IO1_EXP](#a4284a74f7ee7d951f316a5fa721f5b4c)、[MPS3_PINMUX](#ad10638589bc1eaa0bc10ef0529cb816c)、[MPS3_PINCTRL_FUNC_PMOD](#a7ba2947efe4589c519c8a4531def43a9)。

<a id="r_a9115e37a39f5044fe5a31dff174fc773"></a>

```c
#define PMOD0_SCK_EXP MPS3_PINMUX(MPS3_PINCTRL_FUNC_PMOD, 13)
```

相关声明：[PMOD0_SCK_EXP](#a9115e37a39f5044fe5a31dff174fc773)、[MPS3_PINMUX](#ad10638589bc1eaa0bc10ef0529cb816c)、[MPS3_PINCTRL_FUNC_PMOD](#a7ba2947efe4589c519c8a4531def43a9)。

<a id="r_a8056404e55f29ba58bbd4ea106bccbe0"></a>

```c
#define PMOD1_IO3_EXP MPS3_PINMUX(MPS3_PINCTRL_FUNC_PMOD, 14)
```

相关声明：[PMOD1_IO3_EXP](#a8056404e55f29ba58bbd4ea106bccbe0)、[MPS3_PINMUX](#ad10638589bc1eaa0bc10ef0529cb816c)、[MPS3_PINCTRL_FUNC_PMOD](#a7ba2947efe4589c519c8a4531def43a9)。

<a id="r_a882a514f7c45b8969b030d3e715fd6ab"></a>

```c
#define PMOD1_IO2_EXP MPS3_PINMUX(MPS3_PINCTRL_FUNC_PMOD, 15)
```

相关声明：[PMOD1_IO2_EXP](#a882a514f7c45b8969b030d3e715fd6ab)、[MPS3_PINMUX](#ad10638589bc1eaa0bc10ef0529cb816c)、[MPS3_PINCTRL_FUNC_PMOD](#a7ba2947efe4589c519c8a4531def43a9)。

<a id="r_aad1ef19e8c46127baf5ddb680f4a9c2e"></a>

```c
#define UART3_RXD_EXP MPS3_PINMUX(MPS3_PINCTRL_FUNC_UART, 0)
```

相关声明：[UART3_RXD_EXP](#aad1ef19e8c46127baf5ddb680f4a9c2e)、[MPS3_PINMUX](#ad10638589bc1eaa0bc10ef0529cb816c)、[MPS3_PINCTRL_FUNC_UART](#a67c22b434c59a2eee7c6b60e2b70ae59)。

<a id="r_aab7f8b8584aa06a033aa1e93200eb0d6"></a>

```c
#define UART3_TXD_EXP MPS3_PINMUX(MPS3_PINCTRL_FUNC_UART, 1)
```

相关声明：[UART3_TXD_EXP](#aab7f8b8584aa06a033aa1e93200eb0d6)、[MPS3_PINMUX](#ad10638589bc1eaa0bc10ef0529cb816c)、[MPS3_PINCTRL_FUNC_UART](#a67c22b434c59a2eee7c6b60e2b70ae59)。

<a id="r_ae1f9ab03b508c087a9190d742b67fc2a"></a>

```c
#define SPI3_SS_EXP MPS3_PINMUX(MPS3_PINCTRL_FUNC_SPI, 10)
```

相关声明：[SPI3_SS_EXP](#ae1f9ab03b508c087a9190d742b67fc2a)、[MPS3_PINMUX](#ad10638589bc1eaa0bc10ef0529cb816c)、[MPS3_PINCTRL_FUNC_SPI](#a9a5e1735229d515e14606ba2c5347195)。

<a id="r_a95f2fe6603f5ab5de9c410dfaf87dc52"></a>

```c
#define SPI3_MOSI_EXP MPS3_PINMUX(MPS3_PINCTRL_FUNC_SPI, 11)
```

相关声明：[SPI3_MOSI_EXP](#a95f2fe6603f5ab5de9c410dfaf87dc52)、[MPS3_PINMUX](#ad10638589bc1eaa0bc10ef0529cb816c)、[MPS3_PINCTRL_FUNC_SPI](#a9a5e1735229d515e14606ba2c5347195)。

<a id="r_a14c932b34877e7b1f004bdf3edfdcd4b"></a>

```c
#define SPI3_MISO_EXP MPS3_PINMUX(MPS3_PINCTRL_FUNC_SPI, 12)
```

相关声明：[SPI3_MISO_EXP](#a14c932b34877e7b1f004bdf3edfdcd4b)、[MPS3_PINMUX](#ad10638589bc1eaa0bc10ef0529cb816c)、[MPS3_PINCTRL_FUNC_SPI](#a9a5e1735229d515e14606ba2c5347195)。

<a id="r_ac3801e4481859951369757ac96612165"></a>

```c
#define SPI3_SCK_EXP MPS3_PINMUX(MPS3_PINCTRL_FUNC_SPI, 13)
```

相关声明：[SPI3_SCK_EXP](#ac3801e4481859951369757ac96612165)、[MPS3_PINMUX](#ad10638589bc1eaa0bc10ef0529cb816c)、[MPS3_PINCTRL_FUNC_SPI](#a9a5e1735229d515e14606ba2c5347195)。

<a id="r_a8c2f848c26c691ce333e05fe17c9341d"></a>

```c
#define SBCON2_SDA_EXP MPS3_PINMUX(MPS3_PINCTRL_FUNC_I2C, 14)
```

相关声明：[SBCON2_SDA_EXP](#a8c2f848c26c691ce333e05fe17c9341d)、[MPS3_PINMUX](#ad10638589bc1eaa0bc10ef0529cb816c)、[MPS3_PINCTRL_FUNC_I2C](#a23b4c2379a045e9c16bd53d4c5226252)。

<a id="r_a301bb93777a77d4fcbed8617edbe319a"></a>

```c
#define SBCON2_SCL_EXP MPS3_PINMUX(MPS3_PINCTRL_FUNC_I2C, 15)
```

相关声明：[SBCON2_SCL_EXP](#a301bb93777a77d4fcbed8617edbe319a)、[MPS3_PINMUX](#ad10638589bc1eaa0bc10ef0529cb816c)、[MPS3_PINCTRL_FUNC_I2C](#a23b4c2379a045e9c16bd53d4c5226252)。

<a id="r_a960b6b4bf5810595c274fab5842189e4"></a>

```c
#define UART4_RXD_EXP MPS3_PINMUX(MPS3_PINCTRL_FUNC_UART, 16)
```

相关声明：[UART4_RXD_EXP](#a960b6b4bf5810595c274fab5842189e4)、[MPS3_PINMUX](#ad10638589bc1eaa0bc10ef0529cb816c)、[MPS3_PINCTRL_FUNC_UART](#a67c22b434c59a2eee7c6b60e2b70ae59)。

<a id="r_a8f2f8e4cb191c641dad8dff6c4753e38"></a>

```c
#define UART4_TXD_EXP MPS3_PINMUX(MPS3_PINCTRL_FUNC_UART, 17)
```

相关声明：[UART4_TXD_EXP](#a8f2f8e4cb191c641dad8dff6c4753e38)、[MPS3_PINMUX](#ad10638589bc1eaa0bc10ef0529cb816c)、[MPS3_PINCTRL_FUNC_UART](#a67c22b434c59a2eee7c6b60e2b70ae59)。

<a id="r_a525321e1403275e09014f3ff1fa88d78"></a>

```c
#define SPI4_SS_EXP MPS3_PINMUX(MPS3_PINCTRL_FUNC_SPI, 26)
```

相关声明：[SPI4_SS_EXP](#a525321e1403275e09014f3ff1fa88d78)、[MPS3_PINMUX](#ad10638589bc1eaa0bc10ef0529cb816c)、[MPS3_PINCTRL_FUNC_SPI](#a9a5e1735229d515e14606ba2c5347195)。

<a id="r_aa73c8c56e661787cc05b131f86a8478c"></a>

```c
#define SPI4_MOSI_EXP MPS3_PINMUX(MPS3_PINCTRL_FUNC_SPI, 27)
```

相关声明：[SPI4_MOSI_EXP](#aa73c8c56e661787cc05b131f86a8478c)、[MPS3_PINMUX](#ad10638589bc1eaa0bc10ef0529cb816c)、[MPS3_PINCTRL_FUNC_SPI](#a9a5e1735229d515e14606ba2c5347195)。

<a id="r_a9709eee41e54142558c4930f1b034043"></a>

```c
#define SPI4_MISO_EXP MPS3_PINMUX(MPS3_PINCTRL_FUNC_SPI, 28)
```

相关声明：[SPI4_MISO_EXP](#a9709eee41e54142558c4930f1b034043)、[MPS3_PINMUX](#ad10638589bc1eaa0bc10ef0529cb816c)、[MPS3_PINCTRL_FUNC_SPI](#a9a5e1735229d515e14606ba2c5347195)。

<a id="r_aa48a51e34a517797511e7214ad00b7de"></a>

```c
#define SPI4_SCK_EXP MPS3_PINMUX(MPS3_PINCTRL_FUNC_SPI, 29)
```

相关声明：[SPI4_SCK_EXP](#aa48a51e34a517797511e7214ad00b7de)、[MPS3_PINMUX](#ad10638589bc1eaa0bc10ef0529cb816c)、[MPS3_PINCTRL_FUNC_SPI](#a9a5e1735229d515e14606ba2c5347195)。

<a id="r_a1f600b98990e17441e52f65cc0dabddb"></a>

```c
#define SBCON3_SDA_EXP MPS3_PINMUX(MPS3_PINCTRL_FUNC_I2C, 30)
```

相关声明：[SBCON3_SDA_EXP](#a1f600b98990e17441e52f65cc0dabddb)、[MPS3_PINMUX](#ad10638589bc1eaa0bc10ef0529cb816c)、[MPS3_PINCTRL_FUNC_I2C](#a23b4c2379a045e9c16bd53d4c5226252)。

<a id="r_a42708eb48f46a3dd04242b446389057b"></a>

```c
#define SBCON3_SCL_EXP MPS3_PINMUX(MPS3_PINCTRL_FUNC_I2C, 31)
```

相关声明：[SBCON3_SCL_EXP](#a42708eb48f46a3dd04242b446389057b)、[MPS3_PINMUX](#ad10638589bc1eaa0bc10ef0529cb816c)、[MPS3_PINCTRL_FUNC_I2C](#a23b4c2379a045e9c16bd53d4c5226252)。

## 18.2\_详细说明（Detailed Documentation）

<a id="af29520fbd24c4ed2559ff1dcefa9c901"></a>

### `MPS3_ALT_FUNC_MASK`

```c
#define MPS3_ALT_FUNC_MASK 0x7
```

<a id="a92d23b008eed86044d67552ec703f2ab"></a>

### `MPS3_ALT_FUNC_POS`

```c
#define MPS3_ALT_FUNC_POS 0
```

<a id="a38ff399b3140635abe0858e73ad02b5a"></a>

### `MPS3_EXP_NUM_MASK`

```c
#define MPS3_EXP_NUM_MASK 0x1F8
```

<a id="a271fc39e2ac01cf6973857666445b92a"></a>

### `MPS3_EXP_NUM_POS`

```c
#define MPS3_EXP_NUM_POS 3
```

<a id="a89a852a0ee4d66c8031b09f6db24331a"></a>

### `MPS3_PINCTRL_FUNC_GPIO`

```c
#define MPS3_PINCTRL_FUNC_GPIO 1
```

<a id="a23b4c2379a045e9c16bd53d4c5226252"></a>

### `MPS3_PINCTRL_FUNC_I2C`

```c
#define MPS3_PINCTRL_FUNC_I2C 2
```

<a id="a7ba2947efe4589c519c8a4531def43a9"></a>

### `MPS3_PINCTRL_FUNC_PMOD`

```c
#define MPS3_PINCTRL_FUNC_PMOD 4
```

<a id="a9a5e1735229d515e14606ba2c5347195"></a>

### `MPS3_PINCTRL_FUNC_SPI`

```c
#define MPS3_PINCTRL_FUNC_SPI 3
```

<a id="a67c22b434c59a2eee7c6b60e2b70ae59"></a>

### `MPS3_PINCTRL_FUNC_UART`

```c
#define MPS3_PINCTRL_FUNC_UART 0
```

<a id="ad10638589bc1eaa0bc10ef0529cb816c"></a>

### `MPS3_PINMUX`

```c
#define MPS3_PINMUX ( alt_func, exp_num )
```

展开值（Value）：

```c
(exp_num << MPS3_EXP_NUM_POS | \
alt_func << MPS3_ALT_FUNC_POS)
```

<a id="a1957ed3aa96ccfb786632620782c0f49"></a>

### `PMOD0_IO0_EXP`

```c
#define PMOD0_IO0_EXP MPS3_PINMUX(MPS3_PINCTRL_FUNC_PMOD, 11)
```

<a id="a4284a74f7ee7d951f316a5fa721f5b4c"></a>

### `PMOD0_IO1_EXP`

```c
#define PMOD0_IO1_EXP MPS3_PINMUX(MPS3_PINCTRL_FUNC_PMOD, 12)
```

<a id="a0695f557cb8f855300365e2be11bc9bb"></a>

### `PMOD0_IO2_EXP`

```c
#define PMOD0_IO2_EXP MPS3_PINMUX(MPS3_PINCTRL_FUNC_PMOD, 7)
```

<a id="a585aef742cc326eee64903f1fcef6883"></a>

### `PMOD0_IO3_EXP`

```c
#define PMOD0_IO3_EXP MPS3_PINMUX(MPS3_PINCTRL_FUNC_PMOD, 8)
```

<a id="a9115e37a39f5044fe5a31dff174fc773"></a>

### `PMOD0_SCK_EXP`

```c
#define PMOD0_SCK_EXP MPS3_PINMUX(MPS3_PINCTRL_FUNC_PMOD, 13)
```

<a id="a4b78ddad746105930ae289c4afd4d4ca"></a>

### `PMOD0_SS_EXP`

```c
#define PMOD0_SS_EXP MPS3_PINMUX(MPS3_PINCTRL_FUNC_PMOD, 10)
```

<a id="a4424b55dd5454cd7fa120a23cd5df6f4"></a>

### `PMOD1_IO0_EXP`

```c
#define PMOD1_IO0_EXP MPS3_PINMUX(MPS3_PINCTRL_FUNC_PMOD, 1)
```

<a id="a34c7b3c59e141cc0dbae7e0edc2ad129"></a>

### `PMOD1_IO1_EXP`

```c
#define PMOD1_IO1_EXP MPS3_PINMUX(MPS3_PINCTRL_FUNC_PMOD, 0)
```

<a id="a882a514f7c45b8969b030d3e715fd6ab"></a>

### `PMOD1_IO2_EXP`

```c
#define PMOD1_IO2_EXP MPS3_PINMUX(MPS3_PINCTRL_FUNC_PMOD, 15)
```

<a id="a8056404e55f29ba58bbd4ea106bccbe0"></a>

### `PMOD1_IO3_EXP`

```c
#define PMOD1_IO3_EXP MPS3_PINMUX(MPS3_PINCTRL_FUNC_PMOD, 14)
```

<a id="a91e253309b1e5b615c204836c13900da"></a>

### `PMOD1_SCK_EXP`

```c
#define PMOD1_SCK_EXP MPS3_PINMUX(MPS3_PINCTRL_FUNC_PMOD, 9)
```

<a id="a02b3cca65f1c7756a3ffe36b7987222b"></a>

### `PMOD1_SS_EXP`

```c
#define PMOD1_SS_EXP MPS3_PINMUX(MPS3_PINCTRL_FUNC_PMOD, 3)
```

<a id="a301bb93777a77d4fcbed8617edbe319a"></a>

### `SBCON2_SCL_EXP`

```c
#define SBCON2_SCL_EXP MPS3_PINMUX(MPS3_PINCTRL_FUNC_I2C, 15)
```

<a id="a8c2f848c26c691ce333e05fe17c9341d"></a>

### `SBCON2_SDA_EXP`

```c
#define SBCON2_SDA_EXP MPS3_PINMUX(MPS3_PINCTRL_FUNC_I2C, 14)
```

<a id="a42708eb48f46a3dd04242b446389057b"></a>

### `SBCON3_SCL_EXP`

```c
#define SBCON3_SCL_EXP MPS3_PINMUX(MPS3_PINCTRL_FUNC_I2C, 31)
```

<a id="a1f600b98990e17441e52f65cc0dabddb"></a>

### `SBCON3_SDA_EXP`

```c
#define SBCON3_SDA_EXP MPS3_PINMUX(MPS3_PINCTRL_FUNC_I2C, 30)
```

<a id="a14c932b34877e7b1f004bdf3edfdcd4b"></a>

### `SPI3_MISO_EXP`

```c
#define SPI3_MISO_EXP MPS3_PINMUX(MPS3_PINCTRL_FUNC_SPI, 12)
```

<a id="a95f2fe6603f5ab5de9c410dfaf87dc52"></a>

### `SPI3_MOSI_EXP`

```c
#define SPI3_MOSI_EXP MPS3_PINMUX(MPS3_PINCTRL_FUNC_SPI, 11)
```

<a id="ac3801e4481859951369757ac96612165"></a>

### `SPI3_SCK_EXP`

```c
#define SPI3_SCK_EXP MPS3_PINMUX(MPS3_PINCTRL_FUNC_SPI, 13)
```

<a id="ae1f9ab03b508c087a9190d742b67fc2a"></a>

### `SPI3_SS_EXP`

```c
#define SPI3_SS_EXP MPS3_PINMUX(MPS3_PINCTRL_FUNC_SPI, 10)
```

<a id="a9709eee41e54142558c4930f1b034043"></a>

### `SPI4_MISO_EXP`

```c
#define SPI4_MISO_EXP MPS3_PINMUX(MPS3_PINCTRL_FUNC_SPI, 28)
```

<a id="aa73c8c56e661787cc05b131f86a8478c"></a>

### `SPI4_MOSI_EXP`

```c
#define SPI4_MOSI_EXP MPS3_PINMUX(MPS3_PINCTRL_FUNC_SPI, 27)
```

<a id="aa48a51e34a517797511e7214ad00b7de"></a>

### `SPI4_SCK_EXP`

```c
#define SPI4_SCK_EXP MPS3_PINMUX(MPS3_PINCTRL_FUNC_SPI, 29)
```

<a id="a525321e1403275e09014f3ff1fa88d78"></a>

### `SPI4_SS_EXP`

```c
#define SPI4_SS_EXP MPS3_PINMUX(MPS3_PINCTRL_FUNC_SPI, 26)
```

<a id="aad1ef19e8c46127baf5ddb680f4a9c2e"></a>

### `UART3_RXD_EXP`

```c
#define UART3_RXD_EXP MPS3_PINMUX(MPS3_PINCTRL_FUNC_UART, 0)
```

<a id="aab7f8b8584aa06a033aa1e93200eb0d6"></a>

### `UART3_TXD_EXP`

```c
#define UART3_TXD_EXP MPS3_PINMUX(MPS3_PINCTRL_FUNC_UART, 1)
```

<a id="a960b6b4bf5810595c274fab5842189e4"></a>

### `UART4_RXD_EXP`

```c
#define UART4_RXD_EXP MPS3_PINMUX(MPS3_PINCTRL_FUNC_UART, 16)
```

<a id="a8f2f8e4cb191c641dad8dff6c4753e38"></a>

### `UART4_TXD_EXP`

```c
#define UART4_TXD_EXP MPS3_PINMUX(MPS3_PINCTRL_FUNC_UART, 17)
```


## 18.3\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_configuration_reference/P005_arm-mps3-pinctrl.h_源码浏览.md)

<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="aarm-mps3-pinctrl_8h_html_a271fc39e2ac01cf6973857666445b92a"></a>
<a id="aarm-mps3-pinctrl_8h_html_a92d23b008eed86044d67552ec703f2ab"></a>

---

[上一章](P017_zephyr__dt-bindings__pinctrl__arm-mps2-pinctrl.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P019_zephyr__dt-bindings__pinctrl__arm-mps4-pinctrl.h_文件参考.md)
