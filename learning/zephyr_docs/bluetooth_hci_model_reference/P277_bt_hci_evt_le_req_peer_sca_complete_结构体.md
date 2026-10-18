---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-277
title: bt_hci_evt_le_req_peer_sca_complete_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__evt__le__req__peer__sca__complete.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第277章\_bt\_hci\_evt\_le\_req\_peer\_sca\_complete\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__evt__le__req__peer__sca__complete.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 277.1\_数据成员（Data Fields）

<a id="r_a814d17b8aae9dd68f57402c857ca1810"></a>

```c
uint8_t status
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[status](#a814d17b8aae9dd68f57402c857ca1810)。

<a id="r_ab6b648e7f4bff9e84b274e9e22a26166"></a>

```c
uint16_t handle
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[handle](#ab6b648e7f4bff9e84b274e9e22a26166)。

<a id="r_a88f93ead6ec67e1612b1a0e8402a30e7"></a>

```c
uint8_t sca
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[sca](#a88f93ead6ec67e1612b1a0e8402a30e7)。

## 277.2\_详细说明（Detailed Documentation）

<a id="ab6b648e7f4bff9e84b274e9e22a26166"></a>

### `handle`

```c
uint16_t bt_hci_evt_le_req_peer_sca_complete::handle
```

<a id="a88f93ead6ec67e1612b1a0e8402a30e7"></a>

### `sca`

```c
uint8_t bt_hci_evt_le_req_peer_sca_complete::sca
```

<a id="a814d17b8aae9dd68f57402c857ca1810"></a>

### `status`

```c
uint8_t bt_hci_evt_le_req_peer_sca_complete::status
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 277.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P276_bt_hci_evt_le_remote_feat_complete_结构体.md) · [返回大纲](大纲.md) · [下一章](P278_bt_hci_evt_le_scan_req_received_结构体.md)
