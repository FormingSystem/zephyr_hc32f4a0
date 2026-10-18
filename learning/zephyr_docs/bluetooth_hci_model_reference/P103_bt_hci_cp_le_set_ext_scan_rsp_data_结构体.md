---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-103
title: bt_hci_cp_le_set_ext_scan_rsp_data_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cp__le__set__ext__scan__rsp__data.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第103章\_bt\_hci\_cp\_le\_set\_ext\_scan\_rsp\_data\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cp__le__set__ext__scan__rsp__data.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 103.1\_数据成员（Data Fields）

<a id="r_a8cf0624b9968686c7f6765ee25e11c90"></a>

```c
uint8_t handle
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[handle](#a8cf0624b9968686c7f6765ee25e11c90)。

<a id="r_a3323a0844680b71cb8aedffa034837d7"></a>

```c
uint8_t op
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[op](#a3323a0844680b71cb8aedffa034837d7)。

<a id="r_ac4e1691926df370b290c9e6d866d310d"></a>

```c
uint8_t frag_pref
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[frag_pref](#ac4e1691926df370b290c9e6d866d310d)。

<a id="r_a6024eac85f600ed3b7051a84b91bdcfa"></a>

```c
uint8_t len
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[len](#a6024eac85f600ed3b7051a84b91bdcfa)。

<a id="r_ab086720e1a22523ba155cb238ad75197"></a>

```c
uint8_t data [0]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[data](#ab086720e1a22523ba155cb238ad75197)。

## 103.2\_详细说明（Detailed Documentation）

<a id="ab086720e1a22523ba155cb238ad75197"></a>

### `data`

```c
uint8_t bt_hci_cp_le_set_ext_scan_rsp_data::data[0]
```

<a id="ac4e1691926df370b290c9e6d866d310d"></a>

### `frag_pref`

```c
uint8_t bt_hci_cp_le_set_ext_scan_rsp_data::frag_pref
```

<a id="a8cf0624b9968686c7f6765ee25e11c90"></a>

### `handle`

```c
uint8_t bt_hci_cp_le_set_ext_scan_rsp_data::handle
```

<a id="a6024eac85f600ed3b7051a84b91bdcfa"></a>

### `len`

```c
uint8_t bt_hci_cp_le_set_ext_scan_rsp_data::len
```

<a id="a3323a0844680b71cb8aedffa034837d7"></a>

### `op`

```c
uint8_t bt_hci_cp_le_set_ext_scan_rsp_data::op
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 103.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P102_bt_hci_cp_le_set_ext_scan_param_结构体.md) · [返回大纲](大纲.md) · [下一章](P104_bt_hci_cp_le_set_host_chan_classif_结构体.md)
