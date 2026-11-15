---
id: learning.zephyr-docs.device-power-control-model-reference.page-82
title: sbs_gauge_device_chemistry_结构体
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structsbs__gauge__device__chemistry.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第82章\_sbs\_gauge\_device\_chemistry\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structsbs__gauge__device__chemistry.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/drivers/fuel_gauge.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 82.1\_数据成员（Data Fields）

<a id="r_a340cfddcc1ad7a758f75208b38208df4"></a>

```c
uint8_t device_chemistry_length
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[device_chemistry_length](#a340cfddcc1ad7a758f75208b38208df4)。

<a id="r_a2a3990be7618165d88790e53ac7b4e72"></a>

```c
char device_chemistry [4]
```

相关声明：[device_chemistry](#a2a3990be7618165d88790e53ac7b4e72)。

## 82.2\_详细说明（Detailed Documentation）

<a id="a2a3990be7618165d88790e53ac7b4e72"></a>

### `device_chemistry`

```c
char sbs_gauge_device_chemistry::device_chemistry[4]
```

<a id="a340cfddcc1ad7a758f75208b38208df4"></a>

### `device_chemistry_length`

```c
uint8_t sbs_gauge_device_chemistry::device_chemistry_length
```

本数据类型文档由以下文件生成：

- `zephyr/drivers/fuel_gauge.h`

## 82.3\_原页交叉引用（Cross References）

- [zephyr/drivers/fuel_gauge.h](https://docs.zephyrproject.org/latest/doxygen/html/fuel__gauge_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P081_sam_sckc_config_结构体.md) · [返回大纲](大纲.md) · [下一章](P083_sbs_gauge_device_name_结构体.md)
