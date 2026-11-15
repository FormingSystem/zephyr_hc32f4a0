---
id: learning.zephyr-docs.api-protocol-topic-reference.page-3
title: ADXL367 API主题
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__adxl367__interface.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第3章\_ADXL367 API主题

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__adxl367__interface.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Analog Devices ADXL367 三轴加速度计（3-axis accelerometer）。

<a id="details"></a>

Analog Devices ADXL367 三轴加速度计（3-axis accelerometer）。

<a id="header-files"></a>
<a id="files"></a>

## 3.1\_文件（Files）

<a id="r_adxl367_2Eh"></a>

```c
file adxl367.h
```

相关声明：[adxl367.h](../api_file_interface_reference/P003_zephyr__dt-bindings__sensor__adxl367.h_文件参考.md)。

the Analog Devices ADXL367 accelerometer的设备树绑定常量（Devicetree Binding Constants）。

<a id="header-member-group"></a>
<a id="member-group"></a>

## 3.2\_FIFO 模式选项（FIFO mode options）

设备树 `fifo-mode` 属性的取值。

<a id="r_ga263ef6fecf67b97692d04c51add47138"></a>

```c
#define ADXL367_FIFO_MODE_DISABLED 0x0
```

相关声明：[ADXL367_FIFO_MODE_DISABLED](#ga263ef6fecf67b97692d04c51add47138)。

禁用先进先出缓冲区（FIFO）。

<a id="r_ga8f5ce6faf0e0839661e9b036d51979ce"></a>

```c
#define ADXL367_FIFO_MODE_OLDEST_SAVED 0x1
```

相关声明：[ADXL367_FIFO_MODE_OLDEST_SAVED](#ga8f5ce6faf0e0839661e9b036d51979ce)。

缓冲区满时停止，保留最早的样本（samples）。

<a id="r_gaaeff202cb640db5129bf014434a01857"></a>

```c
#define ADXL367_FIFO_MODE_STREAM 0x2
```

相关声明：[ADXL367_FIFO_MODE_STREAM](#gaaeff202cb640db5129bf014434a01857)。

连续流（continuous stream）模式，覆盖最早的样本。

<a id="r_ga3348f6dce35164f80a6d5da50760ba12"></a>

```c
#define ADXL367_FIFO_MODE_TRIGGERED 0x3
```

相关声明：[ADXL367_FIFO_MODE_TRIGGERED](#ga3348f6dce35164f80a6d5da50760ba12)。

采集触发事件（trigger event）前后的样本。

## 3.3\_详细说明（Detailed Documentation）

<a id="ga263ef6fecf67b97692d04c51add47138"></a>

### `ADXL367_FIFO_MODE_DISABLED`

```c
#define ADXL367_FIFO_MODE_DISABLED 0x0
```

```c
#include <zephyr/dt-bindings/sensor/adxl367.h>
```

禁用先进先出缓冲区（FIFO）。

<a id="ga8f5ce6faf0e0839661e9b036d51979ce"></a>

### `ADXL367_FIFO_MODE_OLDEST_SAVED`

```c
#define ADXL367_FIFO_MODE_OLDEST_SAVED 0x1
```

```c
#include <zephyr/dt-bindings/sensor/adxl367.h>
```

缓冲区满时停止，保留最早的样本（samples）。

<a id="gaaeff202cb640db5129bf014434a01857"></a>

### `ADXL367_FIFO_MODE_STREAM`

```c
#define ADXL367_FIFO_MODE_STREAM 0x2
```

```c
#include <zephyr/dt-bindings/sensor/adxl367.h>
```

连续流（continuous stream）模式，覆盖最早的样本。

<a id="ga3348f6dce35164f80a6d5da50760ba12"></a>

### `ADXL367_FIFO_MODE_TRIGGERED`

```c
#define ADXL367_FIFO_MODE_TRIGGERED 0x3
```

```c
#include <zephyr/dt-bindings/sensor/adxl367.h>
```

采集触发事件（trigger event）前后的样本。


## 3.4\_原页交叉引用（Cross References）

- [adxl367.h](../api_file_interface_reference/P003_zephyr__dt-bindings__sensor__adxl367.h_文件参考.md)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P002_ADXL362 API主题.md) · [返回大纲](大纲.md) · [下一章](P004_ADXL372 API主题.md)
