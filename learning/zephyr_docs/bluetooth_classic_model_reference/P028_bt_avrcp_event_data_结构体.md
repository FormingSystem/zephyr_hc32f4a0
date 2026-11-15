---
id: learning.zephyr-docs.bluetooth-classic-model-reference.page-28
title: bt_avrcp_event_data_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__avrcp__event__data.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第28章\_bt\_avrcp\_event\_data\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__avrcp__event__data.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/classic/avrcp.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 28.1\_数据成员（Data Fields）

```c
union {
```

<a id="r_a3bb4d1bdcae7fa52ce13ebab08433211"></a>

```c
uint8_t play_status
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[play_status](#aed5c7ed3f0a1cc935544cf12ee0dcda9)。

<a id="r_aaf4058b92a1d218fadd47492c4e6698e"></a>

```c
uint8_t identifier [8]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[identifier](#a4aae90303b04cab680045b88a636e22a)。

<a id="r_ae8d950e34fe19480a0c4872e1321965d"></a>

```c
uint32_t playback_pos
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[playback_pos](#adf71db04b3c1821ceafe0e1071af5c38)。

<a id="r_aa6a657a96b6da2fd2760a14e7982220d"></a>

```c
uint8_t battery_status
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[battery_status](#ae47d1a2379088e929bfb44df7c172511)。

<a id="r_af207765e00d8281f14c0ac008ecb5b25"></a>

```c
uint8_t system_status
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[system_status](#a5eeea0ad88794d23965a83e68c93015f)。

```c
struct {
```

<a id="r_a46dc0e1e01049e0da03b8e94a88b14a5"></a>

```c
uint8_t num_of_attr
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[num_of_attr](#a77e7bb507e86be528ad40cbae329c7fc)。

<a id="r_a63652a67fba46b3a06bfa6fcd2d57a9d"></a>

```c
struct bt_avrcp_app_setting_attr_val * attr_vals
```

相关声明：[bt_avrcp_app_setting_attr_val](P018_bt_avrcp_app_setting_attr_val_结构体.md)、[attr_vals](#ae7f5a7e755f7dfd6d1d962e9df5ca716)。

<a id="r_a1802147c2c17ae7dc043d7cc54790858"></a>

```c
} setting_changed
```

相关声明：[setting_changed](#ad23631ca5ca2dd4dd33ba3b76f281c44)。

```c
struct {
```

<a id="r_a65c94717a25009c833403477f7f8f4aa"></a>

```c
uint16_t player_id
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[player_id](#ae5a21b8f540b69791b65e2ec565c876e)。

<a id="r_abb04b386d026461b7be4e07b0f527a40"></a>

```c
uint16_t uid_counter
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[uid_counter](#a9c650742790ded89f1a9c583a22b7895)。

<a id="r_a3e2d28ee7b2d234d202db6c9f986e08d"></a>

```c
} addressed_player_changed
```

相关声明：[addressed_player_changed](#a5471d42d0e9a589690304811028931c4)。

<a id="r_a6862ce6263362b2271e04174460ef6af"></a>

```c
uint16_t uid_counter
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[uid_counter](#a9c650742790ded89f1a9c583a22b7895)。

<a id="r_a0bd5fe8d2b164d169ef4b1f8e515c596"></a>

```c
uint8_t absolute_volume
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[absolute_volume](#af8aadd59a58de168cba94cdfa22549db)。

<a id="r_ae2fdf22273fe0af5cf2f3be5ca120b5f"></a>

```c
};
```

## 28.2\_详细说明（Detailed Documentation）

<a id="ae2fdf22273fe0af5cf2f3be5ca120b5f"></a>

### `[union]`

```c
union { ... } bt_avrcp_event_data
```

<a id="af8aadd59a58de168cba94cdfa22549db"></a>

### `absolute_volume`

```c
uint8_t bt_avrcp_event_data::absolute_volume
```

<a id="a5471d42d0e9a589690304811028931c4"></a>

### `[struct]`

```c
struct { ... } bt_avrcp_event_data::addressed_player_changed
```

<a id="ae7f5a7e755f7dfd6d1d962e9df5ca716"></a>

### `attr_vals`

```c
struct bt_avrcp_app_setting_attr_val* bt_avrcp_event_data::attr_vals
```

<a id="ae47d1a2379088e929bfb44df7c172511"></a>

### `battery_status`

```c
uint8_t bt_avrcp_event_data::battery_status
```

<a id="a4aae90303b04cab680045b88a636e22a"></a>

### `identifier`

```c
uint8_t bt_avrcp_event_data::identifier[8]
```

<a id="a77e7bb507e86be528ad40cbae329c7fc"></a>

### `num_of_attr`

```c
uint8_t bt_avrcp_event_data::num_of_attr
```

<a id="aed5c7ed3f0a1cc935544cf12ee0dcda9"></a>

### `play_status`

```c
uint8_t bt_avrcp_event_data::play_status
```

<a id="adf71db04b3c1821ceafe0e1071af5c38"></a>

### `playback_pos`

```c
uint32_t bt_avrcp_event_data::playback_pos
```

<a id="ae5a21b8f540b69791b65e2ec565c876e"></a>

### `player_id`

```c
uint16_t bt_avrcp_event_data::player_id
```

<a id="ad23631ca5ca2dd4dd33ba3b76f281c44"></a>

### `[struct]`

```c
struct { ... } bt_avrcp_event_data::setting_changed
```

<a id="a5eeea0ad88794d23965a83e68c93015f"></a>

### `system_status`

```c
uint8_t bt_avrcp_event_data::system_status
```

<a id="a9c650742790ded89f1a9c583a22b7895"></a>

### `uid_counter`

```c
uint16_t bt_avrcp_event_data::uid_counter
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/classic/avrcp.h`

## 28.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/classic/avrcp.h](https://docs.zephyrproject.org/latest/doxygen/html/avrcp_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [bt_avrcp_app_setting_attr_val](P018_bt_avrcp_app_setting_attr_val_结构体.md)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [bt_avrcp_event_data](P028_bt_avrcp_event_data_结构体.md)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P027_bt_avrcp_ct_cb_结构体.md) · [返回大纲](大纲.md) · [下一章](P029_bt_avrcp_folder_item_结构体.md)
