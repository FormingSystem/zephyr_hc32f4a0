---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-37
title: bt_hci_cp_le_cs_set_default_settings_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cp__le__cs__set__default__settings.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第37章\_bt\_hci\_cp\_le\_cs\_set\_default\_settings\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cp__le__cs__set__default__settings.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 37.1\_数据成员（Data Fields）

<a id="r_a096c3238ccc6624bae89d5a45dd95600"></a>

```c
uint16_t handle
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[handle](#a096c3238ccc6624bae89d5a45dd95600)。

<a id="r_a04aea510e26136f874ccfbabbbd080bb"></a>

```c
uint8_t role_enable
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[role_enable](#a04aea510e26136f874ccfbabbbd080bb)。

<a id="r_aa001c88ab42250c2cfd604af11e0ae27"></a>

```c
uint8_t cs_sync_antenna_selection
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[cs_sync_antenna_selection](#aa001c88ab42250c2cfd604af11e0ae27)。

<a id="r_a333341ec01554ab90fc5e340dbfb5130"></a>

```c
int8_t max_tx_power
```

相关声明：[int8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#accbd6432732c88ad6adc5365800433b6)、[max_tx_power](#a333341ec01554ab90fc5e340dbfb5130)。

## 37.2\_详细说明（Detailed Documentation）

<a id="aa001c88ab42250c2cfd604af11e0ae27"></a>

### `cs_sync_antenna_selection`

```c
uint8_t bt_hci_cp_le_cs_set_default_settings::cs_sync_antenna_selection
```

<a id="a096c3238ccc6624bae89d5a45dd95600"></a>

### `handle`

```c
uint16_t bt_hci_cp_le_cs_set_default_settings::handle
```

<a id="a333341ec01554ab90fc5e340dbfb5130"></a>

### `max_tx_power`

```c
int8_t bt_hci_cp_le_cs_set_default_settings::max_tx_power
```

<a id="a04aea510e26136f874ccfbabbbd080bb"></a>

### `role_enable`

```c
uint8_t bt_hci_cp_le_cs_set_default_settings::role_enable
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 37.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [int8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#accbd6432732c88ad6adc5365800433b6)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P036_bt_hci_cp_le_cs_remove_config_结构体.md) · [返回大纲](大纲.md) · [下一章](P038_bt_hci_cp_le_default_past_param_结构体.md)
