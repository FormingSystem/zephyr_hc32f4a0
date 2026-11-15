---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-425
title: bt_hci_rp_vs_read_host_stack_cmds_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__rp__vs__read__host__stack__cmds.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第425章\_bt\_hci\_rp\_vs\_read\_host\_stack\_cmds\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__rp__vs__read__host__stack__cmds.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_vs.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 425.1\_数据成员（Data Fields）

<a id="r_a374e54391bcb72b5cde885cb04269e9a"></a>

```c
uint8_t status
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[status](#a374e54391bcb72b5cde885cb04269e9a)。

<a id="r_ac11d1ed48e49f9ce1d31709be76aed95"></a>

```c
uint8_t num_cmds
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[num_cmds](#ac11d1ed48e49f9ce1d31709be76aed95)。

<a id="r_a27b591f7784aaec063afc37105c00880"></a>

```c
struct bt_hci_vs_cmd c [0]
```

相关声明：[bt_hci_vs_cmd](P442_bt_hci_vs_cmd_结构体.md)、[c](#a27b591f7784aaec063afc37105c00880)。

## 425.2\_详细说明（Detailed Documentation）

<a id="a27b591f7784aaec063afc37105c00880"></a>

### `c`

```c
struct bt_hci_vs_cmd bt_hci_rp_vs_read_host_stack_cmds::c[0]
```

<a id="ac11d1ed48e49f9ce1d31709be76aed95"></a>

### `num_cmds`

```c
uint8_t bt_hci_rp_vs_read_host_stack_cmds::num_cmds
```

<a id="a374e54391bcb72b5cde885cb04269e9a"></a>

### `status`

```c
uint8_t bt_hci_rp_vs_read_host_stack_cmds::status
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_vs.h`

## 425.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_vs.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__vs_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bt_hci_vs_cmd](P442_bt_hci_vs_cmd_结构体.md)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P424_bt_hci_rp_vs_read_chip_temp_结构体.md) · [返回大纲](大纲.md) · [下一章](P426_bt_hci_rp_vs_read_key_hierarchy_roots_结构体.md)
