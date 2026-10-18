---
id: learning.zephyr-docs.sensor-navigation-model-reference.page-23
title: r502a_template_结构体
kind: reference
status: maintained
domains: [zephyr, sensors, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structr502a__template.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第23章\_r502a\_template\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structr502a__template.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

指纹模板（Fingerprint Template）。

```c
#include <zephyr/drivers/sensor/grow_r502a.h>
```

<a id="details"></a>

指纹模板（Fingerprint template）。此结构体保存指纹匹配所用的模板数据。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 23.1\_数据成员（Data Fields）

<a id="r_aca6dc417fc7e1de22da94e4d4e2b96a9"></a>

```c
uint8_t * data
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[data](#aca6dc417fc7e1de22da94e4d4e2b96a9)。

<a id="r_a2d4ab0b0ea4e4cf8b061705910639ae4"></a>

```c
size_t len
```

相关声明：[len](#a2d4ab0b0ea4e4cf8b061705910639ae4)。

## 23.2\_详细说明（Detailed Documentation）

<a id="aca6dc417fc7e1de22da94e4d4e2b96a9"></a>

### `data`

```c
uint8_t* r502a_template::data
```

<a id="a2d4ab0b0ea4e4cf8b061705910639ae4"></a>

### `len`

```c
size_t r502a_template::len
```

本数据类型文档由以下文件生成：

- `zephyr/drivers/sensor/grow_r502a.h`

## 23.3\_原页交叉引用（Cross References）

- [zephyr/drivers/sensor/grow_r502a.h](https://docs.zephyrproject.org/latest/doxygen/html/grow__r502a_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P022_r502a_sys_param_结构体.md) · [返回大纲](大纲.md) · [下一章](P024_sensing_callback_list_结构体.md)
