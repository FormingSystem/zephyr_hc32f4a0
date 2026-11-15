---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-228
title: bt_hci_evt_le_big_terminate_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__evt__le__big__terminate.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第228章\_bt\_hci\_evt\_le\_big\_terminate\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__evt__le__big__terminate.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 228.1\_数据成员（Data Fields）

<a id="r_ad9c9e6d42661366d62d79163fa9ad1c7"></a>

```c
uint8_t big_handle
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[big_handle](#ad9c9e6d42661366d62d79163fa9ad1c7)。

<a id="r_a0303ac64b825f93210dfc70a8a081ea6"></a>

```c
uint8_t reason
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[reason](#a0303ac64b825f93210dfc70a8a081ea6)。

## 228.2\_详细说明（Detailed Documentation）

<a id="ad9c9e6d42661366d62d79163fa9ad1c7"></a>

### `big_handle`

```c
uint8_t bt_hci_evt_le_big_terminate::big_handle
```

<a id="a0303ac64b825f93210dfc70a8a081ea6"></a>

### `reason`

```c
uint8_t bt_hci_evt_le_big_terminate::reason
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 228.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P227_bt_hci_evt_le_big_sync_lost_结构体.md) · [返回大纲](大纲.md) · [下一章](P229_bt_hci_evt_le_biginfo_adv_report_结构体.md)
