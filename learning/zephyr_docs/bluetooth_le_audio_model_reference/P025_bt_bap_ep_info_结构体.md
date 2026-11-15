---
id: learning.zephyr-docs.bluetooth-le-audio-model-reference.page-25
title: bt_bap_ep_info_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__bap__ep__info.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第25章\_bt\_bap\_ep\_info\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__bap__ep__info.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

保存音频流端点信息的结构体。

```c
#include <zephyr/bluetooth/audio/bap.h>
```

<a id="details"></a>

保存音频流端点信息的结构体。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 25.1\_数据成员（Data Fields）

<a id="r_a07e8878e7e6a8ee059639330ffa78c1c"></a>

```c
uint8_t id
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[id](#a07e8878e7e6a8ee059639330ffa78c1c)。

端点 ID。

<a id="r_a650727747d0a093528544c3e16255feb"></a>

```c
enum bt_bap_ep_state state
```

相关声明：[bt_bap_ep_state](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#gaf210a91e1ff11d9bf7792ba47d1e1b4a)、[state](#a650727747d0a093528544c3e16255feb)。

端点状态（Endpoint State）。

<a id="r_abb0dc6d25744cd734f8fd6ba2bc84b24"></a>

```c
enum bt_audio_dir dir
```

相关声明：[bt_audio_dir](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio.html#ga5bd899fb5e4d844058184913866e462f)、[dir](#abb0dc6d25744cd734f8fd6ba2bc84b24)。

能力类型（Capabilities Type）。

<a id="r_a54dd673e21455c85193df844f3aa4083"></a>

```c
struct bt_iso_chan * iso_chan
```

相关声明：[bt_iso_chan](https://docs.zephyrproject.org/latest/doxygen/html/structbt__iso__chan.html)、[iso_chan](#a54dd673e21455c85193df844f3aa4083)。

与端点关联的等时通道（Isochronous Channel）。

<a id="r_abbad124bf9e40ed530b2a33fefbadc84"></a>

```c
bool can_send
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[can_send](#abbad124bf9e40ed530b2a33fefbadc84)。

与端点关联的流能够发送数据时为 `true`。

<a id="r_a30698c71f556ca876a1c69bffefac653"></a>

```c
bool can_recv
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[can_recv](#a30698c71f556ca876a1c69bffefac653)。

与端点关联的流能够接收数据时为 `true`。

<a id="r_a819ac77dcf7cb6985e97f290a666ed09"></a>

```c
struct bt_bap_ep * paired_ep
```

相关声明：[bt_bap_ep](P024_bt_bap_ep_结构体.md)、[paired_ep](#a819ac77dcf7cb6985e97f290a666ed09)。

如果端点属于双向连接等时流（Connected Isochronous Stream，CIS），则为指向配对端点的指针；否则为 `NULL`。

<a id="r_ad5201e9b9623e8ff8e74e1be87ece864"></a>

```c
const struct bt_bap_qos_cfg_pref * qos_pref
```

相关声明：[bt_bap_qos_cfg_pref](P028_bt_bap_qos_cfg_pref_结构体.md)、[qos_pref](#ad5201e9b9623e8ff8e74e1be87ece864)。

指向与端点关联的首选 QoS 设置的指针。

## 25.2\_详细说明（Detailed Documentation）

<a id="a30698c71f556ca876a1c69bffefac653"></a>

### `can_recv`

```c
bool bt_bap_ep_info::can_recv
```

与端点关联的流能够接收数据时为 `true`。

<a id="abbad124bf9e40ed530b2a33fefbadc84"></a>

### `can_send`

```c
bool bt_bap_ep_info::can_send
```

与端点关联的流能够发送数据时为 `true`。

<a id="abb0dc6d25744cd734f8fd6ba2bc84b24"></a>

### `dir`

```c
enum bt_audio_dir bt_bap_ep_info::dir
```

能力类型（Capabilities Type）。

<a id="a07e8878e7e6a8ee059639330ffa78c1c"></a>

### `id`

```c
uint8_t bt_bap_ep_info::id
```

端点 ID。

<a id="a54dd673e21455c85193df844f3aa4083"></a>

### `iso_chan`

```c
struct bt_iso_chan* bt_bap_ep_info::iso_chan
```

与端点关联的等时通道（Isochronous Channel）。

<a id="a819ac77dcf7cb6985e97f290a666ed09"></a>

### `paired_ep`

```c
struct bt_bap_ep* bt_bap_ep_info::paired_ep
```

如果端点属于双向连接等时流（Connected Isochronous Stream，CIS），则为指向配对端点的指针；否则为 `NULL`。

<a id="ad5201e9b9623e8ff8e74e1be87ece864"></a>

### `qos_pref`

```c
const struct bt_bap_qos_cfg_pref* bt_bap_ep_info::qos_pref
```

指向与端点关联的首选 QoS 设置的指针。

<a id="a650727747d0a093528544c3e16255feb"></a>

### `state`

```c
enum bt_bap_ep_state bt_bap_ep_info::state
```

端点状态（Endpoint State）。

本结构体文档由以下文件生成：

- `zephyr/bluetooth/audio/bap.h`

## 25.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/audio/bap.h](https://docs.zephyrproject.org/latest/doxygen/html/bap_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bt_bap_ep_state](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#gaf210a91e1ff11d9bf7792ba47d1e1b4a)
- [bt_audio_dir](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio.html#ga5bd899fb5e4d844058184913866e462f)
- [bt_iso_chan](https://docs.zephyrproject.org/latest/doxygen/html/structbt__iso__chan.html)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)
- [bt_bap_ep](P024_bt_bap_ep_结构体.md)
- [bt_bap_qos_cfg_pref](P028_bt_bap_qos_cfg_pref_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P024_bt_bap_ep_结构体.md) · [返回大纲](大纲.md) · [下一章](P026_bt_bap_lc3_preset_结构体.md)
