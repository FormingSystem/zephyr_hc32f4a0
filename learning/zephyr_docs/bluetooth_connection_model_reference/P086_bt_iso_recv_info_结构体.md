---
id: learning.zephyr-docs.bluetooth-connection-model-reference.page-86
title: bt_iso_recv_info_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__iso__recv__info.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第86章\_bt\_iso\_recv\_info\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__iso__recv__info.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

接收等时数据包（ISO Packet）的元数据结构。

```c
#include <zephyr/bluetooth/iso.h>
```

<a id="details"></a>

接收等时数据包（ISO Packet）的元数据结构。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 86.1\_数据成员（Data Fields）

<a id="r_a4bf778ae9be39eb4a740c2eb9670d98a"></a>

```c
uint32_t ts
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[ts](#a4bf778ae9be39eb4a740c2eb9670d98a)。

等时时间戳（ISO timestamp）。

<a id="r_a7c5b950df0359bb561140d0c2726fae6"></a>

```c
uint16_t seq_num
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[seq_num](#a7c5b950df0359bb561140d0c2726fae6)。

服务数据单元（SDU）第一个片段的等时数据包序列号（ISO packet sequence number）。

<a id="r_a0a7842fcb3251ed89b99fde43ba235a5"></a>

```c
uint8_t flags
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[flags](#a0a7842fcb3251ed89b99fde43ba235a5)。

等时数据包标志位域（ISO packet flags bitfield），使用 `BT_ISO_FLAGS_*`。

## 86.2\_详细说明（Detailed Documentation）

<a id="a0a7842fcb3251ed89b99fde43ba235a5"></a>

### `flags`

```c
uint8_t bt_iso_recv_info::flags
```

等时数据包标志位域（ISO packet flags bitfield），使用 `BT_ISO_FLAGS_*`。

<a id="a7c5b950df0359bb561140d0c2726fae6"></a>

### `seq_num`

```c
uint16_t bt_iso_recv_info::seq_num
```

服务数据单元（SDU）第一个片段的等时数据包序列号（ISO packet sequence number）。

<a id="a4bf778ae9be39eb4a740c2eb9670d98a"></a>

### `ts`

```c
uint32_t bt_iso_recv_info::ts
```

等时时间戳（ISO timestamp）。

仅当 `flags` 中设置了 `BT_ISO_FLAGS_TS` 位时有效。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/iso.h`

## 86.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/iso.h](https://docs.zephyrproject.org/latest/doxygen/html/iso_8h_source.html)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [BT_ISO_FLAGS_TS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#gga2c62af103a71aa8f5f8aa103b1245866a96f645c1c14593370fd6e0443b019a23)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P085_bt_iso_info_结构体.md) · [返回大纲](大纲.md) · [下一章](P087_bt_iso_server_结构体.md)
