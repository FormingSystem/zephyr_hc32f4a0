---
id: learning.zephyr-docs.api-network-time-topic-reference.page-15
title: IIS2ICLX API主题
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__iis2iclx__interface.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第15章\_IIS2ICLX API主题

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__iis2iclx__interface.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

STMicroelectronics IIS2ICLX 双轴倾角计（2-axis inclinometer）。

<a id="details"></a>

STMicroelectronics IIS2ICLX 双轴倾角计（2-axis inclinometer）。

<a id="header-files"></a>
<a id="files"></a>

## 15.1\_文件（Files）

<a id="r_iis2iclx_2Eh"></a>

```c
file iis2iclx.h
```

相关声明：[iis2iclx.h](https://docs.zephyrproject.org/latest/doxygen/html/iis2iclx_8h.html)。

the ST IIS2ICLX inclinometer的设备树绑定常量（Devicetree Binding Constants）。

<a id="header-member-group"></a>
<a id="member-group"></a>

## 15.2\_加速度计满量程范围（Accelerometer full-scale range）

设备树 `range` 属性的取值。

<a id="r_ga95903c983d457bc48d2a49efb7f2846c"></a>

```c
#define IIS2ICLX_DT_FS_500mG 0
```

相关声明：[IIS2ICLX_DT_FS_500mG](#ga95903c983d457bc48d2a49efb7f2846c)。

量程（range）：±0.5 g。

<a id="r_ga3d96639b08dc2d1dac0e4a07c3c27f55"></a>

```c
#define IIS2ICLX_DT_FS_3G 1
```

相关声明：[IIS2ICLX_DT_FS_3G](#ga3d96639b08dc2d1dac0e4a07c3c27f55)。

量程（range）：±3 g。

<a id="r_ga30d90393414465eb9ee5356cecc491a1"></a>

```c
#define IIS2ICLX_DT_FS_1G 2
```

相关声明：[IIS2ICLX_DT_FS_1G](#ga30d90393414465eb9ee5356cecc491a1)。

量程（range）：±1 g。

<a id="r_gae5be8696d32f8c3774e6a9cd8212c66c"></a>

```c
#define IIS2ICLX_DT_FS_2G 3
```

相关声明：[IIS2ICLX_DT_FS_2G](#gae5be8696d32f8c3774e6a9cd8212c66c)。

量程（range）：±2 g。

## 15.3\_加速度计输出数据率（Accelerometer output data rate）

设备树 `odr` 属性的取值。

<a id="r_gaa2856b0a48b1a1396b31d40226f8f257"></a>

```c
#define IIS2ICLX_DT_ODR_OFF 0x0
```

相关声明：[IIS2ICLX_DT_ODR_OFF](#gaa2856b0a48b1a1396b31d40226f8f257)。

掉电（Power-down）。

<a id="r_ga8a223914a9e619b7a229e81dfc6931a3"></a>

```c
#define IIS2ICLX_DT_ODR_12Hz5 0x1
```

相关声明：[IIS2ICLX_DT_ODR_12Hz5](#ga8a223914a9e619b7a229e81dfc6931a3)。

频率：12.5 Hz。

<a id="r_ga80341116af73bd318edcfc1fbdc3ef3d"></a>

```c
#define IIS2ICLX_DT_ODR_26H 0x2
```

相关声明：[IIS2ICLX_DT_ODR_26H](#ga80341116af73bd318edcfc1fbdc3ef3d)。

频率：26 Hz。

<a id="r_ga0dae0aaf2c7bc79f004aa3427750a3d2"></a>

```c
#define IIS2ICLX_DT_ODR_52Hz 0x3
```

相关声明：[IIS2ICLX_DT_ODR_52Hz](#ga0dae0aaf2c7bc79f004aa3427750a3d2)。

频率：52 Hz。

<a id="r_gacbde936ff668bf3e32f6b9f8a36d7f05"></a>

```c
#define IIS2ICLX_DT_ODR_104Hz 0x4
```

相关声明：[IIS2ICLX_DT_ODR_104Hz](#gacbde936ff668bf3e32f6b9f8a36d7f05)。

频率：104 Hz。

<a id="r_ga49da4463f1cd8a26867b126543a05900"></a>

```c
#define IIS2ICLX_DT_ODR_208Hz 0x5
```

相关声明：[IIS2ICLX_DT_ODR_208Hz](#ga49da4463f1cd8a26867b126543a05900)。

频率：208 Hz。

<a id="r_ga81441c39564b83b2ad6262f616b4a108"></a>

```c
#define IIS2ICLX_DT_ODR_416Hz 0x6
```

相关声明：[IIS2ICLX_DT_ODR_416Hz](#ga81441c39564b83b2ad6262f616b4a108)。

频率：416 Hz。

<a id="r_gacc53fe7776bcbab828e619d0081bcdf6"></a>

```c
#define IIS2ICLX_DT_ODR_833Hz 0x7
```

相关声明：[IIS2ICLX_DT_ODR_833Hz](#gacc53fe7776bcbab828e619d0081bcdf6)。

频率：833 Hz。

## 15.4\_详细说明（Detailed Documentation）

<a id="ga30d90393414465eb9ee5356cecc491a1"></a>

### `IIS2ICLX_DT_FS_1G`

```c
#define IIS2ICLX_DT_FS_1G 2
```

```c
#include <zephyr/dt-bindings/sensor/iis2iclx.h>
```

量程（range）：±1 g。

<a id="gae5be8696d32f8c3774e6a9cd8212c66c"></a>

### `IIS2ICLX_DT_FS_2G`

```c
#define IIS2ICLX_DT_FS_2G 3
```

```c
#include <zephyr/dt-bindings/sensor/iis2iclx.h>
```

量程（range）：±2 g。

<a id="ga3d96639b08dc2d1dac0e4a07c3c27f55"></a>

### `IIS2ICLX_DT_FS_3G`

```c
#define IIS2ICLX_DT_FS_3G 1
```

```c
#include <zephyr/dt-bindings/sensor/iis2iclx.h>
```

量程（range）：±3 g。

<a id="ga95903c983d457bc48d2a49efb7f2846c"></a>

### `IIS2ICLX_DT_FS_500mG`

```c
#define IIS2ICLX_DT_FS_500mG 0
```

```c
#include <zephyr/dt-bindings/sensor/iis2iclx.h>
```

量程（range）：±0.5 g。

<a id="gacbde936ff668bf3e32f6b9f8a36d7f05"></a>

### `IIS2ICLX_DT_ODR_104Hz`

```c
#define IIS2ICLX_DT_ODR_104Hz 0x4
```

```c
#include <zephyr/dt-bindings/sensor/iis2iclx.h>
```

频率：104 Hz。

<a id="ga8a223914a9e619b7a229e81dfc6931a3"></a>

### `IIS2ICLX_DT_ODR_12Hz5`

```c
#define IIS2ICLX_DT_ODR_12Hz5 0x1
```

```c
#include <zephyr/dt-bindings/sensor/iis2iclx.h>
```

频率：12.5 Hz。

<a id="ga49da4463f1cd8a26867b126543a05900"></a>

### `IIS2ICLX_DT_ODR_208Hz`

```c
#define IIS2ICLX_DT_ODR_208Hz 0x5
```

```c
#include <zephyr/dt-bindings/sensor/iis2iclx.h>
```

频率：208 Hz。

<a id="ga80341116af73bd318edcfc1fbdc3ef3d"></a>

### `IIS2ICLX_DT_ODR_26H`

```c
#define IIS2ICLX_DT_ODR_26H 0x2
```

```c
#include <zephyr/dt-bindings/sensor/iis2iclx.h>
```

频率：26 Hz。

<a id="ga81441c39564b83b2ad6262f616b4a108"></a>

### `IIS2ICLX_DT_ODR_416Hz`

```c
#define IIS2ICLX_DT_ODR_416Hz 0x6
```

```c
#include <zephyr/dt-bindings/sensor/iis2iclx.h>
```

频率：416 Hz。

<a id="ga0dae0aaf2c7bc79f004aa3427750a3d2"></a>

### `IIS2ICLX_DT_ODR_52Hz`

```c
#define IIS2ICLX_DT_ODR_52Hz 0x3
```

```c
#include <zephyr/dt-bindings/sensor/iis2iclx.h>
```

频率：52 Hz。

<a id="gacc53fe7776bcbab828e619d0081bcdf6"></a>

### `IIS2ICLX_DT_ODR_833Hz`

```c
#define IIS2ICLX_DT_ODR_833Hz 0x7
```

```c
#include <zephyr/dt-bindings/sensor/iis2iclx.h>
```

频率：833 Hz。

<a id="gaa2856b0a48b1a1396b31d40226f8f257"></a>

### `IIS2ICLX_DT_ODR_OFF`

```c
#define IIS2ICLX_DT_ODR_OFF 0x0
```

```c
#include <zephyr/dt-bindings/sensor/iis2iclx.h>
```

掉电（Power-down）。


## 15.5\_原页交叉引用（Cross References）

- [iis2iclx.h](https://docs.zephyrproject.org/latest/doxygen/html/iis2iclx_8h.html)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P014_互联网组管理协议（IGMP）的API。.md) · [返回大纲](大纲.md) · [下一章](P016_模拟轴（Analog axis）.md)
