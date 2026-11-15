---
id: learning.zephyr-docs.bluetooth-classic-model-reference.page-61
title: bt_avrcp_register_notification_cmd_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__avrcp__register__notification__cmd.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第61章\_bt\_avrcp\_register\_notification\_cmd\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__avrcp__register__notification__cmd.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

注册通知（RegisterNotification）命令请求。

```c
#include <zephyr/bluetooth/classic/avrcp.h>
```

<a id="details"></a>

注册通知（RegisterNotification）命令请求。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 61.1\_数据成员（Data Fields）

<a id="r_a631509c0abadf1f4f2bdf5a5c58f0b80"></a>

```c
uint8_t event_id
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[event_id](#a631509c0abadf1f4f2bdf5a5c58f0b80)。

要注册的事件 ID。

<a id="r_a3bc85acb4c0b45be4fc082890f9fa744"></a>

```c
uint32_t interval
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[interval](#a3bc85acb4c0b45be4fc082890f9fa744)。

播放间隔（Playback Interval），仅在 `event_id = 0x05` 时使用。

## 61.2\_详细说明（Detailed Documentation）

<a id="a631509c0abadf1f4f2bdf5a5c58f0b80"></a>

### `event_id`

```c
uint8_t bt_avrcp_register_notification_cmd::event_id
```

要注册的事件 ID。

<a id="a3bc85acb4c0b45be4fc082890f9fa744"></a>

### `interval`

```c
uint32_t bt_avrcp_register_notification_cmd::interval
```

播放间隔（Playback Interval），仅在 `event_id = 0x05` 时使用。

本结构体文档由以下文件生成：

- `zephyr/bluetooth/classic/avrcp.h`

## 61.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/classic/avrcp.h](https://docs.zephyrproject.org/latest/doxygen/html/avrcp_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P060_bt_avrcp_play_item_rsp_结构体.md) · [返回大纲](大纲.md) · [下一章](P062_bt_avrcp_search_cmd_结构体.md)
