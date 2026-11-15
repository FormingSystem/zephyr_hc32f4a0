---
id: learning.zephyr-docs.network-core-model-reference.page-155
title: net_trickle_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structnet__trickle.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第155章\_net\_trickle\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structnet__trickle.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

适用时，变量名直接取自RFC 6206。

```c
#include <zephyr/net/trickle.h>
```

<a id="details"></a>

适用时，变量名直接采用 RFC 6206 中的名称。注意，不应直接访问结构成员（Struct members），只能通过 Trickle API 访问。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 155.1\_数据成员（Data Fields）

<a id="r_a6186d8e41cce5193851587d1c72162ea"></a>

```c
uint32_t I
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[I](#a6186d8e41cce5193851587d1c72162ea)。

当前区间长度（Current interval size）。

<a id="r_aaf14e013a0fa74488a26cd7ff476f6e7"></a>

```c
uint32_t Imin
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[Imin](#aaf14e013a0fa74488a26cd7ff476f6e7)。

最小区间长度（Minimum interval size），单位为毫秒。

<a id="r_aab8a98c8a918528db6f2ddec85df4796"></a>

```c
uint32_t Istart
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[Istart](#aab8a98c8a918528db6f2ddec85df4796)。

区间起始时刻（Start of interval），单位为毫秒。

<a id="r_ae9f7ecd9b9730cd1c232ead5d21fec05"></a>

```c
uint32_t Imax_abs
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[Imax_abs](#ae9f7ecd9b9730cd1c232ead5d21fec05)。

最大区间长度（Maximum interval size），单位为毫秒，而非翻倍次数（Doublings）。

<a id="r_a01ffd968b645bb66db67c759520298aa"></a>

```c
uint8_t Imax
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[Imax](#a01ffd968b645bb66db67c759520298aa)。

最大翻倍次数（Maximum number of doublings）。

<a id="r_a7c3399e45f85874cec48434d605066d9"></a>

```c
uint8_t k
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[k](#a7c3399e45f85874cec48434d605066d9)。

冗余常量（Redundancy constant）。

<a id="r_aaa03f7763e6bd335b932896ee4433b3b"></a>

```c
uint8_t c
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[c](#aaa03f7763e6bd335b932896ee4433b3b)。

一致性计数器（Consistency counter）。

<a id="r_a2a1fb8ad04123ebcb781bc3e0173d8be"></a>

```c
bool double_to
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[double_to](#a2a1fb8ad04123ebcb781bc3e0173d8be)。

指示区间是否已翻倍的标志（Interval doubled flag）。

<a id="r_a2dde5d732f009a85a27ff6fa0c778636"></a>

```c
struct k_work_delayable timer
```

相关声明：[k_work_delayable](../kernel_runtime_model_reference/P009_k_work_delayable_结构体.md)、[timer](#a2dde5d732f009a85a27ff6fa0c778636)。

内部定时器结构（Internal timer struct）。

<a id="r_a63a3cbf019c99def91e3a9dde7c2f9b4"></a>

```c
net_trickle_cb_t cb
```

相关声明：[net_trickle_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__trickle.html#gaef7719dc563ae9bb93ed5313ed568b44)、[cb](#a63a3cbf019c99def91e3a9dde7c2f9b4)。

定时器到期（Timer expires）时调用的回调。

<a id="r_a40f69e10d41e34541ca88c092d6a3341"></a>

```c
void * user_data
```

相关声明：[user_data](#a40f69e10d41e34541ca88c092d6a3341)。

用户专用的不透明数据（Opaque Data）。

## 155.2\_详细说明（Detailed Documentation）

<a id="aaa03f7763e6bd335b932896ee4433b3b"></a>

### `c`

```c
uint8_t net_trickle::c
```

一致性计数器（Consistency counter）。

<a id="a63a3cbf019c99def91e3a9dde7c2f9b4"></a>

### `cb`

```c
net_trickle_cb_t net_trickle::cb
```

定时器到期（Timer expires）时调用的回调。

<a id="a2a1fb8ad04123ebcb781bc3e0173d8be"></a>

### `double_to`

```c
bool net_trickle::double_to
```

指示区间是否已翻倍的标志（Interval doubled flag）。

<a id="a6186d8e41cce5193851587d1c72162ea"></a>

### `I`

```c
uint32_t net_trickle::I
```

当前区间长度（Current interval size）。

<a id="a01ffd968b645bb66db67c759520298aa"></a>

### `Imax`

```c
uint8_t net_trickle::Imax
```

最大翻倍次数（Maximum number of doublings）。

<a id="ae9f7ecd9b9730cd1c232ead5d21fec05"></a>

### `Imax_abs`

```c
uint32_t net_trickle::Imax_abs
```

最大区间长度（Maximum interval size），单位为毫秒，而非翻倍次数（Doublings）。

<a id="aaf14e013a0fa74488a26cd7ff476f6e7"></a>

### `Imin`

```c
uint32_t net_trickle::Imin
```

最小区间长度（Minimum interval size），单位为毫秒。

<a id="aab8a98c8a918528db6f2ddec85df4796"></a>

### `Istart`

```c
uint32_t net_trickle::Istart
```

区间起始时刻（Start of interval），单位为毫秒。

<a id="a7c3399e45f85874cec48434d605066d9"></a>

### `k`

```c
uint8_t net_trickle::k
```

冗余常量（Redundancy constant）。

<a id="a2dde5d732f009a85a27ff6fa0c778636"></a>

### `timer`

```c
struct k_work_delayable net_trickle::timer
```

内部定时器结构（Internal timer struct）。

<a id="a40f69e10d41e34541ca88c092d6a3341"></a>

### `user_data`

```c
void* net_trickle::user_data
```

用户专用的不透明数据（Opaque Data）。

本数据类型文档由以下文件生成：

- `zephyr/net/trickle.h`

## 155.3\_原页交叉引用（Cross References）

- [RFC 6206](https://datatracker.ietf.org/doc/html/rfc6206)
- [zephyr/net/trickle.h](https://docs.zephyrproject.org/latest/doxygen/html/trickle_8h_source.html)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)
- [k_work_delayable](../kernel_runtime_model_reference/P009_k_work_delayable_结构体.md)
- [net_trickle_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__trickle.html#gaef7719dc563ae9bb93ed5313ed568b44)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P154_net_traffic_class_结构体.md) · [返回大纲](大纲.md) · [下一章](P156_net_tuple_结构体.md)
