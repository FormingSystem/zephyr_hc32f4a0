---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-446
title: bt_hci_vs_codecs_v2_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__vs__codecs__v2.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第446章\_bt\_hci\_vs\_codecs\_v2\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__vs__codecs__v2.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 446.1\_数据成员（Data Fields）

<a id="r_ae4cb3a40401594f8e0f18391b9d31a23"></a>

```c
uint8_t num_codecs
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[num_codecs](#ae4cb3a40401594f8e0f18391b9d31a23)。

<a id="r_a6cd8aa58517d59d565474513f755cfee"></a>

```c
struct bt_hci_vs_codec_info_v2 codec_info [0]
```

相关声明：[bt_hci_vs_codec_info_v2](P444_bt_hci_vs_codec_info_v2_结构体.md)、[codec_info](#a6cd8aa58517d59d565474513f755cfee)。

## 446.2\_详细说明（Detailed Documentation）

<a id="a6cd8aa58517d59d565474513f755cfee"></a>

### `codec_info`

```c
struct bt_hci_vs_codec_info_v2 bt_hci_vs_codecs_v2::codec_info[0]
```

<a id="ae4cb3a40401594f8e0f18391b9d31a23"></a>

### `num_codecs`

```c
uint8_t bt_hci_vs_codecs_v2::num_codecs
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 446.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bt_hci_vs_codec_info_v2](P444_bt_hci_vs_codec_info_v2_结构体.md)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P445_bt_hci_vs_codecs_结构体.md) · [返回大纲](大纲.md) · [下一章](P447_bt_hci_vs_fatal_error_cpu_data_cortex_m_结构体.md)
