---
id: learning.zephyr-docs.api-file-runtime-reference.page-54
title: zephyr__dt-bindings__gpio__renesas-rzt2m-gpio.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/renesas-rzt2m-gpio_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第54章\_zephyr\_\_dt-bindings\_\_gpio\_\_renesas-rzt2m-gpio.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/renesas-rzt2m-gpio_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/sys/util.h>
```

查看此文件的源码。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 54.1\_宏定义（Macros）

<a id="r_a8fdc883e48d39eb950e47c8a7433630f"></a>

```c
#define RZT2M_GPIO_DRIVE_OFFSET 8
```

相关声明：[RZT2M_GPIO_DRIVE_OFFSET](#a8fdc883e48d39eb950e47c8a7433630f)。

<a id="r_a16ed0517a7b43d606ea0849ebb2d96a7"></a>

```c
#define RZT2M_GPIO_DRIVE_MASK GENMASK(RZT2M_GPIO_DRIVE_OFFSET + 2, RZT2M_GPIO_DRIVE_OFFSET)
```

相关声明：[RZT2M_GPIO_DRIVE_MASK](#a16ed0517a7b43d606ea0849ebb2d96a7)、[GENMASK](../util_reference/P001_通用工具公共接口.md#ga58530d20924859d16358c7400c37738d)、[RZT2M_GPIO_DRIVE_OFFSET](#a8fdc883e48d39eb950e47c8a7433630f)、[RZT2M_GPIO_DRIVE_OFFSET](#a8fdc883e48d39eb950e47c8a7433630f)。

<a id="r_a0e2542438d2c829d6509399314a01682"></a>

```c
#define RZT2M_GPIO_DRIVE_LOW (0U << RZT2M_GPIO_DRIVE_OFFSET)
```

相关声明：[RZT2M_GPIO_DRIVE_LOW](#a0e2542438d2c829d6509399314a01682)、[RZT2M_GPIO_DRIVE_OFFSET](#a8fdc883e48d39eb950e47c8a7433630f)。

选择 GPIO 引脚驱动强度（Drive Strength）。

<a id="r_a683f1d1fc91e508793141734caaef335"></a>

```c
#define RZT2M_GPIO_DRIVE_MIDDLE (1U << RZT2M_GPIO_DRIVE_OFFSET)
```

相关声明：[RZT2M_GPIO_DRIVE_MIDDLE](#a683f1d1fc91e508793141734caaef335)、[RZT2M_GPIO_DRIVE_OFFSET](#a8fdc883e48d39eb950e47c8a7433630f)。

<a id="r_a814748063a20fe7d971e19d6e296eb59"></a>

```c
#define RZT2M_GPIO_DRIVE_HIGH (2U << RZT2M_GPIO_DRIVE_OFFSET)
```

相关声明：[RZT2M_GPIO_DRIVE_HIGH](#a814748063a20fe7d971e19d6e296eb59)、[RZT2M_GPIO_DRIVE_OFFSET](#a8fdc883e48d39eb950e47c8a7433630f)。

<a id="r_a2b60d89adec85b941aa8d7963233aafb"></a>

```c
#define RZT2M_GPIO_DRIVE_ULTRA_HIGH (3U << RZT2M_GPIO_DRIVE_OFFSET)
```

相关声明：[RZT2M_GPIO_DRIVE_ULTRA_HIGH](#a2b60d89adec85b941aa8d7963233aafb)、[RZT2M_GPIO_DRIVE_OFFSET](#a8fdc883e48d39eb950e47c8a7433630f)。

<a id="r_a0536626285ce7ba19c1a8baf57365902"></a>

```c
#define RZT2M_GPIO_SCHMITT_TRIGGER_OFFSET 10
```

相关声明：[RZT2M_GPIO_SCHMITT_TRIGGER_OFFSET](#a0536626285ce7ba19c1a8baf57365902)。

<a id="r_a5650f1078ef92c15174bf2ce8c7e6f08"></a>

```c
#define RZT2M_GPIO_SCHMITT_TRIGGER_MASK BIT(RZT2M_GPIO_SCHMITT_TRIGGER_OFFSET)
```

相关声明：[RZT2M_GPIO_SCHMITT_TRIGGER_MASK](#a5650f1078ef92c15174bf2ce8c7e6f08)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)、[RZT2M_GPIO_SCHMITT_TRIGGER_OFFSET](#a0536626285ce7ba19c1a8baf57365902)。

<a id="r_ac2d2e1cef0fa53eb0ce6f7dcb32cb4ef"></a>

```c
#define RZT2M_GPIO_SCHMITT_TRIGGER BIT(RZT2M_GPIO_SCHMITT_TRIGGER_OFFSET)
```

相关声明：[RZT2M_GPIO_SCHMITT_TRIGGER](#ac2d2e1cef0fa53eb0ce6f7dcb32cb4ef)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)、[RZT2M_GPIO_SCHMITT_TRIGGER_OFFSET](#a0536626285ce7ba19c1a8baf57365902)。

启用 GPIO 引脚施密特触发器（Schmitt Trigger）。

<a id="r_a4f3e3fb225e921d3405c189b87980a16"></a>

```c
#define RZT2M_GPIO_SLEW_RATE_OFFSET 11
```

相关声明：[RZT2M_GPIO_SLEW_RATE_OFFSET](#a4f3e3fb225e921d3405c189b87980a16)。

<a id="r_a595d6e02f3fd2168deb2fe06f6d00f7d"></a>

```c
#define RZT2M_GPIO_SLEW_RATE_MASK BIT(RZT2M_GPIO_SLEW_RATE_OFFSET)
```

相关声明：[RZT2M_GPIO_SLEW_RATE_MASK](#a595d6e02f3fd2168deb2fe06f6d00f7d)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)、[RZT2M_GPIO_SLEW_RATE_OFFSET](#a4f3e3fb225e921d3405c189b87980a16)。

<a id="r_a2f754f8752b7c42ee89286725b2be4bb"></a>

```c
#define RZT2M_GPIO_SLEW_RATE_SLOW 0U
```

相关声明：[RZT2M_GPIO_SLEW_RATE_SLOW](#a2f754f8752b7c42ee89286725b2be4bb)。

选择 GPIO 引脚转换速率（Slew Rate）。

<a id="r_a752db650514faa34a43bf14a70746dac"></a>

```c
#define RZT2M_GPIO_SLEW_RATE_FAST BIT(RZT2M_GPIO_SLEW_RATE_OFFSET)
```

相关声明：[RZT2M_GPIO_SLEW_RATE_FAST](#a752db650514faa34a43bf14a70746dac)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)、[RZT2M_GPIO_SLEW_RATE_OFFSET](#a4f3e3fb225e921d3405c189b87980a16)。

## 54.2\_详细说明（Detailed Documentation）

<a id="a814748063a20fe7d971e19d6e296eb59"></a>

### `RZT2M_GPIO_DRIVE_HIGH`

```c
#define RZT2M_GPIO_DRIVE_HIGH (2U << RZT2M_GPIO_DRIVE_OFFSET)
```

<a id="a0e2542438d2c829d6509399314a01682"></a>

### `RZT2M_GPIO_DRIVE_LOW`

```c
#define RZT2M_GPIO_DRIVE_LOW (0U << RZT2M_GPIO_DRIVE_OFFSET)
```

选择 GPIO 引脚驱动强度（Drive Strength）。

<a id="a16ed0517a7b43d606ea0849ebb2d96a7"></a>

### `RZT2M_GPIO_DRIVE_MASK`

```c
#define RZT2M_GPIO_DRIVE_MASK GENMASK(RZT2M_GPIO_DRIVE_OFFSET + 2, RZT2M_GPIO_DRIVE_OFFSET)
```

<a id="a683f1d1fc91e508793141734caaef335"></a>

### `RZT2M_GPIO_DRIVE_MIDDLE`

```c
#define RZT2M_GPIO_DRIVE_MIDDLE (1U << RZT2M_GPIO_DRIVE_OFFSET)
```

<a id="a8fdc883e48d39eb950e47c8a7433630f"></a>

### `RZT2M_GPIO_DRIVE_OFFSET`

```c
#define RZT2M_GPIO_DRIVE_OFFSET 8
```

<a id="a2b60d89adec85b941aa8d7963233aafb"></a>

### `RZT2M_GPIO_DRIVE_ULTRA_HIGH`

```c
#define RZT2M_GPIO_DRIVE_ULTRA_HIGH (3U << RZT2M_GPIO_DRIVE_OFFSET)
```

<a id="ac2d2e1cef0fa53eb0ce6f7dcb32cb4ef"></a>

### `RZT2M_GPIO_SCHMITT_TRIGGER`

```c
#define RZT2M_GPIO_SCHMITT_TRIGGER BIT(RZT2M_GPIO_SCHMITT_TRIGGER_OFFSET)
```

启用 GPIO 引脚施密特触发器（Schmitt Trigger）。

<a id="a5650f1078ef92c15174bf2ce8c7e6f08"></a>

### `RZT2M_GPIO_SCHMITT_TRIGGER_MASK`

```c
#define RZT2M_GPIO_SCHMITT_TRIGGER_MASK BIT(RZT2M_GPIO_SCHMITT_TRIGGER_OFFSET)
```

<a id="a0536626285ce7ba19c1a8baf57365902"></a>

### `RZT2M_GPIO_SCHMITT_TRIGGER_OFFSET`

```c
#define RZT2M_GPIO_SCHMITT_TRIGGER_OFFSET 10
```

<a id="a752db650514faa34a43bf14a70746dac"></a>

### `RZT2M_GPIO_SLEW_RATE_FAST`

```c
#define RZT2M_GPIO_SLEW_RATE_FAST BIT(RZT2M_GPIO_SLEW_RATE_OFFSET)
```

<a id="a595d6e02f3fd2168deb2fe06f6d00f7d"></a>

### `RZT2M_GPIO_SLEW_RATE_MASK`

```c
#define RZT2M_GPIO_SLEW_RATE_MASK BIT(RZT2M_GPIO_SLEW_RATE_OFFSET)
```

<a id="a4f3e3fb225e921d3405c189b87980a16"></a>

### `RZT2M_GPIO_SLEW_RATE_OFFSET`

```c
#define RZT2M_GPIO_SLEW_RATE_OFFSET 11
```

<a id="a2f754f8752b7c42ee89286725b2be4bb"></a>

### `RZT2M_GPIO_SLEW_RATE_SLOW`

```c
#define RZT2M_GPIO_SLEW_RATE_SLOW 0U
```

选择 GPIO 引脚转换速率（Slew Rate）。


## 54.3\_原页交叉引用（Cross References）

- [zephyr/sys/util.h](../util_reference/P003_通用工具头文件源码.md)
- [查看此文件的源码。](../api_source_reference/P705_renesas-rzt2m-gpio.h_源码浏览.md)
- [GENMASK](../util_reference/P001_通用工具公共接口.md#ga58530d20924859d16358c7400c37738d)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)

<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P053_zephyr__dt-bindings__pwm__pwm_ifx_tcpwm.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P055_zephyr__drivers__clock_control__renesas_rcar_generic.h_文件参考.md)
