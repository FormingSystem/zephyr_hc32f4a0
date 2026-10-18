---
id: learning.zephyr-docs.api-input-runtime-topic-reference.page-15
title: 网络链路地址库（Network Link Address Library）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__net__linkaddr.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第15章\_网络链路地址库（Network Link Address Library）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__net__linkaddr.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

网络链路地址库（Network link address library）

<a id="details"></a>

网络链路地址库（Network Link Address Library）。**引入版本（Since）：**1.0。**版本（Version）：**1.0.0。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 15.1\_数据结构（Data Structures）

<a id="r_net_5Flinkaddr"></a>

```c
struct net_linkaddr
```

相关声明：[net_linkaddr](../network_core_model_reference/P105_net_linkaddr_结构体.md)。

硬件链路地址（Hardware Link Address）结构。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 15.2\_宏定义（Macros）

<a id="r_ga5680cf2ac9302bbee824148f36193b2b"></a>

```c
#define NET_LINK_ADDR_MAX_LENGTH 6
```

相关声明：[NET_LINK_ADDR_MAX_LENGTH](#ga5680cf2ac9302bbee824148f36193b2b)。

链路地址（link address）的最大长度。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 15.3\_枚举（Enumerations）

<a id="r_ga1312c2322bc4a4f1c3b76d6466806b24"></a>

```c
enum net_link_type { NET_LINK_UNKNOWN = 0 , NET_LINK_IEEE802154 , NET_LINK_BLUETOOTH , NET_LINK_ETHERNET , NET_LINK_DUMMY , NET_LINK_CANBUS_RAW }
```

相关声明：[net_link_type](#ga1312c2322bc4a4f1c3b76d6466806b24)、[NET_LINK_UNKNOWN](#gga1312c2322bc4a4f1c3b76d6466806b24a3e12f6af3333134a3e118fb16458bd34)、[NET_LINK_IEEE802154](#gga1312c2322bc4a4f1c3b76d6466806b24a4f365da4c9300c31cd4022600e630ce3)、[NET_LINK_BLUETOOTH](#gga1312c2322bc4a4f1c3b76d6466806b24abc3c811d04e998cbf498cc19644d182a)、[NET_LINK_ETHERNET](#gga1312c2322bc4a4f1c3b76d6466806b24a7fc0b181a04fe90ca3a9c72170810d7b)、[NET_LINK_DUMMY](#gga1312c2322bc4a4f1c3b76d6466806b24a7895ba2ce84de4c6dc03cbc57a87b7c8)、[NET_LINK_CANBUS_RAW](#gga1312c2322bc4a4f1c3b76d6466806b24ab452eaef0ff58af43468da87ecfa404a)。

链路地址的类型。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 15.4\_函数（Functions）

<a id="r_ga36387353825a70fbe54dd16d076a9e26"></a>

```c
static bool net_linkaddr_cmp (struct net_linkaddr *lladdr1, struct net_linkaddr *lladdr2)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_linkaddr_cmp](#ga36387353825a70fbe54dd16d076a9e26)、[net_linkaddr](../network_core_model_reference/P105_net_linkaddr_结构体.md)、[net_linkaddr](../network_core_model_reference/P105_net_linkaddr_结构体.md)。

比较两个链路层地址（link-layer addresses）。

<a id="r_gab0c451240b31d61749b724eaa6d61d45"></a>

```c
static int net_linkaddr_set (struct net_linkaddr *lladdr, const uint8_t *new_addr, uint8_t new_len)
```

相关声明：[net_linkaddr_set](#gab0c451240b31d61749b724eaa6d61d45)、[net_linkaddr](../network_core_model_reference/P105_net_linkaddr_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置链路层地址存储结构体的成员数据。

<a id="r_ga1230eb353dd8f6671bf8ed31c464b712"></a>

```c
static int net_linkaddr_copy (struct net_linkaddr *dst, const struct net_linkaddr *src)
```

相关声明：[net_linkaddr_copy](#ga1230eb353dd8f6671bf8ed31c464b712)、[net_linkaddr](../network_core_model_reference/P105_net_linkaddr_结构体.md)、[net_linkaddr](../network_core_model_reference/P105_net_linkaddr_结构体.md)。

将链路地址从一个变量复制到另一个变量。

<a id="r_gae8a73ee528b82ae36357bd066dc8128b"></a>

```c
static int net_linkaddr_create (struct net_linkaddr *lladdr, const uint8_t *addr, uint8_t len, enum net_link_type type)
```

相关声明：[net_linkaddr_create](#gae8a73ee528b82ae36357bd066dc8128b)、[net_linkaddr](../network_core_model_reference/P105_net_linkaddr_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_link_type](#ga1312c2322bc4a4f1c3b76d6466806b24)。

创建链路地址结构体。

<a id="r_ga4061ecaf3b1c4c06968ef6a744de0185"></a>

```c
static int net_linkaddr_clear (struct net_linkaddr *lladdr)
```

相关声明：[net_linkaddr_clear](#ga4061ecaf3b1c4c06968ef6a744de0185)、[net_linkaddr](../network_core_model_reference/P105_net_linkaddr_结构体.md)。

清除链路地址。

## 15.5\_详细说明（Detailed Documentation）

<a id="ga5680cf2ac9302bbee824148f36193b2b"></a>

### `NET_LINK_ADDR_MAX_LENGTH`

```c
#define NET_LINK_ADDR_MAX_LENGTH 6
```

```c
#include <zephyr/net/net_linkaddr.h>
```

链路地址（link address）的最大长度。

<a id="ga1312c2322bc4a4f1c3b76d6466806b24"></a>

### `net_link_type`

```c
enum net_link_type
```

```c
#include <zephyr/net/net_linkaddr.h>
```

链路地址的类型。

表示该地址用于哪种网络技术（Network Technology）。为节省空间，此值存储在 `uint8_t` 变量中，因此不要向此枚举加入大于 `255` 的值。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `NET_LINK_UNKNOWN` | 未知链路地址类型（Unknown Link Address Type）。 |
| `NET_LINK_IEEE802154` | IEEE 802.15.4 链路地址（Link Address）。 |
| `NET_LINK_BLUETOOTH` | 蓝牙 IPSP 链路地址（Link Address）。 |
| `NET_LINK_ETHERNET` | 以太网链路地址（Ethernet Link Address）。 |
| `NET_LINK_DUMMY` | 虚拟链路地址（Dummy Link Address），用于测试应用和回环支持（Loopback Support）。 |
| `NET_LINK_CANBUS_RAW` | CAN 总线链路地址（CANBUS Link Address）。 |

<a id="ga4061ecaf3b1c4c06968ef6a744de0185"></a>

### `net_linkaddr_clear()`

```c
int net_linkaddr_clear ( struct net_linkaddr * lladdr)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/net_linkaddr.h>
```

清除链路地址。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `lladdr` | 链路地址结构体（Link Address Structure）。 |

返回（Returns）：成功时为0，出错时小于0。

<a id="ga36387353825a70fbe54dd16d076a9e26"></a>

### `net_linkaddr_cmp()`

```c
bool net_linkaddr_cmp ( struct net_linkaddr * lladdr1, struct net_linkaddr * lladdr2 )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/net_linkaddr.h>
```

比较两个链路层地址（link-layer addresses）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `lladdr1` | 指向链路层地址（Link Layer Address）的指针。 |
| `lladdr2` | 指向链路层地址（Link Layer Address）的指针。 |

**返回（Returns）**：**返回值（Returns）：**地址相同返回 `true`，否则返回 `false`。

<a id="ga1230eb353dd8f6671bf8ed31c464b712"></a>

### `net_linkaddr_copy()`

```c
int net_linkaddr_copy ( struct net_linkaddr * dst, const struct net_linkaddr * src )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/net_linkaddr.h>
```

将链路地址从一个变量复制到另一个变量。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dst` | 目标链路地址结构体（Destination Link Address Structure）。 |
| `src` | 源链路地址结构体（Source Link Address Structure）。 |

返回（Returns）：成功时为0，出错时小于0。

<a id="gae8a73ee528b82ae36357bd066dc8128b"></a>

### `net_linkaddr_create()`

```c
int net_linkaddr_create ( struct net_linkaddr * lladdr, const uint8_t * addr, uint8_t len, enum net_link_type type )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/net_linkaddr.h>
```

创建链路地址结构体。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `lladdr` | 要修改的链路地址结构体（Link Address Structure）。 |
| `addr` | 包含链路地址（Link Address）的字节数组；设为 `NULL` 时清除地址。 |
| `len` | 链路地址数组长度（Link Address Array Length）。 |
| `type` | 链路地址的类型。 |

返回（Returns）：成功时为0，出错时小于0。

<a id="gab0c451240b31d61749b724eaa6d61d45"></a>

### `net_linkaddr_set()`

```c
int net_linkaddr_set ( struct net_linkaddr * lladdr, const uint8_t * new_addr, uint8_t new_len )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/net_linkaddr.h>
```

设置链路层地址存储结构体的成员数据。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `lladdr` | 要修改的链路地址存储结构体（Link Address Storage Structure）。 |
| `new_addr` | 包含链路地址（Link Address）的字节数组。 |
| `new_len` | 链路地址数组长度（Link Address Array Length），必须始终小于或等于 `NET_LINK_ADDR_MAX_LENGTH`。 |

返回（Returns）：成功时为0，出错时小于0。


## 15.6\_原页交叉引用（Cross References）

- [net_linkaddr](../network_core_model_reference/P105_net_linkaddr_结构体.md)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [zephyr/net/net_linkaddr.h](../api_file_system_device_reference/P029_zephyr__net__net_linkaddr.h_文件参考.md)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="gga1312c2322bc4a4f1c3b76d6466806b24a3e12f6af3333134a3e118fb16458bd34"></a>
<a id="gga1312c2322bc4a4f1c3b76d6466806b24a4f365da4c9300c31cd4022600e630ce3"></a>
<a id="gga1312c2322bc4a4f1c3b76d6466806b24abc3c811d04e998cbf498cc19644d182a"></a>
<a id="gga1312c2322bc4a4f1c3b76d6466806b24a7fc0b181a04fe90ca3a9c72170810d7b"></a>
<a id="gga1312c2322bc4a4f1c3b76d6466806b24a7895ba2ce84de4c6dc03cbc57a87b7c8"></a>
<a id="gga1312c2322bc4a4f1c3b76d6466806b24ab452eaef0ff58af43468da87ecfa404a"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P014_线程（Threads）.md) · [返回大纲](大纲.md) · [下一章](P016_系统电源协议（System Power Protocol）.md)
