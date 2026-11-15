---
id: learning.zephyr-docs.api-update-memory-topic-reference.page-15
title: Trickle 算法库（Trickle Algorithm Library）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__trickle.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第15章\_Trickle 算法库（Trickle Algorithm Library）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__trickle.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Trickle 算法库（Trickle algorithm library）

<a id="details"></a>

Trickle 算法库（Algorithm Library）。**引入版本（Since）：**1.7。**版本（Version）：**0.8.0。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 15.1\_数据结构（Data Structures）

<a id="r_net_5Ftrickle"></a>

```c
struct net_trickle
```

相关声明：[net_trickle](../network_core_model_reference/P155_net_trickle_结构体.md)。

适用时，变量名直接取自RFC 6206。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 15.2\_类型定义（Typedefs）

<a id="r_gaef7719dc563ae9bb93ed5313ed568b44"></a>

```c
typedef void(* net_trickle_cb_t) (struct net_trickle *trickle, bool do_suppress, void *user_data)
```

相关声明：[net_trickle_cb_t](#gaef7719dc563ae9bb93ed5313ed568b44)、[net_trickle](../network_core_model_reference/P155_net_trickle_结构体.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

Trickle 定时器回调（Timer Callback）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 15.3\_函数（Functions）

<a id="r_gac412d65ad2a8483920de32c1e0ae6be5"></a>

```c
int net_trickle_create (struct net_trickle *trickle, uint32_t Imin, uint8_t Imax, uint8_t k)
```

相关声明：[net_trickle_create](#gac412d65ad2a8483920de32c1e0ae6be5)、[net_trickle](../network_core_model_reference/P155_net_trickle_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

创建 Trickle 定时器（Timer）。

<a id="r_ga6674fac118a187320d73dc742f0e216f"></a>

```c
int net_trickle_start (struct net_trickle *trickle, net_trickle_cb_t cb, void *user_data)
```

相关声明：[net_trickle_start](#ga6674fac118a187320d73dc742f0e216f)、[net_trickle](../network_core_model_reference/P155_net_trickle_结构体.md)、[net_trickle_cb_t](#gaef7719dc563ae9bb93ed5313ed568b44)。

启动 Trickle 定时器（Timer）。

<a id="r_ga8477e45a95abccfb714e3f3369686c6d"></a>

```c
int net_trickle_stop (struct net_trickle *trickle)
```

相关声明：[net_trickle_stop](#ga8477e45a95abccfb714e3f3369686c6d)、[net_trickle](../network_core_model_reference/P155_net_trickle_结构体.md)。

停止 Trickle 定时器（Timer）。

<a id="r_gacefb4b5ba518fd1e3f776df012998a9b"></a>

```c
void net_trickle_consistency (struct net_trickle *trickle)
```

相关声明：[net_trickle_consistency](#gacefb4b5ba518fd1e3f776df012998a9b)、[net_trickle](../network_core_model_reference/P155_net_trickle_结构体.md)。

协议处理程序（Protocol Handler）监听到一致的网络传输（Consistent Network Transmission）时应调用此函数。

<a id="r_gad0815f9368a17532c8b5293a122cd8a9"></a>

```c
void net_trickle_inconsistency (struct net_trickle *trickle)
```

相关声明：[net_trickle_inconsistency](#gad0815f9368a17532c8b5293a122cd8a9)、[net_trickle](../network_core_model_reference/P155_net_trickle_结构体.md)。

协议处理程序（Protocol Handler）监听到不一致的网络传输（Inconsistent Network Transmission）时应调用此函数。

<a id="r_ga95ceb01a7d56ce5a9d9128a42e1f8eb9"></a>

```c
static bool net_trickle_is_running (struct net_trickle *trickle)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_trickle_is_running](#ga95ceb01a7d56ce5a9d9128a42e1f8eb9)、[net_trickle](../network_core_model_reference/P155_net_trickle_结构体.md)。

检查 Trickle 定时器是否正在运行（Running）。

## 15.4\_详细说明（Detailed Documentation）

<a id="gaef7719dc563ae9bb93ed5313ed568b44"></a>

### `net_trickle_cb_t`

```c
typedef void(* net_trickle_cb_t) (struct net_trickle *trickle, bool do_suppress, void *user_data)
```

```c
#include <zephyr/net/trickle.h>
```

Trickle 定时器回调（Timer Callback）。

Trickle 超时到期后调用此回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `Trickle Algorithm Library` | 要使用的 Trickle 上下文（Context）。 |
| `do_suppress` | 是否允许发送（TX）：`true` 表示允许，`false` 表示不允许。 |
| `user_data` | 调用 `net_trickle_start()` 时提供的用户数据（User Data）。 |

<a id="gacefb4b5ba518fd1e3f776df012998a9b"></a>

### `net_trickle_consistency()`

```c
void net_trickle_consistency ( struct net_trickle * trickle)
```

```c
#include <zephyr/net/trickle.h>
```

协议处理程序（Protocol Handler）监听到一致的网络传输（Consistent Network Transmission）时应调用此函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `Trickle Algorithm Library` | 指向 Trickle 结构体的指针。 |

<a id="gac412d65ad2a8483920de32c1e0ae6be5"></a>

### `net_trickle_create()`

```c
int net_trickle_create ( struct net_trickle * trickle, uint32_t Imin, uint8_t Imax, uint8_t k )
```

```c
#include <zephyr/net/trickle.h>
```

创建 Trickle 定时器（Timer）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `Trickle Algorithm Library` | 指向 Trickle 结构体的指针。 |
| `Imin` | `Imin` 配置参数，单位为毫秒（ms）。 |
| `Imax` | 最大翻倍次数（Maximum number of doublings）。 |
| `k` | 冗余常量（Redundancy Constant）参数，详情参见 RFC 6206。 |

**返回（Returns）**：**返回值（Returns）：**成功返回 0，出错返回小于 0 的值。

<a id="gad0815f9368a17532c8b5293a122cd8a9"></a>

### `net_trickle_inconsistency()`

```c
void net_trickle_inconsistency ( struct net_trickle * trickle)
```

```c
#include <zephyr/net/trickle.h>
```

协议处理程序（Protocol Handler）监听到不一致的网络传输（Inconsistent Network Transmission）时应调用此函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `Trickle Algorithm Library` | 指向 Trickle 结构体的指针。 |

<a id="ga95ceb01a7d56ce5a9d9128a42e1f8eb9"></a>

### `net_trickle_is_running()`

```c
bool net_trickle_is_running ( struct net_trickle * trickle)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/trickle.h>
```

检查 Trickle 定时器是否正在运行（Running）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `Trickle Algorithm Library` | 指向 Trickle 结构体的指针。 |

**返回（Returns）**：**返回值（Returns）：**定时器正在运行时返回 `True`，否则返回 `False`。

<a id="ga6674fac118a187320d73dc742f0e216f"></a>

### `net_trickle_start()`

```c
int net_trickle_start ( struct net_trickle * trickle, net_trickle_cb_t cb, void * user_data )
```

```c
#include <zephyr/net/trickle.h>
```

启动 Trickle 定时器（Timer）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `Trickle Algorithm Library` | 指向 Trickle 结构体的指针。 |
| `cb` | 在当前 Trickle 间隔内的时间 T 调用的用户回调（User Callback）。 |
| `user_data` | 传给回调的用户指针（User Pointer）。 |

**返回（Returns）**：**返回值（Returns）：**成功返回 0，出错返回小于 0 的值。

<a id="ga8477e45a95abccfb714e3f3369686c6d"></a>

### `net_trickle_stop()`

```c
int net_trickle_stop ( struct net_trickle * trickle)
```

```c
#include <zephyr/net/trickle.h>
```

停止 Trickle 定时器（Timer）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `Trickle Algorithm Library` | 指向 Trickle 结构体的指针。 |

**返回（Returns）**：**返回值（Returns）：**成功返回 0，出错返回小于 0 的值。


## 15.5\_原页交叉引用（Cross References）

- [net_trickle](../network_core_model_reference/P155_net_trickle_结构体.md)
- [RFC 6206](https://datatracker.ietf.org/doc/html/rfc6206)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [zephyr/net/trickle.h](../api_file_service_interface_reference/P053_zephyr__net__trickle.h_文件参考.md)
- [Trickle 算法库（Trickle Algorithm Library）](P015_Trickle 算法库（Trickle Algorithm Library）.md)

<a id="header-details"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P014_共享内存（Shared Memory）.md) · [返回大纲](大纲.md)
