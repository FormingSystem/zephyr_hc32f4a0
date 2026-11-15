---
id: learning.zephyr-docs.api-auxiliary-topic-reference.page-16
title: STTS22H API主题
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__stts22h__interface.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第16章\_STTS22H API主题

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__stts22h__interface.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

STMicroelectronics STTS22H 温度传感器（Temperature sensor）。

<a id="details"></a>

STMicroelectronics STTS22H 温度传感器（Temperature sensor）。

<a id="header-files"></a>
<a id="files"></a>

## 16.1\_文件（Files）

<a id="r_stts22h_2Eh"></a>

```c
file stts22h.h
```

相关声明：[stts22h.h](https://docs.zephyrproject.org/latest/doxygen/html/stts22h_8h.html)。

the ST STTS22H temperature sensor的设备树绑定常量（Devicetree Binding Constants）。

<a id="header-member-group"></a>
<a id="member-group"></a>

## 16.2\_输出数据率选项（Output data rate options）

设备树 `sampling-rate` 属性的取值。

<a id="r_ga2c2da98606a8b88b279d0138be13cb76"></a>

```c
#define STTS22H_POWER_DOWN 0x00
```

相关声明：[STTS22H_POWER_DOWN](#ga2c2da98606a8b88b279d0138be13cb76)。

掉电（Power-down）。

<a id="r_ga7c93186f94872a54a8ee97b154aa13ab"></a>

```c
#define STTS22H_ONE_SHOT 0x01
```

相关声明：[STTS22H_ONE_SHOT](#ga7c93186f94872a54a8ee97b154aa13ab)。

单次转换（one-shot conversion）。

<a id="r_gaa152218e7bf6be16cbee2f7e480d8e4d"></a>

```c
#define STTS22H_1Hz 0x04
```

相关声明：[STTS22H_1Hz](#gaa152218e7bf6be16cbee2f7e480d8e4d)。

频率：1 Hz。

<a id="r_ga2cefaa04bb4d8e855301088b3e9ed327"></a>

```c
#define STTS22H_25Hz 0x02
```

相关声明：[STTS22H_25Hz](#ga2cefaa04bb4d8e855301088b3e9ed327)。

频率：25 Hz。

<a id="r_ga43a2f447c68beab340f39b10f9a6df7b"></a>

```c
#define STTS22H_50Hz 0x12
```

相关声明：[STTS22H_50Hz](#ga43a2f447c68beab340f39b10f9a6df7b)。

频率：50 Hz。

<a id="r_ga9a6ff258f66017556825cad883744594"></a>

```c
#define STTS22H_100Hz 0x22
```

相关声明：[STTS22H_100Hz](#ga9a6ff258f66017556825cad883744594)。

频率：100 Hz。

<a id="r_ga572f26908bc83a3bb7b9f4daf165f855"></a>

```c
#define STTS22H_200Hz 0x32
```

相关声明：[STTS22H_200Hz](#ga572f26908bc83a3bb7b9f4daf165f855)。

频率：200 Hz。

## 16.3\_详细说明（Detailed Documentation）

<a id="ga9a6ff258f66017556825cad883744594"></a>

### `STTS22H_100Hz`

```c
#define STTS22H_100Hz 0x22
```

```c
#include <zephyr/dt-bindings/sensor/stts22h.h>
```

频率：100 Hz。

<a id="gaa152218e7bf6be16cbee2f7e480d8e4d"></a>

### `STTS22H_1Hz`

```c
#define STTS22H_1Hz 0x04
```

```c
#include <zephyr/dt-bindings/sensor/stts22h.h>
```

频率：1 Hz。

<a id="ga572f26908bc83a3bb7b9f4daf165f855"></a>

### `STTS22H_200Hz`

```c
#define STTS22H_200Hz 0x32
```

```c
#include <zephyr/dt-bindings/sensor/stts22h.h>
```

频率：200 Hz。

<a id="ga2cefaa04bb4d8e855301088b3e9ed327"></a>

### `STTS22H_25Hz`

```c
#define STTS22H_25Hz 0x02
```

```c
#include <zephyr/dt-bindings/sensor/stts22h.h>
```

频率：25 Hz。

<a id="ga43a2f447c68beab340f39b10f9a6df7b"></a>

### `STTS22H_50Hz`

```c
#define STTS22H_50Hz 0x12
```

```c
#include <zephyr/dt-bindings/sensor/stts22h.h>
```

频率：50 Hz。

<a id="ga7c93186f94872a54a8ee97b154aa13ab"></a>

### `STTS22H_ONE_SHOT`

```c
#define STTS22H_ONE_SHOT 0x01
```

```c
#include <zephyr/dt-bindings/sensor/stts22h.h>
```

单次转换（one-shot conversion）。

<a id="ga2c2da98606a8b88b279d0138be13cb76"></a>

### `STTS22H_POWER_DOWN`

```c
#define STTS22H_POWER_DOWN 0x00
```

```c
#include <zephyr/dt-bindings/sensor/stts22h.h>
```

掉电（Power-down）。


## 16.4\_原页交叉引用（Cross References）

- [stts22h.h](https://docs.zephyrproject.org/latest/doxygen/html/stts22h_8h.html)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P015_MTCH9010 API主题.md) · [返回大纲](大纲.md) · [下一章](P017_1-Wire 传感器 API（Sensor API）.md)
