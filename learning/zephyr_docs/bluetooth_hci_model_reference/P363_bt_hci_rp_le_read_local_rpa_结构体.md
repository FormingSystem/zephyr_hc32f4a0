---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-363
title: bt_hci_rp_le_read_local_rpa_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__rp__le__read__local__rpa.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第363章\_bt\_hci\_rp\_le\_read\_local\_rpa\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__rp__le__read__local__rpa.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 363.1\_数据成员（Data Fields）

<a id="r_a55b1ac66c986c0a7879b144163064be2"></a>

```c
uint8_t status
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[status](#a55b1ac66c986c0a7879b144163064be2)。

<a id="r_a5b27c5b02cb290452be62c22772fbc53"></a>

```c
bt_addr_t local_rpa
```

相关声明：[bt_addr_t](../bluetooth_classic_model_reference/P012_bt_addr_t_结构体.md)、[local_rpa](#a5b27c5b02cb290452be62c22772fbc53)。

## 363.2\_详细说明（Detailed Documentation）

<a id="a5b27c5b02cb290452be62c22772fbc53"></a>

### `local_rpa`

```c
bt_addr_t bt_hci_rp_le_read_local_rpa::local_rpa
```

<a id="a55b1ac66c986c0a7879b144163064be2"></a>

### `status`

```c
uint8_t bt_hci_rp_le_read_local_rpa::status
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 363.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bt_addr_t](../bluetooth_classic_model_reference/P012_bt_addr_t_结构体.md)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P362_bt_hci_rp_le_read_local_features_结构体.md) · [返回大纲](大纲.md) · [下一章](P364_bt_hci_rp_le_read_local_supported_capabilities_结构体.md)
