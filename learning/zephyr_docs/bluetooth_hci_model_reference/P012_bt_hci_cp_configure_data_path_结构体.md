---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-12
title: bt_hci_cp_configure_data_path_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cp__configure__data__path.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第12章\_bt\_hci\_cp\_configure\_data\_path\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cp__configure__data__path.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 12.1\_数据成员（Data Fields）

<a id="r_a528ba2bd5a220d1b7db064f8b51a8718"></a>

```c
uint8_t data_path_dir
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[data_path_dir](#a528ba2bd5a220d1b7db064f8b51a8718)。

<a id="r_a92967e6b5258b2acd6d82bfbfb8b7940"></a>

```c
uint8_t data_path_id
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[data_path_id](#a92967e6b5258b2acd6d82bfbfb8b7940)。

<a id="r_a2573fe029e1774bf5fa7e8cffff08cec"></a>

```c
uint8_t vs_config_len
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[vs_config_len](#a2573fe029e1774bf5fa7e8cffff08cec)。

<a id="r_aa79c4aa6603b09f49a8c7f216f135e6e"></a>

```c
uint8_t vs_config [0]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[vs_config](#aa79c4aa6603b09f49a8c7f216f135e6e)。

## 12.2\_详细说明（Detailed Documentation）

<a id="a528ba2bd5a220d1b7db064f8b51a8718"></a>

### `data_path_dir`

```c
uint8_t bt_hci_cp_configure_data_path::data_path_dir
```

<a id="a92967e6b5258b2acd6d82bfbfb8b7940"></a>

### `data_path_id`

```c
uint8_t bt_hci_cp_configure_data_path::data_path_id
```

<a id="aa79c4aa6603b09f49a8c7f216f135e6e"></a>

### `vs_config`

```c
uint8_t bt_hci_cp_configure_data_path::vs_config[0]
```

<a id="a2573fe029e1774bf5fa7e8cffff08cec"></a>

### `vs_config_len`

```c
uint8_t bt_hci_cp_configure_data_path::vs_config_len
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 12.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P011_bt_hci_cp_codec_id_结构体.md) · [返回大纲](大纲.md) · [下一章](P013_bt_hci_cp_connect_结构体.md)
