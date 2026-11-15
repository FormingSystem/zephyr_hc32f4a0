---
id: learning.zephyr-docs.bluetooth-service-model-reference.page-179
title: bt_vcp_included_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__vcp__included.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第179章\_bt\_vcp\_included\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__vcp__included.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

音量控制服务（Volume Control Service）包含的服务。

```c
#include <zephyr/bluetooth/audio/vcp.h>
```

<a id="details"></a>

音量控制服务（Volume Control Service）包含的服务。用于表示客户端或服务器的音量控制服务所包含的服务实例。实例指针可以表示本地服务器实例，也可以表示远端服务实例。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 179.1\_数据成员（Data Fields）

<a id="r_acb0c8e853808adfd9c3b92b45e874103"></a>

```c
uint8_t vocs_cnt
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[vocs_cnt](#acb0c8e853808adfd9c3b92b45e874103)。

音量偏移控制服务（Volume Offset Control Service，VOCS）实例数量。

<a id="r_a1f04068dd88d2fecef5fd78a3c7d4429"></a>

```c
struct bt_vocs ** vocs
```

相关声明：[bt_vocs](P184_bt_vocs_结构体.md)、[vocs](#a1f04068dd88d2fecef5fd78a3c7d4429)。

指向音量偏移控制服务（VOCS）实例的指针数组。

<a id="r_af521bb12ebef4c5f60609040140474c0"></a>

```c
uint8_t aics_cnt
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[aics_cnt](#af521bb12ebef4c5f60609040140474c0)。

音频输入控制服务（Audio Input Control Service，AICS）实例的数量。

<a id="r_aa6c87b8c9b4b2be6ec6429fd2ee68398"></a>

```c
struct bt_aics ** aics
```

相关声明：[bt_aics](../bluetooth_le_audio_model_reference/P001_bt_aics_结构体.md)、[aics](#aa6c87b8c9b4b2be6ec6429fd2ee68398)。

指向音频输入控制服务（AICS）实例的指针数组。

## 179.2\_详细说明（Detailed Documentation）

<a id="aa6c87b8c9b4b2be6ec6429fd2ee68398"></a>

### `aics`

```c
struct bt_aics** bt_vcp_included::aics
```

指向音频输入控制服务（AICS）实例的指针数组。

<a id="af521bb12ebef4c5f60609040140474c0"></a>

### `aics_cnt`

```c
uint8_t bt_vcp_included::aics_cnt
```

音频输入控制服务（Audio Input Control Service，AICS）实例的数量。

<a id="a1f04068dd88d2fecef5fd78a3c7d4429"></a>

### `vocs`

```c
struct bt_vocs** bt_vcp_included::vocs
```

指向音量偏移控制服务（VOCS）实例的指针数组。

<a id="acb0c8e853808adfd9c3b92b45e874103"></a>

### `vocs_cnt`

```c
uint8_t bt_vcp_included::vocs_cnt
```

音量偏移控制服务（Volume Offset Control Service，VOCS）实例数量。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/audio/vcp.h`

## 179.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/audio/vcp.h](https://docs.zephyrproject.org/latest/doxygen/html/vcp_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bt_vocs](P184_bt_vocs_结构体.md)
- [bt_aics](../bluetooth_le_audio_model_reference/P001_bt_aics_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P178_bt_tmap_cb_结构体.md) · [返回大纲](大纲.md) · [下一章](P180_bt_vcp_vol_ctlr_结构体.md)
