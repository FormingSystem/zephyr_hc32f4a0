---
id: learning.zephyr-docs.api-file-service-reference.page-9
title: zephyr__dt-bindings__gpio__ene-kb106x-gpio.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/ene-kb106x-gpio_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第9章\_zephyr\_\_dt-bindings\_\_gpio\_\_ene-kb106x-gpio.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/ene-kb106x-gpio_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

查看此文件的源码。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 9.1\_宏定义（Macros）

<a id="define-members-0"></a>

### GPIO 引脚电压标志（Voltage Flags）

电压标志（Voltage Flags）是 Zephyr 对 Linux GPIO 绑定所规定的标准 GPIO 标志的扩展，供 ENE KB106x 片上系统（SoCs）使用。

注意（Note）：位 15～8 保留给 SoC 专用标志（SoC-Specific Flags）。

<a id="r_a9f09adacf5a53ad88eb129aace5fc769"></a>

```c
#define ENE_GPIO_VOLTAGE_DEFAULT (0U << ENE_GPIO_VOLTAGE_POS)
```

相关声明：[ENE_GPIO_VOLTAGE_DEFAULT](#a9f09adacf5a53ad88eb129aace5fc769)。

将引脚设置为默认电压电平（Default Voltage Level）：3.3 V。

<a id="r_a514da2fb72995d3d891d52d802b0c33b"></a>

```c
#define ENE_GPIO_VOLTAGE_1P8 (1U << ENE_GPIO_VOLTAGE_POS)
```

相关声明：[ENE_GPIO_VOLTAGE_1P8](#a514da2fb72995d3d891d52d802b0c33b)。

将引脚电压电平（Pin Voltage Level）设置为 1.8 V。

<a id="r_a95fcfd50fc67206cea5d561124388e2d"></a>

```c
#define ENE_GPIO_DRIVING_DEFAULT (0U << ENE_GPIO_DRIVING_POS)
```

相关声明：[ENE_GPIO_DRIVING_DEFAULT](#a95fcfd50fc67206cea5d561124388e2d)。

将引脚设置为默认驱动电流（Default Driving Current）：4 mA。

<a id="r_a1f22235e59a9196da91ff2fa3be4c608"></a>

```c
#define ENE_GPIO_DRIVING_16MA (1U << ENE_GPIO_DRIVING_POS)
```

相关声明：[ENE_GPIO_DRIVING_16MA](#a1f22235e59a9196da91ff2fa3be4c608)。

将引脚驱动电流（Pin Driving Current）设置为 16 mA。

## 9.2\_详细说明（Detailed Documentation）

<a id="a1f22235e59a9196da91ff2fa3be4c608"></a>

### `ENE_GPIO_DRIVING_16MA`

```c
#define ENE_GPIO_DRIVING_16MA (1U << ENE_GPIO_DRIVING_POS)
```

将引脚驱动电流（Pin Driving Current）设置为 16 mA。

<a id="a95fcfd50fc67206cea5d561124388e2d"></a>

### `ENE_GPIO_DRIVING_DEFAULT`

```c
#define ENE_GPIO_DRIVING_DEFAULT (0U << ENE_GPIO_DRIVING_POS)
```

将引脚设置为默认驱动电流（Default Driving Current）：4 mA。

<a id="a514da2fb72995d3d891d52d802b0c33b"></a>

### `ENE_GPIO_VOLTAGE_1P8`

```c
#define ENE_GPIO_VOLTAGE_1P8 (1U << ENE_GPIO_VOLTAGE_POS)
```

将引脚电压电平（Pin Voltage Level）设置为 1.8 V。

<a id="a9f09adacf5a53ad88eb129aace5fc769"></a>

### `ENE_GPIO_VOLTAGE_DEFAULT`

```c
#define ENE_GPIO_VOLTAGE_DEFAULT (0U << ENE_GPIO_VOLTAGE_POS)
```

将引脚设置为默认电压电平（Default Voltage Level）：3.3 V。


## 9.3\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_reference/P227_ene-kb106x-gpio.h_源码浏览.md)

<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P008_zephyr__dt-bindings__mipi_dsi__mipi_dsi.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P010_zephyr__dt-bindings__gpio__ene-kb1200-gpio.h_文件参考.md)
