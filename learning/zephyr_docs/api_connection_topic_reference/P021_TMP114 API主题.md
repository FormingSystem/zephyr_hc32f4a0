---
id: learning.zephyr-docs.api-connection-topic-reference.page-21
title: TMP114 API主题
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__tmp114__interface.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第21章\_TMP114 API主题

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__tmp114__interface.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Texas Instruments TMP114 温度传感器（Temperature sensor）。

<a id="details"></a>

Texas Instruments TMP114 温度传感器（Temperature sensor）。

<a id="header-files"></a>
<a id="files"></a>

## 21.1\_文件（Files）

<a id="r_tmp114_2Eh"></a>

```c
file tmp114.h
```

相关声明：[tmp114.h](https://docs.zephyrproject.org/latest/doxygen/html/tmp114_8h.html)。

the TI TMP114 temperature sensor的设备树绑定常量（Devicetree Binding Constants）。

<a id="header-member-group"></a>
<a id="member-group"></a>

## 21.2\_输出数据率选项（Output data rate options）

设备树 `odr` 属性的取值。

<a id="r_ga8307c6d068d5d26fad96750f726e33bd"></a>

```c
#define TMP114_DT_ODR_6_4_MS 0
```

相关声明：[TMP114_DT_ODR_6_4_MS](#ga8307c6d068d5d26fad96750f726e33bd)。

时间：6.4 ms。

<a id="r_gae531ff2e29bb83dec0d43e48c81d2de2"></a>

```c
#define TMP114_DT_ODR_31_25_MS 1
```

相关声明：[TMP114_DT_ODR_31_25_MS](#gae531ff2e29bb83dec0d43e48c81d2de2)。

时间：31.25 ms。

<a id="r_ga697504d058ad6b374807f824856ae8e9"></a>

```c
#define TMP114_DT_ODR_62_5_MS 2
```

相关声明：[TMP114_DT_ODR_62_5_MS](#ga697504d058ad6b374807f824856ae8e9)。

时间：62.5 ms。

<a id="r_ga7968bd1e019c209c9a6533249da3ed13"></a>

```c
#define TMP114_DT_ODR_125_MS 3
```

相关声明：[TMP114_DT_ODR_125_MS](#ga7968bd1e019c209c9a6533249da3ed13)。

时间：125 ms。

<a id="r_ga71bb7f27e8ba099c09a0e064c7c946bb"></a>

```c
#define TMP114_DT_ODR_250_MS 4
```

相关声明：[TMP114_DT_ODR_250_MS](#ga71bb7f27e8ba099c09a0e064c7c946bb)。

时间：250 ms。

<a id="r_ga5a2784ffcccb973644b22d5d91ed0ad1"></a>

```c
#define TMP114_DT_ODR_500_MS 5
```

相关声明：[TMP114_DT_ODR_500_MS](#ga5a2784ffcccb973644b22d5d91ed0ad1)。

时间：500 ms。

<a id="r_ga7cbabe7106cc263e22f785658f5a6b5c"></a>

```c
#define TMP114_DT_ODR_1000_MS 6
```

相关声明：[TMP114_DT_ODR_1000_MS](#ga7cbabe7106cc263e22f785658f5a6b5c)。

时间：1000 ms。

<a id="r_ga195eb753c11c73c7a5be0ff50cbde481"></a>

```c
#define TMP114_DT_ODR_2000_MS 7
```

相关声明：[TMP114_DT_ODR_2000_MS](#ga195eb753c11c73c7a5be0ff50cbde481)。

时间：2000 ms。

## 21.3\_详细说明（Detailed Documentation）

<a id="ga7cbabe7106cc263e22f785658f5a6b5c"></a>

### `TMP114_DT_ODR_1000_MS`

```c
#define TMP114_DT_ODR_1000_MS 6
```

```c
#include <zephyr/dt-bindings/sensor/tmp114.h>
```

时间：1000 ms。

<a id="ga7968bd1e019c209c9a6533249da3ed13"></a>

### `TMP114_DT_ODR_125_MS`

```c
#define TMP114_DT_ODR_125_MS 3
```

```c
#include <zephyr/dt-bindings/sensor/tmp114.h>
```

时间：125 ms。

<a id="ga195eb753c11c73c7a5be0ff50cbde481"></a>

### `TMP114_DT_ODR_2000_MS`

```c
#define TMP114_DT_ODR_2000_MS 7
```

```c
#include <zephyr/dt-bindings/sensor/tmp114.h>
```

时间：2000 ms。

<a id="ga71bb7f27e8ba099c09a0e064c7c946bb"></a>

### `TMP114_DT_ODR_250_MS`

```c
#define TMP114_DT_ODR_250_MS 4
```

```c
#include <zephyr/dt-bindings/sensor/tmp114.h>
```

时间：250 ms。

<a id="gae531ff2e29bb83dec0d43e48c81d2de2"></a>

### `TMP114_DT_ODR_31_25_MS`

```c
#define TMP114_DT_ODR_31_25_MS 1
```

```c
#include <zephyr/dt-bindings/sensor/tmp114.h>
```

时间：31.25 ms。

<a id="ga5a2784ffcccb973644b22d5d91ed0ad1"></a>

### `TMP114_DT_ODR_500_MS`

```c
#define TMP114_DT_ODR_500_MS 5
```

```c
#include <zephyr/dt-bindings/sensor/tmp114.h>
```

时间：500 ms。

<a id="ga697504d058ad6b374807f824856ae8e9"></a>

### `TMP114_DT_ODR_62_5_MS`

```c
#define TMP114_DT_ODR_62_5_MS 2
```

```c
#include <zephyr/dt-bindings/sensor/tmp114.h>
```

时间：62.5 ms。

<a id="ga8307c6d068d5d26fad96750f726e33bd"></a>

### `TMP114_DT_ODR_6_4_MS`

```c
#define TMP114_DT_ODR_6_4_MS 0
```

```c
#include <zephyr/dt-bindings/sensor/tmp114.h>
```

时间：6.4 ms。


## 21.4\_原页交叉引用（Cross References）

- [tmp114.h](https://docs.zephyrproject.org/latest/doxygen/html/tmp114_8h.html)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P020_SHT4X API主题.md) · [返回大纲](大纲.md) · [下一章](P022_按字粒度访问内存 API（Word Granular Access Memory APIs）.md)
