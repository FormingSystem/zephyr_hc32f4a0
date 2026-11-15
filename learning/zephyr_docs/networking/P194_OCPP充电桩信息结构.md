---
id: learning.zephyr-docs.networking.api-194
title: OCPP充电桩信息结构
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structocpp__cp__info.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第194章\_OCPP充电桩信息结构

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structocpp__cp__info.html)。读取日期：2026-10-14；基线为保存的 `latest` 页面，HTML 摘要见[来源记录](../SOURCES.md)。

## 194.1\_阅读说明与来源

译注：先读[OCPP 充电桩协议指南](P179_OCPP充电桩协议.md)和[充电桩示例](P182_OCPP充电桩示例.md)，理解充电桩（Charge Point，CP）、中央系统（Central System，CS）、连接器（Connector）、会话（Session）与交易（Transaction）的关系，再按符号查询。

本组：[OCPP完整API参考](P191_OCPP完整API参考.md) · [OCPP头文件参考](P192_OCPP头文件参考.md) · [OCPP头文件源码](P193_OCPP头文件源码.md) · [OCPP充电桩信息结构](P194_OCPP充电桩信息结构.md) · [OCPP中央系统信息结构](P195_OCPP中央系统信息结构.md) · [OCPP的TLS凭据结构](P196_OCPP的TLS凭据结构.md) · [OCPP回调输入输出联合体](P197_OCPP回调输入输出联合体.md)。

传给 `ocpp_init` 的充电桩（Charge Point，CP）信息参数。除 `num_of_con` 外，各项均为字符串字面量（String Literal）。

```c
#include <zephyr/net/ocpp.h>
```

传给 `ocpp_init` 的充电桩（Charge Point，CP）信息参数。除 `num_of_con` 外，各项均为字符串字面量（String Literal）。

## 194.2\_数据成员（Data Fields）

<a id="r_a28f4cc142ecd584a4d2477092f7f1c3f"></a>

```c
char * model
```

充电桩（Charge Point，CP）型号。

<a id="r_a273f5ed3ef61465bda6c54033be994bd"></a>

```c
char * vendor
```

充电桩厂商。

<a id="r_af2cdde4d27e0223644456842240723e2"></a>

```c
int num_of_con
```

最大数量。

<a id="r_a52ad8e1e7509f56e13c9f45b821e354c"></a>

```c
char * sl_no
```

可选字段（Optional Fields）。

<a id="r_a5b6dcc9c966a09f15e38ac927237f2e1"></a>

```c
char * box_sl_no
```

箱体序列号（Box Serial Number）。

<a id="r_a7c043b50beb91d98f546b809867e8405"></a>

```c
char * fw_ver
```

固件版本（Firmware Version）。

<a id="r_a22553b2e207558ea51915cc45f4a385c"></a>

```c
char * iccid
```

集成电路卡标识（Integrated Circuit Card Identifier，ICCID）。

<a id="r_ae7cae41736a48a01377c5e230adef80c"></a>

```c
char * imsi
```

国际移动用户识别码（International Mobile Subscriber Identity，IMSI）。

<a id="r_a38e5219ba817bb7cfcf9ab7582b594f2"></a>

```c
char * meter_sl_no
```

主电能表序列号。

<a id="r_a7876ac178c93df2065fe95bae76c274d"></a>

```c
char * meter_type
```

主电能表类型。

## 194.3\_详细说明（Detailed Documentation）

<a id="a5b6dcc9c966a09f15e38ac927237f2e1"></a>

### `box_sl_no`

```c
char* ocpp_cp_info::box_sl_no
```

箱体序列号（Box Serial Number）。

<a id="a7c043b50beb91d98f546b809867e8405"></a>

### `fw_ver`

```c
char* ocpp_cp_info::fw_ver
```

固件版本（Firmware Version）。

<a id="a22553b2e207558ea51915cc45f4a385c"></a>

### `iccid`

```c
char* ocpp_cp_info::iccid
```

集成电路卡标识（Integrated Circuit Card Identifier，ICCID）。

<a id="ae7cae41736a48a01377c5e230adef80c"></a>

### `imsi`

```c
char* ocpp_cp_info::imsi
```

国际移动用户识别码（International Mobile Subscriber Identity，IMSI）。

<a id="a38e5219ba817bb7cfcf9ab7582b594f2"></a>

### `meter_sl_no`

```c
char* ocpp_cp_info::meter_sl_no
```

主电能表序列号。

<a id="a7876ac178c93df2065fe95bae76c274d"></a>

### `meter_type`

```c
char* ocpp_cp_info::meter_type
```

主电能表类型。

<a id="a28f4cc142ecd584a4d2477092f7f1c3f"></a>

### `model`

```c
char* ocpp_cp_info::model
```

充电桩（Charge Point，CP）型号。

<a id="af2cdde4d27e0223644456842240723e2"></a>

### `num_of_con`

```c
int ocpp_cp_info::num_of_con
```

最大数量。

所支持的连接器数量。

<a id="a52ad8e1e7509f56e13c9f45b821e354c"></a>

### `sl_no`

```c
char* ocpp_cp_info::sl_no
```

可选字段（Optional Fields）。

充电桩序列号。

<a id="a273f5ed3ef61465bda6c54033be994bd"></a>

### `vendor`

```c
char* ocpp_cp_info::vendor
```

充电桩厂商。

## 194.4\_相关源码与使用边界

声明来自 `<zephyr/net/ocpp.h>`。本仓库的[对应头文件](../../../include/zephyr/net/ocpp.h)可用于源码追踪，版本可能与官网 `latest` 不同。源码核对依据为本批保存的[官方协议实现](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/ocpp/ocpp.c)、[官方请求实现](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/ocpp/core.c)及[官方示例](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/ocpp/src/main.c)，摘要见[来源记录](../SOURCES.md)。

> 译注：`num_of_con` 表示支持的最大连接器数量，原页将“Max.”和后半句拆开显示。`sl_no` 及其后的序列号、固件、移动网络标识和电表信息为可选字段。头文件实际使用 `char *` 表示字符串；原文的“字符串字面量”不是说这些字段内嵌存放固定长度字符数组。当前初始化检查 `model`、`vendor` 非空且连接器数量至少为 1。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>
<a id="details"></a>
<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

[上一章](P193_OCPP头文件源码.md) · [返回大纲](大纲.md) · [下一章](P195_OCPP中央系统信息结构.md)
