---
id: learning.zephyr-docs.api-protocol-topic-reference.page-2
title: ADXL362 API主题
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__adxl362__interface.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第2章\_ADXL362 API主题

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__adxl362__interface.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Analog Devices ADXL362 三轴加速度计（3-axis accelerometer）。

<a id="details"></a>

Analog Devices ADXL362 三轴加速度计（3-axis accelerometer）。

<a id="header-files"></a>
<a id="files"></a>

## 2.1\_文件（Files）

<a id="r_adxl362_2Eh"></a>

```c
file adxl362.h
```

相关声明：[adxl362.h](../api_file_interface_reference/P002_zephyr__dt-bindings__sensor__adxl362.h_文件参考.md)。

the Analog Devices ADXL362 accelerometer的设备树绑定常量（Devicetree Binding Constants）。

<a id="header-member-group"></a>
<a id="member-group"></a>

## 2.2\_FIFO 模式选项（FIFO mode options）

设备树 `fifo-mode` 属性的取值。

<a id="r_ga6c8ae8a7e2f330e6f08e4d607bd9a5ca"></a>

```c
#define ADXL362_FIFO_MODE_DISABLED 0x0
```

相关声明：[ADXL362_FIFO_MODE_DISABLED](#ga6c8ae8a7e2f330e6f08e4d607bd9a5ca)。

禁用先进先出缓冲区（FIFO）。

<a id="r_ga9587df579db31964427b563df59451e3"></a>

```c
#define ADXL362_FIFO_MODE_OLDEST_SAVED 0x1
```

相关声明：[ADXL362_FIFO_MODE_OLDEST_SAVED](#ga9587df579db31964427b563df59451e3)。

缓冲区满时停止，保留最早的样本（samples）。

<a id="r_gaa4e66bfd6d847c8c610b12cd77f16b68"></a>

```c
#define ADXL362_FIFO_MODE_STREAM 0x2
```

相关声明：[ADXL362_FIFO_MODE_STREAM](#gaa4e66bfd6d847c8c610b12cd77f16b68)。

连续流（continuous stream）模式，覆盖最早的样本。

<a id="r_ga8ea6f788f0236a3dec48c47bb2997d28"></a>

```c
#define ADXL362_FIFO_MODE_TRIGGERED 0x3
```

相关声明：[ADXL362_FIFO_MODE_TRIGGERED](#ga8ea6f788f0236a3dec48c47bb2997d28)。

采集触发事件（trigger event）前后的样本。

## 2.3\_详细说明（Detailed Documentation）

<a id="ga6c8ae8a7e2f330e6f08e4d607bd9a5ca"></a>

### `ADXL362_FIFO_MODE_DISABLED`

```c
#define ADXL362_FIFO_MODE_DISABLED 0x0
```

```c
#include <zephyr/dt-bindings/sensor/adxl362.h>
```

禁用先进先出缓冲区（FIFO）。

<a id="ga9587df579db31964427b563df59451e3"></a>

### `ADXL362_FIFO_MODE_OLDEST_SAVED`

```c
#define ADXL362_FIFO_MODE_OLDEST_SAVED 0x1
```

```c
#include <zephyr/dt-bindings/sensor/adxl362.h>
```

缓冲区满时停止，保留最早的样本（samples）。

<a id="gaa4e66bfd6d847c8c610b12cd77f16b68"></a>

### `ADXL362_FIFO_MODE_STREAM`

```c
#define ADXL362_FIFO_MODE_STREAM 0x2
```

```c
#include <zephyr/dt-bindings/sensor/adxl362.h>
```

连续流（continuous stream）模式，覆盖最早的样本。

<a id="ga8ea6f788f0236a3dec48c47bb2997d28"></a>

### `ADXL362_FIFO_MODE_TRIGGERED`

```c
#define ADXL362_FIFO_MODE_TRIGGERED 0x3
```

```c
#include <zephyr/dt-bindings/sensor/adxl362.h>
```

采集触发事件（trigger event）前后的样本。


## 2.4\_原页交叉引用（Cross References）

- [adxl362.h](../api_file_interface_reference/P002_zephyr__dt-bindings__sensor__adxl362.h_文件参考.md)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P001_ADLTC2990 API主题.md) · [返回大纲](大纲.md) · [下一章](P003_ADXL367 API主题.md)
