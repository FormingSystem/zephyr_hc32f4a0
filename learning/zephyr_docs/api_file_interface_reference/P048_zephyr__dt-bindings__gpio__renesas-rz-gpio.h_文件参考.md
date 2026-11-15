---
id: learning.zephyr-docs.api-file-interface-reference.page-48
title: zephyr__dt-bindings__gpio__renesas-rz-gpio.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/renesas-rz-gpio_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第48章\_zephyr\_\_dt-bindings\_\_gpio\_\_renesas-rz-gpio.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/renesas-rz-gpio_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

查看此文件的源码。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 48.1\_宏定义（Macros）

<a id="r_afacb3123f587a2129cd1ed472ce2b3e5"></a>

```c
#define RZ_GPIO_IOLH_SHIFT 8U
```

相关声明：[RZ_GPIO_IOLH_SHIFT](#afacb3123f587a2129cd1ed472ce2b3e5)。

RZ/A、RZ/G、RZ/V 专用 GPIO 标志。引脚驱动能力标志（pin driving ability flags）编码在 `gpio_dt_flags_t` 的高 8 位中，具体如下：

<a id="r_a6916bb2358989ef5498e1c87209dd995"></a>

```c
#define RZ_GPIO_IOLH_SET(iolh_val)
```

相关声明：[RZ_GPIO_IOLH_SET](#a6916bb2358989ef5498e1c87209dd995)。

<a id="r_aa309713f69b69a9650496f6238380c6d"></a>

```c
#define RZ_GPIO_FILTER_SHIFT 10U
```

相关声明：[RZ_GPIO_FILTER_SHIFT](#aa309713f69b69a9650496f6238380c6d)。

<a id="r_a1f1f1a0433c86dc7f50b368bd258a107"></a>

```c
#define RZ_GPIO_FILNUM_SHIFT 1U
```

相关声明：[RZ_GPIO_FILNUM_SHIFT](#a1f1f1a0433c86dc7f50b368bd258a107)。

<a id="r_abcdbf6cf77765df961496a3698f9102d"></a>

```c
#define RZ_GPIO_FILCLKSEL_SHIFT 3U
```

相关声明：[RZ_GPIO_FILCLKSEL_SHIFT](#abcdbf6cf77765df961496a3698f9102d)。

<a id="r_aa905a388dc0ca8b9c532620be7029b8e"></a>

```c
#define RZ_GPIO_FILTER_SET(fillonoff, filnum, filclksel)
```

相关声明：[RZ_GPIO_FILTER_SET](#aa905a388dc0ca8b9c532620be7029b8e)。

## 48.2\_详细说明（Detailed Documentation）

<a id="abcdbf6cf77765df961496a3698f9102d"></a>

### `RZ_GPIO_FILCLKSEL_SHIFT`

```c
#define RZ_GPIO_FILCLKSEL_SHIFT 3U
```

<a id="a1f1f1a0433c86dc7f50b368bd258a107"></a>

### `RZ_GPIO_FILNUM_SHIFT`

```c
#define RZ_GPIO_FILNUM_SHIFT 1U
```

<a id="aa905a388dc0ca8b9c532620be7029b8e"></a>

### `RZ_GPIO_FILTER_SET`

```c
#define RZ_GPIO_FILTER_SET ( fillonoff, filnum, filclksel )
```

展开值（Value）：

```c
(((fillonoff) | ((filnum) << RZ_GPIO_FILNUM_SHIFT) |                                       \
  ((filclksel) << RZ_GPIO_FILCLKSEL_SHIFT))                                                \
 << RZ_GPIO_FILTER_SHIFT)
```

<a id="aa309713f69b69a9650496f6238380c6d"></a>

### `RZ_GPIO_FILTER_SHIFT`

```c
#define RZ_GPIO_FILTER_SHIFT 10U
```

<a id="a6916bb2358989ef5498e1c87209dd995"></a>

### `RZ_GPIO_IOLH_SET`

```c
#define RZ_GPIO_IOLH_SET ( iolh_val)
```

展开值（Value）：

```c
(iolh_val << RZ_GPIO_IOLH_SHIFT)
```

<a id="afacb3123f587a2129cd1ed472ce2b3e5"></a>

### `RZ_GPIO_IOLH_SHIFT`

```c
#define RZ_GPIO_IOLH_SHIFT 8U
```

RZ/A、RZ/G、RZ/V 专用 GPIO 标志。引脚驱动能力标志（pin driving ability flags）编码在 `gpio_dt_flags_t` 的高 8 位中，具体如下：

- 位 8–9：引脚驱动能力（pin driving ability）值。
- 位 10：数字噪声滤波器（Digital Noise Filter）开关。
- 位 11–12：数字噪声滤波器的计数值（Number value）。
- 位 13–14：数字噪声滤波器的时钟选择（Clock Selection）值。下方为原始配置示例。

`gpio-consumer { out-gpios = <&port8 2 (GPIO_PULL_UP | RZ_GPIO_FILTER_SET(1, 3, 3))>; }; gpio-consumer { out-gpios = <&port8 2 (GPIO_PULL_UP | RZ_GPIO_IOLH_SET(2))>; };`


## 48.3\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_device_reference/P032_renesas-rz-gpio.h_源码浏览.md)
- [gpio_dt_flags_t](../hardware/P266_GPIO公共接口.md#gad435719dccdc37c05852960a7218fbd2)

<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="arenesas-rz-gpio_8h_html_a1f1f1a0433c86dc7f50b368bd258a107"></a>
<a id="arenesas-rz-gpio_8h_html_aa309713f69b69a9650496f6238380c6d"></a>
<a id="arenesas-rz-gpio_8h_html_abcdbf6cf77765df961496a3698f9102d"></a>
<a id="arenesas-rz-gpio_8h_html_afacb3123f587a2129cd1ed472ce2b3e5"></a>

---

[上一章](P047_zephyr__xen__regions.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P049_zephyr__drivers__clock_control__renesas_rx_cgc.h_文件参考.md)
