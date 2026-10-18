---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-111
title: bt_hci_cp_le_set_pawr_sync_subevent_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cp__le__set__pawr__sync__subevent.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第111章\_bt\_hci\_cp\_le\_set\_pawr\_sync\_subevent\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cp__le__set__pawr__sync__subevent.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 111.1\_数据成员（Data Fields）

<a id="r_a89f3092c2dd561e5469bb5bf57a06172"></a>

```c
uint16_t sync_handle
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[sync_handle](#a89f3092c2dd561e5469bb5bf57a06172)。

<a id="r_aa73b23816e6c2c6546de15f6f6caff27"></a>

```c
uint16_t periodic_adv_properties
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[periodic_adv_properties](#aa73b23816e6c2c6546de15f6f6caff27)。

<a id="r_a2648ff50e0bad585e77e6f340836555a"></a>

```c
uint8_t num_subevents
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[num_subevents](#a2648ff50e0bad585e77e6f340836555a)。

<a id="r_a9a362ae841e5305b3985c4b2d88c6753"></a>

```c
uint8_t subevents [0]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[subevents](#a9a362ae841e5305b3985c4b2d88c6753)。

## 111.2\_详细说明（Detailed Documentation）

<a id="a2648ff50e0bad585e77e6f340836555a"></a>

### `num_subevents`

```c
uint8_t bt_hci_cp_le_set_pawr_sync_subevent::num_subevents
```

<a id="aa73b23816e6c2c6546de15f6f6caff27"></a>

### `periodic_adv_properties`

```c
uint16_t bt_hci_cp_le_set_pawr_sync_subevent::periodic_adv_properties
```

<a id="a9a362ae841e5305b3985c4b2d88c6753"></a>

### `subevents`

```c
uint8_t bt_hci_cp_le_set_pawr_sync_subevent::subevents[0]
```

<a id="a89f3092c2dd561e5469bb5bf57a06172"></a>

### `sync_handle`

```c
uint16_t bt_hci_cp_le_set_pawr_sync_subevent::sync_handle
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 111.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P110_bt_hci_cp_le_set_pawr_subevent_data_element_结构体.md) · [返回大纲](大纲.md) · [下一章](P112_bt_hci_cp_le_set_per_adv_data_结构体.md)
