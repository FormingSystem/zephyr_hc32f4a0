---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-307
title: bt_hci_ext_adv_set_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__ext__adv__set.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第307章\_bt\_hci\_ext\_adv\_set\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__ext__adv__set.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 307.1\_数据成员（Data Fields）

<a id="r_a9d0fd3f6659db172ff4efd74c2c2d216"></a>

```c
uint8_t handle
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[handle](#a9d0fd3f6659db172ff4efd74c2c2d216)。

<a id="r_acc2afc91fe5c0dfcb4c95eaade4a047a"></a>

```c
uint16_t duration
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[duration](#acc2afc91fe5c0dfcb4c95eaade4a047a)。

<a id="r_a4467ac9a564ea24bb701de46cda2579a"></a>

```c
uint8_t max_ext_adv_evts
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[max_ext_adv_evts](#a4467ac9a564ea24bb701de46cda2579a)。

## 307.2\_详细说明（Detailed Documentation）

<a id="acc2afc91fe5c0dfcb4c95eaade4a047a"></a>

### `duration`

```c
uint16_t bt_hci_ext_adv_set::duration
```

<a id="a9d0fd3f6659db172ff4efd74c2c2d216"></a>

### `handle`

```c
uint8_t bt_hci_ext_adv_set::handle
```

<a id="a4467ac9a564ea24bb701de46cda2579a"></a>

### `max_ext_adv_evts`

```c
uint8_t bt_hci_ext_adv_set::max_ext_adv_evts
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 307.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P306_bt_hci_evt_vs_trace_info_结构体.md) · [返回大纲](大纲.md) · [下一章](P308_bt_hci_ext_conn_phy_结构体.md)
