---
id: learning.zephyr-docs.api-file-service-reference.page-19
title: zephyr__dt-bindings__gpio__ite-it8xxx2-gpio.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/ite-it8xxx2-gpio_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第19章\_zephyr\_\_dt-bindings\_\_gpio\_\_ite-it8xxx2-gpio.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/ite-it8xxx2-gpio_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

查看此文件的源码。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 19.1\_宏定义（Macros）

<a id="define-members-0"></a>

### GPIO 引脚电压标志（Voltage Flags）

电压标志（Voltage Flags）是 Zephyr 对 Linux GPIO 绑定所规定的标准 GPIO 标志的扩展，供 ITE IT8xxx2 片上系统（SoCs）使用。

<a id="r_ac65596dfb83850449186a54a915373d8"></a>

```c
#define IT8XXX2_GPIO_VOLTAGE_DEFAULT (0U << IT8XXX2_GPIO_VOLTAGE_POS)
```

相关声明：[IT8XXX2_GPIO_VOLTAGE_DEFAULT](#ac65596dfb83850449186a54a915373d8)。

将引脚设置为默认电压电平（Default Voltage Level）。

<a id="r_ae6592bbcc1426357a96d0308367d74a9"></a>

```c
#define IT8XXX2_GPIO_VOLTAGE_1P8 (1U << IT8XXX2_GPIO_VOLTAGE_POS)
```

相关声明：[IT8XXX2_GPIO_VOLTAGE_1P8](#ae6592bbcc1426357a96d0308367d74a9)。

将引脚电压电平（Pin Voltage Level）设置为 1.8 V。

<a id="r_a0961ededa9521d8987b57cd8b8401474"></a>

```c
#define IT8XXX2_GPIO_VOLTAGE_3P3 (2U << IT8XXX2_GPIO_VOLTAGE_POS)
```

相关声明：[IT8XXX2_GPIO_VOLTAGE_3P3](#a0961ededa9521d8987b57cd8b8401474)。

将引脚电压电平（Pin Voltage Level）设置为 3.3 V。

<a id="r_a058087db025d461980583d2ad38aa0c2"></a>

```c
#define IT8XXX2_GPIO_VOLTAGE_5P0 (3U << IT8XXX2_GPIO_VOLTAGE_POS)
```

相关声明：[IT8XXX2_GPIO_VOLTAGE_5P0](#a058087db025d461980583d2ad38aa0c2)。

将引脚电压电平（Pin Voltage Level）设置为 5.0 V。

## 19.2\_详细说明（Detailed Documentation）

<a id="ae6592bbcc1426357a96d0308367d74a9"></a>

### `IT8XXX2_GPIO_VOLTAGE_1P8`

```c
#define IT8XXX2_GPIO_VOLTAGE_1P8 (1U << IT8XXX2_GPIO_VOLTAGE_POS)
```

将引脚电压电平（Pin Voltage Level）设置为 1.8 V。

<a id="a0961ededa9521d8987b57cd8b8401474"></a>

### `IT8XXX2_GPIO_VOLTAGE_3P3`

```c
#define IT8XXX2_GPIO_VOLTAGE_3P3 (2U << IT8XXX2_GPIO_VOLTAGE_POS)
```

将引脚电压电平（Pin Voltage Level）设置为 3.3 V。

<a id="a058087db025d461980583d2ad38aa0c2"></a>

### `IT8XXX2_GPIO_VOLTAGE_5P0`

```c
#define IT8XXX2_GPIO_VOLTAGE_5P0 (3U << IT8XXX2_GPIO_VOLTAGE_POS)
```

将引脚电压电平（Pin Voltage Level）设置为 5.0 V。

<a id="ac65596dfb83850449186a54a915373d8"></a>

### `IT8XXX2_GPIO_VOLTAGE_DEFAULT`

```c
#define IT8XXX2_GPIO_VOLTAGE_DEFAULT (0U << IT8XXX2_GPIO_VOLTAGE_POS)
```

将引脚设置为默认电压电平（Default Voltage Level）。


## 19.3\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_reference/P423_ite-it8xxx2-gpio.h_源码浏览.md)

<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P018_zephyr__arch__common__instr_mem.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P020_zephyr__drivers__clock_control__mchp_sam_pmc.h_文件参考.md)
