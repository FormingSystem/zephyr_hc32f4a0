---
id: learning.zephyr-docs.api-file-reference.page-364
title: zephyr__dt-bindings__pinctrl__rpi-pico-rp2040-pinctrl.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/rpi-pico-rp2040-pinctrl_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第364章\_zephyr\_\_dt-bindings\_\_pinctrl\_\_rpi-pico-rp2040-pinctrl.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/rpi-pico-rp2040-pinctrl_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include "rpi-pico-pinctrl-common.h"
```

查看此文件的源码。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 364.1\_宏定义（Macros）

<a id="r_ab8dc9ad840eb89cad37bb211e6c74b91"></a>

```c
#define RP2_PINCTRL_GPIO_FUNC_XIP 0
```

相关声明：[RP2_PINCTRL_GPIO_FUNC_XIP](#ab8dc9ad840eb89cad37bb211e6c74b91)。

<a id="r_ae8dbbdfe35ec98d85c37a26567f6c5a6"></a>

```c
#define RP2_PINCTRL_GPIO_FUNC_GPCK 8
```

相关声明：[RP2_PINCTRL_GPIO_FUNC_GPCK](#ae8dbbdfe35ec98d85c37a26567f6c5a6)。

<a id="r_aaebc20e84ac500bf54912993a85c59e0"></a>

```c
#define RP2_PINCTRL_GPIO_FUNC_USB 9
```

相关声明：[RP2_PINCTRL_GPIO_FUNC_USB](#aaebc20e84ac500bf54912993a85c59e0)。

<a id="r_ad63060076f6b9b29d5c8fcb3bbda2e3a"></a>

```c
#define RP2_PINCTRL_GPIO_FUNC_NULL 0xf
```

相关声明：[RP2_PINCTRL_GPIO_FUNC_NULL](#ad63060076f6b9b29d5c8fcb3bbda2e3a)。

<a id="r_a6ab3748b716a2c39ff7e0e78afec3bdf"></a>

```c
#define ADC_CH0_P26 RP2XXX_PINMUX(26, RP2_PINCTRL_GPIO_FUNC_NULL)
```

相关声明：[ADC_CH0_P26](#a6ab3748b716a2c39ff7e0e78afec3bdf)、[RP2XXX_PINMUX](P363_zephyr__dt-bindings__pinctrl__rpi-pico-pinctrl-common.h_文件参考.md#a5072c7fc08cc1f5eee10ad37b9b58461)、[RP2_PINCTRL_GPIO_FUNC_NULL](#ad63060076f6b9b29d5c8fcb3bbda2e3a)。

<a id="r_a237c44c257ad8b0c7d15bca6f83e2b75"></a>

```c
#define ADC_CH1_P27 RP2XXX_PINMUX(27, RP2_PINCTRL_GPIO_FUNC_NULL)
```

相关声明：[ADC_CH1_P27](#a237c44c257ad8b0c7d15bca6f83e2b75)、[RP2XXX_PINMUX](P363_zephyr__dt-bindings__pinctrl__rpi-pico-pinctrl-common.h_文件参考.md#a5072c7fc08cc1f5eee10ad37b9b58461)、[RP2_PINCTRL_GPIO_FUNC_NULL](#ad63060076f6b9b29d5c8fcb3bbda2e3a)。

<a id="r_a8bf50dbc36c4a534e26159c8a961a18c"></a>

```c
#define ADC_CH2_P28 RP2XXX_PINMUX(28, RP2_PINCTRL_GPIO_FUNC_NULL)
```

相关声明：[ADC_CH2_P28](#a8bf50dbc36c4a534e26159c8a961a18c)、[RP2XXX_PINMUX](P363_zephyr__dt-bindings__pinctrl__rpi-pico-pinctrl-common.h_文件参考.md#a5072c7fc08cc1f5eee10ad37b9b58461)、[RP2_PINCTRL_GPIO_FUNC_NULL](#ad63060076f6b9b29d5c8fcb3bbda2e3a)。

<a id="r_ad2ab3e2ede7b0c85b17387eddbbc97ed"></a>

```c
#define ADC_CH3_P29 RP2XXX_PINMUX(29, RP2_PINCTRL_GPIO_FUNC_NULL)
```

相关声明：[ADC_CH3_P29](#ad2ab3e2ede7b0c85b17387eddbbc97ed)、[RP2XXX_PINMUX](P363_zephyr__dt-bindings__pinctrl__rpi-pico-pinctrl-common.h_文件参考.md#a5072c7fc08cc1f5eee10ad37b9b58461)、[RP2_PINCTRL_GPIO_FUNC_NULL](#ad63060076f6b9b29d5c8fcb3bbda2e3a)。

## 364.2\_详细说明（Detailed Documentation）

<a id="a6ab3748b716a2c39ff7e0e78afec3bdf"></a>

### `ADC_CH0_P26`

```c
#define ADC_CH0_P26 RP2XXX_PINMUX(26, RP2_PINCTRL_GPIO_FUNC_NULL)
```

<a id="a237c44c257ad8b0c7d15bca6f83e2b75"></a>

### `ADC_CH1_P27`

```c
#define ADC_CH1_P27 RP2XXX_PINMUX(27, RP2_PINCTRL_GPIO_FUNC_NULL)
```

<a id="a8bf50dbc36c4a534e26159c8a961a18c"></a>

### `ADC_CH2_P28`

```c
#define ADC_CH2_P28 RP2XXX_PINMUX(28, RP2_PINCTRL_GPIO_FUNC_NULL)
```

<a id="ad2ab3e2ede7b0c85b17387eddbbc97ed"></a>

### `ADC_CH3_P29`

```c
#define ADC_CH3_P29 RP2XXX_PINMUX(29, RP2_PINCTRL_GPIO_FUNC_NULL)
```

<a id="ae8dbbdfe35ec98d85c37a26567f6c5a6"></a>

### `RP2_PINCTRL_GPIO_FUNC_GPCK`

```c
#define RP2_PINCTRL_GPIO_FUNC_GPCK 8
```

<a id="ad63060076f6b9b29d5c8fcb3bbda2e3a"></a>

### `RP2_PINCTRL_GPIO_FUNC_NULL`

```c
#define RP2_PINCTRL_GPIO_FUNC_NULL 0xf
```

<a id="aaebc20e84ac500bf54912993a85c59e0"></a>

### `RP2_PINCTRL_GPIO_FUNC_USB`

```c
#define RP2_PINCTRL_GPIO_FUNC_USB 9
```

<a id="ab8dc9ad840eb89cad37bb211e6c74b91"></a>

### `RP2_PINCTRL_GPIO_FUNC_XIP`

```c
#define RP2_PINCTRL_GPIO_FUNC_XIP 0
```


## 364.3\_原页交叉引用（Cross References）

- [rpi-pico-pinctrl-common.h](../api_source_configuration_reference/P097_rpi-pico-pinctrl-common.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P725_rpi-pico-rp2040-pinctrl.h_源码浏览.md)
- [RP2XXX_PINMUX](P363_zephyr__dt-bindings__pinctrl__rpi-pico-pinctrl-common.h_文件参考.md#a5072c7fc08cc1f5eee10ad37b9b58461)

<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P363_zephyr__dt-bindings__pinctrl__rpi-pico-pinctrl-common.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P365_zephyr__dt-bindings__pinctrl__rpi-pico-rp2350-pinctrl-common.h_文件参考.md)
