---
id: learning.zephyr-docs.bluetooth-service-model-reference.page-120
title: bt_micp_included_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__micp__included.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第120章\_bt\_micp\_included\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__micp__included.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

麦克风控制配置文件（Microphone Control Profile）包含的服务。

```c
#include <zephyr/bluetooth/audio/micp.h>
```

<a id="details"></a>

麦克风控制规范（Microphone Control Profile）包含的服务。用于表示麦克风控制器（Microphone Controller）或麦克风设备（Microphone Device）的麦克风控制规范所包含的服务实例。实例指针可以表示本地服务实例，也可以表示远端服务实例。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 120.1\_数据成员（Data Fields）

<a id="r_a32cff1b68d96319958eeba66f249cd67"></a>

```c
uint8_t aics_cnt
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[aics_cnt](#a32cff1b68d96319958eeba66f249cd67)。

音频输入控制服务（Audio Input Control Service，AICS）实例的数量。

<a id="r_a2afddd15bd726039682151038b2415d1"></a>

```c
struct bt_aics ** aics
```

相关声明：[bt_aics](../bluetooth_le_audio_model_reference/P001_bt_aics_结构体.md)、[aics](#a2afddd15bd726039682151038b2415d1)。

指向音频输入控制服务（AICS）实例的指针数组。

## 120.2\_详细说明（Detailed Documentation）

<a id="a2afddd15bd726039682151038b2415d1"></a>

### `aics`

```c
struct bt_aics** bt_micp_included::aics
```

指向音频输入控制服务（AICS）实例的指针数组。

<a id="a32cff1b68d96319958eeba66f249cd67"></a>

### `aics_cnt`

```c
uint8_t bt_micp_included::aics_cnt
```

音频输入控制服务（Audio Input Control Service，AICS）实例的数量。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/audio/micp.h`

## 120.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/audio/micp.h](https://docs.zephyrproject.org/latest/doxygen/html/micp_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bt_aics](../bluetooth_le_audio_model_reference/P001_bt_aics_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P119_bt_mcc_cb_结构体.md) · [返回大纲](大纲.md) · [下一章](P121_bt_micp_mic_ctlr_结构体.md)
