---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-421
title: bt_hci_rp_sniff_subrating_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__rp__sniff__subrating.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第421章\_bt\_hci\_rp\_sniff\_subrating\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__rp__sniff__subrating.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

HCI 嗅探子速率（Sniff Subrating）返回参数。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="details"></a>

HCI 嗅探子速率（Sniff Subrating）返回参数。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 421.1\_数据成员（Data Fields）

<a id="r_aa5d11db99d6f467a1e93afe031c08e14"></a>

```c
uint8_t status
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[status](#aa5d11db99d6f467a1e93afe031c08e14)。

状态（Status）。

<a id="r_a39e9f3ec6e7d9c534ca6160172990fa6"></a>

```c
uint16_t handle
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[handle](#a39e9f3ec6e7d9c534ca6160172990fa6)。

异步面向连接逻辑传输（ACL）的连接句柄。

## 421.2\_详细说明（Detailed Documentation）

<a id="a39e9f3ec6e7d9c534ca6160172990fa6"></a>

### `handle`

```c
uint16_t bt_hci_rp_sniff_subrating::handle
```

异步面向连接逻辑传输（ACL）的连接句柄。

<a id="aa5d11db99d6f467a1e93afe031c08e14"></a>

### `status`

```c
uint8_t bt_hci_rp_sniff_subrating::status
```

状态（Status）。

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 421.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P420_bt_hci_rp_remote_name_cancel_结构体.md) · [返回大纲](大纲.md) · [下一章](P422_bt_hci_rp_user_confirm_reply_结构体.md)
