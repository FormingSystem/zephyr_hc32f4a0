---
id: learning.zephyr-docs.sensor-navigation-model-reference.page-16
title: gnss_satellites_callback_结构体
kind: reference
status: maintained
domains: [zephyr, sensors, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structgnss__satellites__callback.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第16章\_gnss\_satellites\_callback\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structgnss__satellites__callback.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

全球导航卫星系统（GNSS）的回调结构。

```c
#include <zephyr/drivers/gnss.h>
```

<a id="details"></a>

全球导航卫星系统（GNSS）的回调结构。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 16.1\_数据成员（Data Fields）

<a id="r_a19e64ff2450c00080ae39528f7d07b2b"></a>

```c
const struct device * dev
```

相关声明：[device](../device_reference/P002_设备对象结构.md)、[dev](#a19e64ff2450c00080ae39528f7d07b2b)。

如果非 `NULL`，则将回调限定为仅接收此设备的 GNSS 数据。

<a id="r_af12fc64ff9c696b5862b5adfef31269b"></a>

```c
gnss_satellites_callback_t callback
```

相关声明：[gnss_satellites_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface.html#ga80cf700468d1c942cfa064368e212e6f)、[callback](#af12fc64ff9c696b5862b5adfef31269b)。

发布 GNSS 卫星信息时调用的回调。

## 16.2\_详细说明（Detailed Documentation）

<a id="af12fc64ff9c696b5862b5adfef31269b"></a>

### `callback`

```c
gnss_satellites_callback_t gnss_satellites_callback::callback
```

发布 GNSS 卫星信息时调用的回调。

<a id="a19e64ff2450c00080ae39528f7d07b2b"></a>

### `dev`

```c
const struct device* gnss_satellites_callback::dev
```

如果非 `NULL`，则将回调限定为仅接收此设备的 GNSS 数据。

本数据类型文档由以下文件生成：

- `zephyr/drivers/gnss.h`

## 16.3\_原页交叉引用（Cross References）

- [zephyr/drivers/gnss.h](https://docs.zephyrproject.org/latest/doxygen/html/gnss_8h_source.html)
- [device](../device_reference/P002_设备对象结构.md)
- [gnss_satellites_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface.html#ga80cf700468d1c942cfa064368e212e6f)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P015_gnss_satellite_结构体.md) · [返回大纲](大纲.md) · [下一章](P017_gnss_time_结构体.md)
