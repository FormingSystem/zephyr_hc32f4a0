---
id: learning.zephyr-docs.device-power-control-model-reference.page-114
title: pd_header_联合体
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/unionpd__header.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第114章\_pd\_header\_联合体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/unionpd__header.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

构造电力传输（PD）消息头部，见表6-1“消息头部”。

```c
#include <zephyr/drivers/usb_c/usbc_pd.h>
```

<a id="details"></a>

构造电力传输（PD）消息头部，见表6-1“消息头部”。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 114.1\_数据成员（Data Fields）

```c
struct {
```

<a id="r_af63e8a6bdfc4d21f1cb4383cafa55203"></a>

```c
uint16_t message_type: 5
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[message_type](#a70768acc6a6bc9ebb9249df7ed635a94)。

消息类型。

<a id="r_a4eb617977e479b03fa646ed21ca05221"></a>

```c
uint16_t port_data_role: 1
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[port_data_role](#af1b027c9c57497421117b290dcb6ac66)。

端口数据角色（Port Data Role）。

<a id="r_ae3f38bde804176ceb10452e9470f2744"></a>

```c
uint16_t specification_revision: 2
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[specification_revision](#a85cce1728afe0d62bb29f618a1cf70e1)。

规范修订版本（Specification Revision）。

<a id="r_a9ab32ffd9f7eab8bccb07926a7311d27"></a>

```c
uint16_t port_power_role: 1
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[port_power_role](#a20ac99d9738c9d278a78e8ccfc401902)。

端口电源角色（Port Power Role）。

<a id="r_af81549240b259415aef0c0704db9bea9"></a>

```c
uint16_t message_id: 3
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[message_id](#ae4a0a5695e73fd3e1b7e3f38cd2a758c)。

消息编号（Message ID）。

<a id="r_a0fcbe9efc709a11a2ea7d0f6cdf92445"></a>

```c
uint16_t number_of_data_objects: 3
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[number_of_data_objects](#a63d89119f0918ba7d6eb9e01fa1ed406)。

数据对象（Data Objects）的数量。

<a id="r_a2aa7c3278710cbd6bd3f82f9dfcffb73"></a>

```c
uint16_t extended: 1
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[extended](#a5750b964c12c3bc2d2523a64cb9eb7d0)。

扩展消息（Extended Message）。

<a id="r_a3b4f5771e6e0fe0072d310732ea43959"></a>

```c
};
```

PD 消息头字段。

<a id="r_afa6c6699be5fe95bcb4962396e33e35d"></a>

```c
uint16_t raw_value
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[raw_value](#afa6c6699be5fe95bcb4962396e33e35d)。

原始 PD 消息头值。

## 114.2\_详细说明（Detailed Documentation）

<a id="a3b4f5771e6e0fe0072d310732ea43959"></a>

### `[struct]`

```c
struct { ... } pd_header
```

PD 消息头字段。

<a id="a5750b964c12c3bc2d2523a64cb9eb7d0"></a>

### `extended`

```c
uint16_t pd_header::extended
```

扩展消息（Extended Message）。

<a id="ae4a0a5695e73fd3e1b7e3f38cd2a758c"></a>

### `message_id`

```c
uint16_t pd_header::message_id
```

消息编号（Message ID）。

<a id="a70768acc6a6bc9ebb9249df7ed635a94"></a>

### `message_type`

```c
uint16_t pd_header::message_type
```

消息类型。

<a id="a63d89119f0918ba7d6eb9e01fa1ed406"></a>

### `number_of_data_objects`

```c
uint16_t pd_header::number_of_data_objects
```

数据对象（Data Objects）的数量。

<a id="af1b027c9c57497421117b290dcb6ac66"></a>

### `port_data_role`

```c
uint16_t pd_header::port_data_role
```

端口数据角色（Port Data Role）。

<a id="a20ac99d9738c9d278a78e8ccfc401902"></a>

### `port_power_role`

```c
uint16_t pd_header::port_power_role
```

端口电源角色（Port Power Role）。

<a id="afa6c6699be5fe95bcb4962396e33e35d"></a>

### `raw_value`

```c
uint16_t pd_header::raw_value
```

原始 PD 消息头值。

<a id="a85cce1728afe0d62bb29f618a1cf70e1"></a>

### `specification_revision`

```c
uint16_t pd_header::specification_revision
```

规范修订版本（Specification Revision）。

本数据类型文档由以下文件生成：

- `zephyr/drivers/usb_c/usbc_pd.h`

## 114.3\_原页交叉引用（Cross References）

- [zephyr/drivers/usb_c/usbc_pd.h](https://docs.zephyrproject.org/latest/doxygen/html/usbc__pd_8h_source.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [pd_header](P114_pd_header_联合体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P113_pd_fixed_supply_pdo_source_联合体.md) · [返回大纲](大纲.md) · [下一章](P115_pd_rdo_联合体.md)
