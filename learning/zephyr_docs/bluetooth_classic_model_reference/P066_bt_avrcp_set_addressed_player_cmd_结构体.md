---
id: learning.zephyr-docs.bluetooth-classic-model-reference.page-66
title: bt_avrcp_set_addressed_player_cmd_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__avrcp__set__addressed__player__cmd.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第66章\_bt\_avrcp\_set\_addressed\_player\_cmd\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__avrcp__set__addressed__player__cmd.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

设置受控播放器（SetAddressedPlayer）命令请求。

```c
#include <zephyr/bluetooth/classic/avrcp.h>
```

<a id="details"></a>

设置受控播放器（SetAddressedPlayer）命令请求。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 66.1\_数据成员（Data Fields）

<a id="r_a0cb667cb10375fcd16570fd3fbda20d7"></a>

```c
uint16_t player_id
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[player_id](#a0cb667cb10375fcd16570fd3fbda20d7)。

要设为受控播放器（Addressed Player）的播放器 ID。

## 66.2\_详细说明（Detailed Documentation）

<a id="a0cb667cb10375fcd16570fd3fbda20d7"></a>

### `player_id`

```c
uint16_t bt_avrcp_set_addressed_player_cmd::player_id
```

要设为受控播放器（Addressed Player）的播放器 ID。

本结构体文档由以下文件生成：

- `zephyr/bluetooth/classic/avrcp.h`

## 66.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/classic/avrcp.h](https://docs.zephyrproject.org/latest/doxygen/html/avrcp_8h_source.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P065_bt_avrcp_set_absolute_volume_rsp_结构体.md) · [返回大纲](大纲.md) · [下一章](P067_bt_avrcp_set_browsed_player_rsp_结构体.md)
