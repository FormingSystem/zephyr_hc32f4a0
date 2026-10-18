---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-237
title: bt_hci_evt_le_conn_update_complete_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__evt__le__conn__update__complete.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第237章\_bt\_hci\_evt\_le\_conn\_update\_complete\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__evt__le__conn__update__complete.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 237.1\_数据成员（Data Fields）

<a id="r_ad428bd5e29d40f7551ccdd0747e429d6"></a>

```c
uint8_t status
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[status](#ad428bd5e29d40f7551ccdd0747e429d6)。

<a id="r_a81c0688a5e3b4b3a4d92fbc756a068d5"></a>

```c
uint16_t handle
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[handle](#a81c0688a5e3b4b3a4d92fbc756a068d5)。

<a id="r_a69aa00c0c50978b2aa620aad671119f3"></a>

```c
uint16_t interval
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[interval](#a69aa00c0c50978b2aa620aad671119f3)。

<a id="r_ade2421709a35e0cd0fce3a4d992470c3"></a>

```c
uint16_t latency
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[latency](#ade2421709a35e0cd0fce3a4d992470c3)。

<a id="r_aca728975619a10a6e3280b127b59f2f1"></a>

```c
uint16_t supv_timeout
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[supv_timeout](#aca728975619a10a6e3280b127b59f2f1)。

## 237.2\_详细说明（Detailed Documentation）

<a id="a81c0688a5e3b4b3a4d92fbc756a068d5"></a>

### `handle`

```c
uint16_t bt_hci_evt_le_conn_update_complete::handle
```

<a id="a69aa00c0c50978b2aa620aad671119f3"></a>

### `interval`

```c
uint16_t bt_hci_evt_le_conn_update_complete::interval
```

<a id="ade2421709a35e0cd0fce3a4d992470c3"></a>

### `latency`

```c
uint16_t bt_hci_evt_le_conn_update_complete::latency
```

<a id="ad428bd5e29d40f7551ccdd0747e429d6"></a>

### `status`

```c
uint8_t bt_hci_evt_le_conn_update_complete::status
```

<a id="aca728975619a10a6e3280b127b59f2f1"></a>

### `supv_timeout`

```c
uint16_t bt_hci_evt_le_conn_update_complete::supv_timeout
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 237.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P236_bt_hci_evt_le_conn_rate_change_结构体.md) · [返回大纲](大纲.md) · [下一章](P238_bt_hci_evt_le_connection_iq_report_结构体.md)
