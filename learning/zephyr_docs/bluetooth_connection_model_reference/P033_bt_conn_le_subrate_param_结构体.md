---
id: learning.zephyr-docs.bluetooth-connection-model-reference.page-33
title: bt_conn_le_subrate_param_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__conn__le__subrate__param.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第33章\_bt\_conn\_le\_subrate\_param\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__conn__le__subrate__param.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

LE 连接的连接子速率参数。

```c
#include <zephyr/bluetooth/conn.h>
```

<a id="details"></a>

LE 连接的连接子速率参数。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 33.1\_数据成员（Data Fields）

<a id="r_aef75fec8ba8c9987d55e81aa2539b96e"></a>

```c
uint16_t subrate_min
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[subrate_min](#aef75fec8ba8c9987d55e81aa2539b96e)。

最小子速率因子（Minimum subrate factor）。

<a id="r_a59d2d244e3568b8f97ce936121d41b1a"></a>

```c
uint16_t subrate_max
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[subrate_max](#a59d2d244e3568b8f97ce936121d41b1a)。

最大子速率因子（Maximum subrate factor）。

<a id="r_a15d05324708ddeea8d2f3515eea396bb"></a>

```c
uint16_t max_latency
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[max_latency](#a15d05324708ddeea8d2f3515eea396bb)。

最大外设延迟（Maximum Peripheral latency），以子速率连接间隔（Subrated connection intervals）为单位。

<a id="r_a978cef5f2f14a5a7fe7ded09c6fdf2d9"></a>

```c
uint16_t continuation_number
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[continuation_number](#a978cef5f2f14a5a7fe7ded09c6fdf2d9)。

发送或接收到包含长度字段（Length field）非零的链路层协议数据单元（Link Layer PDU）的数据包后，继续保持活动状态的底层连接事件最小数量（Underlying connection events）。

<a id="r_aca0897d00a1dd1735dbbaf5bfde711ed"></a>

```c
uint16_t supervision_timeout
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[supervision_timeout](#aca0897d00a1dd1735dbbaf5bfde711ed)。

连接监督超时（Connection Supervision timeout），为 N × 10 毫秒。

## 33.2\_详细说明（Detailed Documentation）

<a id="a978cef5f2f14a5a7fe7ded09c6fdf2d9"></a>

### `continuation_number`

```c
uint16_t bt_conn_le_subrate_param::continuation_number
```

发送或接收到包含长度字段（Length field）非零的链路层协议数据单元（Link Layer PDU）的数据包后，继续保持活动状态的底层连接事件最小数量（Underlying connection events）。

<a id="a15d05324708ddeea8d2f3515eea396bb"></a>

### `max_latency`

```c
uint16_t bt_conn_le_subrate_param::max_latency
```

最大外设延迟（Maximum Peripheral latency），以子速率连接间隔（Subrated connection intervals）为单位。

<a id="a59d2d244e3568b8f97ce936121d41b1a"></a>

### `subrate_max`

```c
uint16_t bt_conn_le_subrate_param::subrate_max
```

最大子速率因子（Maximum subrate factor）。

<a id="aef75fec8ba8c9987d55e81aa2539b96e"></a>

### `subrate_min`

```c
uint16_t bt_conn_le_subrate_param::subrate_min
```

最小子速率因子（Minimum subrate factor）。

<a id="aca0897d00a1dd1735dbbaf5bfde711ed"></a>

### `supervision_timeout`

```c
uint16_t bt_conn_le_subrate_param::supervision_timeout
```

连接监督超时（Connection Supervision timeout），为 N × 10 毫秒。

使用 `bt_conn_le_subrate_set_defaults` 时，此值表示允许外设（Peripheral）在请求中指定的最大监督超时（Supervision timeout）。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/conn.h`

## 33.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/conn.h](https://docs.zephyrproject.org/latest/doxygen/html/conn_8h_source.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [bt_conn_le_subrate_set_defaults](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gac7bb456c530c7e08b4fa9f4d478fdaf9)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P032_bt_conn_le_subrate_changed_结构体.md) · [返回大纲](大纲.md) · [下一章](P034_bt_conn_le_subrating_info_结构体.md)
