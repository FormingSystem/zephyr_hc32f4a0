---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-11
title: bt_hci_cp_codec_id_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cp__codec__id.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第11章\_bt\_hci\_cp\_codec\_id\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cp__codec__id.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 11.1\_数据成员（Data Fields）

<a id="r_aec80c74b12edb9c63330cc5a404eed5d"></a>

```c
uint8_t coding_format
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[coding_format](#aec80c74b12edb9c63330cc5a404eed5d)。

<a id="r_a98fd438270a64d843fa27c7c196645df"></a>

```c
uint16_t company_id
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[company_id](#a98fd438270a64d843fa27c7c196645df)。

<a id="r_a70296440c202544af11db2dc8e80fc5b"></a>

```c
uint16_t vs_codec_id
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[vs_codec_id](#a70296440c202544af11db2dc8e80fc5b)。

## 11.2\_详细说明（Detailed Documentation）

<a id="aec80c74b12edb9c63330cc5a404eed5d"></a>

### `coding_format`

```c
uint8_t bt_hci_cp_codec_id::coding_format
```

<a id="a98fd438270a64d843fa27c7c196645df"></a>

### `company_id`

```c
uint16_t bt_hci_cp_codec_id::company_id
```

<a id="a70296440c202544af11db2dc8e80fc5b"></a>

### `vs_codec_id`

```c
uint16_t bt_hci_cp_codec_id::vs_codec_id
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 11.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P010_bt_hci_cp_change_conn_packet_type_结构体.md) · [返回大纲](大纲.md) · [下一章](P012_bt_hci_cp_configure_data_path_结构体.md)
