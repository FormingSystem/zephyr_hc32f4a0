---
id: learning.zephyr-docs.api-file-service-interface-reference.page-53
title: zephyr__net__trickle.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/trickle_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第53章\_zephyr\_\_net\_\_trickle.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/trickle_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Trickle定时器库（Timer Library）。

<a id="details"></a>

```c
#include <stdbool.h>
#include <zephyr/types.h>
#include <zephyr/kernel.h>
#include <zephyr/net/net_core.h>
```

查看此文件的源码。

Trickle 定时器库（Timer Library），实现 RFC 6206 规定的 Trickle 定时器。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 53.1\_数据结构（Data Structures）

<a id="r_net_5Ftrickle"></a>

```c
struct net_trickle
```

相关声明：[net_trickle](../network_core_model_reference/P155_net_trickle_结构体.md)。

适用时，变量名直接取自RFC 6206。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 53.2\_类型定义（Typedefs）

<a id="r_gaef7719dc563ae9bb93ed5313ed568b44"></a>

```c
typedef void(* net_trickle_cb_t) (struct net_trickle *trickle, bool do_suppress, void *user_data)
```

相关声明：[net_trickle_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__trickle.html#gaef7719dc563ae9bb93ed5313ed568b44)、[net_trickle](../network_core_model_reference/P155_net_trickle_结构体.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

Trickle 定时器回调（Timer Callback）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 53.3\_函数（Functions）

<a id="r_gac412d65ad2a8483920de32c1e0ae6be5"></a>

```c
int net_trickle_create (struct net_trickle *trickle, uint32_t Imin, uint8_t Imax, uint8_t k)
```

相关声明：[net_trickle_create](https://docs.zephyrproject.org/latest/doxygen/html/group__trickle.html#gac412d65ad2a8483920de32c1e0ae6be5)、[net_trickle](../network_core_model_reference/P155_net_trickle_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

创建 Trickle 定时器（Timer）。

<a id="r_ga6674fac118a187320d73dc742f0e216f"></a>

```c
int net_trickle_start (struct net_trickle *trickle, net_trickle_cb_t cb, void *user_data)
```

相关声明：[net_trickle_start](https://docs.zephyrproject.org/latest/doxygen/html/group__trickle.html#ga6674fac118a187320d73dc742f0e216f)、[net_trickle](../network_core_model_reference/P155_net_trickle_结构体.md)、[net_trickle_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__trickle.html#gaef7719dc563ae9bb93ed5313ed568b44)。

启动 Trickle 定时器（Timer）。

<a id="r_ga8477e45a95abccfb714e3f3369686c6d"></a>

```c
int net_trickle_stop (struct net_trickle *trickle)
```

相关声明：[net_trickle_stop](https://docs.zephyrproject.org/latest/doxygen/html/group__trickle.html#ga8477e45a95abccfb714e3f3369686c6d)、[net_trickle](../network_core_model_reference/P155_net_trickle_结构体.md)。

停止 Trickle 定时器（Timer）。

<a id="r_gacefb4b5ba518fd1e3f776df012998a9b"></a>

```c
void net_trickle_consistency (struct net_trickle *trickle)
```

相关声明：[net_trickle_consistency](https://docs.zephyrproject.org/latest/doxygen/html/group__trickle.html#gacefb4b5ba518fd1e3f776df012998a9b)、[net_trickle](../network_core_model_reference/P155_net_trickle_结构体.md)。

协议处理程序（Protocol Handler）监听到一致的网络传输（Consistent Network Transmission）时应调用此函数。

<a id="r_gad0815f9368a17532c8b5293a122cd8a9"></a>

```c
void net_trickle_inconsistency (struct net_trickle *trickle)
```

相关声明：[net_trickle_inconsistency](https://docs.zephyrproject.org/latest/doxygen/html/group__trickle.html#gad0815f9368a17532c8b5293a122cd8a9)、[net_trickle](../network_core_model_reference/P155_net_trickle_结构体.md)。

协议处理程序（Protocol Handler）监听到不一致的网络传输（Inconsistent Network Transmission）时应调用此函数。

<a id="r_ga95ceb01a7d56ce5a9d9128a42e1f8eb9"></a>

```c
static bool net_trickle_is_running (struct net_trickle *trickle)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_trickle_is_running](https://docs.zephyrproject.org/latest/doxygen/html/group__trickle.html#ga95ceb01a7d56ce5a9d9128a42e1f8eb9)、[net_trickle](../network_core_model_reference/P155_net_trickle_结构体.md)。

检查 Trickle 定时器是否正在运行（Running）。


## 53.4\_原页交叉引用（Cross References）

- [stdbool.h](../api_source_supplement_reference/P186_stdbool.h_源码浏览.md)
- [zephyr/types.h](../api_source_compiler_device_reference/P014_types.h_源码浏览.md)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h_source.html)
- [zephyr/net/net_core.h](../api_source_system_reference/P023_net_core.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P877_trickle.h_源码浏览.md)
- [net_trickle](../network_core_model_reference/P155_net_trickle_结构体.md)
- [RFC 6206](https://datatracker.ietf.org/doc/html/rfc6206)
- [net_trickle_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__trickle.html#gaef7719dc563ae9bb93ed5313ed568b44)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [net_trickle_create](https://docs.zephyrproject.org/latest/doxygen/html/group__trickle.html#gac412d65ad2a8483920de32c1e0ae6be5)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [net_trickle_start](https://docs.zephyrproject.org/latest/doxygen/html/group__trickle.html#ga6674fac118a187320d73dc742f0e216f)
- [net_trickle_stop](https://docs.zephyrproject.org/latest/doxygen/html/group__trickle.html#ga8477e45a95abccfb714e3f3369686c6d)
- [net_trickle_consistency](https://docs.zephyrproject.org/latest/doxygen/html/group__trickle.html#gacefb4b5ba518fd1e3f776df012998a9b)
- [net_trickle_inconsistency](https://docs.zephyrproject.org/latest/doxygen/html/group__trickle.html#gad0815f9368a17532c8b5293a122cd8a9)
- [net_trickle_is_running](https://docs.zephyrproject.org/latest/doxygen/html/group__trickle.html#ga95ceb01a7d56ce5a9d9128a42e1f8eb9)

<a id="header-details"></a>

---

[上一章](P052_zephyr__drivers__misc__tmc6460__tmc6460.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P054_zephyr__drivers__usb__usb_bc12.h_文件参考.md)
