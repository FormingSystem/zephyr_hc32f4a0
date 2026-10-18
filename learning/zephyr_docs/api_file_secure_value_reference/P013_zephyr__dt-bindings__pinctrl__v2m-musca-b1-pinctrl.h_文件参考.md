---
id: learning.zephyr-docs.api-file-secure-value-reference.page-13
title: zephyr__dt-bindings__pinctrl__v2m-musca-b1-pinctrl.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/v2m-musca-b1-pinctrl_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第13章\_zephyr\_\_dt-bindings\_\_pinctrl\_\_v2m-musca-b1-pinctrl.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/v2m-musca-b1-pinctrl_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Musca-B1引脚控制（Pinctrl）的引脚功能宏。

查看此文件的源码。

<a id="details"></a>

Musca-B1 引脚控制（Pinctrl）引脚功能宏。此文件包含的宏可通过开发板的引脚控制驱动，为 Musca-B1 GPIO 引脚选择复用功能（Alternate Functions）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 13.1\_宏定义（Macros）

<a id="r_a068a34e95f049274ed5c12ab6eb18291"></a>

```c
#define MUSCA_B1_ALT_FUNC_MASK 0x1
```

相关声明：[MUSCA_B1_ALT_FUNC_MASK](#a068a34e95f049274ed5c12ab6eb18291)。

在 Musca-B1 上选择 ALTF1 的位掩码（Bitmask）。

<a id="r_ae603a19ceabc16f80c4e8c7511560f42"></a>

```c
#define MUSCA_B1_ALT_FUNC_POS 0
```

相关声明：[MUSCA_B1_ALT_FUNC_POS](#ae603a19ceabc16f80c4e8c7511560f42)。

应用位掩码以选择 Musca-B1 ALTF1 的位位置（Bit Position）。

<a id="r_ac7abcfed23aea443407a473e7fdffe98"></a>

```c
#define MUSCA_B1_EXP_NUM_MASK 0xF
```

相关声明：[MUSCA_B1_EXP_NUM_MASK](#ac7abcfed23aea443407a473e7fdffe98)。

Musca-B1 引脚复用值（Pinmux Value）中引脚编号的位掩码（Bitmask）。

<a id="r_a4d46d255cac25048be8709989e0de104"></a>

```c
#define MUSCA_B1_EXP_NUM_POS 4
```

相关声明：[MUSCA_B1_EXP_NUM_POS](#a4d46d255cac25048be8709989e0de104)。

Musca-B1 引脚复用值（Pinmux Value）中引脚编号的位位置（Bit Position）。

<a id="r_a69d66eb837e03b6155fe68e11b2e1e5c"></a>

```c
#define MUSCA_B1_PINMUX(exp_num)
```

相关声明：[MUSCA_B1_PINMUX](#a69d66eb837e03b6155fe68e11b2e1e5c)。

Musca-B1 GPIO 只有一种复用功能（Alternate Function）；此宏指定 `exp_num` 对应的位应使用该复用功能。

<a id="define-members-0"></a>

### Musca-B1 引脚控制功能（Pinctrl Pin Functions）

<a id="r_a28fc91fb6e973e5f0be9e44e5edd5449"></a>

```c
#define UART0_RXD MUSCA_B1_PINMUX(0)
```

相关声明：[UART0_RXD](#a28fc91fb6e973e5f0be9e44e5edd5449)、[MUSCA_B1_PINMUX](#a69d66eb837e03b6155fe68e11b2e1e5c)。

UART0 接收数据（RxD）。

<a id="r_add71a59fa12734b27043cabf5546d176"></a>

```c
#define UART0_TXD MUSCA_B1_PINMUX(1)
```

相关声明：[UART0_TXD](#add71a59fa12734b27043cabf5546d176)、[MUSCA_B1_PINMUX](#a69d66eb837e03b6155fe68e11b2e1e5c)。

UART0 发送数据（TxD）。

<a id="r_af369bbd5c1250c1013dc05d1e4ae0b48"></a>

```c
#define MR_I2S_SD MUSCA_B1_PINMUX(2)
```

相关声明：[MR_I2S_SD](#af369bbd5c1250c1013dc05d1e4ae0b48)、[MUSCA_B1_PINMUX](#a69d66eb837e03b6155fe68e11b2e1e5c)。

I2S 接收器串行数据（SD）。

<a id="r_aedef2935bbab575b170a727a090bebc5"></a>

```c
#define MR_I2S_WS MUSCA_B1_PINMUX(3)
```

相关声明：[MR_I2S_WS](#aedef2935bbab575b170a727a090bebc5)、[MUSCA_B1_PINMUX](#a69d66eb837e03b6155fe68e11b2e1e5c)。

I2S 接收器字选择（WS）。

<a id="r_a1fe2f9e9669c9291754aa9ef3b2ca69a"></a>

```c
#define MR_I2S_SCK MUSCA_B1_PINMUX(4)
```

相关声明：[MR_I2S_SCK](#a1fe2f9e9669c9291754aa9ef3b2ca69a)、[MUSCA_B1_PINMUX](#a69d66eb837e03b6155fe68e11b2e1e5c)。

I2S 接收器串行时钟（SCK）。

<a id="r_a0523cd744d70a684cb734e8151695b85"></a>

```c
#define MT_I2S_SD0 MUSCA_B1_PINMUX(6)
```

相关声明：[MT_I2S_SD0](#a0523cd744d70a684cb734e8151695b85)、[MUSCA_B1_PINMUX](#a69d66eb837e03b6155fe68e11b2e1e5c)。

I2S 发送器串行数据 0（SD0）。

<a id="r_aba9ccdbffe12ca052a10f8f0d0b761ba"></a>

```c
#define MT_I2S_WS0 MUSCA_B1_PINMUX(5)
```

相关声明：[MT_I2S_WS0](#aba9ccdbffe12ca052a10f8f0d0b761ba)、[MUSCA_B1_PINMUX](#a69d66eb837e03b6155fe68e11b2e1e5c)。

I2S 发送器字选择 0（WS0）。

<a id="r_ab3003f583f98c104b66f66ed71c43aa4"></a>

```c
#define MT_I2S_SD1 MUSCA_B1_PINMUX(7)
```

相关声明：[MT_I2S_SD1](#ab3003f583f98c104b66f66ed71c43aa4)、[MUSCA_B1_PINMUX](#a69d66eb837e03b6155fe68e11b2e1e5c)。

I2S 发送器串行数据 1（SD1）。

<a id="r_a743d33c46dfe5ab02659b98c77b27ca8"></a>

```c
#define MT_I2S_WS1 MUSCA_B1_PINMUX(8)
```

相关声明：[MT_I2S_WS1](#a743d33c46dfe5ab02659b98c77b27ca8)、[MUSCA_B1_PINMUX](#a69d66eb837e03b6155fe68e11b2e1e5c)。

I2S 发送器字选择 1（WS1）。

<a id="r_aca80cc1db0493ef2fb3d95426a8ec73f"></a>

```c
#define MT_I2S_SCK MUSCA_B1_PINMUX(9)
```

相关声明：[MT_I2S_SCK](#aca80cc1db0493ef2fb3d95426a8ec73f)、[MUSCA_B1_PINMUX](#a69d66eb837e03b6155fe68e11b2e1e5c)。

I2S 发送器串行时钟（SCK）。

<a id="r_a93a773be005e44f1ea3a8d96db451fb1"></a>

```c
#define SPIO_NSS0 MUSCA_B1_PINMUX(10)
```

相关声明：[SPIO_NSS0](#a93a773be005e44f1ea3a8d96db451fb1)、[MUSCA_B1_PINMUX](#a69d66eb837e03b6155fe68e11b2e1e5c)。

SPIO 低有效从设备选择 0（nSS0）。

<a id="r_ac9ebacd5c6e8a12e40a36a8ecc054b10"></a>

```c
#define SPIO_MOSI MUSCA_B1_PINMUX(11)
```

相关声明：[SPIO_MOSI](#ac9ebacd5c6e8a12e40a36a8ecc054b10)、[MUSCA_B1_PINMUX](#a69d66eb837e03b6155fe68e11b2e1e5c)。

SPIO 主出从入数据（MOSI）。

<a id="r_aa14d0ee235ea61cae77c3b2219c1e7e2"></a>

```c
#define SPIO_MISO MUSCA_B1_PINMUX(12)
```

相关声明：[SPIO_MISO](#aa14d0ee235ea61cae77c3b2219c1e7e2)、[MUSCA_B1_PINMUX](#a69d66eb837e03b6155fe68e11b2e1e5c)。

SPIO 主入从出数据（MISO）。

<a id="r_ae959dc440dbb6e773c14c1d26af7e22e"></a>

```c
#define SPIO_SCK MUSCA_B1_PINMUX(13)
```

相关声明：[SPIO_SCK](#ae959dc440dbb6e773c14c1d26af7e22e)、[MUSCA_B1_PINMUX](#a69d66eb837e03b6155fe68e11b2e1e5c)。

SPIO 串行时钟（SCK）。

<a id="r_aeb73401daad152dd6e79796873665d4a"></a>

```c
#define I2C0_DATA MUSCA_B1_PINMUX(14)
```

相关声明：[I2C0_DATA](#aeb73401daad152dd6e79796873665d4a)、[MUSCA_B1_PINMUX](#a69d66eb837e03b6155fe68e11b2e1e5c)。

I2C0 数据线（Data）。

<a id="r_a1b89787393ccae5469f21a6cfc100ad6"></a>

```c
#define I2C0_CLOCK MUSCA_B1_PINMUX(15)
```

相关声明：[I2C0_CLOCK](#a1b89787393ccae5469f21a6cfc100ad6)、[MUSCA_B1_PINMUX](#a69d66eb837e03b6155fe68e11b2e1e5c)。

I2C0 时钟（Clock）。

## 13.2\_详细说明（Detailed Documentation）

<a id="a1b89787393ccae5469f21a6cfc100ad6"></a>

### `I2C0_CLOCK`

```c
#define I2C0_CLOCK MUSCA_B1_PINMUX(15)
```

I2C0 时钟（Clock）。

<a id="aeb73401daad152dd6e79796873665d4a"></a>

### `I2C0_DATA`

```c
#define I2C0_DATA MUSCA_B1_PINMUX(14)
```

I2C0 数据线（Data）。

<a id="a1fe2f9e9669c9291754aa9ef3b2ca69a"></a>

### `MR_I2S_SCK`

```c
#define MR_I2S_SCK MUSCA_B1_PINMUX(4)
```

I2S 接收器串行时钟（SCK）。

<a id="af369bbd5c1250c1013dc05d1e4ae0b48"></a>

### `MR_I2S_SD`

```c
#define MR_I2S_SD MUSCA_B1_PINMUX(2)
```

I2S 接收器串行数据（SD）。

<a id="aedef2935bbab575b170a727a090bebc5"></a>

### `MR_I2S_WS`

```c
#define MR_I2S_WS MUSCA_B1_PINMUX(3)
```

I2S 接收器字选择（WS）。

<a id="aca80cc1db0493ef2fb3d95426a8ec73f"></a>

### `MT_I2S_SCK`

```c
#define MT_I2S_SCK MUSCA_B1_PINMUX(9)
```

I2S 发送器串行时钟（SCK）。

<a id="a0523cd744d70a684cb734e8151695b85"></a>

### `MT_I2S_SD0`

```c
#define MT_I2S_SD0 MUSCA_B1_PINMUX(6)
```

I2S 发送器串行数据 0（SD0）。

<a id="ab3003f583f98c104b66f66ed71c43aa4"></a>

### `MT_I2S_SD1`

```c
#define MT_I2S_SD1 MUSCA_B1_PINMUX(7)
```

I2S 发送器串行数据 1（SD1）。

<a id="aba9ccdbffe12ca052a10f8f0d0b761ba"></a>

### `MT_I2S_WS0`

```c
#define MT_I2S_WS0 MUSCA_B1_PINMUX(5)
```

I2S 发送器字选择 0（WS0）。

<a id="a743d33c46dfe5ab02659b98c77b27ca8"></a>

### `MT_I2S_WS1`

```c
#define MT_I2S_WS1 MUSCA_B1_PINMUX(8)
```

I2S 发送器字选择 1（WS1）。

<a id="a068a34e95f049274ed5c12ab6eb18291"></a>

### `MUSCA_B1_ALT_FUNC_MASK`

```c
#define MUSCA_B1_ALT_FUNC_MASK 0x1
```

在 Musca-B1 上选择 ALTF1 的位掩码（Bitmask）。

<a id="ae603a19ceabc16f80c4e8c7511560f42"></a>

### `MUSCA_B1_ALT_FUNC_POS`

```c
#define MUSCA_B1_ALT_FUNC_POS 0
```

应用位掩码以选择 Musca-B1 ALTF1 的位位置（Bit Position）。

<a id="ac7abcfed23aea443407a473e7fdffe98"></a>

### `MUSCA_B1_EXP_NUM_MASK`

```c
#define MUSCA_B1_EXP_NUM_MASK 0xF
```

Musca-B1 引脚复用值（Pinmux Value）中引脚编号的位掩码（Bitmask）。

<a id="a4d46d255cac25048be8709989e0de104"></a>

### `MUSCA_B1_EXP_NUM_POS`

```c
#define MUSCA_B1_EXP_NUM_POS 4
```

Musca-B1 引脚复用值（Pinmux Value）中引脚编号的位位置（Bit Position）。

<a id="a69d66eb837e03b6155fe68e11b2e1e5c"></a>

### `MUSCA_B1_PINMUX`

```c
#define MUSCA_B1_PINMUX ( exp_num)
```

展开值（Value）：

```c
(exp_num << MUSCA_B1_EXP_NUM_POS | 1 << MUSCA_B1_ALT_FUNC_POS)
```

Musca-B1 GPIO 只有一种复用功能（Alternate Function）；此宏指定 `exp_num` 对应的位应使用该复用功能。

<a id="aa14d0ee235ea61cae77c3b2219c1e7e2"></a>

### `SPIO_MISO`

```c
#define SPIO_MISO MUSCA_B1_PINMUX(12)
```

SPIO 主入从出数据（MISO）。

<a id="ac9ebacd5c6e8a12e40a36a8ecc054b10"></a>

### `SPIO_MOSI`

```c
#define SPIO_MOSI MUSCA_B1_PINMUX(11)
```

SPIO 主出从入数据（MOSI）。

<a id="a93a773be005e44f1ea3a8d96db451fb1"></a>

### `SPIO_NSS0`

```c
#define SPIO_NSS0 MUSCA_B1_PINMUX(10)
```

SPIO 低有效从设备选择 0（nSS0）。

<a id="ae959dc440dbb6e773c14c1d26af7e22e"></a>

### `SPIO_SCK`

```c
#define SPIO_SCK MUSCA_B1_PINMUX(13)
```

SPIO 串行时钟（SCK）。

<a id="a28fc91fb6e973e5f0be9e44e5edd5449"></a>

### `UART0_RXD`

```c
#define UART0_RXD MUSCA_B1_PINMUX(0)
```

UART0 接收数据（RxD）。

<a id="add71a59fa12734b27043cabf5546d176"></a>

### `UART0_TXD`

```c
#define UART0_TXD MUSCA_B1_PINMUX(1)
```

UART0 发送数据（TxD）。


## 13.3\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_reference/P900_v2m-musca-b1-pinctrl.h_源码浏览.md)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="av2m-musca-b1-pinctrl_8h_html_a4d46d255cac25048be8709989e0de104"></a>
<a id="av2m-musca-b1-pinctrl_8h_html_ae603a19ceabc16f80c4e8c7511560f42"></a>

---

[上一章](P012_zephyr__drivers__i2c__target__regset_target_lib.h_文件参考.md) · [返回大纲](大纲.md)
