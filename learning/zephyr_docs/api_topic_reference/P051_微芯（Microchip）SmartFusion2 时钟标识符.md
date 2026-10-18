---
id: learning.zephyr-docs.api-topic-reference.page-51
title: 微芯（Microchip）SmartFusion2 时钟标识符
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__microchip__smartfusion2__clocks.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第51章\_微芯（Microchip）SmartFusion2 时钟标识符

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__microchip__smartfusion2__clocks.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Microchip SmartFusion2 片上系统（SoC）的时钟标识符。

<a id="details"></a>

Microchip SmartFusion2 片上系统（SoC）的时钟标识符。

<a id="header-files"></a>
<a id="files"></a>

## 51.1\_文件（Files）

<a id="r_microchip-smartfusion2-clock_2Eh"></a>

```c
file microchip-smartfusion2-clock.h
```

相关声明：[microchip-smartfusion2-clock.h](../api_file_configuration_reference/P053_zephyr__dt-bindings__clock__microchip-smartfusion2-clock.h_文件参考.md)。

Microchip SmartFusion2的时钟标识符（Clock Identifiers）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 51.2\_宏定义（Macros）

<a id="r_gadf5258eba6c345e29427a4a25af1b38c"></a>

```c
#define SMARTFUSION2_CLOCK_CPU 0
```

相关声明：[SMARTFUSION2_CLOCK_CPU](#gadf5258eba6c345e29427a4a25af1b38c)。

主 CPU 时钟（Main CPU Clock）。

<a id="r_gafb057a42ac4f1dbd08663400413fabec"></a>

```c
#define SMARTFUSION2_CLOCK_MSS_PERIPHERAL 1
```

相关声明：[SMARTFUSION2_CLOCK_MSS_PERIPHERAL](#gafb057a42ac4f1dbd08663400413fabec)。

微处理器子系统外设时钟（MSS Peripheral Clock）。

## 51.3\_详细说明（Detailed Documentation）

<a id="gadf5258eba6c345e29427a4a25af1b38c"></a>

### `SMARTFUSION2_CLOCK_CPU`

```c
#define SMARTFUSION2_CLOCK_CPU 0
```

```c
#include <zephyr/dt-bindings/clock/microchip-smartfusion2-clock.h>
```

主 CPU 时钟（Main CPU Clock）。

<a id="gafb057a42ac4f1dbd08663400413fabec"></a>

### `SMARTFUSION2_CLOCK_MSS_PERIPHERAL`

```c
#define SMARTFUSION2_CLOCK_MSS_PERIPHERAL 1
```

```c
#include <zephyr/dt-bindings/clock/microchip-smartfusion2-clock.h>
```

微处理器子系统外设时钟（MSS Peripheral Clock）。


## 51.4\_原页交叉引用（Cross References）

- [microchip-smartfusion2-clock.h](../api_file_configuration_reference/P053_zephyr__dt-bindings__clock__microchip-smartfusion2-clock.h_文件参考.md)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P050_多功能设备（Multi-function Devices）.md) · [返回大纲](大纲.md) · [下一章](P052_其他设备（Miscellaneous Devices）.md)
