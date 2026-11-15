---
id: learning.zephyr-docs.api-power-policy-topic-reference.page-9
title: 基本过滤条件（Basic Filter Conditions）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__npf__basic__cond.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第9章\_基本过滤条件（Basic Filter Conditions）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__npf__basic__cond.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

<a id="details"></a>

**引入版本（Since）：**3.0。**版本（Version）：**0.8.0。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 9.1\_宏定义（Macros）

<a id="r_ga465578272b616c6267ecd13fd86ca73b"></a>

```c
#define NPF_IFACE_MATCH(_name, _iface)
```

相关声明：[NPF_IFACE_MATCH](#ga465578272b616c6267ecd13fd86ca73b)。

静态定义“接口匹配”（Interface Match）数据包过滤条件（Packet Filter Condition）。

<a id="r_gac3607a6736d70b0ea044a2ec7ab6d313"></a>

```c
#define NPF_IFACE_UNMATCH(_name, _iface)
```

相关声明：[NPF_IFACE_UNMATCH](#gac3607a6736d70b0ea044a2ec7ab6d313)。

静态定义“接口不匹配”（Interface Unmatch）数据包过滤条件（Packet Filter Condition）。

<a id="r_ga55021acd131e4684568aaf6434b08789"></a>

```c
#define NPF_ORIG_IFACE_MATCH(_name, _iface)
```

相关声明：[NPF_ORIG_IFACE_MATCH](#ga55021acd131e4684568aaf6434b08789)。

静态定义“原始接口匹配”（Orig Interface Match）数据包过滤条件（Packet Filter Condition）。

<a id="r_gad959dc62d47ca3b4d2f24a6c862c7623"></a>

```c
#define NPF_ORIG_IFACE_UNMATCH(_name, _iface)
```

相关声明：[NPF_ORIG_IFACE_UNMATCH](#gad959dc62d47ca3b4d2f24a6c862c7623)。

静态定义“原始接口不匹配”（Orig Interface Unmatch）数据包过滤条件（Packet Filter Condition）。

<a id="r_gaf142455f9bea3dea8faa0a913072b63e"></a>

```c
#define NPF_SIZE_MIN(_name, _size)
```

相关声明：[NPF_SIZE_MIN](#gaf142455f9bea3dea8faa0a913072b63e)。

静态定义“数据最小大小”（Data Minimum Size）数据包过滤条件（Packet Filter Condition）。

<a id="r_gacd56b9bcf2b2ba4759402650a9bff67a"></a>

```c
#define NPF_SIZE_MAX(_name, _size)
```

相关声明：[NPF_SIZE_MAX](#gacd56b9bcf2b2ba4759402650a9bff67a)。

静态定义“数据最大大小”（Data Maximum Size）数据包过滤条件（Packet Filter Condition）。

<a id="r_gab402bb13c7899d57532d3dcf8a36ed4b"></a>

```c
#define NPF_SIZE_BOUNDS(_name, _min_size, _max_size)
```

相关声明：[NPF_SIZE_BOUNDS](#gab402bb13c7899d57532d3dcf8a36ed4b)。

静态定义“数据大小范围”（Data Bounded Size）数据包过滤条件（Packet Filter Condition）。

<a id="r_ga4dd013f0fb92eb0433f174cf40e89e00"></a>

```c
#define NPF_IP_SRC_ADDR_ALLOWLIST(_name, _ip_addr_array, _ip_addr_num, _af)
```

相关声明：[NPF_IP_SRC_ADDR_ALLOWLIST](#ga4dd013f0fb92eb0433f174cf40e89e00)。

静态定义“IP 地址允许列表”（IP Address Allowlist）数据包过滤条件（Packet Filter Condition）。

<a id="r_ga57fe28a992b1afaf33581292fe5015bd"></a>

```c
#define NPF_IP_SRC_ADDR_BLOCKLIST(_name, _ip_addr_array, _ip_addr_num, _af)
```

相关声明：[NPF_IP_SRC_ADDR_BLOCKLIST](#ga57fe28a992b1afaf33581292fe5015bd)。

静态定义“IP 地址阻止列表”（IP Address Blocklist）数据包过滤条件（Packet Filter Condition）。

## 9.2\_详细说明（Detailed Documentation）

<a id="ga465578272b616c6267ecd13fd86ca73b"></a>

### `NPF_IFACE_MATCH`

```c
#define NPF_IFACE_MATCH ( _name, _iface )
```

```c
#include <zephyr/net/net_pkt_filter.h>
```

展开值（Value）：

```c
struct npf_test_iface _name = {                                 \
        .iface = (_iface),                                      \
        .test.fn = npf_iface_match,                             \
        IF_ENABLED(NPF_TEST_ENABLE_NAME,                        \
                   (.test.name = "iface",                       \
                    .test.type = NPF_TEST_TYPE_IFACE_MATCH,))   \
}
```

静态定义“接口匹配”（Interface Match）数据包过滤条件（Packet Filter Condition）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_name` | 条件名称（Condition Name）。 |
| `_iface` | 要匹配的接口（Interface）。 |

<a id="gac3607a6736d70b0ea044a2ec7ab6d313"></a>

### `NPF_IFACE_UNMATCH`

```c
#define NPF_IFACE_UNMATCH ( _name, _iface )
```

```c
#include <zephyr/net/net_pkt_filter.h>
```

展开值（Value）：

```c
struct npf_test_iface _name = {                                 \
        .iface = (_iface),                                      \
        .test.fn = npf_iface_unmatch,                           \
        IF_ENABLED(NPF_TEST_ENABLE_NAME,                        \
                   (.test.name = "!iface",                      \
                    .test.type = NPF_TEST_TYPE_IFACE_UNMATCH,)) \
}
```

静态定义“接口不匹配”（Interface Unmatch）数据包过滤条件（Packet Filter Condition）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_name` | 条件名称（Condition Name）。 |
| `_iface` | 要排除的接口（Interface）。 |

<a id="ga4dd013f0fb92eb0433f174cf40e89e00"></a>

### `NPF_IP_SRC_ADDR_ALLOWLIST`

```c
#define NPF_IP_SRC_ADDR_ALLOWLIST ( _name, _ip_addr_array, _ip_addr_num, _af )
```

```c
#include <zephyr/net/net_pkt_filter.h>
```

展开值（Value）：

```c
struct npf_test_ip _name = {                                    \
        .addr_family = _af,                                     \
        .ipaddr = (_ip_addr_array),                             \
        .ipaddr_num = _ip_addr_num,                             \
        .test.fn = npf_ip_src_addr_match,                       \
        IF_ENABLED(NPF_TEST_ENABLE_NAME,                        \
                   (.test.name = "ip src allow",                \
                    .test.type = NPF_TEST_TYPE_IP_SRC_ADDR_ALLOWLIST,)) \
}
```

静态定义“IP 地址允许列表”（IP Address Allowlist）数据包过滤条件（Packet Filter Condition）。

测试数据包源 IP 地址（Source IP Address）是否与给定集合中的任意 IP 地址匹配。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_name` | 条件名称（Condition Name）。 |
| `_ip_addr_array` | 用于匹配测试的 `struct net_in_addr` 或 `struct net_in6_addr` 元素数组。 |
| `_ip_addr_num` | 数组中的 IP 地址数量。 |
| `_af` | 数组中的地址族类型（Address Family Type），为 `NET_AF_INET`／`NET_AF_INET6`。 |

<a id="ga57fe28a992b1afaf33581292fe5015bd"></a>

### `NPF_IP_SRC_ADDR_BLOCKLIST`

```c
#define NPF_IP_SRC_ADDR_BLOCKLIST ( _name, _ip_addr_array, _ip_addr_num, _af )
```

```c
#include <zephyr/net/net_pkt_filter.h>
```

展开值（Value）：

```c
struct npf_test_ip _name = {                                    \
        .addr_family = _af,                                     \
        .ipaddr = (_ip_addr_array),                             \
        .ipaddr_num = _ip_addr_num,                             \
        .test.fn = npf_ip_src_addr_unmatch,                     \
        IF_ENABLED(NPF_TEST_ENABLE_NAME,                        \
                   (.test.name = "ip src block",                \
                    .test.type = NPF_TEST_TYPE_IP_SRC_ADDR_BLOCKLIST,)) \
}
```

静态定义“IP 地址阻止列表”（IP Address Blocklist）数据包过滤条件（Packet Filter Condition）。

测试数据包源 IP 地址（Source IP Address）是否与给定集合中的任意 IP 地址匹配。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_name` | 条件名称（Condition Name）。 |
| `_ip_addr_array` | 用于匹配测试的 `struct net_in_addr` 或 `struct net_in6_addr` 元素数组。 |
| `_ip_addr_num` | 数组中的 IP 地址数量。 |
| `_af` | 数组中的地址族类型（Address Family Type），为 `NET_AF_INET`／`NET_AF_INET6`。 |

<a id="ga55021acd131e4684568aaf6434b08789"></a>

### `NPF_ORIG_IFACE_MATCH`

```c
#define NPF_ORIG_IFACE_MATCH ( _name, _iface )
```

```c
#include <zephyr/net/net_pkt_filter.h>
```

展开值（Value）：

```c
struct npf_test_iface _name = {                                 \
        .iface = (_iface),                                      \
        .test.fn = npf_orig_iface_match,                        \
        IF_ENABLED(NPF_TEST_ENABLE_NAME,                        \
                   (.test.name = "orig iface",                  \
                    .test.type = NPF_TEST_TYPE_ORIG_IFACE_MATCH,)) \
}
```

静态定义“原始接口匹配”（Orig Interface Match）数据包过滤条件（Packet Filter Condition）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_name` | 条件名称（Condition Name）。 |
| `_iface` | 要匹配的接口（Interface）。 |

<a id="gad959dc62d47ca3b4d2f24a6c862c7623"></a>

### `NPF_ORIG_IFACE_UNMATCH`

```c
#define NPF_ORIG_IFACE_UNMATCH ( _name, _iface )
```

```c
#include <zephyr/net/net_pkt_filter.h>
```

展开值（Value）：

```c
struct npf_test_iface _name = {                                 \
        .iface = (_iface),                                      \
        .test.fn = npf_orig_iface_unmatch,                      \
        IF_ENABLED(NPF_TEST_ENABLE_NAME,                        \
                   (.test.name = "!orig iface",                 \
                    .test.type = NPF_TEST_TYPE_ORIG_IFACE_UNMATCH,)) \
}
```

静态定义“原始接口不匹配”（Orig Interface Unmatch）数据包过滤条件（Packet Filter Condition）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_name` | 条件名称（Condition Name）。 |
| `_iface` | 要排除的接口（Interface）。 |

<a id="gab402bb13c7899d57532d3dcf8a36ed4b"></a>

### `NPF_SIZE_BOUNDS`

```c
#define NPF_SIZE_BOUNDS ( _name, _min_size, _max_size )
```

```c
#include <zephyr/net/net_pkt_filter.h>
```

展开值（Value）：

```c
struct npf_test_size_bounds _name = {                         \
        .min = (_min_size),                                   \
        .max = (_max_size),                                   \
        .test.fn = npf_size_inbounds,                         \
        IF_ENABLED(NPF_TEST_ENABLE_NAME,                      \
                   (.test.name = "size bounds",               \
                    .test.type = NPF_TEST_TYPE_SIZE_BOUNDS,)) \
}
```

静态定义“数据大小范围”（Data Bounded Size）数据包过滤条件（Packet Filter Condition）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_name` | 条件名称（Condition Name）。 |
| `_min_size` | 数据包数据大小（Data Size）的下界。 |
| `_max_size` | 数据包数据大小（Data Size）的上界。 |

<a id="gacd56b9bcf2b2ba4759402650a9bff67a"></a>

### `NPF_SIZE_MAX`

```c
#define NPF_SIZE_MAX ( _name, _size )
```

```c
#include <zephyr/net/net_pkt_filter.h>
```

展开值（Value）：

```c
struct npf_test_size_bounds _name = {                      \
        .min = 0,                                          \
        .max = (_size),                                    \
        .test.fn = npf_size_inbounds,                      \
        IF_ENABLED(NPF_TEST_ENABLE_NAME,                   \
                   (.test.name = "size max",               \
                    .test.type = NPF_TEST_TYPE_SIZE_MAX,)) \
}
```

静态定义“数据最大大小”（Data Maximum Size）数据包过滤条件（Packet Filter Condition）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_name` | 条件名称（Condition Name）。 |
| `_size` | 数据包数据大小（Data Size）的上界。 |

<a id="gaf142455f9bea3dea8faa0a913072b63e"></a>

### `NPF_SIZE_MIN`

```c
#define NPF_SIZE_MIN ( _name, _size )
```

```c
#include <zephyr/net/net_pkt_filter.h>
```

展开值（Value）：

```c
struct npf_test_size_bounds _name = {                      \
        .min = (_size),                                    \
        .max = SIZE_MAX,                                   \
        .test.fn = npf_size_inbounds,                      \
        IF_ENABLED(NPF_TEST_ENABLE_NAME,                   \
                   (.test.name = "size min",               \
                    .test.type = NPF_TEST_TYPE_SIZE_MIN,)) \
}
```

静态定义“数据最小大小”（Data Minimum Size）数据包过滤条件（Packet Filter Condition）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_name` | 条件名称（Condition Name）。 |
| `_size` | 数据包数据大小（Data Size）的下界。 |


## 9.3\_原页交叉引用（Cross References）

- [zephyr/net/net_pkt_filter.h](https://docs.zephyrproject.org/latest/doxygen/html/net__pkt__filter_8h.html)
- [IF_ENABLED](../util_reference/P001_通用工具公共接口.md#gae67ffe50e848951dbde309ed569ea925)
- [net_in_addr](../network_core_model_reference/P096_net_in_addr_结构体.md)
- [net_in6_addr](../network_core_model_reference/P094_net_in6_addr_结构体.md)
- [max](../numeric_reference/P001_最小最大值与限幅宏参考.md#affe776513b24d84b39af8ab0930fef7f)
- [SIZE_MAX](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3c75bb398badb69c7577b21486f9963f)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="agroup__sys-util_html_gae67ffe50e848951dbde309ed569ea925"></a>
<a id="aminmax_8h_html_affe776513b24d84b39af8ab0930fef7f"></a>
<a id="astdint_8h_html_a3c75bb398badb69c7577b21486f9963f"></a>

---

[上一章](P008_MFD AXP192 接口.md) · [返回大纲](大纲.md) · [下一章](P010_受电端回调（Sink Callbacks）.md)
