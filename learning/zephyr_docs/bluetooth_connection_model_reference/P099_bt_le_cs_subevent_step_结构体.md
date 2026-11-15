---
id: learning.zephyr-docs.bluetooth-connection-model-reference.page-99
title: bt_le_cs_subevent_step_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__le__cs__subevent__step.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第99章\_bt\_le\_cs\_subevent\_step\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__le__cs__subevent__step.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

子事件结果步骤（Subevent Result Step）。

```c
#include <zephyr/bluetooth/cs.h>
```

<a id="details"></a>

子事件结果步骤（Subevent Result Step）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 99.1\_数据成员（Data Fields）

<a id="r_a82103efe7c897abdf5bbb9c0a23cfba4"></a>

```c
uint8_t mode
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[mode](#a82103efe7c897abdf5bbb9c0a23cfba4)。

信道探测步骤模式（CS step mode）。

<a id="r_a54b47ddae09d8ab3f57124f71c4efbca"></a>

```c
uint8_t channel
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[channel](#a54b47ddae09d8ab3f57124f71c4efbca)。

信道探测步骤信道索引（CS step channel index）。

<a id="r_a32d2c13c5513220cf1cd7a13fb18c501"></a>

```c
uint8_t data_len
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[data_len](#a32d2c13c5513220cf1cd7a13fb18c501)。

所报告的角色及模式专用信息长度（Role- and mode-specific information length）。

<a id="r_a46494728a82c6d50f6acd8f88e1a0842"></a>

```c
const uint8_t * data
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[data](#a46494728a82c6d50f6acd8f88e1a0842)。

指向角色及模式专用信息（Role- and mode-specific information）的指针。

## 99.2\_详细说明（Detailed Documentation）

<a id="a54b47ddae09d8ab3f57124f71c4efbca"></a>

### `channel`

```c
uint8_t bt_le_cs_subevent_step::channel
```

信道探测步骤信道索引（CS step channel index）。

<a id="a46494728a82c6d50f6acd8f88e1a0842"></a>

### `data`

```c
const uint8_t* bt_le_cs_subevent_step::data
```

指向角色及模式专用信息（Role- and mode-specific information）的指针。

<a id="a32d2c13c5513220cf1cd7a13fb18c501"></a>

### `data_len`

```c
uint8_t bt_le_cs_subevent_step::data_len
```

所报告的角色及模式专用信息长度（Role- and mode-specific information length）。

<a id="a82103efe7c897abdf5bbb9c0a23cfba4"></a>

### `mode`

```c
uint8_t bt_le_cs_subevent_step::mode
```

信道探测步骤模式（CS step mode）。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/cs.h`

## 99.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/cs.h](https://docs.zephyrproject.org/latest/doxygen/html/cs_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P098_bt_le_cs_set_procedure_parameters_param_结构体.md) · [返回大纲](大纲.md) · [下一章](P100_bt_le_cs_test_cb_结构体.md)
