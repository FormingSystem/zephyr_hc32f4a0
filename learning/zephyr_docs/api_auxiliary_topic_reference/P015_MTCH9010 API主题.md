---
id: learning.zephyr-docs.api-auxiliary-topic-reference.page-15
title: MTCH9010 API主题
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__mtch9010__interface.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第15章\_MTCH9010 API主题

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__mtch9010__interface.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Microchip MTCH9010 电容式/电导式液位传感器（Capacitive/conductive liquid-level sensor）。

<a id="details"></a>

Microchip MTCH9010 电容式/电导式液位传感器（Capacitive/conductive liquid-level sensor）。

<a id="header-files"></a>
<a id="files"></a>

## 15.1\_文件（Files）

<a id="r_mtch9010_2Eh"></a>

```c
file mtch9010.h
```

相关声明：[mtch9010.h](https://docs.zephyrproject.org/latest/doxygen/html/dt-bindings_2sensor_2mtch9010_8h.html)。

the Microchip MTCH9010 sensor的设备树绑定常量（Devicetree Binding Constants）。

<a id="header-member-group"></a>
<a id="member-group"></a>

## 15.2\_工作模式（Operating mode）

设备树 `operating-mode` 属性的取值。

<a id="r_gaef5c74953312c81aaf7c2957a23958c7"></a>

```c
#define MTCH9010_CAPACITIVE 0x0
```

相关声明：[MTCH9010_CAPACITIVE](#gaef5c74953312c81aaf7c2957a23958c7)。

电容感测（capacitive sensing）。

<a id="r_gab6575fc8f31fec440d4a4b1e3a7ecdf9"></a>

```c
#define MTCH9010_CONDUCTIVE 0x1
```

相关声明：[MTCH9010_CONDUCTIVE](#gab6575fc8f31fec440d4a4b1e3a7ecdf9)。

导电感测（conductive sensing）。

## 15.3\_UART 输出数据格式（output data format）

设备树 `extended-output-format` 属性的取值。

<a id="r_gaeeeb7d41b461bae584f72615bc0b95ff"></a>

```c
#define MTCH9010_OUTPUT_FORMAT_DELTA 0x0
```

相关声明：[MTCH9010_OUTPUT_FORMAT_DELTA](#gaeeeb7d41b461bae584f72615bc0b95ff)。

相对于参考值的差值（delta from reference）。

<a id="r_gaaa2201ad6438823188b8a23e859fcf09"></a>

```c
#define MTCH9010_OUTPUT_FORMAT_CURRENT 0x1
```

相关声明：[MTCH9010_OUTPUT_FORMAT_CURRENT](#gaaa2201ad6438823188b8a23e859fcf09)。

当前测量值（current measurement）。

<a id="r_ga181f25eef9166f7e618b20a47e0552c0"></a>

```c
#define MTCH9010_OUTPUT_FORMAT_BOTH 0x2
```

相关声明：[MTCH9010_OUTPUT_FORMAT_BOTH](#ga181f25eef9166f7e618b20a47e0552c0)。

差值和当前测量值（delta and current）。

<a id="r_ga0e85d6c483d0ebec61bc297dc0213bb2"></a>

```c
#define MTCH9010_OUTPUT_FORMAT_MPLAB_DATA_VISUALIZER 0x3
```

相关声明：[MTCH9010_OUTPUT_FORMAT_MPLAB_DATA_VISUALIZER](#ga0e85d6c483d0ebec61bc297dc0213bb2)。

MPLAB Data Visualizer 数据流。

## 15.4\_详细说明（Detailed Documentation）

<a id="gaef5c74953312c81aaf7c2957a23958c7"></a>

### `MTCH9010_CAPACITIVE`

```c
#define MTCH9010_CAPACITIVE 0x0
```

```c
#include <zephyr/dt-bindings/sensor/mtch9010.h>
```

电容感测（capacitive sensing）。

<a id="gab6575fc8f31fec440d4a4b1e3a7ecdf9"></a>

### `MTCH9010_CONDUCTIVE`

```c
#define MTCH9010_CONDUCTIVE 0x1
```

```c
#include <zephyr/dt-bindings/sensor/mtch9010.h>
```

导电感测（conductive sensing）。

<a id="ga181f25eef9166f7e618b20a47e0552c0"></a>

### `MTCH9010_OUTPUT_FORMAT_BOTH`

```c
#define MTCH9010_OUTPUT_FORMAT_BOTH 0x2
```

```c
#include <zephyr/dt-bindings/sensor/mtch9010.h>
```

差值和当前测量值（delta and current）。

<a id="gaaa2201ad6438823188b8a23e859fcf09"></a>

### `MTCH9010_OUTPUT_FORMAT_CURRENT`

```c
#define MTCH9010_OUTPUT_FORMAT_CURRENT 0x1
```

```c
#include <zephyr/dt-bindings/sensor/mtch9010.h>
```

当前测量值（current measurement）。

<a id="gaeeeb7d41b461bae584f72615bc0b95ff"></a>

### `MTCH9010_OUTPUT_FORMAT_DELTA`

```c
#define MTCH9010_OUTPUT_FORMAT_DELTA 0x0
```

```c
#include <zephyr/dt-bindings/sensor/mtch9010.h>
```

相对于参考值的差值（delta from reference）。

<a id="ga0e85d6c483d0ebec61bc297dc0213bb2"></a>

### `MTCH9010_OUTPUT_FORMAT_MPLAB_DATA_VISUALIZER`

```c
#define MTCH9010_OUTPUT_FORMAT_MPLAB_DATA_VISUALIZER 0x3
```

```c
#include <zephyr/dt-bindings/sensor/mtch9010.h>
```

MPLAB Data Visualizer 数据流。


## 15.5\_原页交叉引用（Cross References）

- [mtch9010.h](https://docs.zephyrproject.org/latest/doxygen/html/dt-bindings_2sensor_2mtch9010_8h.html)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P014_多位串行外设接口（MSPI）.md) · [返回大纲](大纲.md) · [下一章](P016_STTS22H API主题.md)
