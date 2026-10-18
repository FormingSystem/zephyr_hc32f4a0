---
id: learning.zephyr-docs.network-service-model-reference.page-10
title: ethernet_qav_param_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structethernet__qav__param.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第10章\_ethernet\_qav\_param\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structethernet__qav__param.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

以太网Qav的专用参数。

```c
#include <zephyr/net/ethernet.h>
```

<a id="details"></a>

以太网Qav的专用参数。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 10.1\_数据成员（Data Fields）

<a id="r_a4e2d2967669b758422c166140af0c1ba"></a>

```c
int queue_id
```

相关声明：[queue_id](#a4e2d2967669b758422c166140af0c1ba)。

要使用的优先级队列 ID。

<a id="r_a38861d9f790a61aa88801cb1373077a8"></a>

```c
enum ethernet_qav_param_type type
```

相关声明：[type](#a38861d9f790a61aa88801cb1373077a8)。

Qav 参数类型。

```c
union {
```

<a id="r_ac3c69f2649e969110b5e47373f4d5ea3"></a>

```c
bool enabled
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[enabled](#a031d3896b14eb8b32c3c050738421b85)。

队列启用了 Qav 时为 `true`。

<a id="r_a1522287e976e087674c98736e6b6bc41"></a>

```c
unsigned int delta_bandwidth
```

相关声明：[unsigned](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a4089fb16419d359081465355db05f846)、[delta_bandwidth](#a6fde906da905c0598aaa2056c330b6f4)。

带宽增量（Delta Bandwidth），以带宽百分比表示。

<a id="r_aa297635f7cef0810a0b00ba010b37778"></a>

```c
unsigned int idle_slope
```

相关声明：[unsigned](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a4089fb16419d359081465355db05f846)、[idle_slope](#a6d43b199549cade0a07dc10adac85bff)。

空闲斜率（Idle Slope），单位为 bit/s。

<a id="r_a03bcc5b1a249b9568967d4fba0511332"></a>

```c
unsigned int oper_idle_slope
```

相关声明：[unsigned](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a4089fb16419d359081465355db05f846)、[oper_idle_slope](#a0691f10a338d3c49a58d94a1adced477)。

运行态空闲斜率（Oper Idle Slope），单位为 bit/s。

<a id="r_a24f2513113531b8552a5cc5b89cb7979"></a>

```c
unsigned int traffic_class
```

相关声明：[unsigned](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a4089fb16419d359081465355db05f846)、[traffic_class](#a4a795e4a0c7d5bcbe8212d79f772dc6f)。

队列所绑定的流量类别（traffic class）。

<a id="r_aaf80d9556ce4ae4699de67d0cd05a2e4"></a>

```c
};
```

所选 Qav 参数类型对应的值。

## 10.2\_详细说明（Detailed Documentation）

<a id="aaf80d9556ce4ae4699de67d0cd05a2e4"></a>

### `[union]`

```c
union { ... } ethernet_qav_param
```

所选 Qav 参数类型对应的值。

<a id="a6fde906da905c0598aaa2056c330b6f4"></a>

### `delta_bandwidth`

```c
unsigned int ethernet_qav_param::delta_bandwidth
```

带宽增量（Delta Bandwidth），以带宽百分比表示。

<a id="a031d3896b14eb8b32c3c050738421b85"></a>

### `enabled`

```c
bool ethernet_qav_param::enabled
```

队列启用了 Qav 时为 `true`。

<a id="a6d43b199549cade0a07dc10adac85bff"></a>

### `idle_slope`

```c
unsigned int ethernet_qav_param::idle_slope
```

空闲斜率（Idle Slope），单位为 bit/s。

<a id="a0691f10a338d3c49a58d94a1adced477"></a>

### `oper_idle_slope`

```c
unsigned int ethernet_qav_param::oper_idle_slope
```

运行态空闲斜率（Oper Idle Slope），单位为 bit/s。

<a id="a4e2d2967669b758422c166140af0c1ba"></a>

### `queue_id`

```c
int ethernet_qav_param::queue_id
```

要使用的优先级队列 ID。

<a id="a4a795e4a0c7d5bcbe8212d79f772dc6f"></a>

### `traffic_class`

```c
unsigned int ethernet_qav_param::traffic_class
```

队列所绑定的流量类别（traffic class）。

<a id="a38861d9f790a61aa88801cb1373077a8"></a>

### `type`

```c
enum ethernet_qav_param_type ethernet_qav_param::type
```

Qav 参数类型。

本数据类型文档由以下文件生成：

- `zephyr/net/ethernet.h`

## 10.3\_原页交叉引用（Cross References）

- [zephyr/net/ethernet.h](https://docs.zephyrproject.org/latest/doxygen/html/ethernet_8h_source.html)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)
- [unsigned](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a4089fb16419d359081465355db05f846)
- [ethernet_qav_param](P010_ethernet_qav_param_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P009_ethernet_lldp_结构体.md) · [返回大纲](大纲.md) · [下一章](P011_ethernet_qbu_param_结构体.md)
