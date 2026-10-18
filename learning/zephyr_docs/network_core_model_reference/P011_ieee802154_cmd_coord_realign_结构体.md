---
id: learning.zephyr-docs.network-core-model-reference.page-11
title: ieee802154_cmd_coord_realign_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structieee802154__cmd__coord__realign.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第11章\_ieee802154\_cmd\_coord\_realign\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structieee802154__cmd__coord__realign.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

协调器重对齐（Coordinator Realignment）命令的载荷。

```c
#include <zephyr/net/ieee802154_frame.h>
```

<a id="details"></a>

协调器重对齐（Coordinator Realignment）命令的载荷。见第7.5.10节及图7-31。按标准规定，信道页（Channel Page）可选。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 11.1\_数据成员（Data Fields）

<a id="r_a9823ca16d8b99bb17583f402050aa80c"></a>

```c
uint16_t pan_id
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[pan_id](#a9823ca16d8b99bb17583f402050aa80c)。

个人区域网标识（PAN Identifier）。

<a id="r_a07775fefaf0f87425beb6371bd112b26"></a>

```c
uint16_t coordinator_short_addr
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[coordinator_short_addr](#a07775fefaf0f87425beb6371bd112b26)。

协调器短地址（Coordinator Short Address）。

<a id="r_a6f91305584cf44c910a95cf93e73c84d"></a>

```c
uint8_t channel
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[channel](#a6f91305584cf44c910a95cf93e73c84d)。

逻辑信道（Logical Channel）。

<a id="r_ae8867213cecfe3342dd951b1e03bde2d"></a>

```c
uint16_t short_addr
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[short_addr](#ae8867213cecfe3342dd951b1e03bde2d)。

此命令所寻址设备的短地址（Short Address）。

<a id="r_a0602708c2dc512c12f2901d84d090f30"></a>

```c
uint8_t channel_page
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[channel_page](#a0602708c2dc512c12f2901d84d090f30)。

信道页（Channel Page），为信道规格中可选的第四个八位组。

## 11.2\_详细说明（Detailed Documentation）

<a id="a6f91305584cf44c910a95cf93e73c84d"></a>

### `channel`

```c
uint8_t ieee802154_cmd_coord_realign::channel
```

逻辑信道（Logical Channel）。

<a id="a0602708c2dc512c12f2901d84d090f30"></a>

### `channel_page`

```c
uint8_t ieee802154_cmd_coord_realign::channel_page
```

信道页（Channel Page），为信道规格中可选的第四个八位组。

<a id="a07775fefaf0f87425beb6371bd112b26"></a>

### `coordinator_short_addr`

```c
uint16_t ieee802154_cmd_coord_realign::coordinator_short_addr
```

协调器短地址（Coordinator Short Address）。

<a id="a9823ca16d8b99bb17583f402050aa80c"></a>

### `pan_id`

```c
uint16_t ieee802154_cmd_coord_realign::pan_id
```

个人区域网标识（PAN Identifier）。

<a id="ae8867213cecfe3342dd951b1e03bde2d"></a>

### `short_addr`

```c
uint16_t ieee802154_cmd_coord_realign::short_addr
```

此命令所寻址设备的短地址（Short Address）。

本数据类型文档由以下文件生成：

- `zephyr/net/ieee802154_frame.h`

## 11.3\_原页交叉引用（Cross References）

- [zephyr/net/ieee802154_frame.h](https://docs.zephyrproject.org/latest/doxygen/html/ieee802154__frame_8h_source.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P010_ieee802154_cmd_assoc_res_结构体.md) · [返回大纲](大纲.md) · [下一章](P012_ieee802154_cmd_disassoc_note_结构体.md)
