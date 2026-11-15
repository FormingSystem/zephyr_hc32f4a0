---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-170
title: bt_hci_cp_sniff_subrating_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cp__sniff__subrating.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第170章\_bt\_hci\_cp\_sniff\_subrating\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cp__sniff__subrating.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

HCI 嗅探子速率（Sniff Subrating）命令参数。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="details"></a>

HCI 嗅探子速率（Sniff Subrating）命令参数。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 170.1\_数据成员（Data Fields）

<a id="r_af25eb1e9ee6eef5888ffa31b9fdd2887"></a>

```c
uint16_t handle
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[handle](#af25eb1e9ee6eef5888ffa31b9fdd2887)。

异步面向连接逻辑传输（ACL）的连接句柄。

<a id="r_a3534ddbf9876a82855b569ef7e01fd96"></a>

```c
uint16_t max_latency
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[max_latency](#a3534ddbf9876a82855b569ef7e01fd96)。

最大延迟（Maximum Latency）。

<a id="r_ab11c374063c6219b942b839f10d6a74d"></a>

```c
uint16_t min_remote_timeout
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[min_remote_timeout](#ab11c374063c6219b942b839f10d6a74d)。

远端最小超时（Minimum Remote Timeout）。

<a id="r_aa6de505cd8ba606d893dc74590083963"></a>

```c
uint16_t min_local_timeout
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[min_local_timeout](#aa6de505cd8ba606d893dc74590083963)。

本地最小超时（Minimum Local Timeout）。

## 170.2\_详细说明（Detailed Documentation）

<a id="af25eb1e9ee6eef5888ffa31b9fdd2887"></a>

### `handle`

```c
uint16_t bt_hci_cp_sniff_subrating::handle
```

异步面向连接逻辑传输（ACL）的连接句柄。

<a id="a3534ddbf9876a82855b569ef7e01fd96"></a>

### `max_latency`

```c
uint16_t bt_hci_cp_sniff_subrating::max_latency
```

最大延迟（Maximum Latency）。

<a id="aa6de505cd8ba606d893dc74590083963"></a>

### `min_local_timeout`

```c
uint16_t bt_hci_cp_sniff_subrating::min_local_timeout
```

本地最小超时（Minimum Local Timeout）。

<a id="ab11c374063c6219b942b839f10d6a74d"></a>

### `min_remote_timeout`

```c
uint16_t bt_hci_cp_sniff_subrating::min_remote_timeout
```

远端最小超时（Minimum Remote Timeout）。

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 170.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P169_bt_hci_cp_sniff_mode_结构体.md) · [返回大纲](大纲.md) · [下一章](P171_bt_hci_cp_switch_role_结构体.md)
