---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-449
title: bt_hci_vs_static_addr_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__vs__static__addr.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第449章\_bt\_hci\_vs\_static\_addr\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__vs__static__addr.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_vs.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 449.1\_数据成员（Data Fields）

<a id="r_aa9b61e3f589465c68a4b6356c9de8b66"></a>

```c
bt_addr_t bdaddr
```

相关声明：[bt_addr_t](../bluetooth_classic_model_reference/P012_bt_addr_t_结构体.md)、[bdaddr](#aa9b61e3f589465c68a4b6356c9de8b66)。

<a id="r_afef2fbf31b7d5101ee48e51476c81698"></a>

```c
uint8_t ir [16]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[ir](#afef2fbf31b7d5101ee48e51476c81698)。

## 449.2\_详细说明（Detailed Documentation）

<a id="aa9b61e3f589465c68a4b6356c9de8b66"></a>

### `bdaddr`

```c
bt_addr_t bt_hci_vs_static_addr::bdaddr
```

<a id="afef2fbf31b7d5101ee48e51476c81698"></a>

### `ir`

```c
uint8_t bt_hci_vs_static_addr::ir[16]
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_vs.h`

## 449.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_vs.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__vs_8h_source.html)
- [bt_addr_t](../bluetooth_classic_model_reference/P012_bt_addr_t_结构体.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P448_bt_hci_vs_fatal_error_stack_frame_结构体.md) · [返回大纲](大纲.md) · [下一章](P450_bt_hci_write_local_name_结构体.md)
