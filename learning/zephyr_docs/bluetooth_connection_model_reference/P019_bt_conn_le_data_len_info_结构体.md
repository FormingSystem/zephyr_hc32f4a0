---
id: learning.zephyr-docs.bluetooth-connection-model-reference.page-19
title: bt_conn_le_data_len_info_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__conn__le__data__len__info.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第19章\_bt\_conn\_le\_data\_len\_info\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__conn__le__data__len__info.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

LE 连接的连接数据长度（Connection Data Length）信息。

```c
#include <zephyr/bluetooth/conn.h>
```

<a id="details"></a>

LE 连接的连接数据长度（Connection Data Length）信息。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 19.1\_数据成员（Data Fields）

<a id="r_a48d175f3c4b03dbdee129feae3edab23"></a>

```c
uint16_t tx_max_len
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[tx_max_len](#a48d175f3c4b03dbdee129feae3edab23)。

链路层发送载荷的最大大小（Maximum Link Layer transmission payload size），单位为字节。

<a id="r_a14288429cbbcce2ef34580a581815eb7"></a>

```c
uint16_t tx_max_time
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[tx_max_time](#a14288429cbbcce2ef34580a581815eb7)。

链路层发送载荷的最长时间（Maximum Link Layer transmission payload time），单位为微秒。

<a id="r_a18ddc603e922586e331187c9b29f2908"></a>

```c
uint16_t rx_max_len
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[rx_max_len](#a18ddc603e922586e331187c9b29f2908)。

链路层接收载荷的最大大小（Maximum Link Layer reception payload size），单位为字节。

<a id="r_af2316cdc921e9ec19491501e15248f73"></a>

```c
uint16_t rx_max_time
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[rx_max_time](#af2316cdc921e9ec19491501e15248f73)。

链路层接收载荷的最长时间（Maximum Link Layer reception payload time），单位为微秒。

## 19.2\_详细说明（Detailed Documentation）

<a id="a18ddc603e922586e331187c9b29f2908"></a>

### `rx_max_len`

```c
uint16_t bt_conn_le_data_len_info::rx_max_len
```

链路层接收载荷的最大大小（Maximum Link Layer reception payload size），单位为字节。

<a id="af2316cdc921e9ec19491501e15248f73"></a>

### `rx_max_time`

```c
uint16_t bt_conn_le_data_len_info::rx_max_time
```

链路层接收载荷的最长时间（Maximum Link Layer reception payload time），单位为微秒。

<a id="a48d175f3c4b03dbdee129feae3edab23"></a>

### `tx_max_len`

```c
uint16_t bt_conn_le_data_len_info::tx_max_len
```

链路层发送载荷的最大大小（Maximum Link Layer transmission payload size），单位为字节。

<a id="a14288429cbbcce2ef34580a581815eb7"></a>

### `tx_max_time`

```c
uint16_t bt_conn_le_data_len_info::tx_max_time
```

链路层发送载荷的最长时间（Maximum Link Layer transmission payload time），单位为微秒。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/conn.h`

## 19.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/conn.h](https://docs.zephyrproject.org/latest/doxygen/html/conn_8h_source.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P018_bt_conn_le_cs_subevent_result_结构体.md) · [返回大纲](大纲.md) · [下一章](P020_bt_conn_le_data_len_param_结构体.md)
