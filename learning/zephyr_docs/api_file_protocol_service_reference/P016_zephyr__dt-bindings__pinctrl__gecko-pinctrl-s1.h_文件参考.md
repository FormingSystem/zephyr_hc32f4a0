---
id: learning.zephyr-docs.api-file-protocol-service-reference.page-16
title: zephyr__dt-bindings__pinctrl__gecko-pinctrl-s1.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/gecko-pinctrl-s1_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第16章\_zephyr\_\_dt-bindings\_\_pinctrl\_\_gecko-pinctrl-s1.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/gecko-pinctrl-s1_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

查看此文件的源码。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 16.1\_宏定义（Macros）

<a id="r_af1017b3a2df0dfa3e7e034e2714dfbd4"></a>

```c
#define GECKO_PORT_A 0
```

相关声明：[GECKO_PORT_A](#af1017b3a2df0dfa3e7e034e2714dfbd4)。

<a id="r_a23ce2182c7b7296899dce3022b70fd1d"></a>

```c
#define GECKO_PORT_B 1
```

相关声明：[GECKO_PORT_B](#a23ce2182c7b7296899dce3022b70fd1d)。

<a id="r_a9a8a5a42323fba6d1d7102bf5e84ac31"></a>

```c
#define GECKO_PORT_C 2
```

相关声明：[GECKO_PORT_C](#a9a8a5a42323fba6d1d7102bf5e84ac31)。

<a id="r_a740208b46b6a57eff76c08900ddcb09e"></a>

```c
#define GECKO_PORT_D 3
```

相关声明：[GECKO_PORT_D](#a740208b46b6a57eff76c08900ddcb09e)。

<a id="r_acd268feccf2103b9d10e98a3ee716696"></a>

```c
#define GECKO_PORT_E 4
```

相关声明：[GECKO_PORT_E](#acd268feccf2103b9d10e98a3ee716696)。

<a id="r_a149072d68a31c47c7d75bce5b5dfa596"></a>

```c
#define GECKO_PORT_F 5
```

相关声明：[GECKO_PORT_F](#a149072d68a31c47c7d75bce5b5dfa596)。

<a id="r_a931423cbccb8542cf8554779bcac16a1"></a>

```c
#define GECKO_PORT_G 6
```

相关声明：[GECKO_PORT_G](#a931423cbccb8542cf8554779bcac16a1)。

<a id="r_af954756a1aa7f78e8e61a31f8226ae74"></a>

```c
#define GECKO_PORT_H 7
```

相关声明：[GECKO_PORT_H](#af954756a1aa7f78e8e61a31f8226ae74)。

<a id="r_acb405086add8f2c8f215038b148c2c25"></a>

```c
#define GECKO_PORT_I 8
```

相关声明：[GECKO_PORT_I](#acb405086add8f2c8f215038b148c2c25)。

<a id="r_a066e26d3a586b420e4dcb0c1ff5c709d"></a>

```c
#define GECKO_PORT_J 9
```

相关声明：[GECKO_PORT_J](#a066e26d3a586b420e4dcb0c1ff5c709d)。

<a id="r_ac90348555b1c71e25048e21751b9b181"></a>

```c
#define GECKO_PORT_K 10
```

相关声明：[GECKO_PORT_K](#ac90348555b1c71e25048e21751b9b181)。

<a id="r_afd3e7b18220ac0786d63d15766288ec1"></a>

```c
#define GECKO_PIN(n)
```

相关声明：[GECKO_PIN](#afd3e7b18220ac0786d63d15766288ec1)。

<a id="r_a462dc592c5260981e679be5d9e0de7df"></a>

```c
#define GECKO_LOCATION(n)
```

相关声明：[GECKO_LOCATION](#a462dc592c5260981e679be5d9e0de7df)。

<a id="r_ac1af8b10c541907308332856fa9affe7"></a>

```c
#define GECKO_PSEL(fun, port, pin)
```

相关声明：[GECKO_PSEL](#ac1af8b10c541907308332856fa9affe7)。

构造 GECKO `psels` 属性条目（Property Entry）的工具宏。

<a id="r_a0c4e8fbbb218ce88bd4059bda8170e6d"></a>

```c
#define GECKO_LOC(fun, loc)
```

相关声明：[GECKO_LOC](#a0c4e8fbbb218ce88bd4059bda8170e6d)。

构造 `GECKO_psels` 属性条目（Property Entry）的工具宏。

<a id="define-members-0"></a>

### GECKO 引脚配置位域的位置和掩码（Pin Configuration Bit Field Positions and Masks）

<a id="r_af582c317ab79a3961ea00645514fc3f6"></a>

```c
#define GECKO_FUN_POS 24U
```

相关声明：[GECKO_FUN_POS](#af582c317ab79a3961ea00645514fc3f6)。

功能字段（Function Field）的位位置。

<a id="r_a87d929d0a1bc9808a854ce582a0c8251"></a>

```c
#define GECKO_FUN_MSK 0xFFU
```

相关声明：[GECKO_FUN_MSK](#a87d929d0a1bc9808a854ce582a0c8251)。

功能字段（Function Field）的掩码。

<a id="r_af4fc3615fcff891841b6226b363f9f4c"></a>

```c
#define GECKO_PIN_POS 0U
```

相关声明：[GECKO_PIN_POS](#af4fc3615fcff891841b6226b363f9f4c)。

引脚字段（Pin Field）的位位置。

<a id="r_a9e62aad832626ee3f12e55b8e0102b68"></a>

```c
#define GECKO_PIN_MSK 0xFFU
```

相关声明：[GECKO_PIN_MSK](#a9e62aad832626ee3f12e55b8e0102b68)。

引脚字段（Pin Field）的掩码。

<a id="r_aafabc892e5cc1298ff87a10afdd203ca"></a>

```c
#define GECKO_PORT_POS 8U
```

相关声明：[GECKO_PORT_POS](#aafabc892e5cc1298ff87a10afdd203ca)。

端口字段（Port Field）的位置。

<a id="r_a750badf0aada694862e9cc8135ef435c"></a>

```c
#define GECKO_PORT_MSK 0xFFU
```

相关声明：[GECKO_PORT_MSK](#a750badf0aada694862e9cc8135ef435c)。

端口字段（Port Field）的掩码。

<a id="r_a12208aabccc02edd6c64a857f14455f7"></a>

```c
#define GECKO_LOC_POS 0U
```

相关声明：[GECKO_LOC_POS](#a12208aabccc02edd6c64a857f14455f7)。

位置字段（Loc Field）的位置。

<a id="r_adef6df5f1daf2e87dbed89b433ef7d84"></a>

```c
#define GECKO_LOC_MSK 0xFFU
```

相关声明：[GECKO_LOC_MSK](#adef6df5f1daf2e87dbed89b433ef7d84)。

引脚字段（Pin Field）的掩码。

<a id="define-members-1"></a>

### GECKO 引脚控制功能（Pinctrl Pin Functions）

<a id="r_a2b19bb5a846aab3b44a3628c586df77b"></a>

```c
#define GECKO_FUN_UART_TX 0U
```

相关声明：[GECKO_FUN_UART_TX](#a2b19bb5a846aab3b44a3628c586df77b)。

UART 发送（TX）。

<a id="r_a68699f16723f6a99594f068dd0c95b2a"></a>

```c
#define GECKO_FUN_UART_RX 1U
```

相关声明：[GECKO_FUN_UART_RX](#a68699f16723f6a99594f068dd0c95b2a)。

UART 接收（RX）。

<a id="r_a65f270929aae6f65e659f1f6393d34fa"></a>

```c
#define GECKO_FUN_UART_RTS 2U
```

相关声明：[GECKO_FUN_UART_RTS](#a65f270929aae6f65e659f1f6393d34fa)。

UART 请求发送（RTS）。

<a id="r_ad4dc9908bb86aea93aaa896ea7755a29"></a>

```c
#define GECKO_FUN_UART_CTS 3U
```

相关声明：[GECKO_FUN_UART_CTS](#ad4dc9908bb86aea93aaa896ea7755a29)。

UART 清除发送（CTS）。

<a id="r_ac7e6a762e1e7e63f9172d736354820b3"></a>

```c
#define GECKO_FUN_UART_RX_LOC 4U
```

相关声明：[GECKO_FUN_UART_RX_LOC](#ac7e6a762e1e7e63f9172d736354820b3)。

UART 接收位置（RX LOCATION）。

<a id="r_a59225761dc92d12b23be60f2616c0f9f"></a>

```c
#define GECKO_FUN_UART_TX_LOC 5U
```

相关声明：[GECKO_FUN_UART_TX_LOC](#a59225761dc92d12b23be60f2616c0f9f)。

UART 发送位置（TX LOCATION）。

<a id="r_a8edacb8e79f7d7a84736104949157870"></a>

```c
#define GECKO_FUN_UART_RTS_LOC 6U
```

相关声明：[GECKO_FUN_UART_RTS_LOC](#a8edacb8e79f7d7a84736104949157870)。

UART 请求发送位置（RTS LOCATION）。

<a id="r_a3ef104d8e946ef746ba9e71bb5c469f5"></a>

```c
#define GECKO_FUN_UART_CTS_LOC 7U
```

相关声明：[GECKO_FUN_UART_CTS_LOC](#a3ef104d8e946ef746ba9e71bb5c469f5)。

UART 清除发送位置（CTS LOCATION）。

<a id="r_ad356cf8a63077cd810a13c32d7591e47"></a>

```c
#define GECKO_FUN_SPIM_MISO 8U
```

相关声明：[GECKO_FUN_SPIM_MISO](#ad356cf8a63077cd810a13c32d7591e47)。

<a id="r_a2a24765e466f1264e300d4975429c67c"></a>

```c
#define GECKO_FUN_SPIM_MOSI 9U
```

相关声明：[GECKO_FUN_SPIM_MOSI](#a2a24765e466f1264e300d4975429c67c)。

<a id="r_a570a5464219faf2252412f09f6281646"></a>

```c
#define GECKO_FUN_SPIM_CS 10U
```

相关声明：[GECKO_FUN_SPIM_CS](#a570a5464219faf2252412f09f6281646)。

<a id="r_ab77e588c302f3d18d18b72efa943e0db"></a>

```c
#define GECKO_FUN_SPIM_SCK 11U
```

相关声明：[GECKO_FUN_SPIM_SCK](#ab77e588c302f3d18d18b72efa943e0db)。

<a id="r_a1a9fef5c16e0ab5f2987b4f9ffdc6d22"></a>

```c
#define GECKO_FUN_LEUART_RX_LOC 12U
```

相关声明：[GECKO_FUN_LEUART_RX_LOC](#a1a9fef5c16e0ab5f2987b4f9ffdc6d22)。

<a id="r_a49bd14236c6fb7efb44418c05f1a91da"></a>

```c
#define GECKO_FUN_LEUART_TX_LOC 13U
```

相关声明：[GECKO_FUN_LEUART_TX_LOC](#a49bd14236c6fb7efb44418c05f1a91da)。

<a id="r_a61eedadfb95bdd6fe6e183e9c22fb7ed"></a>

```c
#define GECKO_FUN_SPIS_MISO 14U
```

相关声明：[GECKO_FUN_SPIS_MISO](#a61eedadfb95bdd6fe6e183e9c22fb7ed)。

<a id="r_a8958587b66b8cd4942b4c9ce9826f689"></a>

```c
#define GECKO_FUN_SPIS_MOSI 15U
```

相关声明：[GECKO_FUN_SPIS_MOSI](#a8958587b66b8cd4942b4c9ce9826f689)。

<a id="r_af67b9548ffaecb030464cd5f52b16285"></a>

```c
#define GECKO_FUN_SPIS_CS 16U
```

相关声明：[GECKO_FUN_SPIS_CS](#af67b9548ffaecb030464cd5f52b16285)。

<a id="r_ae77d65d5717e27242322424179de1cbe"></a>

```c
#define GECKO_FUN_SPIS_SCK 17U
```

相关声明：[GECKO_FUN_SPIS_SCK](#ae77d65d5717e27242322424179de1cbe)。

<a id="r_afb0d7445bbbba745b9cc08cb5aa01f44"></a>

```c
#define GECKO_FUN_SPI_MISO_LOC 18U
```

相关声明：[GECKO_FUN_SPI_MISO_LOC](#afb0d7445bbbba745b9cc08cb5aa01f44)。

<a id="r_a518ae94f50c55f1a19ff70d898bacf34"></a>

```c
#define GECKO_FUN_SPI_MOSI_LOC 19U
```

相关声明：[GECKO_FUN_SPI_MOSI_LOC](#a518ae94f50c55f1a19ff70d898bacf34)。

<a id="r_ad6df2bcea0c8e0e68107d70eab753f5f"></a>

```c
#define GECKO_FUN_SPI_CS_LOC 20U
```

相关声明：[GECKO_FUN_SPI_CS_LOC](#ad6df2bcea0c8e0e68107d70eab753f5f)。

<a id="r_a73dea09e9111d11f41fd52ee9a296570"></a>

```c
#define GECKO_FUN_SPI_SCK_LOC 21U
```

相关声明：[GECKO_FUN_SPI_SCK_LOC](#a73dea09e9111d11f41fd52ee9a296570)。

<a id="r_a3c29c6046d30a743df9aaae55c2b0803"></a>

```c
#define GECKO_FUN_I2C_SDA 22U
```

相关声明：[GECKO_FUN_I2C_SDA](#a3c29c6046d30a743df9aaae55c2b0803)。

<a id="r_a455a393df63ad05434c993ff18b9d3b5"></a>

```c
#define GECKO_FUN_I2C_SCL 23U
```

相关声明：[GECKO_FUN_I2C_SCL](#a455a393df63ad05434c993ff18b9d3b5)。

<a id="r_a405973ead4fd3aa22f2d976257929185"></a>

```c
#define GECKO_FUN_I2C_SDA_LOC 24U
```

相关声明：[GECKO_FUN_I2C_SDA_LOC](#a405973ead4fd3aa22f2d976257929185)。

<a id="r_a3216f884cccdd06204765849deec56b0"></a>

```c
#define GECKO_FUN_I2C_SCL_LOC 25U
```

相关声明：[GECKO_FUN_I2C_SCL_LOC](#a3216f884cccdd06204765849deec56b0)。

## 16.2\_详细说明（Detailed Documentation）

<a id="a455a393df63ad05434c993ff18b9d3b5"></a>

### `GECKO_FUN_I2C_SCL`

```c
#define GECKO_FUN_I2C_SCL 23U
```

<a id="a3216f884cccdd06204765849deec56b0"></a>

### `GECKO_FUN_I2C_SCL_LOC`

```c
#define GECKO_FUN_I2C_SCL_LOC 25U
```

<a id="a3c29c6046d30a743df9aaae55c2b0803"></a>

### `GECKO_FUN_I2C_SDA`

```c
#define GECKO_FUN_I2C_SDA 22U
```

<a id="a405973ead4fd3aa22f2d976257929185"></a>

### `GECKO_FUN_I2C_SDA_LOC`

```c
#define GECKO_FUN_I2C_SDA_LOC 24U
```

<a id="a1a9fef5c16e0ab5f2987b4f9ffdc6d22"></a>

### `GECKO_FUN_LEUART_RX_LOC`

```c
#define GECKO_FUN_LEUART_RX_LOC 12U
```

<a id="a49bd14236c6fb7efb44418c05f1a91da"></a>

### `GECKO_FUN_LEUART_TX_LOC`

```c
#define GECKO_FUN_LEUART_TX_LOC 13U
```

<a id="a87d929d0a1bc9808a854ce582a0c8251"></a>

### `GECKO_FUN_MSK`

```c
#define GECKO_FUN_MSK 0xFFU
```

功能字段（Function Field）的掩码。

<a id="af582c317ab79a3961ea00645514fc3f6"></a>

### `GECKO_FUN_POS`

```c
#define GECKO_FUN_POS 24U
```

功能字段（Function Field）的位位置。

<a id="ad6df2bcea0c8e0e68107d70eab753f5f"></a>

### `GECKO_FUN_SPI_CS_LOC`

```c
#define GECKO_FUN_SPI_CS_LOC 20U
```

<a id="afb0d7445bbbba745b9cc08cb5aa01f44"></a>

### `GECKO_FUN_SPI_MISO_LOC`

```c
#define GECKO_FUN_SPI_MISO_LOC 18U
```

<a id="a518ae94f50c55f1a19ff70d898bacf34"></a>

### `GECKO_FUN_SPI_MOSI_LOC`

```c
#define GECKO_FUN_SPI_MOSI_LOC 19U
```

<a id="a73dea09e9111d11f41fd52ee9a296570"></a>

### `GECKO_FUN_SPI_SCK_LOC`

```c
#define GECKO_FUN_SPI_SCK_LOC 21U
```

<a id="a570a5464219faf2252412f09f6281646"></a>

### `GECKO_FUN_SPIM_CS`

```c
#define GECKO_FUN_SPIM_CS 10U
```

<a id="ad356cf8a63077cd810a13c32d7591e47"></a>

### `GECKO_FUN_SPIM_MISO`

```c
#define GECKO_FUN_SPIM_MISO 8U
```

<a id="a2a24765e466f1264e300d4975429c67c"></a>

### `GECKO_FUN_SPIM_MOSI`

```c
#define GECKO_FUN_SPIM_MOSI 9U
```

<a id="ab77e588c302f3d18d18b72efa943e0db"></a>

### `GECKO_FUN_SPIM_SCK`

```c
#define GECKO_FUN_SPIM_SCK 11U
```

<a id="af67b9548ffaecb030464cd5f52b16285"></a>

### `GECKO_FUN_SPIS_CS`

```c
#define GECKO_FUN_SPIS_CS 16U
```

<a id="a61eedadfb95bdd6fe6e183e9c22fb7ed"></a>

### `GECKO_FUN_SPIS_MISO`

```c
#define GECKO_FUN_SPIS_MISO 14U
```

<a id="a8958587b66b8cd4942b4c9ce9826f689"></a>

### `GECKO_FUN_SPIS_MOSI`

```c
#define GECKO_FUN_SPIS_MOSI 15U
```

<a id="ae77d65d5717e27242322424179de1cbe"></a>

### `GECKO_FUN_SPIS_SCK`

```c
#define GECKO_FUN_SPIS_SCK 17U
```

<a id="ad4dc9908bb86aea93aaa896ea7755a29"></a>

### `GECKO_FUN_UART_CTS`

```c
#define GECKO_FUN_UART_CTS 3U
```

UART 清除发送（CTS）。

<a id="a3ef104d8e946ef746ba9e71bb5c469f5"></a>

### `GECKO_FUN_UART_CTS_LOC`

```c
#define GECKO_FUN_UART_CTS_LOC 7U
```

UART 清除发送位置（CTS LOCATION）。

<a id="a65f270929aae6f65e659f1f6393d34fa"></a>

### `GECKO_FUN_UART_RTS`

```c
#define GECKO_FUN_UART_RTS 2U
```

UART 请求发送（RTS）。

<a id="a8edacb8e79f7d7a84736104949157870"></a>

### `GECKO_FUN_UART_RTS_LOC`

```c
#define GECKO_FUN_UART_RTS_LOC 6U
```

UART 请求发送位置（RTS LOCATION）。

<a id="a68699f16723f6a99594f068dd0c95b2a"></a>

### `GECKO_FUN_UART_RX`

```c
#define GECKO_FUN_UART_RX 1U
```

UART 接收（RX）。

<a id="ac7e6a762e1e7e63f9172d736354820b3"></a>

### `GECKO_FUN_UART_RX_LOC`

```c
#define GECKO_FUN_UART_RX_LOC 4U
```

UART 接收位置（RX LOCATION）。

<a id="a2b19bb5a846aab3b44a3628c586df77b"></a>

### `GECKO_FUN_UART_TX`

```c
#define GECKO_FUN_UART_TX 0U
```

UART 发送（TX）。

<a id="a59225761dc92d12b23be60f2616c0f9f"></a>

### `GECKO_FUN_UART_TX_LOC`

```c
#define GECKO_FUN_UART_TX_LOC 5U
```

UART 发送位置（TX LOCATION）。

<a id="a0c4e8fbbb218ce88bd4059bda8170e6d"></a>

### `GECKO_LOC`

```c
#define GECKO_LOC ( fun, loc )
```

展开值（Value）：

```c
(((GECKO_LOCATION(##loc##) & GECKO_LOC_MSK) << GECKO_LOC_POS) |                            \
 ((GECKO_FUN_##fun##_LOC & GECKO_FUN_MSK) << GECKO_FUN_POS))
```

构造 `GECKO_psels` 属性条目（Property Entry）的工具宏。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `fun` | 引脚功能配置（Pin Function Configuration），参见 `GECKO_FUNC_{name}` 宏。 |
| `loc` | 位置（Location）。 |

<a id="adef6df5f1daf2e87dbed89b433ef7d84"></a>

### `GECKO_LOC_MSK`

```c
#define GECKO_LOC_MSK 0xFFU
```

引脚字段（Pin Field）的掩码。

<a id="a12208aabccc02edd6c64a857f14455f7"></a>

### `GECKO_LOC_POS`

```c
#define GECKO_LOC_POS 0U
```

位置字段（Loc Field）的位置。

<a id="a462dc592c5260981e679be5d9e0de7df"></a>

### `GECKO_LOCATION`

```c
#define GECKO_LOCATION ( n)
```

展开值（Value）：

```c
(n)
```

<a id="afd3e7b18220ac0786d63d15766288ec1"></a>

### `GECKO_PIN`

```c
#define GECKO_PIN ( n)
```

展开值（Value）：

```c
(n)
```

<a id="a9e62aad832626ee3f12e55b8e0102b68"></a>

### `GECKO_PIN_MSK`

```c
#define GECKO_PIN_MSK 0xFFU
```

引脚字段（Pin Field）的掩码。

<a id="af4fc3615fcff891841b6226b363f9f4c"></a>

### `GECKO_PIN_POS`

```c
#define GECKO_PIN_POS 0U
```

引脚字段（Pin Field）的位位置。

<a id="af1017b3a2df0dfa3e7e034e2714dfbd4"></a>

### `GECKO_PORT_A`

```c
#define GECKO_PORT_A 0
```

<a id="a23ce2182c7b7296899dce3022b70fd1d"></a>

### `GECKO_PORT_B`

```c
#define GECKO_PORT_B 1
```

<a id="a9a8a5a42323fba6d1d7102bf5e84ac31"></a>

### `GECKO_PORT_C`

```c
#define GECKO_PORT_C 2
```

<a id="a740208b46b6a57eff76c08900ddcb09e"></a>

### `GECKO_PORT_D`

```c
#define GECKO_PORT_D 3
```

<a id="acd268feccf2103b9d10e98a3ee716696"></a>

### `GECKO_PORT_E`

```c
#define GECKO_PORT_E 4
```

<a id="a149072d68a31c47c7d75bce5b5dfa596"></a>

### `GECKO_PORT_F`

```c
#define GECKO_PORT_F 5
```

<a id="a931423cbccb8542cf8554779bcac16a1"></a>

### `GECKO_PORT_G`

```c
#define GECKO_PORT_G 6
```

<a id="af954756a1aa7f78e8e61a31f8226ae74"></a>

### `GECKO_PORT_H`

```c
#define GECKO_PORT_H 7
```

<a id="acb405086add8f2c8f215038b148c2c25"></a>

### `GECKO_PORT_I`

```c
#define GECKO_PORT_I 8
```

<a id="a066e26d3a586b420e4dcb0c1ff5c709d"></a>

### `GECKO_PORT_J`

```c
#define GECKO_PORT_J 9
```

<a id="ac90348555b1c71e25048e21751b9b181"></a>

### `GECKO_PORT_K`

```c
#define GECKO_PORT_K 10
```

<a id="a750badf0aada694862e9cc8135ef435c"></a>

### `GECKO_PORT_MSK`

```c
#define GECKO_PORT_MSK 0xFFU
```

端口字段（Port Field）的掩码。

<a id="aafabc892e5cc1298ff87a10afdd203ca"></a>

### `GECKO_PORT_POS`

```c
#define GECKO_PORT_POS 8U
```

端口字段（Port Field）的位置。

<a id="ac1af8b10c541907308332856fa9affe7"></a>

### `GECKO_PSEL`

```c
#define GECKO_PSEL ( fun, port, pin )
```

展开值（Value）：

```c
(((GECKO_PORT_##port & GECKO_PORT_MSK) << GECKO_PORT_POS) |                                \
 ((GECKO_PIN(##pin##) & GECKO_PIN_MSK) << GECKO_PIN_POS) |                                 \
 ((GECKO_FUN_##fun & GECKO_FUN_MSK) << GECKO_FUN_POS))
```

构造 GECKO `psels` 属性条目（Property Entry）的工具宏。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `fun` | 引脚功能配置（Pin Function Configuration），参见 `GECKO_FUNC_{name}` 宏。 |
| `port` | 端口（Port），为 `0` 或 `1`。 |
| `pin` | 引脚（Pin）：0～31。 |


## 16.3\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_supplement_reference/P076_gecko-pinctrl-s1.h_源码浏览.md)

<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="agecko-pinctrl-s1_8h_html_a12208aabccc02edd6c64a857f14455f7"></a>
<a id="agecko-pinctrl-s1_8h_html_a462dc592c5260981e679be5d9e0de7df"></a>
<a id="agecko-pinctrl-s1_8h_html_a87d929d0a1bc9808a854ce582a0c8251"></a>
<a id="agecko-pinctrl-s1_8h_html_adef6df5f1daf2e87dbed89b433ef7d84"></a>
<a id="agecko-pinctrl-s1_8h_html_af582c317ab79a3961ea00645514fc3f6"></a>
<a id="agecko-pinctrl-s1_8h_html_a750badf0aada694862e9cc8135ef435c"></a>
<a id="agecko-pinctrl-s1_8h_html_a9e62aad832626ee3f12e55b8e0102b68"></a>
<a id="agecko-pinctrl-s1_8h_html_aafabc892e5cc1298ff87a10afdd203ca"></a>
<a id="agecko-pinctrl-s1_8h_html_af4fc3615fcff891841b6226b363f9f4c"></a>
<a id="agecko-pinctrl-s1_8h_html_afd3e7b18220ac0786d63d15766288ec1"></a>

---

[上一章](P015_zephyr__debug__gcov.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P017_zephyr__net__gptp.h_文件参考.md)
