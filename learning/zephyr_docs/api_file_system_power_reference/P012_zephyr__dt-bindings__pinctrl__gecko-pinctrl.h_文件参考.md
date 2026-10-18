---
id: learning.zephyr-docs.api-file-system-power-reference.page-12
title: zephyr__dt-bindings__pinctrl__gecko-pinctrl.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/gecko-pinctrl_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第12章\_zephyr\_\_dt-bindings\_\_pinctrl\_\_gecko-pinctrl.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/gecko-pinctrl_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

查看此文件的源码。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 12.1\_宏定义（Macros）

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

<a id="r_a3cf2407ef84050edc079bd0e372b514b"></a>

```c
#define GECKO_FUN_UART_LOC 4U
```

相关声明：[GECKO_FUN_UART_LOC](#a3cf2407ef84050edc079bd0e372b514b)。

UART 位置（LOCATION）。

<a id="r_a469abb3acc66dfe55f73918b8b2bf5ec"></a>

```c
#define GECKO_FUN_SPI_MISO 5U
```

相关声明：[GECKO_FUN_SPI_MISO](#a469abb3acc66dfe55f73918b8b2bf5ec)。

<a id="r_ac694f5ec91bde5c9e3de7af7fed94b6b"></a>

```c
#define GECKO_FUN_SPI_MOSI 6U
```

相关声明：[GECKO_FUN_SPI_MOSI](#ac694f5ec91bde5c9e3de7af7fed94b6b)。

<a id="r_a3a5f06615a2add43e56c58a8b497f14b"></a>

```c
#define GECKO_FUN_SPI_CSN 7U
```

相关声明：[GECKO_FUN_SPI_CSN](#a3a5f06615a2add43e56c58a8b497f14b)。

<a id="r_a71471924b76182052cbad22824d5992e"></a>

```c
#define GECKO_FUN_SPI_SCK 8U
```

相关声明：[GECKO_FUN_SPI_SCK](#a71471924b76182052cbad22824d5992e)。

<a id="r_a3c29c6046d30a743df9aaae55c2b0803"></a>

```c
#define GECKO_FUN_I2C_SDA 9U
```

相关声明：[GECKO_FUN_I2C_SDA](#a3c29c6046d30a743df9aaae55c2b0803)。

<a id="r_a455a393df63ad05434c993ff18b9d3b5"></a>

```c
#define GECKO_FUN_I2C_SCL 10U
```

相关声明：[GECKO_FUN_I2C_SCL](#a455a393df63ad05434c993ff18b9d3b5)。

<a id="r_a405973ead4fd3aa22f2d976257929185"></a>

```c
#define GECKO_FUN_I2C_SDA_LOC 11U
```

相关声明：[GECKO_FUN_I2C_SDA_LOC](#a405973ead4fd3aa22f2d976257929185)。

<a id="r_a3216f884cccdd06204765849deec56b0"></a>

```c
#define GECKO_FUN_I2C_SCL_LOC 12U
```

相关声明：[GECKO_FUN_I2C_SCL_LOC](#a3216f884cccdd06204765849deec56b0)。

## 12.2\_详细说明（Detailed Documentation）

<a id="a455a393df63ad05434c993ff18b9d3b5"></a>

### `GECKO_FUN_I2C_SCL`

```c
#define GECKO_FUN_I2C_SCL 10U
```

<a id="a3216f884cccdd06204765849deec56b0"></a>

### `GECKO_FUN_I2C_SCL_LOC`

```c
#define GECKO_FUN_I2C_SCL_LOC 12U
```

<a id="a3c29c6046d30a743df9aaae55c2b0803"></a>

### `GECKO_FUN_I2C_SDA`

```c
#define GECKO_FUN_I2C_SDA 9U
```

<a id="a405973ead4fd3aa22f2d976257929185"></a>

### `GECKO_FUN_I2C_SDA_LOC`

```c
#define GECKO_FUN_I2C_SDA_LOC 11U
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

<a id="a3a5f06615a2add43e56c58a8b497f14b"></a>

### `GECKO_FUN_SPI_CSN`

```c
#define GECKO_FUN_SPI_CSN 7U
```

<a id="a469abb3acc66dfe55f73918b8b2bf5ec"></a>

### `GECKO_FUN_SPI_MISO`

```c
#define GECKO_FUN_SPI_MISO 5U
```

<a id="ac694f5ec91bde5c9e3de7af7fed94b6b"></a>

### `GECKO_FUN_SPI_MOSI`

```c
#define GECKO_FUN_SPI_MOSI 6U
```

<a id="a71471924b76182052cbad22824d5992e"></a>

### `GECKO_FUN_SPI_SCK`

```c
#define GECKO_FUN_SPI_SCK 8U
```

<a id="ad4dc9908bb86aea93aaa896ea7755a29"></a>

### `GECKO_FUN_UART_CTS`

```c
#define GECKO_FUN_UART_CTS 3U
```

UART 清除发送（CTS）。

<a id="a3cf2407ef84050edc079bd0e372b514b"></a>

### `GECKO_FUN_UART_LOC`

```c
#define GECKO_FUN_UART_LOC 4U
```

UART 位置（LOCATION）。

<a id="a65f270929aae6f65e659f1f6393d34fa"></a>

### `GECKO_FUN_UART_RTS`

```c
#define GECKO_FUN_UART_RTS 2U
```

UART 请求发送（RTS）。

<a id="a68699f16723f6a99594f068dd0c95b2a"></a>

### `GECKO_FUN_UART_RX`

```c
#define GECKO_FUN_UART_RX 1U
```

UART 接收（RX）。

<a id="a2b19bb5a846aab3b44a3628c586df77b"></a>

### `GECKO_FUN_UART_TX`

```c
#define GECKO_FUN_UART_TX 0U
```

UART 发送（TX）。

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


## 12.3\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_supplement_reference/P077_gecko-pinctrl.h_源码浏览.md)
- [GECKO_LOCATION](https://docs.zephyrproject.org/latest/doxygen/html/gecko-pinctrl-s1_8h.html#a462dc592c5260981e679be5d9e0de7df)
- [GECKO_LOC_MSK](https://docs.zephyrproject.org/latest/doxygen/html/gecko-pinctrl-s1_8h.html#adef6df5f1daf2e87dbed89b433ef7d84)
- [GECKO_LOC_POS](https://docs.zephyrproject.org/latest/doxygen/html/gecko-pinctrl-s1_8h.html#a12208aabccc02edd6c64a857f14455f7)
- [GECKO_FUN_MSK](https://docs.zephyrproject.org/latest/doxygen/html/gecko-pinctrl-s1_8h.html#a87d929d0a1bc9808a854ce582a0c8251)
- [GECKO_FUN_POS](https://docs.zephyrproject.org/latest/doxygen/html/gecko-pinctrl-s1_8h.html#af582c317ab79a3961ea00645514fc3f6)
- [GECKO_PORT_MSK](https://docs.zephyrproject.org/latest/doxygen/html/gecko-pinctrl-s1_8h.html#a750badf0aada694862e9cc8135ef435c)
- [GECKO_PORT_POS](https://docs.zephyrproject.org/latest/doxygen/html/gecko-pinctrl-s1_8h.html#aafabc892e5cc1298ff87a10afdd203ca)
- [GECKO_PIN](https://docs.zephyrproject.org/latest/doxygen/html/gecko-pinctrl-s1_8h.html#afd3e7b18220ac0786d63d15766288ec1)
- [GECKO_PIN_MSK](https://docs.zephyrproject.org/latest/doxygen/html/gecko-pinctrl-s1_8h.html#a9e62aad832626ee3f12e55b8e0102b68)
- [GECKO_PIN_POS](https://docs.zephyrproject.org/latest/doxygen/html/gecko-pinctrl-s1_8h.html#af4fc3615fcff891841b6226b363f9f4c)

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

[上一章](P011_zephyr__dt-bindings__gpio__espressif-esp32-gpio.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P013_zephyr__drivers__gnss__gnss_emul.h_文件参考.md)
