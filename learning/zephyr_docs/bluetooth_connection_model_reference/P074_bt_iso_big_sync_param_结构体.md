---
id: learning.zephyr-docs.bluetooth-connection-model-reference.page-74
title: bt_iso_big_sync_param_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__iso__big__sync__param.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第74章\_bt\_iso\_big\_sync\_param\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__iso__big__sync__param.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

广播等时组（Broadcast Isochronous Group，BIG）的同步参数。

```c
#include <zephyr/bluetooth/iso.h>
```

<a id="details"></a>

广播等时组（Broadcast Isochronous Group，BIG）的同步参数。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 74.1\_数据成员（Data Fields）

<a id="r_ac56d7206c3434837a52059716355adad"></a>

```c
struct bt_iso_chan ** bis_channels
```

相关声明：[bt_iso_chan](P077_bt_iso_chan_结构体.md)、[bis_channels](#ac56d7206c3434837a52059716355adad)。

广播等时流通道指针数组（BIS channel pointers）。

<a id="r_a96cd109e9f5820531635d48e88b4bff8"></a>

```c
uint8_t num_bis
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[num_bis](#a96cd109e9f5820531635d48e88b4bff8)。

`bis_channels` 中的通道数量（Number of channels）。

<a id="r_a14b03509daf760edbead86659f733136"></a>

```c
uint32_t bis_bitfield
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[bis_bitfield](#a14b03509daf760edbead86659f733136)。

要同步的广播等时流位域（BISes bitfield）。

<a id="r_a16b332b4a0f373cb21e5da6e6e383b9e"></a>

```c
uint32_t mse
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[mse](#a16b332b4a0f373cb21e5da6e6e383b9e)。

最大子事件数（Maximum subevents）。

<a id="r_a8e344870fc0e380e6588eb90c7ef72f9"></a>

```c
uint16_t sync_timeout
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[sync_timeout](#a8e344870fc0e380e6588eb90c7ef72f9)。

广播等时组（BIG）的同步超时（Synchronization timeout），为 N × 10 毫秒。

<a id="r_a8e5cffe8960477e7f64707d7dd4191f6"></a>

```c
bool encryption
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[encryption](#a8e5cffe8960477e7f64707d7dd4191f6)。

广播等时组（BIG）的各个流是否加密（Encrypted）。

<a id="r_ac47bfe3ee0c46f5d55d38f24835ac48d"></a>

```c
uint8_t bcode [0x10]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bcode](#ac47bfe3ee0c46f5d55d38f24835ac48d)。

广播码（Broadcast Code）。

## 74.2\_详细说明（Detailed Documentation）

<a id="ac47bfe3ee0c46f5d55d38f24835ac48d"></a>

### `bcode`

```c
uint8_t bt_iso_big_sync_param::bcode[0x10]
```

广播码（Broadcast Code）。

用于派生会话密钥（Session key）的代码；该密钥用于加密和解密广播等时流载荷（BIS payloads）。

如果该值是字符串，或者不足 16 个八位字节，则其余八位字节必须为 0。

例如，字符串 `"Broadcast Code"` 必须表示为 `[42 72 6F 61 64 63 61 73 74 20 43 6F 64 65 00 00]`。

<a id="a14b03509daf760edbead86659f733136"></a>

### `bis_bitfield`

```c
uint32_t bt_iso_big_sync_param::bis_bitfield
```

要同步的广播等时流位域（BISes bitfield）。

使用 `BT_ISO_BIS_INDEX_BIT` 将广播等时流索引（BIS indexes）转换为位域。

例如，要同步到广播等时流索引（BIS indexes）`0x01` 和 `0x02`，可设为 `BT_ISO_BIS_INDEX_BIT(0x01) | BT_ISO_BIS_INDEX_BIT(0x02)`。

<a id="ac56d7206c3434837a52059716355adad"></a>

### `bis_channels`

```c
struct bt_iso_chan** bt_iso_big_sync_param::bis_channels
```

广播等时流通道指针数组（BIS channel pointers）。

<a id="a8e5cffe8960477e7f64707d7dd4191f6"></a>

### `encryption`

```c
bool bt_iso_big_sync_param::encryption
```

广播等时组（BIG）的各个流是否加密（Encrypted）。

<a id="a16b332b4a0f373cb21e5da6e6e383b9e"></a>

### `mse`

```c
uint32_t bt_iso_big_sync_param::mse
```

最大子事件数（Maximum subevents）。

最大子事件数（Maximum Subevents，MSE）参数规定控制器在每个广播等时流（BIS）间隔内，接收数据载荷时最多应使用的子事件数量。

取值范围为 `BT_ISO_SYNC_MSE_MIN` 至 `BT_ISO_SYNC_MSE_MAX`；也可设为 `BT_ISO_SYNC_MSE_ANY`，由控制器选择。

<a id="a96cd109e9f5820531635d48e88b4bff8"></a>

### `num_bis`

```c
uint8_t bt_iso_big_sync_param::num_bis
```

`bis_channels` 中的通道数量（Number of channels）。

单组最大通道数量（Maximum channels per group）为 `BT_ISO_MAX_GROUP_ISO_COUNT`。

<a id="a8e344870fc0e380e6588eb90c7ef72f9"></a>

### `sync_timeout`

```c
uint16_t bt_iso_big_sync_param::sync_timeout
```

广播等时组（BIG）的同步超时（Synchronization timeout），为 N × 10 毫秒。

取值范围为 `BT_ISO_SYNC_TIMEOUT_MIN` 至 `BT_ISO_SYNC_TIMEOUT_MAX`。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/iso.h`

## 74.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/iso.h](https://docs.zephyrproject.org/latest/doxygen/html/iso_8h_source.html)
- [bt_iso_chan](P077_bt_iso_chan_结构体.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)
- [BT_ISO_BIS_INDEX_BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#ga01b975b441fa5d8f039562ab66857bbf)
- [BT_ISO_SYNC_MSE_MIN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#gafef299e43e0f58ac23e1a1e75ccd0163)
- [BT_ISO_SYNC_MSE_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#gafd6e7b48394d6f6c8ddd485927b02b4b)
- [BT_ISO_SYNC_MSE_ANY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#ga47802144b8523b3d46af9ef97e744bbd)
- [BT_ISO_MAX_GROUP_ISO_COUNT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#gae9dc30b300e2c309d646e3227e8cc00e)
- [BT_ISO_SYNC_TIMEOUT_MIN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#gaa1bd6484a248a6fb5abc31202e5076d4)
- [BT_ISO_SYNC_TIMEOUT_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#gaeb66806b649bf828afbd83d15c9823eb)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P073_bt_iso_big_create_param_结构体.md) · [返回大纲](大纲.md) · [下一章](P075_bt_iso_biginfo_结构体.md)
