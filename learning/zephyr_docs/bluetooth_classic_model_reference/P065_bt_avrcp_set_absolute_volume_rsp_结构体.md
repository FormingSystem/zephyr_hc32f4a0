---
id: learning.zephyr-docs.bluetooth-classic-model-reference.page-65
title: bt_avrcp_set_absolute_volume_rsp_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__avrcp__set__absolute__volume__rsp.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第65章\_bt\_avrcp\_set\_absolute\_volume\_rsp\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__avrcp__set__absolute__volume__rsp.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

设置绝对音量（SetAbsoluteVolume）响应。

```c
#include <zephyr/bluetooth/classic/avrcp.h>
```

<a id="details"></a>

设置绝对音量（SetAbsoluteVolume）响应。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 65.1\_数据成员（Data Fields）

<a id="r_ae542d562193e9b42e14b04b7a91f1500"></a>

```c
uint8_t absolute_volume
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[absolute_volume](#ae542d562193e9b42e14b04b7a91f1500)。

已确认的音量等级。

## 65.2\_详细说明（Detailed Documentation）

<a id="ae542d562193e9b42e14b04b7a91f1500"></a>

### `absolute_volume`

```c
uint8_t bt_avrcp_set_absolute_volume_rsp::absolute_volume
```

已确认的音量等级。

本结构体文档由以下文件生成：

- `zephyr/bluetooth/classic/avrcp.h`

## 65.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/classic/avrcp.h](https://docs.zephyrproject.org/latest/doxygen/html/avrcp_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P064_bt_avrcp_set_absolute_volume_cmd_结构体.md) · [返回大纲](大纲.md) · [下一章](P066_bt_avrcp_set_addressed_player_cmd_结构体.md)
