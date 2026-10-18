---
id: learning.zephyr-docs.network-service-model-reference.page-11
title: ethernet_qbu_param_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structethernet__qbu__param.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第11章\_ethernet\_qbu\_param\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structethernet__qbu__param.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

以太网Qbu的专用参数。

```c
#include <zephyr/net/ethernet.h>
```

<a id="details"></a>

以太网Qbu的专用参数。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 11.1\_数据成员（Data Fields）

<a id="r_ae6d61f0c9d2f2e56eb494db953a5e846"></a>

```c
int port_id
```

相关声明：[port_id](#ae6d61f0c9d2f2e56eb494db953a5e846)。

端口 ID。

<a id="r_a4a8a3d26a12a06a787ae6b35ea40c37a"></a>

```c
enum ethernet_qbu_param_type type
```

相关声明：[type](#a4a8a3d26a12a06a787ae6b35ea40c37a)。

Qbu 参数类型。

```c
union {
```

<a id="r_af90c070fa093d610b003238a3e413a13"></a>

```c
uint32_t hold_advance
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[hold_advance](#a8ffde09a540817b7a68c7180c327196f)。

保持提前量（Hold advance），单位为纳秒。

<a id="r_a10ca11a5505982721c121e51cf178d08"></a>

```c
uint32_t release_advance
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[release_advance](#a3f62d0462376225c8609c7e26ebd314b)。

释放提前量（Release advance），单位为纳秒。

<a id="r_a710a5f6abc61a2f52dd98fdbb5426f0c"></a>

```c
enum ethernet_qbu_preempt_status frame_preempt_statuses [NET_TC_TX_COUNT]
```

相关声明：[frame_preempt_statuses](#a3f5dfd9cfbc1ec86896eaf517bdc5c88)。

`framePreemptionAdminStatus` 值的序列。

<a id="r_a91e59ad613ec3e1da241ba047f7278b2"></a>

```c
bool enabled
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[enabled](#a9717dd68adde62a454593d72fdbc43a5)。

启用 Qbu 时为 `true`，否则为 `false`。

<a id="r_a7eac9a89811395e89bc5ff443042fcbc"></a>

```c
bool link_partner_status
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[link_partner_status](#ad8c92a7f7b4aa124adaa62dd4e65b5ca)。

链路伙伴状态（Link partner status），来自 Qbr。

<a id="r_a309af3373e2497983dbc3b30176b4a9e"></a>

```c
uint8_t additional_fragment_size: 2
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[additional_fragment_size](#afb455507b29d84de42638e47ecacadeb)。

附加分片大小（Additional fragment size），来自 Qbr。

<a id="r_a2caabdb2d8a69b83360c79f15fa1206e"></a>

```c
};
```

所选 Qbu 参数类型对应的值。

## 11.2\_详细说明（Detailed Documentation）

<a id="a2caabdb2d8a69b83360c79f15fa1206e"></a>

### `[union]`

```c
union { ... } ethernet_qbu_param
```

所选 Qbu 参数类型对应的值。

<a id="afb455507b29d84de42638e47ecacadeb"></a>

### `additional_fragment_size`

```c
uint8_t ethernet_qbu_param::additional_fragment_size
```

附加分片大小（Additional fragment size），来自 Qbr。

非末尾分片的最小大小为 `(additional_fragment_size + 1) * 64` 个八位字节。

<a id="a9717dd68adde62a454593d72fdbc43a5"></a>

### `enabled`

```c
bool ethernet_qbu_param::enabled
```

启用 Qbu 时为 `true`，否则为 `false`。

<a id="a3f5dfd9cfbc1ec86896eaf517bdc5c88"></a>

### `frame_preempt_statuses`

```c
enum ethernet_qbu_preempt_status ethernet_qbu_param::frame_preempt_statuses[NET_TC_TX_COUNT]
```

`framePreemptionAdminStatus` 值的序列。

<a id="a8ffde09a540817b7a68c7180c327196f"></a>

### `hold_advance`

```c
uint32_t ethernet_qbu_param::hold_advance
```

保持提前量（Hold advance），单位为纳秒。

<a id="ad8c92a7f7b4aa124adaa62dd4e65b5ca"></a>

### `link_partner_status`

```c
bool ethernet_qbu_param::link_partner_status
```

链路伙伴状态（Link partner status），来自 Qbr。

<a id="ae6d61f0c9d2f2e56eb494db953a5e846"></a>

### `port_id`

```c
int ethernet_qbu_param::port_id
```

端口 ID。

<a id="a3f62d0462376225c8609c7e26ebd314b"></a>

### `release_advance`

```c
uint32_t ethernet_qbu_param::release_advance
```

释放提前量（Release advance），单位为纳秒。

<a id="a4a8a3d26a12a06a787ae6b35ea40c37a"></a>

### `type`

```c
enum ethernet_qbu_param_type ethernet_qbu_param::type
```

Qbu 参数类型。

本数据类型文档由以下文件生成：

- `zephyr/net/ethernet.h`

## 11.3\_原页交叉引用（Cross References）

- [zephyr/net/ethernet.h](https://docs.zephyrproject.org/latest/doxygen/html/ethernet_8h_source.html)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [ethernet_qbu_param](P011_ethernet_qbu_param_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P010_ethernet_qav_param_结构体.md) · [返回大纲](大纲.md) · [下一章](P012_ethernet_qbv_param_结构体.md)
