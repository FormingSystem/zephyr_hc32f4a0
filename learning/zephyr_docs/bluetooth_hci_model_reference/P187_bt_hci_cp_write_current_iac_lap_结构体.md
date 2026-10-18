---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-187
title: bt_hci_cp_write_current_iac_lap_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cp__write__current__iac__lap.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第187章\_bt\_hci\_cp\_write\_current\_iac\_lap\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cp__write__current__iac__lap.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 187.1\_数据成员（Data Fields）

<a id="r_aaaf3e9c66729a3b4081abb5f8a954108"></a>

```c
uint8_t num_current_iac
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[num_current_iac](#aaaf3e9c66729a3b4081abb5f8a954108)。

<a id="r_ad44e9a0d65bc5140e313176f5b98e932"></a>

```c
struct bt_hci_iac_lap lap [0]
```

相关声明：[bt_hci_iac_lap](P311_bt_hci_iac_lap_结构体.md)、[lap](#ad44e9a0d65bc5140e313176f5b98e932)。

## 187.2\_详细说明（Detailed Documentation）

<a id="ad44e9a0d65bc5140e313176f5b98e932"></a>

### `lap`

```c
struct bt_hci_iac_lap bt_hci_cp_write_current_iac_lap::lap[0]
```

<a id="aaaf3e9c66729a3b4081abb5f8a954108"></a>

### `num_current_iac`

```c
uint8_t bt_hci_cp_write_current_iac_lap::num_current_iac
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 187.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bt_hci_iac_lap](P311_bt_hci_iac_lap_结构体.md)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P186_bt_hci_cp_write_conn_accept_timeout_结构体.md) · [返回大纲](大纲.md) · [下一章](P188_bt_hci_cp_write_default_link_policy_settings_结构体.md)
