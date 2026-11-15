---
id: learning.zephyr-docs.bluetooth-connection-model-reference.page-107
title: bt_le_ext_adv_sent_info_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__le__ext__adv__sent__info.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第107章\_bt\_le\_ext\_adv\_sent\_info\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__le__ext__adv__sent__info.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

广播发送事件（Advertising Sent Event）的信息。

```c
#include <zephyr/bluetooth/bluetooth.h>
```

<a id="details"></a>

广播发送事件信息（Advertising sent event information）。注意（Note）：用于 `bt_le_ext_adv_cb`。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 107.1\_数据成员（Data Fields）

<a id="r_a80f661efd35b069c2f8700851e9429a2"></a>

```c
uint8_t num_sent
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[num_sent](#a80f661efd35b069c2f8700851e9429a2)。

若广播集启动时指定了非零的 `bt_le_ext_adv_start_param::num_events`，此字段包含广播集从启用以来已发送的次数。

## 107.2\_详细说明（Detailed Documentation）

<a id="a80f661efd35b069c2f8700851e9429a2"></a>

### `num_sent`

```c
uint8_t bt_le_ext_adv_sent_info::num_sent
```

若广播集启动时指定了非零的 `bt_le_ext_adv_start_param::num_events`，此字段包含广播集从启用以来已发送的次数。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/bluetooth.h`

## 107.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/bluetooth.h](https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2bluetooth_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bt_le_ext_adv_start_param::num_events](P108_bt_le_ext_adv_start_param_结构体.md#ab45ae0bfdb144071efcc64c30648388f)
- [bt_le_ext_adv_cb](P103_bt_le_ext_adv_cb_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P106_bt_le_ext_adv_scanned_info_结构体.md) · [返回大纲](大纲.md) · [下一章](P108_bt_le_ext_adv_start_param_结构体.md)
