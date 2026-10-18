---
id: learning.zephyr-docs.api-file-flash-test-reference.page-15
title: zephyr__dt-bindings__pinctrl__tiva-c-pinctrl.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/tiva-c-pinctrl_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第15章\_zephyr\_\_dt-bindings\_\_pinctrl\_\_tiva-c-pinctrl.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/tiva-c-pinctrl_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Tiva C引脚控制编码（Pinctrl Encoding）的定义。

查看此文件的源码。

<a id="details"></a>

Tiva C 引脚控制编码定义（Pinctrl Encoding Definitions）。SPDX-License-Identifier: Apache-2.0 Copyright (c) 2026 Linumiz

<a id="header-define-members"></a>
<a id="define-members"></a>

## 15.1\_宏定义（Macros）

<a id="r_a707b524bdecf74b88c0a684fc2f16d44"></a>

```c
#define TIVA_C_PORT_SHIFT 0
```

相关声明：[TIVA_C_PORT_SHIFT](#a707b524bdecf74b88c0a684fc2f16d44)。

GPIO 端口（GPIO Port）字段的位移量（Bit Shift）。

<a id="r_a1db071f8525d56a67047b204514580f0"></a>

```c
#define TIVA_C_PORT_MASK 0x7
```

相关声明：[TIVA_C_PORT_MASK](#a1db071f8525d56a67047b204514580f0)。

GPIO 端口（GPIO Port）字段的位掩码（Bit Mask）。

<a id="r_aea57ed4179f4bf7fb2aba8bc2d54149c"></a>

```c
#define TIVA_C_PIN_SHIFT 16
```

相关声明：[TIVA_C_PIN_SHIFT](#aea57ed4179f4bf7fb2aba8bc2d54149c)。

GPIO 引脚（GPIO Pin）字段的位移量（Bit Shift）。

<a id="r_a49409391b6198227758fb059bd27e990"></a>

```c
#define TIVA_C_PIN_MASK 0x7
```

相关声明：[TIVA_C_PIN_MASK](#a49409391b6198227758fb059bd27e990)。

GPIO 引脚（GPIO Pin）字段的位掩码（Bit Mask）。

<a id="r_a5c92c30136b3ac463e671c47c1fd06e6"></a>

```c
#define TIVA_C_MUX_SHIFT 19
```

相关声明：[TIVA_C_MUX_SHIFT](#a5c92c30136b3ac463e671c47c1fd06e6)。

复用功能（Mux Function）字段的位移量（Bit Shift）。

<a id="r_abb71d695e3ef0886f98581b4caded275"></a>

```c
#define TIVA_C_MUX_MASK 0xF
```

相关声明：[TIVA_C_MUX_MASK](#abb71d695e3ef0886f98581b4caded275)。

复用功能（Mux Function）字段的位掩码（Bit Mask）。

<a id="r_a1e66f0ac913068f23ae59cf8cfa3cacb"></a>

```c
#define TIVA_C_TYPE_SHIFT 23
```

相关声明：[TIVA_C_TYPE_SHIFT](#a1e66f0ac913068f23ae59cf8cfa3cacb)。

引脚类型（Pin Type）字段的位移量（Bit Shift）。

<a id="r_a2cbfe76fc260b2c914b4e341b5d7d830"></a>

```c
#define TIVA_C_TYPE_MASK 0x7
```

相关声明：[TIVA_C_TYPE_MASK](#a2cbfe76fc260b2c914b4e341b5d7d830)。

引脚类型（Pin Type）字段的位掩码（Bit Mask）。

<a id="r_aaa1018ec8584ff5d2ed5dc0837d0870d"></a>

```c
#define TIVA_C_PORT_A 0
```

相关声明：[TIVA_C_PORT_A](#aaa1018ec8584ff5d2ed5dc0837d0870d)。

GPIO 端口（Port）A 标识符（Identifier）。

<a id="r_af06435e6abe238a630dbf51199250d12"></a>

```c
#define TIVA_C_PORT_B 1
```

相关声明：[TIVA_C_PORT_B](#af06435e6abe238a630dbf51199250d12)。

GPIO 端口（Port）B 标识符（Identifier）。

<a id="r_ae4800d816602660bd98d63bf1b63bb44"></a>

```c
#define TIVA_C_PORT_C 2
```

相关声明：[TIVA_C_PORT_C](#ae4800d816602660bd98d63bf1b63bb44)。

GPIO 端口（Port）C 标识符（Identifier）。

<a id="r_aac824256357b19c0e109f515ac31a7e2"></a>

```c
#define TIVA_C_PORT_D 3
```

相关声明：[TIVA_C_PORT_D](#aac824256357b19c0e109f515ac31a7e2)。

GPIO 端口（Port）D 标识符（Identifier）。

<a id="r_aa6b4c184a5afd34a5e5db2f242fd059f"></a>

```c
#define TIVA_C_PORT_E 4
```

相关声明：[TIVA_C_PORT_E](#aa6b4c184a5afd34a5e5db2f242fd059f)。

GPIO 端口（Port）E 标识符（Identifier）。

<a id="r_a4533efd24ef11225f40757544c71209d"></a>

```c
#define TIVA_C_PORT_F 5
```

相关声明：[TIVA_C_PORT_F](#a4533efd24ef11225f40757544c71209d)。

GPIO 端口（Port）F 标识符（Identifier）。

<a id="r_a2e6eada34128d3b8b141819dbae8875a"></a>

```c
#define TIVA_C_TYPE_GPIO 0
```

相关声明：[TIVA_C_TYPE_GPIO](#a2e6eada34128d3b8b141819dbae8875a)。

GPIO 引脚类型（Pin Type）。

<a id="r_a7b68ff0ddce89d090d94f3ae9960b317"></a>

```c
#define TIVA_C_TYPE_UART 1
```

相关声明：[TIVA_C_TYPE_UART](#a7b68ff0ddce89d090d94f3ae9960b317)。

UART 引脚类型（Pin Type）。

<a id="r_a16695183695a4097a881894915e62e0b"></a>

```c
#define TIVA_C_TYPE_I2C 2
```

相关声明：[TIVA_C_TYPE_I2C](#a16695183695a4097a881894915e62e0b)。

I2C SDA 引脚类型（Pin Type）。

<a id="r_a43e83f9e994c3bc8c7db5468ef5c0a5e"></a>

```c
#define TIVA_C_TYPE_I2C_SCL 3
```

相关声明：[TIVA_C_TYPE_I2C_SCL](#a43e83f9e994c3bc8c7db5468ef5c0a5e)。

I2C SCL 引脚类型（Pin Type）。

<a id="r_a0e443e5ac1113d670e348fa1c4a8f35a"></a>

```c
#define TIVA_C_TYPE_SSI 4
```

相关声明：[TIVA_C_TYPE_SSI](#a0e443e5ac1113d670e348fa1c4a8f35a)。

SSI 引脚类型（Pin Type）。

<a id="r_ae6e2db9596b540ada20fc7f3bb9882ae"></a>

```c
#define TIVA_C_TYPE_CAN 5
```

相关声明：[TIVA_C_TYPE_CAN](#ae6e2db9596b540ada20fc7f3bb9882ae)。

CAN 引脚类型（Pin Type）。

<a id="r_a0b340d757e9ec06d05065b442d525ef7"></a>

```c
#define TIVA_C_TYPE_PWM 6
```

相关声明：[TIVA_C_TYPE_PWM](#a0b340d757e9ec06d05065b442d525ef7)。

PWM 引脚类型（Pin Type）。

<a id="r_a44bf55882387e9430f6a6c1724b649c1"></a>

```c
#define TIVA_C_PINMUX(port, pin, mux, type)
```

相关声明：[TIVA_C_PINMUX](#a44bf55882387e9430f6a6c1724b649c1)。

编码一个 32 位 Tiva C 引脚复用值（Pinmux Value）。

<a id="r_a90192b340d41c96972a0b6a9b8e9ff73"></a>

```c
#define TIVA_C_PINMUX_PORT(pm)
```

相关声明：[TIVA_C_PINMUX_PORT](#a90192b340d41c96972a0b6a9b8e9ff73)。

从编码后的引脚复用值（Pinmux Value）中提取 GPIO 端口（Port）。

<a id="r_a7d0a78f89826daa715018bbfeb5a8918"></a>

```c
#define TIVA_C_PINMUX_PIN(pm)
```

相关声明：[TIVA_C_PINMUX_PIN](#a7d0a78f89826daa715018bbfeb5a8918)。

从编码后的引脚复用值（Pinmux Value）中提取 GPIO 引脚（Pin）。

<a id="r_aa0c5b3a9d19d90a2254c0d0da346438d"></a>

```c
#define TIVA_C_PINMUX_MUX(pm)
```

相关声明：[TIVA_C_PINMUX_MUX](#aa0c5b3a9d19d90a2254c0d0da346438d)。

从编码后的引脚复用值（Pinmux Value）中提取复用功能（Mux Function）。

<a id="r_ae3fd32b88ccfbe97784138136c83407f"></a>

```c
#define TIVA_C_PINMUX_TYPE(pm)
```

相关声明：[TIVA_C_PINMUX_TYPE](#ae3fd32b88ccfbe97784138136c83407f)。

从编码后的引脚复用值（Pinmux Value）中提取外设类型（Peripheral Type）。

<a id="r_a55db4701841798ee0809fff6f254b7eb"></a>

```c
#define TIVA_C_PULL_UP_SHIFT 26
```

相关声明：[TIVA_C_PULL_UP_SHIFT](#a55db4701841798ee0809fff6f254b7eb)。

上拉标志（Pull-up Flag）的位位置。

<a id="r_adbc6151a6939134406d73ec34f723f0d"></a>

```c
#define TIVA_C_PULL_DOWN_SHIFT 27
```

相关声明：[TIVA_C_PULL_DOWN_SHIFT](#adbc6151a6939134406d73ec34f723f0d)。

下拉标志（Pull-down Flag）的位位置。

<a id="r_aa598ba7152d0a88ec71da90f06e017ea"></a>

```c
#define TIVA_C_OPEN_DRAIN_SHIFT 28
```

相关声明：[TIVA_C_OPEN_DRAIN_SHIFT](#aa598ba7152d0a88ec71da90f06e017ea)。

开漏标志（Open-drain Flag）的位位置。

<a id="r_afd373731f58f2fad02b1e568f76aaa80"></a>

```c
#define TIVA_C_PINMUX_PULL_UP(pm)
```

相关声明：[TIVA_C_PINMUX_PULL_UP](#afd373731f58f2fad02b1e568f76aaa80)。

返回编码后的上拉标志（Pull-up Flag）。

<a id="r_a2f498f649ddd7962de535baca6eaad1a"></a>

```c
#define TIVA_C_PINMUX_PULL_DOWN(pm)
```

相关声明：[TIVA_C_PINMUX_PULL_DOWN](#a2f498f649ddd7962de535baca6eaad1a)。

返回编码后的下拉标志（Pull-down Flag）。

<a id="r_a0bd7bac14b2c42baff24db3f41241be6"></a>

```c
#define TIVA_C_PINMUX_OPEN_DRAIN(pm)
```

相关声明：[TIVA_C_PINMUX_OPEN_DRAIN](#a0bd7bac14b2c42baff24db3f41241be6)。

返回编码后的开漏标志（Open-drain Flag）。

<a id="r_a31a1e2e4712fbab4f6a83c411d7978dd"></a>

```c
#define TIVA_C_PINCFG_PORT_SHIFT 16
```

相关声明：[TIVA_C_PINCFG_PORT_SHIFT](#a31a1e2e4712fbab4f6a83c411d7978dd)。

引脚配置端口字段（Pin Configuration Port Field）的位移量。

<a id="r_a7013980c946c6824075b6a2eba7e0f87"></a>

```c
#define TIVA_C_PINCFG_PIN_SHIFT 10
```

相关声明：[TIVA_C_PINCFG_PIN_SHIFT](#a7013980c946c6824075b6a2eba7e0f87)。

引脚配置引脚字段（Pin Configuration Pin Field）的位移量。

## 15.2\_详细说明（Detailed Documentation）

<a id="abb71d695e3ef0886f98581b4caded275"></a>

### `TIVA_C_MUX_MASK`

```c
#define TIVA_C_MUX_MASK 0xF
```

复用功能（Mux Function）字段的位掩码（Bit Mask）。

<a id="a5c92c30136b3ac463e671c47c1fd06e6"></a>

### `TIVA_C_MUX_SHIFT`

```c
#define TIVA_C_MUX_SHIFT 19
```

复用功能（Mux Function）字段的位移量（Bit Shift）。

<a id="aa598ba7152d0a88ec71da90f06e017ea"></a>

### `TIVA_C_OPEN_DRAIN_SHIFT`

```c
#define TIVA_C_OPEN_DRAIN_SHIFT 28
```

开漏标志（Open-drain Flag）的位位置。

<a id="a49409391b6198227758fb059bd27e990"></a>

### `TIVA_C_PIN_MASK`

```c
#define TIVA_C_PIN_MASK 0x7
```

GPIO 引脚（GPIO Pin）字段的位掩码（Bit Mask）。

<a id="aea57ed4179f4bf7fb2aba8bc2d54149c"></a>

### `TIVA_C_PIN_SHIFT`

```c
#define TIVA_C_PIN_SHIFT 16
```

GPIO 引脚（GPIO Pin）字段的位移量（Bit Shift）。

<a id="a7013980c946c6824075b6a2eba7e0f87"></a>

### `TIVA_C_PINCFG_PIN_SHIFT`

```c
#define TIVA_C_PINCFG_PIN_SHIFT 10
```

引脚配置引脚字段（Pin Configuration Pin Field）的位移量。

<a id="a31a1e2e4712fbab4f6a83c411d7978dd"></a>

### `TIVA_C_PINCFG_PORT_SHIFT`

```c
#define TIVA_C_PINCFG_PORT_SHIFT 16
```

引脚配置端口字段（Pin Configuration Port Field）的位移量。

<a id="a44bf55882387e9430f6a6c1724b649c1"></a>

### `TIVA_C_PINMUX`

```c
#define TIVA_C_PINMUX ( port, pin, mux, type )
```

展开值（Value）：

```c
((((port) & TIVA_C_PORT_MASK) << TIVA_C_PORT_SHIFT) | \
 (((pin) & TIVA_C_PIN_MASK) << TIVA_C_PIN_SHIFT) | \
 (((mux) & TIVA_C_MUX_MASK) << TIVA_C_MUX_SHIFT) | \
 (((type) & TIVA_C_TYPE_MASK) << TIVA_C_TYPE_SHIFT))
```

编码一个 32 位 Tiva C 引脚复用值（Pinmux Value）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `port` | GPIO 端口标识符。 |
| `pin` | GPIO引脚编号。 |
| `mux` | 复用功能编号（Alternate Function Number）。 |
| `type` | 外设类型（Peripheral Type）。 |

**返回（Returns）**：返回值：编码后的引脚复用值（pinmux value）。

<a id="aa0c5b3a9d19d90a2254c0d0da346438d"></a>

### `TIVA_C_PINMUX_MUX`

```c
#define TIVA_C_PINMUX_MUX ( pm)
```

展开值（Value）：

```c
(((pm) >> TIVA_C_MUX_SHIFT) & TIVA_C_MUX_MASK)
```

从编码后的引脚复用值（Pinmux Value）中提取复用功能（Mux Function）。

<a id="a0bd7bac14b2c42baff24db3f41241be6"></a>

### `TIVA_C_PINMUX_OPEN_DRAIN`

```c
#define TIVA_C_PINMUX_OPEN_DRAIN ( pm)
```

展开值（Value）：

```c
(((pm) >> TIVA_C_OPEN_DRAIN_SHIFT) & 0x1U)
```

返回编码后的开漏标志（Open-drain Flag）。

<a id="a7d0a78f89826daa715018bbfeb5a8918"></a>

### `TIVA_C_PINMUX_PIN`

```c
#define TIVA_C_PINMUX_PIN ( pm)
```

展开值（Value）：

```c
(((pm) >> TIVA_C_PIN_SHIFT) & TIVA_C_PIN_MASK)
```

从编码后的引脚复用值（Pinmux Value）中提取 GPIO 引脚（Pin）。

<a id="a90192b340d41c96972a0b6a9b8e9ff73"></a>

### `TIVA_C_PINMUX_PORT`

```c
#define TIVA_C_PINMUX_PORT ( pm)
```

展开值（Value）：

```c
(((pm) >> TIVA_C_PORT_SHIFT) & TIVA_C_PORT_MASK)
```

从编码后的引脚复用值（Pinmux Value）中提取 GPIO 端口（Port）。

<a id="a2f498f649ddd7962de535baca6eaad1a"></a>

### `TIVA_C_PINMUX_PULL_DOWN`

```c
#define TIVA_C_PINMUX_PULL_DOWN ( pm)
```

展开值（Value）：

```c
(((pm) >> TIVA_C_PULL_DOWN_SHIFT) & 0x1U)
```

返回编码后的下拉标志（Pull-down Flag）。

<a id="afd373731f58f2fad02b1e568f76aaa80"></a>

### `TIVA_C_PINMUX_PULL_UP`

```c
#define TIVA_C_PINMUX_PULL_UP ( pm)
```

展开值（Value）：

```c
(((pm) >> TIVA_C_PULL_UP_SHIFT) & 0x1U)
```

返回编码后的上拉标志（Pull-up Flag）。

<a id="ae3fd32b88ccfbe97784138136c83407f"></a>

### `TIVA_C_PINMUX_TYPE`

```c
#define TIVA_C_PINMUX_TYPE ( pm)
```

展开值（Value）：

```c
(((pm) >> TIVA_C_TYPE_SHIFT) & TIVA_C_TYPE_MASK)
```

从编码后的引脚复用值（Pinmux Value）中提取外设类型（Peripheral Type）。

<a id="aaa1018ec8584ff5d2ed5dc0837d0870d"></a>

### `TIVA_C_PORT_A`

```c
#define TIVA_C_PORT_A 0
```

GPIO 端口（Port）A 标识符（Identifier）。

<a id="af06435e6abe238a630dbf51199250d12"></a>

### `TIVA_C_PORT_B`

```c
#define TIVA_C_PORT_B 1
```

GPIO 端口（Port）B 标识符（Identifier）。

<a id="ae4800d816602660bd98d63bf1b63bb44"></a>

### `TIVA_C_PORT_C`

```c
#define TIVA_C_PORT_C 2
```

GPIO 端口（Port）C 标识符（Identifier）。

<a id="aac824256357b19c0e109f515ac31a7e2"></a>

### `TIVA_C_PORT_D`

```c
#define TIVA_C_PORT_D 3
```

GPIO 端口（Port）D 标识符（Identifier）。

<a id="aa6b4c184a5afd34a5e5db2f242fd059f"></a>

### `TIVA_C_PORT_E`

```c
#define TIVA_C_PORT_E 4
```

GPIO 端口（Port）E 标识符（Identifier）。

<a id="a4533efd24ef11225f40757544c71209d"></a>

### `TIVA_C_PORT_F`

```c
#define TIVA_C_PORT_F 5
```

GPIO 端口（Port）F 标识符（Identifier）。

<a id="a1db071f8525d56a67047b204514580f0"></a>

### `TIVA_C_PORT_MASK`

```c
#define TIVA_C_PORT_MASK 0x7
```

GPIO 端口（GPIO Port）字段的位掩码（Bit Mask）。

<a id="a707b524bdecf74b88c0a684fc2f16d44"></a>

### `TIVA_C_PORT_SHIFT`

```c
#define TIVA_C_PORT_SHIFT 0
```

GPIO 端口（GPIO Port）字段的位移量（Bit Shift）。

<a id="adbc6151a6939134406d73ec34f723f0d"></a>

### `TIVA_C_PULL_DOWN_SHIFT`

```c
#define TIVA_C_PULL_DOWN_SHIFT 27
```

下拉标志（Pull-down Flag）的位位置。

<a id="a55db4701841798ee0809fff6f254b7eb"></a>

### `TIVA_C_PULL_UP_SHIFT`

```c
#define TIVA_C_PULL_UP_SHIFT 26
```

上拉标志（Pull-up Flag）的位位置。

<a id="ae6e2db9596b540ada20fc7f3bb9882ae"></a>

### `TIVA_C_TYPE_CAN`

```c
#define TIVA_C_TYPE_CAN 5
```

CAN 引脚类型（Pin Type）。

<a id="a2e6eada34128d3b8b141819dbae8875a"></a>

### `TIVA_C_TYPE_GPIO`

```c
#define TIVA_C_TYPE_GPIO 0
```

GPIO 引脚类型（Pin Type）。

<a id="a16695183695a4097a881894915e62e0b"></a>

### `TIVA_C_TYPE_I2C`

```c
#define TIVA_C_TYPE_I2C 2
```

I2C SDA 引脚类型（Pin Type）。

<a id="a43e83f9e994c3bc8c7db5468ef5c0a5e"></a>

### `TIVA_C_TYPE_I2C_SCL`

```c
#define TIVA_C_TYPE_I2C_SCL 3
```

I2C SCL 引脚类型（Pin Type）。

<a id="a2cbfe76fc260b2c914b4e341b5d7d830"></a>

### `TIVA_C_TYPE_MASK`

```c
#define TIVA_C_TYPE_MASK 0x7
```

引脚类型（Pin Type）字段的位掩码（Bit Mask）。

<a id="a0b340d757e9ec06d05065b442d525ef7"></a>

### `TIVA_C_TYPE_PWM`

```c
#define TIVA_C_TYPE_PWM 6
```

PWM 引脚类型（Pin Type）。

<a id="a1e66f0ac913068f23ae59cf8cfa3cacb"></a>

### `TIVA_C_TYPE_SHIFT`

```c
#define TIVA_C_TYPE_SHIFT 23
```

引脚类型（Pin Type）字段的位移量（Bit Shift）。

<a id="a0e443e5ac1113d670e348fa1c4a8f35a"></a>

### `TIVA_C_TYPE_SSI`

```c
#define TIVA_C_TYPE_SSI 4
```

SSI 引脚类型（Pin Type）。

<a id="a7b68ff0ddce89d090d94f3ae9960b317"></a>

### `TIVA_C_TYPE_UART`

```c
#define TIVA_C_TYPE_UART 1
```

UART 引脚类型（Pin Type）。


## 15.3\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_supplement_reference/P226_tiva-c-pinctrl.h_源码浏览.md)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="ativa-c-pinctrl_8h_html_a1db071f8525d56a67047b204514580f0"></a>
<a id="ativa-c-pinctrl_8h_html_a1e66f0ac913068f23ae59cf8cfa3cacb"></a>
<a id="ativa-c-pinctrl_8h_html_a2cbfe76fc260b2c914b4e341b5d7d830"></a>
<a id="ativa-c-pinctrl_8h_html_a49409391b6198227758fb059bd27e990"></a>
<a id="ativa-c-pinctrl_8h_html_a5c92c30136b3ac463e671c47c1fd06e6"></a>
<a id="ativa-c-pinctrl_8h_html_a707b524bdecf74b88c0a684fc2f16d44"></a>
<a id="ativa-c-pinctrl_8h_html_abb71d695e3ef0886f98581b4caded275"></a>
<a id="ativa-c-pinctrl_8h_html_aea57ed4179f4bf7fb2aba8bc2d54149c"></a>
<a id="ativa-c-pinctrl_8h_html_aa598ba7152d0a88ec71da90f06e017ea"></a>
<a id="ativa-c-pinctrl_8h_html_adbc6151a6939134406d73ec34f723f0d"></a>
<a id="ativa-c-pinctrl_8h_html_a55db4701841798ee0809fff6f254b7eb"></a>

---

[上一章](P014_zephyr__dt-bindings__pinctrl__syna-sr100-pinctrl.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P016_____w__zephyr__zephyr__subsys__testsuite__ztest__include__zephyr__ztest_assert.h_文件参考.md)
