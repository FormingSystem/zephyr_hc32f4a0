---
id: learning.zephyr-docs.bluetooth-le-audio-model-reference.page-6
title: bt_ascs_register_param_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__ascs__register__param.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第6章\_bt\_ascs\_register\_param\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__ascs__register__param.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

注册音频流控制服务（Audio Stream Control Service，ASCS）的参数。

```c
#include <zephyr/bluetooth/audio/ascs.h>
```

<a id="details"></a>

注册音频流控制服务（Audio Stream Control Service，ASCS）的参数。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 6.1\_数据成员（Data Fields）

<a id="r_a04839e2149a25e801905fff837b7ab59"></a>

```c
uint8_t snk_cnt
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[snk_cnt](#a04839e2149a25e801905fff837b7ab59)。

要注册的接收端（Sink）数量。

<a id="r_ad830e2991175f5e86fd8be34692e7af5"></a>

```c
uint8_t src_cnt
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[src_cnt](#ad830e2991175f5e86fd8be34692e7af5)。

要注册的发送源（Source）数量。

<a id="r_a9607646e7f44a39fa589b13d2bcaa9bb"></a>

```c
const struct bt_ascs_cb * cb
```

相关声明：[bt_ascs_cb](P005_bt_ascs_cb_结构体.md)、[cb](#a9607646e7f44a39fa589b13d2bcaa9bb)。

回调结构体（Callback Structure）。

## 6.2\_详细说明（Detailed Documentation）

<a id="a9607646e7f44a39fa589b13d2bcaa9bb"></a>

### `cb`

```c
const struct bt_ascs_cb* bt_ascs_register_param::cb
```

回调结构体（Callback Structure）。

<a id="a04839e2149a25e801905fff837b7ab59"></a>

### `snk_cnt`

```c
uint8_t bt_ascs_register_param::snk_cnt
```

要注册的接收端（Sink）数量。

应在 0 到 `CONFIG_BT_ASCS_MAX_ASE_SNK_COUNT` 范围内。

<a id="ad830e2991175f5e86fd8be34692e7af5"></a>

### `src_cnt`

```c
uint8_t bt_ascs_register_param::src_cnt
```

要注册的发送源（Source）数量。

应在 0 到 `CONFIG_BT_ASCS_MAX_ASE_SRC_COUNT` 范围内。

本结构体文档由以下文件生成：

- `zephyr/bluetooth/audio/ascs.h`

## 6.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/audio/ascs.h](https://docs.zephyrproject.org/latest/doxygen/html/ascs_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bt_ascs_cb](P005_bt_ascs_cb_结构体.md)
- [CONFIG_BT_ASCS_MAX_ASE_SNK_COUNT](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_ASCS_MAX_ASE_SNK_COUNT)
- [CONFIG_BT_ASCS_MAX_ASE_SRC_COUNT](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_ASCS_MAX_ASE_SRC_COUNT)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P005_bt_ascs_cb_结构体.md) · [返回大纲](大纲.md) · [下一章](P007_bt_audio_codec_cap_结构体.md)
