---
id: learning.zephyr-docs.device-power-control-model-reference.page-84
title: sbs_gauge_manufacturer_name_结构体
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structsbs__gauge__manufacturer__name.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第84章\_sbs\_gauge\_manufacturer\_name\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structsbs__gauge__manufacturer__name.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/drivers/fuel_gauge.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 84.1\_数据成员（Data Fields）

<a id="r_a13a5902df94842f7a69a8028b8708ced"></a>

```c
uint8_t manufacturer_name_length
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[manufacturer_name_length](#a13a5902df94842f7a69a8028b8708ced)。

<a id="r_a40af61fe30263b21e9b9c92383562b0d"></a>

```c
char manufacturer_name [20]
```

相关声明：[manufacturer_name](#a40af61fe30263b21e9b9c92383562b0d)。

## 84.2\_详细说明（Detailed Documentation）

<a id="a40af61fe30263b21e9b9c92383562b0d"></a>

### `manufacturer_name`

```c
char sbs_gauge_manufacturer_name::manufacturer_name[20]
```

<a id="a13a5902df94842f7a69a8028b8708ced"></a>

### `manufacturer_name_length`

```c
uint8_t sbs_gauge_manufacturer_name::manufacturer_name_length
```

本数据类型文档由以下文件生成：

- `zephyr/drivers/fuel_gauge.h`

## 84.3\_原页交叉引用（Cross References）

- [zephyr/drivers/fuel_gauge.h](https://docs.zephyrproject.org/latest/doxygen/html/fuel__gauge_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P083_sbs_gauge_device_name_结构体.md) · [返回大纲](大纲.md) · [下一章](P085_sf32lb_clock_dt_spec_结构体.md)
