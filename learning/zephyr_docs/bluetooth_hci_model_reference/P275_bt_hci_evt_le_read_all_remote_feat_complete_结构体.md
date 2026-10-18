---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-275
title: bt_hci_evt_le_read_all_remote_feat_complete_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__evt__le__read__all__remote__feat__complete.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第275章\_bt\_hci\_evt\_le\_read\_all\_remote\_feat\_complete\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__evt__le__read__all__remote__feat__complete.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 275.1\_数据成员（Data Fields）

<a id="r_acab09b5b552faef296c6e0442c4a2bc9"></a>

```c
uint8_t status
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[status](#acab09b5b552faef296c6e0442c4a2bc9)。

<a id="r_af4a77910c32dbbdb259a9532818a0746"></a>

```c
uint16_t handle
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[handle](#af4a77910c32dbbdb259a9532818a0746)。

<a id="r_a3582ff03fd6a680e006b94ff6080dc37"></a>

```c
uint8_t max_remote_page
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[max_remote_page](#a3582ff03fd6a680e006b94ff6080dc37)。

<a id="r_aefc3508368f6a103c9b2d218f66f6a11"></a>

```c
uint8_t max_valid_page
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[max_valid_page](#aefc3508368f6a103c9b2d218f66f6a11)。

<a id="r_afd04ae00d6ce4b2cb57861b0cd2e9a03"></a>

```c
uint8_t features [248]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[features](#afd04ae00d6ce4b2cb57861b0cd2e9a03)。

## 275.2\_详细说明（Detailed Documentation）

<a id="afd04ae00d6ce4b2cb57861b0cd2e9a03"></a>

### `features`

```c
uint8_t bt_hci_evt_le_read_all_remote_feat_complete::features[248]
```

<a id="af4a77910c32dbbdb259a9532818a0746"></a>

### `handle`

```c
uint16_t bt_hci_evt_le_read_all_remote_feat_complete::handle
```

<a id="a3582ff03fd6a680e006b94ff6080dc37"></a>

### `max_remote_page`

```c
uint8_t bt_hci_evt_le_read_all_remote_feat_complete::max_remote_page
```

<a id="aefc3508368f6a103c9b2d218f66f6a11"></a>

### `max_valid_page`

```c
uint8_t bt_hci_evt_le_read_all_remote_feat_complete::max_valid_page
```

<a id="acab09b5b552faef296c6e0442c4a2bc9"></a>

### `status`

```c
uint8_t bt_hci_evt_le_read_all_remote_feat_complete::status
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 275.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P274_bt_hci_evt_le_phy_update_complete_结构体.md) · [返回大纲](大纲.md) · [下一章](P276_bt_hci_evt_le_remote_feat_complete_结构体.md)
