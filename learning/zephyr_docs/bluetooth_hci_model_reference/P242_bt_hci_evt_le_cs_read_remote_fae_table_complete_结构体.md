---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-242
title: bt_hci_evt_le_cs_read_remote_fae_table_complete_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__evt__le__cs__read__remote__fae__table__complete.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第242章\_bt\_hci\_evt\_le\_cs\_read\_remote\_fae\_table\_complete\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__evt__le__cs__read__remote__fae__table__complete.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 242.1\_数据成员（Data Fields）

<a id="r_a1ee4d133955f28f45d16226730344428"></a>

```c
uint8_t status
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[status](#a1ee4d133955f28f45d16226730344428)。

<a id="r_adcdfbfd2d9c19be0c41121235fbb8eaa"></a>

```c
uint16_t conn_handle
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[conn_handle](#adcdfbfd2d9c19be0c41121235fbb8eaa)。

<a id="r_ae1ca6d2d4f4305565f1d491ef202fcad"></a>

```c
int8_t remote_fae_table [72]
```

相关声明：[int8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#accbd6432732c88ad6adc5365800433b6)、[remote_fae_table](#ae1ca6d2d4f4305565f1d491ef202fcad)。

## 242.2\_详细说明（Detailed Documentation）

<a id="adcdfbfd2d9c19be0c41121235fbb8eaa"></a>

### `conn_handle`

```c
uint16_t bt_hci_evt_le_cs_read_remote_fae_table_complete::conn_handle
```

<a id="ae1ca6d2d4f4305565f1d491ef202fcad"></a>

### `remote_fae_table`

```c
int8_t bt_hci_evt_le_cs_read_remote_fae_table_complete::remote_fae_table[72]
```

<a id="a1ee4d133955f28f45d16226730344428"></a>

### `status`

```c
uint8_t bt_hci_evt_le_cs_read_remote_fae_table_complete::status
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 242.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [int8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#accbd6432732c88ad6adc5365800433b6)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P241_bt_hci_evt_le_cs_procedure_enable_complete_结构体.md) · [返回大纲](大纲.md) · [下一章](P243_bt_hci_evt_le_cs_read_remote_supported_capabilities_complete_结构体.md)
