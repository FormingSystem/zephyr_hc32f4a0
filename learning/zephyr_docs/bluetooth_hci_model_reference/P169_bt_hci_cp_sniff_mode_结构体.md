---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-169
title: bt_hci_cp_sniff_mode_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cp__sniff__mode.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第169章\_bt\_hci\_cp\_sniff\_mode\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cp__sniff__mode.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 169.1\_数据成员（Data Fields）

<a id="r_a37cc61e67148cf8993aa3c6410094d7e"></a>

```c
uint16_t handle
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[handle](#a37cc61e67148cf8993aa3c6410094d7e)。

<a id="r_ad765b1aebc101886d5e9805245252718"></a>

```c
uint16_t max_interval
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[max_interval](#ad765b1aebc101886d5e9805245252718)。

<a id="r_aaba62465c5fb76641715eed4bc8c25e9"></a>

```c
uint16_t min_interval
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[min_interval](#aaba62465c5fb76641715eed4bc8c25e9)。

<a id="r_a1896272c588ed2ffe0052353eed528c4"></a>

```c
uint16_t attempt
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[attempt](#a1896272c588ed2ffe0052353eed528c4)。

<a id="r_aa0bfa66eb627378a820144b8ca748b5f"></a>

```c
uint16_t timeout
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[timeout](#aa0bfa66eb627378a820144b8ca748b5f)。

## 169.2\_详细说明（Detailed Documentation）

<a id="a1896272c588ed2ffe0052353eed528c4"></a>

### `attempt`

```c
uint16_t bt_hci_cp_sniff_mode::attempt
```

<a id="a37cc61e67148cf8993aa3c6410094d7e"></a>

### `handle`

```c
uint16_t bt_hci_cp_sniff_mode::handle
```

<a id="ad765b1aebc101886d5e9805245252718"></a>

### `max_interval`

```c
uint16_t bt_hci_cp_sniff_mode::max_interval
```

<a id="aaba62465c5fb76641715eed4bc8c25e9"></a>

### `min_interval`

```c
uint16_t bt_hci_cp_sniff_mode::min_interval
```

<a id="aa0bfa66eb627378a820144b8ca748b5f"></a>

### `timeout`

```c
uint16_t bt_hci_cp_sniff_mode::timeout
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 169.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P168_bt_hci_cp_setup_sync_conn_结构体.md) · [返回大纲](大纲.md) · [下一章](P170_bt_hci_cp_sniff_subrating_结构体.md)
