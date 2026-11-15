---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-30
title: bt_hci_cp_le_conn_param_req_reply_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cp__le__conn__param__req__reply.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第30章\_bt\_hci\_cp\_le\_conn\_param\_req\_reply\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cp__le__conn__param__req__reply.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 30.1\_数据成员（Data Fields）

<a id="r_aa3b938afe13d4e05806fb6cdfab5cb14"></a>

```c
uint16_t handle
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[handle](#aa3b938afe13d4e05806fb6cdfab5cb14)。

<a id="r_a10547c7d4836980947d17bbde0d75a51"></a>

```c
uint16_t interval_min
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[interval_min](#a10547c7d4836980947d17bbde0d75a51)。

<a id="r_aed58f9aa722a284ae39df842394c06cf"></a>

```c
uint16_t interval_max
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[interval_max](#aed58f9aa722a284ae39df842394c06cf)。

<a id="r_a8c76816cc230387c249ab8e05c402964"></a>

```c
uint16_t latency
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[latency](#a8c76816cc230387c249ab8e05c402964)。

<a id="r_af25a3f226ceccbe19e7f1482ed5f141e"></a>

```c
uint16_t timeout
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[timeout](#af25a3f226ceccbe19e7f1482ed5f141e)。

<a id="r_a512d605d5c4aacf81b78794fcf260abf"></a>

```c
uint16_t min_ce_len
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[min_ce_len](#a512d605d5c4aacf81b78794fcf260abf)。

<a id="r_a932e6a3a45ec0409656325f7246d5d7e"></a>

```c
uint16_t max_ce_len
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[max_ce_len](#a932e6a3a45ec0409656325f7246d5d7e)。

## 30.2\_详细说明（Detailed Documentation）

<a id="aa3b938afe13d4e05806fb6cdfab5cb14"></a>

### `handle`

```c
uint16_t bt_hci_cp_le_conn_param_req_reply::handle
```

<a id="aed58f9aa722a284ae39df842394c06cf"></a>

### `interval_max`

```c
uint16_t bt_hci_cp_le_conn_param_req_reply::interval_max
```

<a id="a10547c7d4836980947d17bbde0d75a51"></a>

### `interval_min`

```c
uint16_t bt_hci_cp_le_conn_param_req_reply::interval_min
```

<a id="a8c76816cc230387c249ab8e05c402964"></a>

### `latency`

```c
uint16_t bt_hci_cp_le_conn_param_req_reply::latency
```

<a id="a932e6a3a45ec0409656325f7246d5d7e"></a>

### `max_ce_len`

```c
uint16_t bt_hci_cp_le_conn_param_req_reply::max_ce_len
```

<a id="a512d605d5c4aacf81b78794fcf260abf"></a>

### `min_ce_len`

```c
uint16_t bt_hci_cp_le_conn_param_req_reply::min_ce_len
```

<a id="af25a3f226ceccbe19e7f1482ed5f141e"></a>

### `timeout`

```c
uint16_t bt_hci_cp_le_conn_param_req_reply::timeout
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 30.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P029_bt_hci_cp_le_conn_param_req_neg_reply_结构体.md) · [返回大纲](大纲.md) · [下一章](P031_bt_hci_cp_le_create_big_结构体.md)
