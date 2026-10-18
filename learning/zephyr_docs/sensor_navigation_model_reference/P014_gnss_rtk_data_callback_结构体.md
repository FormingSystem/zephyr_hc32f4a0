---
id: learning.zephyr-docs.sensor-navigation-model-reference.page-14
title: gnss_rtk_data_callback_结构体
kind: reference
status: maintained
domains: [zephyr, sensors, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structgnss__rtk__data__callback.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第14章\_gnss\_rtk\_data\_callback\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structgnss__rtk__data__callback.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/gnss/rtk/rtk.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 14.1\_数据成员（Data Fields）

<a id="r_ab418432aeca49fdc7a8b26ffc3b0f443"></a>

```c
const struct device * dev
```

相关声明：[device](../device_reference/P002_设备对象结构.md)、[dev](#ab418432aeca49fdc7a8b26ffc3b0f443)。

<a id="r_a63231a7df0b5e6346a61c28334dc6c71"></a>

```c
gnss_rtk_data_callback_t callback
```

相关声明：[gnss_rtk_data_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/rtk_8h.html#a3fdf2f1d4f0414cc99c926a6fa06acf2)、[callback](#a63231a7df0b5e6346a61c28334dc6c71)。

## 14.2\_详细说明（Detailed Documentation）

<a id="a63231a7df0b5e6346a61c28334dc6c71"></a>

### `callback`

```c
gnss_rtk_data_callback_t gnss_rtk_data_callback::callback
```

<a id="ab418432aeca49fdc7a8b26ffc3b0f443"></a>

### `dev`

```c
const struct device* gnss_rtk_data_callback::dev
```

本数据类型文档由以下文件生成：

- `zephyr/gnss/rtk/rtk.h`

## 14.3\_原页交叉引用（Cross References）

- [zephyr/gnss/rtk/rtk.h](https://docs.zephyrproject.org/latest/doxygen/html/rtk_8h_source.html)
- [device](../device_reference/P002_设备对象结构.md)
- [gnss_rtk_data_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/rtk_8h.html#a3fdf2f1d4f0414cc99c926a6fa06acf2)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P013_gnss_rtk_data_结构体.md) · [返回大纲](大纲.md) · [下一章](P015_gnss_satellite_结构体.md)
