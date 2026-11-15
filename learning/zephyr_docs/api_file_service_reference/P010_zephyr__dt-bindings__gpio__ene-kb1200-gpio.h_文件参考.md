---
id: learning.zephyr-docs.api-file-service-reference.page-10
title: zephyr__dt-bindings__gpio__ene-kb1200-gpio.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/ene-kb1200-gpio_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第10章\_zephyr\_\_dt-bindings\_\_gpio\_\_ene-kb1200-gpio.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/ene-kb1200-gpio_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

查看此文件的源码。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 10.1\_宏定义（Macros）

<a id="define-members-0"></a>

### GPIO 引脚电压标志（Voltage Flags）

电压和驱动标志（Voltage and Driving Flags）是 Zephyr 对 Linux GPIO 绑定所规定的标准 GPIO 标志的扩展，供 ENE KB1200 片上系统（SoC）使用。

注意（Note）：位 15～8 保留给 SoC 专用标志（SoC-Specific Flags）。

<a id="r_ac4d6a2febad81ac12ea70df48b66daa8"></a>

```c
#define KB1200_GPIO_VOLTAGE_DEFAULT (0U << KB1200_GPIO_VOLTAGE_POS)
```

相关声明：[KB1200_GPIO_VOLTAGE_DEFAULT](#ac4d6a2febad81ac12ea70df48b66daa8)。

将引脚设置为默认电压电平（Default Voltage Level）：3.3 V。

<a id="r_a97289e46577a8e5a206d91824750c9fc"></a>

```c
#define KB1200_GPIO_VOLTAGE_1P8 (1U << KB1200_GPIO_VOLTAGE_POS)
```

相关声明：[KB1200_GPIO_VOLTAGE_1P8](#a97289e46577a8e5a206d91824750c9fc)。

将引脚电压电平（Pin Voltage Level）设置为 1.8 V。

<a id="r_a19eaa0c7a6564e0de3505846ae536f7d"></a>

```c
#define KB1200_GPIO_DRIVING_DEFAULT (0U << KB1200_GPIO_DRIVING_POS)
```

相关声明：[KB1200_GPIO_DRIVING_DEFAULT](#a19eaa0c7a6564e0de3505846ae536f7d)。

将引脚设置为默认驱动电流（Default Driving Current）：4 mA。

<a id="r_a55a268c4cc8feed539006571dc7efce3"></a>

```c
#define KB1200_GPIO_DRIVING_16MA (1U << KB1200_GPIO_DRIVING_POS)
```

相关声明：[KB1200_GPIO_DRIVING_16MA](#a55a268c4cc8feed539006571dc7efce3)。

将引脚驱动电流（Pin Driving Current）设置为 16 mA。

## 10.2\_详细说明（Detailed Documentation）

<a id="a55a268c4cc8feed539006571dc7efce3"></a>

### `KB1200_GPIO_DRIVING_16MA`

```c
#define KB1200_GPIO_DRIVING_16MA (1U << KB1200_GPIO_DRIVING_POS)
```

将引脚驱动电流（Pin Driving Current）设置为 16 mA。

<a id="a19eaa0c7a6564e0de3505846ae536f7d"></a>

### `KB1200_GPIO_DRIVING_DEFAULT`

```c
#define KB1200_GPIO_DRIVING_DEFAULT (0U << KB1200_GPIO_DRIVING_POS)
```

将引脚设置为默认驱动电流（Default Driving Current）：4 mA。

<a id="a97289e46577a8e5a206d91824750c9fc"></a>

### `KB1200_GPIO_VOLTAGE_1P8`

```c
#define KB1200_GPIO_VOLTAGE_1P8 (1U << KB1200_GPIO_VOLTAGE_POS)
```

将引脚电压电平（Pin Voltage Level）设置为 1.8 V。

<a id="ac4d6a2febad81ac12ea70df48b66daa8"></a>

### `KB1200_GPIO_VOLTAGE_DEFAULT`

```c
#define KB1200_GPIO_VOLTAGE_DEFAULT (0U << KB1200_GPIO_VOLTAGE_POS)
```

将引脚设置为默认电压电平（Default Voltage Level）：3.3 V。


## 10.3\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_reference/P228_ene-kb1200-gpio.h_源码浏览.md)

<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P009_zephyr__dt-bindings__gpio__ene-kb106x-gpio.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P011_zephyr__net__ethernet_mgmt.h_文件参考.md)
