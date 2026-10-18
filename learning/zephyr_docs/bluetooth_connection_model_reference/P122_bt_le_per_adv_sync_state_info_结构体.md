---
id: learning.zephyr-docs.bluetooth-connection-model-reference.page-122
title: bt_le_per_adv_sync_state_info_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__le__per__adv__sync__state__info.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第122章\_bt\_le\_per\_adv\_sync\_state\_info\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__le__per__adv__sync__state__info.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

周期广播同步（Periodic Advertising Sync）状态的信息。

```c
#include <zephyr/bluetooth/bluetooth.h>
```

<a id="details"></a>

周期广播同步状态信息（Periodic advertising sync state information）。此结构提供当前周期广播同步的状态，指示是否启用了周期广播接收。通常通过 `bt_le_per_adv_sync_cb` 结构中的回调报告状态变化。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 122.1\_数据成员（Data Fields）

<a id="r_a4b0a3b7e36f935e06072304d6b92579f"></a>

```c
bool recv_enabled
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[recv_enabled](#a4b0a3b7e36f935e06072304d6b92579f)。

正在接收周期广播（Periodic advertisements）时为 `true`，否则为 `false`。

## 122.2\_详细说明（Detailed Documentation）

<a id="a4b0a3b7e36f935e06072304d6b92579f"></a>

### `recv_enabled`

```c
bool bt_le_per_adv_sync_state_info::recv_enabled
```

正在接收周期广播（Periodic advertisements）时为 `true`，否则为 `false`。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/bluetooth.h`

## 122.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/bluetooth.h](https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2bluetooth_8h_source.html)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)
- [bt_le_per_adv_sync_cb](P118_bt_le_per_adv_sync_cb_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P121_bt_le_per_adv_sync_recv_info_结构体.md) · [返回大纲](大纲.md) · [下一章](P123_bt_le_per_adv_sync_subevent_params_结构体.md)
