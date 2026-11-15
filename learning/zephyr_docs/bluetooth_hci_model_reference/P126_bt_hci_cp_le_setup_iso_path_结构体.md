---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-126
title: bt_hci_cp_le_setup_iso_path_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cp__le__setup__iso__path.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第126章\_bt\_hci\_cp\_le\_setup\_iso\_path\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cp__le__setup__iso__path.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 126.1\_数据成员（Data Fields）

<a id="r_a0054fede0e583cef0dbcf6ef3134e480"></a>

```c
uint16_t handle
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[handle](#a0054fede0e583cef0dbcf6ef3134e480)。

<a id="r_a89c1324359a4fc2f10fee9ebbac5cf2b"></a>

```c
uint8_t path_dir
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[path_dir](#a89c1324359a4fc2f10fee9ebbac5cf2b)。

<a id="r_a7c07d69b2005af1f7f2618f2bfa60d50"></a>

```c
uint8_t path_id
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[path_id](#a7c07d69b2005af1f7f2618f2bfa60d50)。

<a id="r_a5256fc99b362e3a5f986ef2b71b29ccb"></a>

```c
struct bt_hci_cp_codec_id codec_id
```

相关声明：[bt_hci_cp_codec_id](P011_bt_hci_cp_codec_id_结构体.md)、[codec_id](#a5256fc99b362e3a5f986ef2b71b29ccb)。

<a id="r_a31948436e6608f9943d34ce89a65c64c"></a>

```c
uint8_t controller_delay [3]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[controller_delay](#a31948436e6608f9943d34ce89a65c64c)。

<a id="r_a1a816d8e8c434a05ea897b74bc4d89c7"></a>

```c
uint8_t codec_config_len
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[codec_config_len](#a1a816d8e8c434a05ea897b74bc4d89c7)。

<a id="r_ade4dee947e3d288f769d2d69fc57f96a"></a>

```c
uint8_t codec_config [0]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[codec_config](#ade4dee947e3d288f769d2d69fc57f96a)。

## 126.2\_详细说明（Detailed Documentation）

<a id="ade4dee947e3d288f769d2d69fc57f96a"></a>

### `codec_config`

```c
uint8_t bt_hci_cp_le_setup_iso_path::codec_config[0]
```

<a id="a1a816d8e8c434a05ea897b74bc4d89c7"></a>

### `codec_config_len`

```c
uint8_t bt_hci_cp_le_setup_iso_path::codec_config_len
```

<a id="a5256fc99b362e3a5f986ef2b71b29ccb"></a>

### `codec_id`

```c
struct bt_hci_cp_codec_id bt_hci_cp_le_setup_iso_path::codec_id
```

<a id="a31948436e6608f9943d34ce89a65c64c"></a>

### `controller_delay`

```c
uint8_t bt_hci_cp_le_setup_iso_path::controller_delay[3]
```

<a id="a0054fede0e583cef0dbcf6ef3134e480"></a>

### `handle`

```c
uint16_t bt_hci_cp_le_setup_iso_path::handle
```

<a id="a89c1324359a4fc2f10fee9ebbac5cf2b"></a>

### `path_dir`

```c
uint8_t bt_hci_cp_le_setup_iso_path::path_dir
```

<a id="a7c07d69b2005af1f7f2618f2bfa60d50"></a>

### `path_id`

```c
uint8_t bt_hci_cp_le_setup_iso_path::path_id
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 126.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bt_hci_cp_codec_id](P011_bt_hci_cp_codec_id_结构体.md)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P125_bt_hci_cp_le_set_tx_power_report_enable_结构体.md) · [返回大纲](大纲.md) · [下一章](P127_bt_hci_cp_le_start_encryption_结构体.md)
