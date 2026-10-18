---
id: learning.zephyr-docs.bluetooth-connection-model-reference.page-89
title: bt_iso_tx_info_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__iso__tx__info.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第89章\_bt\_iso\_tx\_info\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__iso__tx__info.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

发送等时数据包（ISO Packet）的元数据结构。

```c
#include <zephyr/bluetooth/iso.h>
```

<a id="details"></a>

发送等时数据包（ISO Packet）的元数据结构。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 89.1\_数据成员（Data Fields）

<a id="r_ac8a6a4c073e4df1553d32339a6e4b051"></a>

```c
uint32_t ts
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[ts](#ac8a6a4c073e4df1553d32339a6e4b051)。

已发送服务数据单元（SDU）的连接等时组参考点（CIG reference point）或广播等时组锚点（BIG anchor point），单位为微秒。

<a id="r_a0cff6aa2893fdc11160e4327afebed13"></a>

```c
uint32_t offset
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[offset](#a0cff6aa2893fdc11160e4327afebed13)。

时间偏移量（Time offset），单位为微秒。

<a id="r_a2791edea2f4f4459acc24c8dbaa33ded"></a>

```c
uint16_t seq_num
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[seq_num](#a2791edea2f4f4459acc24c8dbaa33ded)。

数据包序列号（Packet sequence number）。

## 89.2\_详细说明（Detailed Documentation）

<a id="a0cff6aa2893fdc11160e4327afebed13"></a>

### `offset`

```c
uint32_t bt_iso_tx_info::offset
```

时间偏移量（Time offset），单位为微秒。

<a id="a2791edea2f4f4459acc24c8dbaa33ded"></a>

### `seq_num`

```c
uint16_t bt_iso_tx_info::seq_num
```

数据包序列号（Packet sequence number）。

<a id="ac8a6a4c073e4df1553d32339a6e4b051"></a>

### `ts`

```c
uint32_t bt_iso_tx_info::ts
```

已发送服务数据单元（SDU）的连接等时组参考点（CIG reference point）或广播等时组锚点（BIG anchor point），单位为微秒。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/iso.h`

## 89.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/iso.h](https://docs.zephyrproject.org/latest/doxygen/html/iso_8h_source.html)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P088_bt_iso_sync_receiver_info_结构体.md) · [返回大纲](大纲.md) · [下一章](P090_bt_iso_unicast_info_结构体.md)
