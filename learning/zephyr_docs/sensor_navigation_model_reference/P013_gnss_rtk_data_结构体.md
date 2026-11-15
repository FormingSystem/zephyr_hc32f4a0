---
id: learning.zephyr-docs.sensor-navigation-model-reference.page-13
title: gnss_rtk_data_结构体
kind: reference
status: maintained
domains: [zephyr, sensors, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structgnss__rtk__data.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第13章\_gnss\_rtk\_data\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structgnss__rtk__data.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/gnss/rtk/rtk.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 13.1\_数据成员（Data Fields）

<a id="r_a9af2907041a16931c1f0e4119b9e3479"></a>

```c
const uint8_t * data
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[data](#a9af2907041a16931c1f0e4119b9e3479)。

<a id="r_a6843951f83ac4ea1624980cbe4d2f4f2"></a>

```c
size_t len
```

相关声明：[len](#a6843951f83ac4ea1624980cbe4d2f4f2)。

## 13.2\_详细说明（Detailed Documentation）

<a id="a9af2907041a16931c1f0e4119b9e3479"></a>

### `data`

```c
const uint8_t* gnss_rtk_data::data
```

<a id="a6843951f83ac4ea1624980cbe4d2f4f2"></a>

### `len`

```c
size_t gnss_rtk_data::len
```

本数据类型文档由以下文件生成：

- `zephyr/gnss/rtk/rtk.h`

## 13.3\_原页交叉引用（Cross References）

- [zephyr/gnss/rtk/rtk.h](https://docs.zephyrproject.org/latest/doxygen/html/rtk_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P012_gnss_info_结构体.md) · [返回大纲](大纲.md) · [下一章](P014_gnss_rtk_data_callback_结构体.md)
