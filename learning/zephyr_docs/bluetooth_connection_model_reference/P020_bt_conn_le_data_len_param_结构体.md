---
id: learning.zephyr-docs.bluetooth-connection-model-reference.page-20
title: bt_conn_le_data_len_param_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__conn__le__data__len__param.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第20章\_bt\_conn\_le\_data\_len\_param\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__conn__le__data__len__param.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

LE 连接的连接数据长度参数。

```c
#include <zephyr/bluetooth/conn.h>
```

<a id="details"></a>

LE 连接的连接数据长度参数。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 20.1\_数据成员（Data Fields）

<a id="r_a8b279a0dc72c70aaf5205558fd4b4c4a"></a>

```c
uint16_t tx_max_len
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[tx_max_len](#a8b279a0dc72c70aaf5205558fd4b4c4a)。

链路层发送载荷的最大大小（Maximum Link Layer transmission payload size），单位为字节。

<a id="r_a9046542952fa822b944602b398562e6e"></a>

```c
uint16_t tx_max_time
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[tx_max_time](#a9046542952fa822b944602b398562e6e)。

链路层发送载荷的最长时间（Maximum Link Layer transmission payload time），单位为微秒。

## 20.2\_详细说明（Detailed Documentation）

<a id="a8b279a0dc72c70aaf5205558fd4b4c4a"></a>

### `tx_max_len`

```c
uint16_t bt_conn_le_data_len_param::tx_max_len
```

链路层发送载荷的最大大小（Maximum Link Layer transmission payload size），单位为字节。

<a id="a9046542952fa822b944602b398562e6e"></a>

### `tx_max_time`

```c
uint16_t bt_conn_le_data_len_param::tx_max_time
```

链路层发送载荷的最长时间（Maximum Link Layer transmission payload time），单位为微秒。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/conn.h`

## 20.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/conn.h](https://docs.zephyrproject.org/latest/doxygen/html/conn_8h_source.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P019_bt_conn_le_data_len_info_结构体.md) · [返回大纲](大纲.md) · [下一章](P021_bt_conn_le_frame_space_update_param_结构体.md)
