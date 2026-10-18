---
id: learning.zephyr-docs.api-protocol-topic-reference.page-4
title: ADXL372 API主题
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__adxl372__interface.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第4章\_ADXL372 API主题

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__adxl372__interface.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Analog Devices ADXL372 三轴加速度计（3-axis accelerometer）。

<a id="details"></a>

Analog Devices ADXL372 三轴加速度计（3-axis accelerometer）。

<a id="header-files"></a>
<a id="files"></a>

## 4.1\_文件（Files）

<a id="r_adxl372_2Eh"></a>

```c
file adxl372.h
```

相关声明：[adxl372.h](../api_file_interface_reference/P004_zephyr__dt-bindings__sensor__adxl372.h_文件参考.md)。

the Analog Devices ADXL372 accelerometer的设备树绑定常量（Devicetree Binding Constants）。

<a id="header-member-group"></a>
<a id="member-group"></a>

## 4.2\_FIFO 模式选项（FIFO mode options）

设备树 `fifo-mode` 属性的取值。

<a id="r_gace27031371f0fca13791ad77fb7642d3"></a>

```c
#define ADXL372_FIFO_MODE_BYPASSED 0x0
```

相关声明：[ADXL372_FIFO_MODE_BYPASSED](#gace27031371f0fca13791ad77fb7642d3)。

旁路（bypass）FIFO，即禁用 FIFO。

<a id="r_ga28f79424f8d0c8b501b5cb33bbaeca89"></a>

```c
#define ADXL372_FIFO_MODE_STREAMED 0x1
```

相关声明：[ADXL372_FIFO_MODE_STREAMED](#ga28f79424f8d0c8b501b5cb33bbaeca89)。

连续流（continuous stream）模式，覆盖最早的样本。

<a id="r_gad8c7e3cfad1ec512c41a949a22be1c1b"></a>

```c
#define ADXL372_FIFO_MODE_TRIGGERED 0x2
```

相关声明：[ADXL372_FIFO_MODE_TRIGGERED](#gad8c7e3cfad1ec512c41a949a22be1c1b)。

采集触发事件（trigger event）前后的样本。

<a id="r_gae75dd1acf478fb3d0f415691d61f11a9"></a>

```c
#define ADXL372_FIFO_MODE_OLD_SAVED 0x3
```

相关声明：[ADXL372_FIFO_MODE_OLD_SAVED](#gae75dd1acf478fb3d0f415691d61f11a9)。

缓冲区满时停止，保留最早的样本（samples）。

## 4.3\_详细说明（Detailed Documentation）

<a id="gace27031371f0fca13791ad77fb7642d3"></a>

### `ADXL372_FIFO_MODE_BYPASSED`

```c
#define ADXL372_FIFO_MODE_BYPASSED 0x0
```

```c
#include <zephyr/dt-bindings/sensor/adxl372.h>
```

旁路（bypass）FIFO，即禁用 FIFO。

<a id="gae75dd1acf478fb3d0f415691d61f11a9"></a>

### `ADXL372_FIFO_MODE_OLD_SAVED`

```c
#define ADXL372_FIFO_MODE_OLD_SAVED 0x3
```

```c
#include <zephyr/dt-bindings/sensor/adxl372.h>
```

缓冲区满时停止，保留最早的样本（samples）。

<a id="ga28f79424f8d0c8b501b5cb33bbaeca89"></a>

### `ADXL372_FIFO_MODE_STREAMED`

```c
#define ADXL372_FIFO_MODE_STREAMED 0x1
```

```c
#include <zephyr/dt-bindings/sensor/adxl372.h>
```

连续流（continuous stream）模式，覆盖最早的样本。

<a id="gad8c7e3cfad1ec512c41a949a22be1c1b"></a>

### `ADXL372_FIFO_MODE_TRIGGERED`

```c
#define ADXL372_FIFO_MODE_TRIGGERED 0x2
```

```c
#include <zephyr/dt-bindings/sensor/adxl372.h>
```

采集触发事件（trigger event）前后的样本。


## 4.4\_原页交叉引用（Cross References）

- [adxl372.h](../api_file_interface_reference/P004_zephyr__dt-bindings__sensor__adxl372.h_文件参考.md)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P003_ADXL367 API主题.md) · [返回大纲](大纲.md) · [下一章](P005_BD8LB600FS API主题.md)
