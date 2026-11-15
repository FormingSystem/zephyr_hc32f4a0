---
id: learning.zephyr-docs.audio-video-model-reference.page-38
title: mpl_cmd_ntf_结构体
kind: reference
status: maintained
domains: [zephyr, multimedia, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structmpl__cmd__ntf.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第38章\_mpl\_cmd\_ntf\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structmpl__cmd__ntf.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

媒体命令通知（Media Command Notification）。

```c
#include <zephyr/bluetooth/audio/media_proxy.h>
```

<a id="details"></a>

媒体命令通知（Media Command Notification）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 38.1\_数据成员（Data Fields）

<a id="r_adcd5228cef8b7629d54053b155a91aa7"></a>

```c
uint8_t requested_opcode
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[requested_opcode](#adcd5228cef8b7629d54053b155a91aa7)。

已发送的操作码。

<a id="r_a776bd9459d320e609697905067c0b284"></a>

```c
uint8_t result_code
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[result_code](#a776bd9459d320e609697905067c0b284)。

操作结果。

## 38.2\_详细说明（Detailed Documentation）

<a id="adcd5228cef8b7629d54053b155a91aa7"></a>

### `requested_opcode`

```c
uint8_t mpl_cmd_ntf::requested_opcode
```

已发送的操作码。

<a id="a776bd9459d320e609697905067c0b284"></a>

### `result_code`

```c
uint8_t mpl_cmd_ntf::result_code
```

操作结果。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/audio/media_proxy.h`

## 38.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/audio/media_proxy.h](https://docs.zephyrproject.org/latest/doxygen/html/media__proxy_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P037_mpl_cmd_结构体.md) · [返回大纲](大纲.md) · [下一章](P039_mpl_sci_结构体.md)
