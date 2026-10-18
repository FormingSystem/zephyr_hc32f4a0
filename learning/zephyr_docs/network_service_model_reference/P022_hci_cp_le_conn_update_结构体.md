---
id: learning.zephyr-docs.network-service-model-reference.page-22
title: hci_cp_le_conn_update_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structhci__cp__le__conn__update.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第22章\_hci\_cp\_le\_conn\_update\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structhci__cp__le__conn__update.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 22.1\_数据成员（Data Fields）

<a id="r_a5606b8795defc338b27d1a130064351e"></a>

```c
uint16_t handle
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[handle](#a5606b8795defc338b27d1a130064351e)。

<a id="r_adcfee3c727118069897515a00e7ead66"></a>

```c
uint16_t conn_interval_min
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[conn_interval_min](#adcfee3c727118069897515a00e7ead66)。

<a id="r_a99fc0b3b0f810f1d6e174aa9045d298a"></a>

```c
uint16_t conn_interval_max
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[conn_interval_max](#a99fc0b3b0f810f1d6e174aa9045d298a)。

<a id="r_a8e48e5e195aea7f581cfc7246da79d72"></a>

```c
uint16_t conn_latency
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[conn_latency](#a8e48e5e195aea7f581cfc7246da79d72)。

<a id="r_ab76ecdf6f7e5a5bb581cbd26f67d8f9f"></a>

```c
uint16_t supervision_timeout
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[supervision_timeout](#ab76ecdf6f7e5a5bb581cbd26f67d8f9f)。

<a id="r_a3ae86fccacf462463fe520eb1e06fa62"></a>

```c
uint16_t min_ce_len
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[min_ce_len](#a3ae86fccacf462463fe520eb1e06fa62)。

<a id="r_a401169ccc5dbf6cf0abd6154738f00dc"></a>

```c
uint16_t max_ce_len
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[max_ce_len](#a401169ccc5dbf6cf0abd6154738f00dc)。

## 22.2\_详细说明（Detailed Documentation）

<a id="a99fc0b3b0f810f1d6e174aa9045d298a"></a>

### `conn_interval_max`

```c
uint16_t hci_cp_le_conn_update::conn_interval_max
```

<a id="adcfee3c727118069897515a00e7ead66"></a>

### `conn_interval_min`

```c
uint16_t hci_cp_le_conn_update::conn_interval_min
```

<a id="a8e48e5e195aea7f581cfc7246da79d72"></a>

### `conn_latency`

```c
uint16_t hci_cp_le_conn_update::conn_latency
```

<a id="a5606b8795defc338b27d1a130064351e"></a>

### `handle`

```c
uint16_t hci_cp_le_conn_update::handle
```

<a id="a401169ccc5dbf6cf0abd6154738f00dc"></a>

### `max_ce_len`

```c
uint16_t hci_cp_le_conn_update::max_ce_len
```

<a id="a3ae86fccacf462463fe520eb1e06fa62"></a>

### `min_ce_len`

```c
uint16_t hci_cp_le_conn_update::min_ce_len
```

<a id="ab76ecdf6f7e5a5bb581cbd26f67d8f9f"></a>

### `supervision_timeout`

```c
uint16_t hci_cp_le_conn_update::supervision_timeout
```

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 22.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P021_gptp_uscaled_ns_结构体.md) · [返回大纲](大纲.md) · [下一章](P023_hdlc_api_结构体.md)
