---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-413
title: bt_hci_rp_read_link_supervision_timeout_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__rp__read__link__supervision__timeout.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第413章\_bt\_hci\_rp\_read\_link\_supervision\_timeout\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__rp__read__link__supervision__timeout.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

读取链路监督超时（Read Link Supervision Timeout）的 HCI 响应参数。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="details"></a>

读取链路监督超时（Read Link Supervision Timeout）的 HCI 响应参数。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 413.1\_数据成员（Data Fields）

<a id="r_a1400aa0d8172c0cbf6b24b6571e73f73"></a>

```c
uint8_t status
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[status](#a1400aa0d8172c0cbf6b24b6571e73f73)。

状态（Status）。

<a id="r_aec86b11707e4728dd0849f12c32cf8f8"></a>

```c
uint16_t handle
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[handle](#aec86b11707e4728dd0849f12c32cf8f8)。

连接句柄（Connection Handle）。

<a id="r_ad1048becb6523d7302fdbbd739bc1b99"></a>

```c
uint16_t timeout
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[timeout](#ad1048becb6523d7302fdbbd739bc1b99)。

链路监督超时（Link Supervision Timeout）。

## 413.2\_详细说明（Detailed Documentation）

<a id="aec86b11707e4728dd0849f12c32cf8f8"></a>

### `handle`

```c
uint16_t bt_hci_rp_read_link_supervision_timeout::handle
```

连接句柄（Connection Handle）。

<a id="a1400aa0d8172c0cbf6b24b6571e73f73"></a>

### `status`

```c
uint8_t bt_hci_rp_read_link_supervision_timeout::status
```

状态（Status）。

<a id="ad1048becb6523d7302fdbbd739bc1b99"></a>

### `timeout`

```c
uint16_t bt_hci_rp_read_link_supervision_timeout::timeout
```

链路监督超时（Link Supervision Timeout）。

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 413.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P412_bt_hci_rp_read_link_policy_settings_结构体.md) · [返回大纲](大纲.md) · [下一章](P414_bt_hci_rp_read_local_ext_features_结构体.md)
