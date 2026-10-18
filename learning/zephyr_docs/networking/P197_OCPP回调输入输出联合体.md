---
id: learning.zephyr-docs.networking.api-197
title: OCPP回调输入输出联合体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/unionocpp__io__value.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第197章\_OCPP回调输入输出联合体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/unionocpp__io__value.html)。读取日期：2026-10-14；基线为保存的 `latest` 页面，HTML 摘要见[来源记录](../SOURCES.md)。

## 197.1\_阅读说明与来源

译注：先读[OCPP 充电桩协议指南](P179_OCPP充电桩协议.md)和[充电桩示例](P182_OCPP充电桩示例.md)，理解充电桩（Charge Point，CP）、中央系统（Central System，CS）、连接器（Connector）、会话（Session）与交易（Transaction）的关系，再按符号查询。

本组：[OCPP完整API参考](P191_OCPP完整API参考.md) · [OCPP头文件参考](P192_OCPP头文件参考.md) · [OCPP头文件源码](P193_OCPP头文件源码.md) · [OCPP充电桩信息结构](P194_OCPP充电桩信息结构.md) · [OCPP中央系统信息结构](P195_OCPP中央系统信息结构.md) · [OCPP的TLS凭据结构](P196_OCPP的TLS凭据结构.md) · [OCPP回调输入输出联合体](P197_OCPP回调输入输出联合体.md)。

用于 OCPP 用户回调通知／请求的输入输出值。访问联合体（Union）成员时，应根据 `ocpp_notify_reason` 的枚举值选择对应成员。

```c
#include <zephyr/net/ocpp.h>
```

用于 OCPP 用户回调通知／请求的输入输出值。访问联合体（Union）成员时，应根据 `ocpp_notify_reason` 的枚举值选择对应成员。例如，回调原因为 `OCPP_USR_GET_METER_VALUE` 时，`meter_val` 结构成员有效。

## 197.2\_数据成员（Data Fields）

```c
struct {
```



<a id="r_ac17be67ed4bd306fc315f8be7aea8a98"></a>

```c
int id_con
```

提供给用户的输入：所请求的连接器标识 `connector_id`；`0` 表示主电表。

<a id="r_a49cce37916c99deee18817725825ac73"></a>

```c
enum ocpp_meter_measurand mes
```

提供给用户的输入：被测量（Measurand）。

相关声明：[ocpp_meter_measurand](P191_OCPP完整API参考.md#ga626b8c34f21c59cebdd844218a26f809)。

<a id="r_a1f0726c3e8ceab4883cf1363d3b7cfa7"></a>

```c
char val [50]
```

由用户填写的值，以字符串表示。

<a id="r_ae7d64324b4475b1c5ec15633c1a0aa4c"></a>

```c
} meter_val
```



```c
struct {
```



<a id="r_a4c902f0c1a279fe19eb768ea30665d5d"></a>

```c
char idtag [50]
```

提供给用户的输入。

<a id="r_ac1c1255bf159fa4c4014675cf1179d9b"></a>

```c
int id_con
```

提供给用户的可选输入。

<a id="r_acda3059ed054204148b9b5f7d320e958"></a>

```c
} start_charge
```



```c
struct {
```



<a id="r_a7d7d5a2eee62a2f0fff8c441b8130252"></a>

```c
int id_con
```

提供给用户的输入：需要停止充电的连接器。

<a id="r_aae16117ce8458ee8ed2ae394452a2571"></a>

```c
} stop_charge
```



```c
struct {
```



<a id="r_ad4f0d0ddad37beb065304837d3001e54"></a>

```c
int id_con
```

提供给用户的输入：需要解锁的连接器标识。

<a id="r_a2681a91a384efba554996e5090b31887"></a>

```c
} unlock_con
```



## 197.3\_详细说明（Detailed Documentation）

<a id="ae58818d242c3703f79adf32550608100"></a>

### `id_con`

```c
int ocpp_io_value::id_con
```

提供给用户的输入：所请求的连接器标识 `connector_id`；`0` 表示主电表。

提供给用户的输入：需要解锁的连接器标识。

提供给用户的输入：需要停止充电的连接器。

提供给用户的可选输入。

连接器标识为 `-1` 表示无效。

<a id="ae6005468ff90f70b97677ab189b36823"></a>

### `idtag`

```c
char ocpp_io_value::idtag[50]
```

提供给用户的输入。

<a id="a2ba720a5a05f4055a2fd2df55db729a9"></a>

### `mes`

```c
enum ocpp_meter_measurand ocpp_io_value::mes
```

提供给用户的输入：被测量（Measurand）。

<a id="ae7d64324b4475b1c5ec15633c1a0aa4c"></a>

### `[struct]`

```c
struct { ... } ocpp_io_value::meter_val
```

<a id="acda3059ed054204148b9b5f7d320e958"></a>

### `[struct]`

```c
struct { ... } ocpp_io_value::start_charge
```

<a id="aae16117ce8458ee8ed2ae394452a2571"></a>

### `[struct]`

```c
struct { ... } ocpp_io_value::stop_charge
```

<a id="a2681a91a384efba554996e5090b31887"></a>

### `[struct]`

```c
struct { ... } ocpp_io_value::unlock_con
```

<a id="aaf7363d38b1caecf7767c499a9cc5019"></a>

### `val`

```c
char ocpp_io_value::val[50]
```

由用户填写的值，以字符串表示。

## 197.4\_相关源码与使用边界

声明来自 `<zephyr/net/ocpp.h>`。本仓库的[对应头文件](../../../include/zephyr/net/ocpp.h)可用于源码追踪，版本可能与官网 `latest` 不同。源码核对依据为本批保存的[官方协议实现](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/ocpp/ocpp.c)、[官方请求实现](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/ocpp/core.c)及[官方示例](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/ocpp/src/main.c)，摘要见[来源记录](../SOURCES.md)。

> 译注——按原因选择成员：原生成页面把不同匿名结构中的 `id_con` 合并显示，容易误读为同一个顶层字段。实际应通过 `io->meter_val.id_con`、`io->start_charge.id_con` 等完整路径访问；有效分支由回调原因决定，不能同时把同一联合体内容解释成全部结构。

| 回调原因 | 有效成员 | 数据方向与约定 |
| --- | --- | --- |
| `OCPP_USR_GET_METER_VALUE` | `meter_val` | 读取 `id_con` 和 `mes`，填写字符串 `val`；连接器 0 表示主电表 |
| `OCPP_USR_START_CHARGING` | `start_charge` | 读取 `idtag` 与可选 `id_con`；-1 表示未提供有效连接器标识 |
| `OCPP_USR_STOP_CHARGING` | `stop_charge` | 读取需要停止充电的 `id_con` |
| `OCPP_USR_UNLOCK_CONNECTOR` | `unlock_con` | 读取需要解锁的 `id_con` |

译注：`CISTR50` 是固定数组容量。以 C 字符串填写 `val` 等数组时，还须为末尾空字符保留空间，不能把容量 50 理解成可写入 50 个非空字符后再追加结束符。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>
<a id="details"></a>
<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

[上一章](P196_OCPP的TLS凭据结构.md) · [返回大纲](大纲.md) · [下一章](P198_网络示例通用配置.md)
