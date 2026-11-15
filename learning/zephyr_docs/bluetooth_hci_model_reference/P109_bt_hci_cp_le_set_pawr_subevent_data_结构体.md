---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-109
title: bt_hci_cp_le_set_pawr_subevent_data_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cp__le__set__pawr__subevent__data.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第109章\_bt\_hci\_cp\_le\_set\_pawr\_subevent\_data\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cp__le__set__pawr__subevent__data.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 109.1\_数据成员（Data Fields）

<a id="r_a47d84125d15cce1fc969db3e5caa07e1"></a>

```c
uint8_t adv_handle
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[adv_handle](#a47d84125d15cce1fc969db3e5caa07e1)。

<a id="r_a9397eebd6771ad159d1bdae0d59e5f46"></a>

```c
uint8_t num_subevents
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[num_subevents](#a9397eebd6771ad159d1bdae0d59e5f46)。

<a id="r_aa932c1f19de96f89a79bbcb3ecbc1f5d"></a>

```c
struct bt_hci_cp_le_set_pawr_subevent_data_element subevents [0]
```

相关声明：[bt_hci_cp_le_set_pawr_subevent_data_element](P110_bt_hci_cp_le_set_pawr_subevent_data_element_结构体.md)、[subevents](#aa932c1f19de96f89a79bbcb3ecbc1f5d)。

## 109.2\_详细说明（Detailed Documentation）

<a id="a47d84125d15cce1fc969db3e5caa07e1"></a>

### `adv_handle`

```c
uint8_t bt_hci_cp_le_set_pawr_subevent_data::adv_handle
```

<a id="a9397eebd6771ad159d1bdae0d59e5f46"></a>

### `num_subevents`

```c
uint8_t bt_hci_cp_le_set_pawr_subevent_data::num_subevents
```

<a id="aa932c1f19de96f89a79bbcb3ecbc1f5d"></a>

### `subevents`

```c
struct bt_hci_cp_le_set_pawr_subevent_data_element bt_hci_cp_le_set_pawr_subevent_data::subevents[0]
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 109.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bt_hci_cp_le_set_pawr_subevent_data_element](P110_bt_hci_cp_le_set_pawr_subevent_data_element_结构体.md)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P108_bt_hci_cp_le_set_pawr_response_data_结构体.md) · [返回大纲](大纲.md) · [下一章](P110_bt_hci_cp_le_set_pawr_subevent_data_element_结构体.md)
