---
id: learning.zephyr-docs.api-vector-pipeline-topic-reference.page-10
title: ISM330DHCX API主题
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__ism330dhcx__interface.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第10章\_ISM330DHCX API主题

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__ism330dhcx__interface.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

STMicroelectronics ISM330DHCX 六轴惯性测量单元（IMU）。

<a id="details"></a>

STMicroelectronics ISM330DHCX 六轴惯性测量单元（IMU）。

<a id="header-files"></a>
<a id="files"></a>

## 10.1\_文件（Files）

<a id="r_ism330dhcx_2Eh"></a>

```c
file ism330dhcx.h
```

相关声明：[ism330dhcx.h](https://docs.zephyrproject.org/latest/doxygen/html/ism330dhcx_8h.html)。

the ST ISM330DHCX IMU的设备树绑定常量（Devicetree Binding Constants）。

<a id="header-member-group"></a>
<a id="member-group"></a>

## 10.2\_加速度计与陀螺仪输出数据率（Accelerometer and Gyroscope Output Data Rate）

设备树（Devicetree）属性 `accel-odr` 和 `gyro-odr` 的取值。

<a id="r_ga87a5e66db94487da96dfc641d1f361b7"></a>

```c
#define ISM330DHCX_DT_ODR_OFF 0x0
```

相关声明：[ISM330DHCX_DT_ODR_OFF](#ga87a5e66db94487da96dfc641d1f361b7)。

掉电（Power-down）。

<a id="r_gabf89ada8b9ccb619405ae5a6b85b25c8"></a>

```c
#define ISM330DHCX_DT_ODR_12Hz5 0x1
```

相关声明：[ISM330DHCX_DT_ODR_12Hz5](#gabf89ada8b9ccb619405ae5a6b85b25c8)。

频率：12.5 Hz。

<a id="r_ga8a13ead73def96a1eeadd80e36c24ec9"></a>

```c
#define ISM330DHCX_DT_ODR_26H 0x2
```

相关声明：[ISM330DHCX_DT_ODR_26H](#ga8a13ead73def96a1eeadd80e36c24ec9)。

频率：26 Hz。

<a id="r_ga8e867da0f5762b9d92528e83da164d52"></a>

```c
#define ISM330DHCX_DT_ODR_52Hz 0x3
```

相关声明：[ISM330DHCX_DT_ODR_52Hz](#ga8e867da0f5762b9d92528e83da164d52)。

频率：52 Hz。

<a id="r_ga7af183f35760d8e5846f27ba6772a8de"></a>

```c
#define ISM330DHCX_DT_ODR_104Hz 0x4
```

相关声明：[ISM330DHCX_DT_ODR_104Hz](#ga7af183f35760d8e5846f27ba6772a8de)。

频率：104 Hz。

<a id="r_ga3ebda7f972a93b3983e6b999424a101c"></a>

```c
#define ISM330DHCX_DT_ODR_208Hz 0x5
```

相关声明：[ISM330DHCX_DT_ODR_208Hz](#ga3ebda7f972a93b3983e6b999424a101c)。

频率：208 Hz。

<a id="r_ga841dc019b9d82260918954574732f2e2"></a>

```c
#define ISM330DHCX_DT_ODR_416Hz 0x6
```

相关声明：[ISM330DHCX_DT_ODR_416Hz](#ga841dc019b9d82260918954574732f2e2)。

频率：416 Hz。

<a id="r_ga04c641e9e5d6ab3623dad897bf354885"></a>

```c
#define ISM330DHCX_DT_ODR_833Hz 0x7
```

相关声明：[ISM330DHCX_DT_ODR_833Hz](#ga04c641e9e5d6ab3623dad897bf354885)。

频率：833 Hz。

<a id="r_gaeabe6f4e3818189feadb07b24a7094ca"></a>

```c
#define ISM330DHCX_DT_ODR_1666Hz 0x8
```

相关声明：[ISM330DHCX_DT_ODR_1666Hz](#gaeabe6f4e3818189feadb07b24a7094ca)。

1666 Hz（赫兹）。

<a id="r_ga1b177f90f4b9fb03303891a604374ead"></a>

```c
#define ISM330DHCX_DT_ODR_3332Hz 0x9
```

相关声明：[ISM330DHCX_DT_ODR_3332Hz](#ga1b177f90f4b9fb03303891a604374ead)。

3332 Hz（赫兹）。

<a id="r_gacdeff79efe2eb01d76f1db32bc99ee94"></a>

```c
#define ISM330DHCX_DT_ODR_6667Hz 0xa
```

相关声明：[ISM330DHCX_DT_ODR_6667Hz](#gacdeff79efe2eb01d76f1db32bc99ee94)。

6667 Hz（赫兹）。

<a id="r_ga67a0d381f9856c2b13de67c2e75393d9"></a>

```c
#define ISM330DHCX_DT_ODR_1Hz6 0xb
```

相关声明：[ISM330DHCX_DT_ODR_1Hz6](#ga67a0d381f9856c2b13de67c2e75393d9)。

1.6 Hz，低功耗（Low-power）模式。

## 10.3\_详细说明（Detailed Documentation）

<a id="ga7af183f35760d8e5846f27ba6772a8de"></a>

### `ISM330DHCX_DT_ODR_104Hz`

```c
#define ISM330DHCX_DT_ODR_104Hz 0x4
```

```c
#include <zephyr/dt-bindings/sensor/ism330dhcx.h>
```

频率：104 Hz。

<a id="gabf89ada8b9ccb619405ae5a6b85b25c8"></a>

### `ISM330DHCX_DT_ODR_12Hz5`

```c
#define ISM330DHCX_DT_ODR_12Hz5 0x1
```

```c
#include <zephyr/dt-bindings/sensor/ism330dhcx.h>
```

频率：12.5 Hz。

<a id="gaeabe6f4e3818189feadb07b24a7094ca"></a>

### `ISM330DHCX_DT_ODR_1666Hz`

```c
#define ISM330DHCX_DT_ODR_1666Hz 0x8
```

```c
#include <zephyr/dt-bindings/sensor/ism330dhcx.h>
```

1666 Hz（赫兹）。

<a id="ga67a0d381f9856c2b13de67c2e75393d9"></a>

### `ISM330DHCX_DT_ODR_1Hz6`

```c
#define ISM330DHCX_DT_ODR_1Hz6 0xb
```

```c
#include <zephyr/dt-bindings/sensor/ism330dhcx.h>
```

1.6 Hz，低功耗（Low-power）模式。

<a id="ga3ebda7f972a93b3983e6b999424a101c"></a>

### `ISM330DHCX_DT_ODR_208Hz`

```c
#define ISM330DHCX_DT_ODR_208Hz 0x5
```

```c
#include <zephyr/dt-bindings/sensor/ism330dhcx.h>
```

频率：208 Hz。

<a id="ga8a13ead73def96a1eeadd80e36c24ec9"></a>

### `ISM330DHCX_DT_ODR_26H`

```c
#define ISM330DHCX_DT_ODR_26H 0x2
```

```c
#include <zephyr/dt-bindings/sensor/ism330dhcx.h>
```

频率：26 Hz。

<a id="ga1b177f90f4b9fb03303891a604374ead"></a>

### `ISM330DHCX_DT_ODR_3332Hz`

```c
#define ISM330DHCX_DT_ODR_3332Hz 0x9
```

```c
#include <zephyr/dt-bindings/sensor/ism330dhcx.h>
```

3332 Hz（赫兹）。

<a id="ga841dc019b9d82260918954574732f2e2"></a>

### `ISM330DHCX_DT_ODR_416Hz`

```c
#define ISM330DHCX_DT_ODR_416Hz 0x6
```

```c
#include <zephyr/dt-bindings/sensor/ism330dhcx.h>
```

频率：416 Hz。

<a id="ga8e867da0f5762b9d92528e83da164d52"></a>

### `ISM330DHCX_DT_ODR_52Hz`

```c
#define ISM330DHCX_DT_ODR_52Hz 0x3
```

```c
#include <zephyr/dt-bindings/sensor/ism330dhcx.h>
```

频率：52 Hz。

<a id="gacdeff79efe2eb01d76f1db32bc99ee94"></a>

### `ISM330DHCX_DT_ODR_6667Hz`

```c
#define ISM330DHCX_DT_ODR_6667Hz 0xa
```

```c
#include <zephyr/dt-bindings/sensor/ism330dhcx.h>
```

6667 Hz（赫兹）。

<a id="ga04c641e9e5d6ab3623dad897bf354885"></a>

### `ISM330DHCX_DT_ODR_833Hz`

```c
#define ISM330DHCX_DT_ODR_833Hz 0x7
```

```c
#include <zephyr/dt-bindings/sensor/ism330dhcx.h>
```

频率：833 Hz。

<a id="ga87a5e66db94487da96dfc641d1f361b7"></a>

### `ISM330DHCX_DT_ODR_OFF`

```c
#define ISM330DHCX_DT_ODR_OFF 0x0
```

```c
#include <zephyr/dt-bindings/sensor/ism330dhcx.h>
```

掉电（Power-down）。


## 10.4\_原页交叉引用（Cross References）

- [ism330dhcx.h](https://docs.zephyrproject.org/latest/doxygen/html/ism330dhcx_8h.html)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P009_电量计驱动后端 API（Fuel Gauge Driver Backend API）.md) · [返回大纲](大纲.md) · [下一章](P011_ISM6HG256X API主题.md)
