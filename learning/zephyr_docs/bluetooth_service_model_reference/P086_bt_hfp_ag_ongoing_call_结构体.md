---
id: learning.zephyr-docs.bluetooth-service-model-reference.page-86
title: bt_hfp_ag_ongoing_call_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hfp__ag__ongoing__call.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第86章\_bt\_hfp\_ag\_ongoing\_call\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hfp__ag__ongoing__call.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

正在进行的呼叫（Ongoing Call）。

```c
#include <zephyr/bluetooth/classic/hfp_ag.h>
```

<a id="details"></a>

进行中的呼叫（Ongoing call）。参数（Parameters）：`number` 为以 `\0` 终止的呼叫电话号码；`type` 指定电话号码格式；`dir` 为呼叫方向（Call direction）；`status` 为呼叫状态（Call status）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 86.1\_数据成员（Data Fields）

<a id="r_a1e5800a9c0f37539d0505d3223a35e2f"></a>

```c
char number [CONFIG_BT_HFP_AG_PHONE_NUMBER_MAX_LEN+1]
```

相关声明：[number](#a1e5800a9c0f37539d0505d3223a35e2f)。

<a id="r_a26a77093f5aace7dd2d5693f4cb82189"></a>

```c
uint8_t type
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[type](#a26a77093f5aace7dd2d5693f4cb82189)。

<a id="r_a506610c17544daf8a0238a2c4d285526"></a>

```c
enum bt_hfp_ag_call_dir dir
```

相关声明：[bt_hfp_ag_call_dir](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp__ag.html#ga019020ee2ed73c218f7dadf8371bf9a6)、[dir](#a506610c17544daf8a0238a2c4d285526)。

<a id="r_ac865f464436c3e73561fa8f6fcf09947"></a>

```c
enum bt_hfp_ag_call_status status
```

相关声明：[bt_hfp_ag_call_status](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp__ag.html#gad2220b4a470cb3d537cf09492847568e)、[status](#ac865f464436c3e73561fa8f6fcf09947)。

## 86.2\_详细说明（Detailed Documentation）

<a id="a506610c17544daf8a0238a2c4d285526"></a>

### `dir`

```c
enum bt_hfp_ag_call_dir bt_hfp_ag_ongoing_call::dir
```

<a id="a1e5800a9c0f37539d0505d3223a35e2f"></a>

### `number`

```c
char bt_hfp_ag_ongoing_call::number[CONFIG_BT_HFP_AG_PHONE_NUMBER_MAX_LEN+1]
```

<a id="ac865f464436c3e73561fa8f6fcf09947"></a>

### `status`

```c
enum bt_hfp_ag_call_status bt_hfp_ag_ongoing_call::status
```

<a id="a26a77093f5aace7dd2d5693f4cb82189"></a>

### `type`

```c
uint8_t bt_hfp_ag_ongoing_call::type
```

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/classic/hfp_ag.h`

## 86.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/classic/hfp_ag.h](https://docs.zephyrproject.org/latest/doxygen/html/hfp__ag_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bt_hfp_ag_call_dir](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp__ag.html#ga019020ee2ed73c218f7dadf8371bf9a6)
- [bt_hfp_ag_call_status](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp__ag.html#gad2220b4a470cb3d537cf09492847568e)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P085_bt_hfp_ag_cb_结构体.md) · [返回大纲](大纲.md) · [下一章](P087_bt_hfp_hf_结构体.md)
