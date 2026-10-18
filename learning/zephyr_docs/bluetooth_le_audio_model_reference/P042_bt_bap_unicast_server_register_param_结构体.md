---
id: learning.zephyr-docs.bluetooth-le-audio-model-reference.page-42
title: bt_bap_unicast_server_register_param_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__bap__unicast__server__register__param.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第42章\_bt\_bap\_unicast\_server\_register\_param\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__bap__unicast__server__register__param.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

用于注册单播服务器的结构体。

```c
#include <zephyr/bluetooth/audio/bap.h>
```

<a id="details"></a>

用于注册单播服务器的结构体。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 42.1\_数据成员（Data Fields）

<a id="r_a88635d5926173f23f411402b5961f783"></a>

```c
uint8_t snk_cnt
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[snk_cnt](#a88635d5926173f23f411402b5961f783)。

要注册的接收端（Sink）数量。

<a id="r_ab4963c035d75404831ec1293c7f40f95"></a>

```c
uint8_t src_cnt
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[src_cnt](#ab4963c035d75404831ec1293c7f40f95)。

要注册的发送源（Source）数量。

## 42.2\_详细说明（Detailed Documentation）

<a id="a88635d5926173f23f411402b5961f783"></a>

### `snk_cnt`

```c
uint8_t bt_bap_unicast_server_register_param::snk_cnt
```

要注册的接收端（Sink）数量。

应在 0 到 `CONFIG_BT_ASCS_MAX_ASE_SNK_COUNT` 范围内。

<a id="ab4963c035d75404831ec1293c7f40f95"></a>

### `src_cnt`

```c
uint8_t bt_bap_unicast_server_register_param::src_cnt
```

要注册的发送源（Source）数量。

应在 0 到 `CONFIG_BT_ASCS_MAX_ASE_SRC_COUNT` 范围内。

本结构体文档由以下文件生成：

- `zephyr/bluetooth/audio/bap.h`

## 42.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/audio/bap.h](https://docs.zephyrproject.org/latest/doxygen/html/bap_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [CONFIG_BT_ASCS_MAX_ASE_SNK_COUNT](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_ASCS_MAX_ASE_SNK_COUNT)
- [CONFIG_BT_ASCS_MAX_ASE_SRC_COUNT](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_ASCS_MAX_ASE_SRC_COUNT)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P041_bt_bap_unicast_server_cb_结构体.md) · [返回大纲](大纲.md)
