---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-57
title: bt_hci_cp_le_procedure_enable_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cp__le__procedure__enable.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第57章\_bt\_hci\_cp\_le\_procedure\_enable\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cp__le__procedure__enable.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 57.1\_数据成员（Data Fields）

<a id="r_af94d81f71c2fe587c848e34a430825bf"></a>

```c
uint16_t handle
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[handle](#af94d81f71c2fe587c848e34a430825bf)。

<a id="r_ae1dc5c808bed301ddee6e9dd624c00a5"></a>

```c
uint8_t config_id
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[config_id](#ae1dc5c808bed301ddee6e9dd624c00a5)。

<a id="r_a3a203b453bd913db8bec91be9310003a"></a>

```c
uint8_t enable
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[enable](#a3a203b453bd913db8bec91be9310003a)。

## 57.2\_详细说明（Detailed Documentation）

<a id="ae1dc5c808bed301ddee6e9dd624c00a5"></a>

### `config_id`

```c
uint8_t bt_hci_cp_le_procedure_enable::config_id
```

<a id="a3a203b453bd913db8bec91be9310003a"></a>

### `enable`

```c
uint8_t bt_hci_cp_le_procedure_enable::enable
```

<a id="af94d81f71c2fe587c848e34a430825bf"></a>

### `handle`

```c
uint16_t bt_hci_cp_le_procedure_enable::handle
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 57.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P056_bt_hci_cp_le_per_adv_terminate_sync_结构体.md) · [返回大纲](大纲.md) · [下一章](P058_bt_hci_cp_le_read_all_remote_features_结构体.md)
