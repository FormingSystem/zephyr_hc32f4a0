---
id: learning.zephyr-docs.bluetooth-service-model-reference.page-12
title: bt_br_discovery_param_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__br__discovery__param.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第12章\_bt\_br\_discovery\_param\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__br__discovery__param.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

BR/EDR 发现（Discovery）参数。

```c
#include <zephyr/bluetooth/classic/classic.h>
```

<a id="details"></a>

BR/EDR 发现（Discovery）参数。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 12.1\_数据成员（Data Fields）

<a id="r_a3087af0c5a264d50a27395d974f99e1e"></a>

```c
uint8_t length
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[length](#a3087af0c5a264d50a27395d974f99e1e)。

设备发现的最长持续时间（Maximum discovery length），以 1.28 秒为单位。

<a id="r_ac02d03f8cfdf4ad7aee3178e871cc105"></a>

```c
bool limited
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[limited](#ac02d03f8cfdf4ad7aee3178e871cc105)。

要使用受限发现过程（Limited discovery procedure）时为 `true`。

## 12.2\_详细说明（Detailed Documentation）

<a id="a3087af0c5a264d50a27395d974f99e1e"></a>

### `length`

```c
uint8_t bt_br_discovery_param::length
```

设备发现的最长持续时间（Maximum discovery length），以 1.28 秒为单位。

有效范围为 `0x01`–`0x30`。

<a id="ac02d03f8cfdf4ad7aee3178e871cc105"></a>

### `limited`

```c
bool bt_br_discovery_param::limited
```

要使用受限发现过程（Limited discovery procedure）时为 `true`。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/classic/classic.h`

## 12.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/classic/classic.h](https://docs.zephyrproject.org/latest/doxygen/html/classic_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P011_bt_br_discovery_cb_结构体.md) · [返回大纲](大纲.md) · [下一章](P013_bt_br_discovery_result_结构体.md)
