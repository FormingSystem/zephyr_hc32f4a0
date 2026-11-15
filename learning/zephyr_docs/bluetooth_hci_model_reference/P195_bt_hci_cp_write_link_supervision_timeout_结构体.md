---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-195
title: bt_hci_cp_write_link_supervision_timeout_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cp__write__link__supervision__timeout.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第195章\_bt\_hci\_cp\_write\_link\_supervision\_timeout\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cp__write__link__supervision__timeout.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

写入链路监督超时（Write Link Supervision Timeout）的 HCI 命令参数。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="details"></a>

写入链路监督超时（Write Link Supervision Timeout）的 HCI 命令参数。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 195.1\_数据成员（Data Fields）

<a id="r_a1f33613e27db275806eaaa909591e882"></a>

```c
uint16_t handle
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[handle](#a1f33613e27db275806eaaa909591e882)。

连接句柄（Connection Handle）。

<a id="r_a2dd05ca57e20ee4b4fbe2b29cc746bee"></a>

```c
uint16_t timeout
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[timeout](#a2dd05ca57e20ee4b4fbe2b29cc746bee)。

链路监督超时（Link Supervision Timeout）。

## 195.2\_详细说明（Detailed Documentation）

<a id="a1f33613e27db275806eaaa909591e882"></a>

### `handle`

```c
uint16_t bt_hci_cp_write_link_supervision_timeout::handle
```

连接句柄（Connection Handle）。

<a id="a2dd05ca57e20ee4b4fbe2b29cc746bee"></a>

### `timeout`

```c
uint16_t bt_hci_cp_write_link_supervision_timeout::timeout
```

链路监督超时（Link Supervision Timeout）。

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 195.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P194_bt_hci_cp_write_link_policy_settings_结构体.md) · [返回大纲](大纲.md) · [下一章](P196_bt_hci_cp_write_page_scan_activity_结构体.md)
