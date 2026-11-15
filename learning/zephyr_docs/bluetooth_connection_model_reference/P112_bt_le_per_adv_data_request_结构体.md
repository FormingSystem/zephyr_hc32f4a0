---
id: learning.zephyr-docs.bluetooth-connection-model-reference.page-112
title: bt_le_per_adv_data_request_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__le__per__adv__data__request.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第112章\_bt\_le\_per\_adv\_data\_request\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__le__per__adv__data__request.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

带响应的周期广播（PAwR）子事件信息。

```c
#include <zephyr/bluetooth/bluetooth.h>
```

<a id="details"></a>

带响应的周期广播子事件信息（PAwR subevent information）。控制器表示已准备好发送一个或多个 PAwR 子事件时，`bt_le_per_adv_data_request` 保存首个可设置数据的子事件，以及可设置数据的子事件数量等信息。注意（Note）：用于 `bt_le_ext_adv_cb`。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 112.1\_数据成员（Data Fields）

<a id="r_a779ed161919c3117f6ce165deb0a9b0a"></a>

```c
uint8_t start
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[start](#a779ed161919c3117f6ce165deb0a9b0a)。

首个可以设置数据的子事件（First subevent）。

<a id="r_a766991899bc3e689adec36bf1f12e802"></a>

```c
uint8_t count
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[count](#a766991899bc3e689adec36bf1f12e802)。

可以设置数据的子事件数量（Number of subevents）。

## 112.2\_详细说明（Detailed Documentation）

<a id="a766991899bc3e689adec36bf1f12e802"></a>

### `count`

```c
uint8_t bt_le_per_adv_data_request::count
```

可以设置数据的子事件数量（Number of subevents）。

<a id="a779ed161919c3117f6ce165deb0a9b0a"></a>

### `start`

```c
uint8_t bt_le_per_adv_data_request::start
```

首个可以设置数据的子事件（First subevent）。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/bluetooth.h`

## 112.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/bluetooth.h](https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2bluetooth_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bt_le_per_adv_data_request](P112_bt_le_per_adv_data_request_结构体.md)
- [bt_le_ext_adv_cb](P103_bt_le_ext_adv_cb_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P111_bt_le_oob_sc_data_结构体.md) · [返回大纲](大纲.md) · [下一章](P113_bt_le_per_adv_param_结构体.md)
