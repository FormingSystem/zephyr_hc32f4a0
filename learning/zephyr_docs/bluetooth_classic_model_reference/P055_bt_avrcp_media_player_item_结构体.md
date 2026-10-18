---
id: learning.zephyr-docs.bluetooth-classic-model-reference.page-55
title: bt_avrcp_media_player_item_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__avrcp__media__player__item.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第55章\_bt\_avrcp\_media\_player\_item\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__avrcp__media__player__item.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

媒体播放器条目（Media Player Item），`item_type=0x01`。

```c
#include <zephyr/bluetooth/classic/avrcp.h>
```

<a id="details"></a>

媒体播放器条目（Media Player Item），`item_type=0x01`。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 55.1\_数据成员（Data Fields）

<a id="r_a15488d00a442bc3cdfdf44c383bb6738"></a>

```c
struct bt_avrcp_item_hdr hdr
```

相关声明：[bt_avrcp_item_hdr](P049_bt_avrcp_item_hdr_结构体.md)、[hdr](#a15488d00a442bc3cdfdf44c383bb6738)。

<a id="r_a39c8b80e71c70d4cf84ecb25a03b4f8f"></a>

```c
uint16_t player_id
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[player_id](#a39c8b80e71c70d4cf84ecb25a03b4f8f)。

播放器 ID。

<a id="r_aeca27933a1892ac6c6b0951a4bf68370"></a>

```c
uint8_t major_type
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[major_type](#aeca27933a1892ac6c6b0951a4bf68370)。

播放器主类型（Major Player Type）。

<a id="r_a62c18bb03aed36dda87eff9599100dec"></a>

```c
uint32_t player_subtype
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[player_subtype](#a62c18bb03aed36dda87eff9599100dec)。

播放器子类型（Player Subtype）。

<a id="r_ac8571c557795c5fec5512c7868e34dfc"></a>

```c
uint8_t play_status
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[play_status](#ac8571c557795c5fec5512c7868e34dfc)。

播放状态（Play Status），类型为 `bt_avrcp_playback_status_t`。

<a id="r_ad3d1c3443f1a4d0b28623e0a3e1a6607"></a>

```c
uint8_t feature_bitmask [16]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[feature_bitmask](#ad3d1c3443f1a4d0b28623e0a3e1a6607)。

128 位功能位掩码（Feature Bitmask），对应八位字节 0–15。

<a id="r_afda406082181582f7fcf4b44d2f6fc8c"></a>

```c
uint16_t charset_id
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[charset_id](#afda406082181582f7fcf4b44d2f6fc8c)。

可显示名称的字符集，类型为 `bt_avrcp_charset_t`。

<a id="r_a02f71111fc2b4e4f53cd186aaf4372cf"></a>

```c
uint16_t name_len
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[name_len](#a02f71111fc2b4e4f53cd186aaf4372cf)。

可显示名称的长度。

<a id="r_a9e6f3f5621a76b8ab37c0833916dae69"></a>

```c
uint8_t name []
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[name](#a9e6f3f5621a76b8ab37c0833916dae69)。

可显示名称。

## 55.2\_详细说明（Detailed Documentation）

<a id="afda406082181582f7fcf4b44d2f6fc8c"></a>

### `charset_id`

```c
uint16_t bt_avrcp_media_player_item::charset_id
```

可显示名称的字符集，类型为 `bt_avrcp_charset_t`。

<a id="ad3d1c3443f1a4d0b28623e0a3e1a6607"></a>

### `feature_bitmask`

```c
uint8_t bt_avrcp_media_player_item::feature_bitmask[16]
```

128 位功能位掩码（Feature Bitmask），对应八位字节 0–15。

<a id="a15488d00a442bc3cdfdf44c383bb6738"></a>

### `hdr`

```c
struct bt_avrcp_item_hdr bt_avrcp_media_player_item::hdr
```

<a id="aeca27933a1892ac6c6b0951a4bf68370"></a>

### `major_type`

```c
uint8_t bt_avrcp_media_player_item::major_type
```

播放器主类型（Major Player Type）。

<a id="a9e6f3f5621a76b8ab37c0833916dae69"></a>

### `name`

```c
uint8_t bt_avrcp_media_player_item::name[]
```

可显示名称。

<a id="a02f71111fc2b4e4f53cd186aaf4372cf"></a>

### `name_len`

```c
uint16_t bt_avrcp_media_player_item::name_len
```

可显示名称的长度。

<a id="ac8571c557795c5fec5512c7868e34dfc"></a>

### `play_status`

```c
uint8_t bt_avrcp_media_player_item::play_status
```

播放状态（Play Status），类型为 `bt_avrcp_playback_status_t`。

<a id="a39c8b80e71c70d4cf84ecb25a03b4f8f"></a>

### `player_id`

```c
uint16_t bt_avrcp_media_player_item::player_id
```

播放器 ID。

<a id="a62c18bb03aed36dda87eff9599100dec"></a>

### `player_subtype`

```c
uint32_t bt_avrcp_media_player_item::player_subtype
```

播放器子类型（Player Subtype）。

本结构体文档由以下文件生成：

- `zephyr/bluetooth/classic/avrcp.h`

## 55.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/classic/avrcp.h](https://docs.zephyrproject.org/latest/doxygen/html/avrcp_8h_source.html)
- [bt_avrcp_item_hdr](P049_bt_avrcp_item_hdr_结构体.md)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [bt_avrcp_playback_status_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ga433775fa2758df43ee1d26c78e9122d1)
- [bt_avrcp_charset_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ga81330413af9eba049da6557b14ae082c)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P054_bt_avrcp_media_element_item_结构体.md) · [返回大纲](大纲.md) · [下一章](P056_bt_avrcp_passthrough_cmd_结构体.md)
