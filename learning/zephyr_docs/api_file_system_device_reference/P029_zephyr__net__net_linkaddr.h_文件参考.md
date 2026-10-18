---
id: learning.zephyr-docs.api-file-system-device-reference.page-29
title: zephyr__net__net_linkaddr.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/net__linkaddr_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第29章\_zephyr\_\_net\_\_net\_linkaddr.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/net__linkaddr_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

网络链路地址（Network Link Address）的公共API。

<a id="details"></a>

```c
#include <zephyr/types.h>
#include <stdbool.h>
#include <errno.h>
```

查看此文件的源码。

网络链路地址（Network Link Address）的公共API。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 29.1\_数据结构（Data Structures）

<a id="r_net_5Flinkaddr"></a>

```c
struct net_linkaddr
```

相关声明：[net_linkaddr](../network_core_model_reference/P105_net_linkaddr_结构体.md)。

硬件链路地址（Hardware Link Address）结构。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 29.2\_宏定义（Macros）

<a id="r_ga5680cf2ac9302bbee824148f36193b2b"></a>

```c
#define NET_LINK_ADDR_MAX_LENGTH 6
```

相关声明：[NET_LINK_ADDR_MAX_LENGTH](https://docs.zephyrproject.org/latest/doxygen/html/group__net__linkaddr.html#ga5680cf2ac9302bbee824148f36193b2b)。

链路地址（link address）的最大长度。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 29.3\_枚举（Enumerations）

<a id="r_ga1312c2322bc4a4f1c3b76d6466806b24"></a>

```c
enum net_link_type { NET_LINK_UNKNOWN = 0 , NET_LINK_IEEE802154 , NET_LINK_BLUETOOTH , NET_LINK_ETHERNET , NET_LINK_DUMMY , NET_LINK_CANBUS_RAW }
```

相关声明：[net_link_type](https://docs.zephyrproject.org/latest/doxygen/html/group__net__linkaddr.html#ga1312c2322bc4a4f1c3b76d6466806b24)、[NET_LINK_UNKNOWN](https://docs.zephyrproject.org/latest/doxygen/html/group__net__linkaddr.html#gga1312c2322bc4a4f1c3b76d6466806b24a3e12f6af3333134a3e118fb16458bd34)、[NET_LINK_IEEE802154](https://docs.zephyrproject.org/latest/doxygen/html/group__net__linkaddr.html#gga1312c2322bc4a4f1c3b76d6466806b24a4f365da4c9300c31cd4022600e630ce3)、[NET_LINK_BLUETOOTH](https://docs.zephyrproject.org/latest/doxygen/html/group__net__linkaddr.html#gga1312c2322bc4a4f1c3b76d6466806b24abc3c811d04e998cbf498cc19644d182a)、[NET_LINK_ETHERNET](https://docs.zephyrproject.org/latest/doxygen/html/group__net__linkaddr.html#gga1312c2322bc4a4f1c3b76d6466806b24a7fc0b181a04fe90ca3a9c72170810d7b)、[NET_LINK_DUMMY](https://docs.zephyrproject.org/latest/doxygen/html/group__net__linkaddr.html#gga1312c2322bc4a4f1c3b76d6466806b24a7895ba2ce84de4c6dc03cbc57a87b7c8)、[NET_LINK_CANBUS_RAW](https://docs.zephyrproject.org/latest/doxygen/html/group__net__linkaddr.html#gga1312c2322bc4a4f1c3b76d6466806b24ab452eaef0ff58af43468da87ecfa404a)。

链路地址的类型。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 29.4\_函数（Functions）

<a id="r_ga36387353825a70fbe54dd16d076a9e26"></a>

```c
static bool net_linkaddr_cmp (struct net_linkaddr *lladdr1, struct net_linkaddr *lladdr2)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_linkaddr_cmp](https://docs.zephyrproject.org/latest/doxygen/html/group__net__linkaddr.html#ga36387353825a70fbe54dd16d076a9e26)、[net_linkaddr](../network_core_model_reference/P105_net_linkaddr_结构体.md)、[net_linkaddr](../network_core_model_reference/P105_net_linkaddr_结构体.md)。

比较两个链路层地址（link-layer addresses）。

<a id="r_gab0c451240b31d61749b724eaa6d61d45"></a>

```c
static int net_linkaddr_set (struct net_linkaddr *lladdr, const uint8_t *new_addr, uint8_t new_len)
```

相关声明：[net_linkaddr_set](https://docs.zephyrproject.org/latest/doxygen/html/group__net__linkaddr.html#gab0c451240b31d61749b724eaa6d61d45)、[net_linkaddr](../network_core_model_reference/P105_net_linkaddr_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置链路层地址存储结构体的成员数据。

<a id="r_ga1230eb353dd8f6671bf8ed31c464b712"></a>

```c
static int net_linkaddr_copy (struct net_linkaddr *dst, const struct net_linkaddr *src)
```

相关声明：[net_linkaddr_copy](https://docs.zephyrproject.org/latest/doxygen/html/group__net__linkaddr.html#ga1230eb353dd8f6671bf8ed31c464b712)、[net_linkaddr](../network_core_model_reference/P105_net_linkaddr_结构体.md)、[net_linkaddr](../network_core_model_reference/P105_net_linkaddr_结构体.md)。

将链路地址从一个变量复制到另一个变量。

<a id="r_gae8a73ee528b82ae36357bd066dc8128b"></a>

```c
static int net_linkaddr_create (struct net_linkaddr *lladdr, const uint8_t *addr, uint8_t len, enum net_link_type type)
```

相关声明：[net_linkaddr_create](https://docs.zephyrproject.org/latest/doxygen/html/group__net__linkaddr.html#gae8a73ee528b82ae36357bd066dc8128b)、[net_linkaddr](../network_core_model_reference/P105_net_linkaddr_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_link_type](https://docs.zephyrproject.org/latest/doxygen/html/group__net__linkaddr.html#ga1312c2322bc4a4f1c3b76d6466806b24)。

创建链路地址结构体。

<a id="r_ga4061ecaf3b1c4c06968ef6a744de0185"></a>

```c
static int net_linkaddr_clear (struct net_linkaddr *lladdr)
```

相关声明：[net_linkaddr_clear](https://docs.zephyrproject.org/latest/doxygen/html/group__net__linkaddr.html#ga4061ecaf3b1c4c06968ef6a744de0185)、[net_linkaddr](../network_core_model_reference/P105_net_linkaddr_结构体.md)。

清除链路地址。


## 29.5\_原页交叉引用（Cross References）

- [zephyr/types.h](../api_source_compiler_device_reference/P014_types.h_源码浏览.md)
- [stdbool.h](../api_source_supplement_reference/P186_stdbool.h_源码浏览.md)
- [errno.h](../error_reference/P005_错误号头文件源码.md)
- [查看此文件的源码。](../api_source_reference/P576_net_linkaddr.h_源码浏览.md)
- [net_linkaddr](../network_core_model_reference/P105_net_linkaddr_结构体.md)
- [NET_LINK_ADDR_MAX_LENGTH](https://docs.zephyrproject.org/latest/doxygen/html/group__net__linkaddr.html#ga5680cf2ac9302bbee824148f36193b2b)
- [net_link_type](https://docs.zephyrproject.org/latest/doxygen/html/group__net__linkaddr.html#ga1312c2322bc4a4f1c3b76d6466806b24)
- [NET_LINK_UNKNOWN](https://docs.zephyrproject.org/latest/doxygen/html/group__net__linkaddr.html#gga1312c2322bc4a4f1c3b76d6466806b24a3e12f6af3333134a3e118fb16458bd34)
- [NET_LINK_IEEE802154](https://docs.zephyrproject.org/latest/doxygen/html/group__net__linkaddr.html#gga1312c2322bc4a4f1c3b76d6466806b24a4f365da4c9300c31cd4022600e630ce3)
- [NET_LINK_BLUETOOTH](https://docs.zephyrproject.org/latest/doxygen/html/group__net__linkaddr.html#gga1312c2322bc4a4f1c3b76d6466806b24abc3c811d04e998cbf498cc19644d182a)
- [NET_LINK_ETHERNET](https://docs.zephyrproject.org/latest/doxygen/html/group__net__linkaddr.html#gga1312c2322bc4a4f1c3b76d6466806b24a7fc0b181a04fe90ca3a9c72170810d7b)
- [NET_LINK_DUMMY](https://docs.zephyrproject.org/latest/doxygen/html/group__net__linkaddr.html#gga1312c2322bc4a4f1c3b76d6466806b24a7895ba2ce84de4c6dc03cbc57a87b7c8)
- [NET_LINK_CANBUS_RAW](https://docs.zephyrproject.org/latest/doxygen/html/group__net__linkaddr.html#gga1312c2322bc4a4f1c3b76d6466806b24ab452eaef0ff58af43468da87ecfa404a)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [net_linkaddr_cmp](https://docs.zephyrproject.org/latest/doxygen/html/group__net__linkaddr.html#ga36387353825a70fbe54dd16d076a9e26)
- [net_linkaddr_set](https://docs.zephyrproject.org/latest/doxygen/html/group__net__linkaddr.html#gab0c451240b31d61749b724eaa6d61d45)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [net_linkaddr_copy](https://docs.zephyrproject.org/latest/doxygen/html/group__net__linkaddr.html#ga1230eb353dd8f6671bf8ed31c464b712)
- [net_linkaddr_create](https://docs.zephyrproject.org/latest/doxygen/html/group__net__linkaddr.html#gae8a73ee528b82ae36357bd066dc8128b)
- [net_linkaddr_clear](https://docs.zephyrproject.org/latest/doxygen/html/group__net__linkaddr.html#ga4061ecaf3b1c4c06968ef6a744de0185)

<a id="header-details"></a>

---

[上一章](P028_zephyr__mpipe__base__mpipe_app_src.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P030_zephyr__dt-bindings__pinctrl__numicro-pinctrl.h_文件参考.md)
