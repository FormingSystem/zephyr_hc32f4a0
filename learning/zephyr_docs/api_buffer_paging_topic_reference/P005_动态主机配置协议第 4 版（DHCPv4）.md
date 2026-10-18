---
id: learning.zephyr-docs.api-buffer-paging-topic-reference.page-5
title: 动态主机配置协议第 4 版（DHCPv4）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__dhcpv4.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第5章\_动态主机配置协议第 4 版（DHCPv4）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__dhcpv4.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

动态主机配置协议第 4 版（DHCPv4）

<a id="details"></a>

DHCPv4。引入版本（Since）：1.7；API 版本（Version）：0.8.0。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 5.1\_类型定义（Typedefs）

<a id="r_ga75caf142c6c4e058f78c7be0a4a35a9d"></a>

```c
typedef void(* net_dhcpv4_option_callback_handler_t) (struct net_dhcpv4_option_callback *cb, size_t length, enum net_dhcpv4_msg_type msg_type, struct net_if *iface)
```

相关声明：[net_dhcpv4_option_callback_handler_t](#ga75caf142c6c4e058f78c7be0a4a35a9d)、[net_dhcpv4_msg_type](#gacc66584b0776e5a79b1f4ceea479a7f8)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

定义应用程序回调处理函数的签名（Function Signature）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 5.2\_枚举（Enumerations）

<a id="r_gacc66584b0776e5a79b1f4ceea479a7f8"></a>

```c
enum net_dhcpv4_msg_type { NET_DHCPV4_MSG_TYPE_DISCOVER = 1 , NET_DHCPV4_MSG_TYPE_OFFER = 2 , NET_DHCPV4_MSG_TYPE_REQUEST = 3 , NET_DHCPV4_MSG_TYPE_DECLINE = 4 , NET_DHCPV4_MSG_TYPE_ACK = 5 , NET_DHCPV4_MSG_TYPE_NAK = 6 , NET_DHCPV4_MSG_TYPE_RELEASE = 7 , NET_DHCPV4_MSG_TYPE_INFORM = 8 }
```

相关声明：[net_dhcpv4_msg_type](#gacc66584b0776e5a79b1f4ceea479a7f8)、[NET_DHCPV4_MSG_TYPE_DISCOVER](#ggacc66584b0776e5a79b1f4ceea479a7f8ab8cb4caf5ae9de5bf79f791630475f1d)、[NET_DHCPV4_MSG_TYPE_OFFER](#ggacc66584b0776e5a79b1f4ceea479a7f8a7e2888c4bb7cd85e3fb99b72d1a90a4a)、[NET_DHCPV4_MSG_TYPE_REQUEST](#ggacc66584b0776e5a79b1f4ceea479a7f8a4ec90153e2775f013099541acc15b14e)、[NET_DHCPV4_MSG_TYPE_DECLINE](#ggacc66584b0776e5a79b1f4ceea479a7f8ad5e45accf00132a16a3c6042a21e7b9f)、[NET_DHCPV4_MSG_TYPE_ACK](#ggacc66584b0776e5a79b1f4ceea479a7f8a77932735abd547927ed8eef61c9f4925)、[NET_DHCPV4_MSG_TYPE_NAK](#ggacc66584b0776e5a79b1f4ceea479a7f8a95d3e660ab59bdfb9de09e95493055c4)、[NET_DHCPV4_MSG_TYPE_RELEASE](#ggacc66584b0776e5a79b1f4ceea479a7f8a9255fce7b8a52f290f6406e039b298c5)、[NET_DHCPV4_MSG_TYPE_INFORM](#ggacc66584b0776e5a79b1f4ceea479a7f8aba941cf50fabac68e5d0e07fa923b866)。

DHCPv4 消息类型（Message Types）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 5.3\_函数（Functions）

<a id="r_ga84df76c84de248a43e3e26d422cdfc2f"></a>

```c
static void net_dhcpv4_init_option_callback (struct net_dhcpv4_option_callback *callback, net_dhcpv4_option_callback_handler_t handler, uint8_t option, void *data, size_t max_length)
```

相关声明：[net_dhcpv4_init_option_callback](#ga84df76c84de248a43e3e26d422cdfc2f)、[net_dhcpv4_option_callback_handler_t](#ga75caf142c6c4e058f78c7be0a4a35a9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

正确初始化 `struct net_dhcpv4_option_callback` 的辅助接口（Helper）。

<a id="r_gaf073157fcd5cb2d18c40b8697d724a7c"></a>

```c
int net_dhcpv4_add_option_callback (struct net_dhcpv4_option_callback *cb)
```

相关声明：[net_dhcpv4_add_option_callback](#gaf073157fcd5cb2d18c40b8697d724a7c)。

添加应用回调。

<a id="r_gaa90c4ba8010bcd2079512afe5f288dbb"></a>

```c
int net_dhcpv4_remove_option_callback (struct net_dhcpv4_option_callback *cb)
```

相关声明：[net_dhcpv4_remove_option_callback](#gaa90c4ba8010bcd2079512afe5f288dbb)。

移除应用回调。

<a id="r_gaec0f1c87f5093767a4bb1c43b8e18e72"></a>

```c
static void net_dhcpv4_init_option_vendor_callback (struct net_dhcpv4_option_callback *callback, net_dhcpv4_option_callback_handler_t handler, uint8_t option, void *data, size_t max_length)
```

相关声明：[net_dhcpv4_init_option_vendor_callback](#gaec0f1c87f5093767a4bb1c43b8e18e72)、[net_dhcpv4_option_callback_handler_t](#ga75caf142c6c4e058f78c7be0a4a35a9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

为封装的厂商专用选项（Encapsulated Vendor-specific Options）正确初始化 `struct net_dhcpv4_option_callback` 的辅助接口。

<a id="r_gabf3d97139fc4f7122c1bdee52cb003cb"></a>

```c
int net_dhcpv4_add_option_vendor_callback (struct net_dhcpv4_option_callback *cb)
```

相关声明：[net_dhcpv4_add_option_vendor_callback](#gabf3d97139fc4f7122c1bdee52cb003cb)。

为封装的厂商专用选项（Encapsulated Vendor-specific Options）添加应用回调（Application Callback）。

<a id="r_ga1f362cce448226447d892f5ed8401db5"></a>

```c
int net_dhcpv4_remove_option_vendor_callback (struct net_dhcpv4_option_callback *cb)
```

相关声明：[net_dhcpv4_remove_option_vendor_callback](#ga1f362cce448226447d892f5ed8401db5)。

移除封装的厂商专用选项（Encapsulated Vendor-specific Options）的应用回调（Application Callback）。

<a id="r_gafa2ddaa5cf17fbe5c4a3ca6fbf883cbe"></a>

```c
void net_dhcpv4_start (struct net_if *iface)
```

相关声明：[net_dhcpv4_start](#gafa2ddaa5cf17fbe5c4a3ca6fbf883cbe)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

在接口（Interface）上启动 DHCPv4 客户端（Client）。

<a id="r_ga910a416e25c2878b84319f6884883d8e"></a>

```c
void net_dhcpv4_stop (struct net_if *iface)
```

相关声明：[net_dhcpv4_stop](#ga910a416e25c2878b84319f6884883d8e)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

在接口（Interface）上停止 DHCPv4 客户端（Client）。

<a id="r_ga57979593bfb87d006e634b88a64bdf1a"></a>

```c
void net_dhcpv4_restart (struct net_if *iface)
```

相关声明：[net_dhcpv4_restart](#ga57979593bfb87d006e634b88a64bdf1a)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

在接口（Interface）上重新启动 DHCPv4 客户端（Client）。

<a id="r_ga167e66033d902d7ffcab801b738db224"></a>

```c
int net_dhcpv4_set_reboot_hint (struct net_if *iface, const struct net_in_addr *requested_ip)
```

相关声明：[net_dhcpv4_set_reboot_hint](#ga167e66033d902d7ffcab801b738db224)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_in_addr](../network_core_model_reference/P096_net_in_addr_结构体.md)。

设置在 `INIT-REBOOT` 中请求的地址（Requested Address）。

<a id="r_ga571124b93b5dfdf3377877aded0c374c"></a>

```c
const char * net_dhcpv4_msg_type_name (enum net_dhcpv4_msg_type msg_type)
```

相关声明：[net_dhcpv4_msg_type_name](#ga571124b93b5dfdf3377877aded0c374c)、[net_dhcpv4_msg_type](#gacc66584b0776e5a79b1f4ceea479a7f8)。

返回 `msg_type` 的文本表示（Text Representation）。

## 5.4\_详细说明（Detailed Documentation）

<a id="ga75caf142c6c4e058f78c7be0a4a35a9d"></a>

### `net_dhcpv4_option_callback_handler_t`

```c
typedef void(* net_dhcpv4_option_callback_handler_t) (struct net_dhcpv4_option_callback *cb, size_t length, enum net_dhcpv4_msg_type msg_type, struct net_if *iface)
```

```c
#include <zephyr/net/dhcpv4.h>
```

定义应用程序回调处理函数的签名（Function Signature）。

注意：如果原始 struct net_dhcpv4_option_callback 嵌在另一私有结构体中，可利用 cb 指针通过 CONTAINER_OF() 取得私有数据（Private Data）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cb` | 拥有此处理函数的原始 struct net_dhcpv4_option_callback |
| `length` | 服务器返回的数据长度。若大于 cb->max_length，则 cb->data 中仅有 cb->max_length 字节可用。 |
| `msg_type` | 触发回调的 DHCP 消息类型（Message Type） |
| `iface` | 接收此 DHCP 消息的接口（Interface） |

<a id="gacc66584b0776e5a79b1f4ceea479a7f8"></a>

### `net_dhcpv4_msg_type`

```c
enum net_dhcpv4_msg_type
```

```c
#include <zephyr/net/dhcpv4.h>
```

DHCPv4 消息类型（Message Types）。

这些枚举表示 RFC 2132 第 9.6 节定义的消息类型码，不得重新编号。

在此定义中新增、移除或重排条目时，必须相应修改 net_dhcpv4_msg_type_name。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `NET_DHCPV4_MSG_TYPE_DISCOVER` | 发现消息（Discover）。 |
| `NET_DHCPV4_MSG_TYPE_OFFER` | 提供消息（Offer）。 |
| `NET_DHCPV4_MSG_TYPE_REQUEST` | 请求消息（Request）。 |
| `NET_DHCPV4_MSG_TYPE_DECLINE` | 拒绝消息（Decline）。 |
| `NET_DHCPV4_MSG_TYPE_ACK` | 确认消息（Acknowledge）。 |
| `NET_DHCPV4_MSG_TYPE_NAK` | 否定确认消息（Negative Acknowledge）。 |
| `NET_DHCPV4_MSG_TYPE_RELEASE` | 释放消息（Release）。 |
| `NET_DHCPV4_MSG_TYPE_INFORM` | 通知消息（Inform）。 |

<a id="gaf073157fcd5cb2d18c40b8697d724a7c"></a>

### `net_dhcpv4_add_option_callback()`

```c
int net_dhcpv4_add_option_callback ( struct net_dhcpv4_option_callback * cb)
```

```c
#include <zephyr/net/dhcpv4.h>
```

添加应用回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cb` | 有效的应用回调结构体指针。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负 `errno` 错误码。

<a id="gabf3d97139fc4f7122c1bdee52cb003cb"></a>

### `net_dhcpv4_add_option_vendor_callback()`

```c
int net_dhcpv4_add_option_vendor_callback ( struct net_dhcpv4_option_callback * cb)
```

```c
#include <zephyr/net/dhcpv4.h>
```

为封装的厂商专用选项（Encapsulated Vendor-specific Options）添加应用回调（Application Callback）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cb` | 有效的应用回调结构体指针。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负 `errno` 错误码。

<a id="ga84df76c84de248a43e3e26d422cdfc2f"></a>

### `net_dhcpv4_init_option_callback()`

```c
void net_dhcpv4_init_option_callback ( struct net_dhcpv4_option_callback * callback, net_dhcpv4_option_callback_handler_t handler, uint8_t option, void * data, size_t max_length )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/dhcpv4.h>
```

正确初始化 `struct net_dhcpv4_option_callback` 的辅助接口（Helper）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `callback` | 有效的应用回调结构体指针（Callback Structure Pointer）。 |
| `handler` | 有效的处理函数指针（Handler Function Pointer）。 |
| `option` | 该回调响应的 DHCP 选项（Option）。 |
| `data` | 指向可容纳 max_length 字节的缓冲区的指针。 |
| `max_length` | 返回数据的最大长度。 |

<a id="gaec0f1c87f5093767a4bb1c43b8e18e72"></a>

### `net_dhcpv4_init_option_vendor_callback()`

```c
void net_dhcpv4_init_option_vendor_callback ( struct net_dhcpv4_option_callback * callback, net_dhcpv4_option_callback_handler_t handler, uint8_t option, void * data, size_t max_length )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/dhcpv4.h>
```

为封装的厂商专用选项（Encapsulated Vendor-specific Options）正确初始化 `struct net_dhcpv4_option_callback` 的辅助接口。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `callback` | 有效的应用回调结构体指针（Callback Structure Pointer）。 |
| `handler` | 有效的处理函数指针（Handler Function Pointer）。 |
| `option` | 该回调响应的 DHCP 封装厂商专有选项（Encapsulated Vendor-specific Option）。 |
| `data` | 指向可容纳 max_length 字节的缓冲区的指针。 |
| `max_length` | 返回数据的最大长度。 |

<a id="ga571124b93b5dfdf3377877aded0c374c"></a>

### `net_dhcpv4_msg_type_name()`

```c
const char * net_dhcpv4_msg_type_name ( enum net_dhcpv4_msg_type msg_type)
```

```c
#include <zephyr/net/dhcpv4.h>
```

返回 `msg_type` 的文本表示（Text Representation）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `msg_type` | 要转换为文本的 msg_type |

**返回（Returns）**：返回值（Returns）：msg_type 的文本表示。

<a id="gaa90c4ba8010bcd2079512afe5f288dbb"></a>

### `net_dhcpv4_remove_option_callback()`

```c
int net_dhcpv4_remove_option_callback ( struct net_dhcpv4_option_callback * cb)
```

```c
#include <zephyr/net/dhcpv4.h>
```

移除应用回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cb` | 有效的应用回调结构体指针。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负 `errno` 错误码。

<a id="ga1f362cce448226447d892f5ed8401db5"></a>

### `net_dhcpv4_remove_option_vendor_callback()`

```c
int net_dhcpv4_remove_option_vendor_callback ( struct net_dhcpv4_option_callback * cb)
```

```c
#include <zephyr/net/dhcpv4.h>
```

移除封装的厂商专用选项（Encapsulated Vendor-specific Options）的应用回调（Application Callback）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cb` | 有效的应用回调结构体指针。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负 `errno` 错误码。

<a id="ga57979593bfb87d006e634b88a64bdf1a"></a>

### `net_dhcpv4_restart()`

```c
void net_dhcpv4_restart ( struct net_if * iface)
```

```c
#include <zephyr/net/dhcpv4.h>
```

在接口（Interface）上重新启动 DHCPv4 客户端（Client）。

在指定接口上重启 DHCPv4 客户端。客户端重启状态机（State Machine）时，不使用启动阶段的任何初始延迟。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 指向接口（Interface）的有效指针。 |

<a id="ga167e66033d902d7ffcab801b738db224"></a>

### `net_dhcpv4_set_reboot_hint()`

```c
int net_dhcpv4_set_reboot_hint ( struct net_if * iface, const struct net_in_addr * requested_ip )
```

```c
#include <zephyr/net/dhcpv4.h>
```

设置在 `INIT-REBOOT` 中请求的地址（Requested Address）。

为 DHCPv4 客户端提供先前租用的地址，例如从非易失性存储（Non-volatile Storage）恢复的地址，使下次 net_dhcpv4_start 从 INIT-REBOOT 状态开始，直接请求该地址，而不执行完整发现流程。必须在 DHCPv4 客户端停止时调用。要求启用 CONFIG_NET_DHCPV4_INIT_REBOOT。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | DHCPv4 接口（Interface）。 |
| `requested_ip` | 要请求的地址，或用于清除提示地址的未指定地址（Unspecified Address）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时返回。 |
| `-EINVAL` | 参数无效（Invalid Argument）。 |
| `-EBUSY` | DHCPv4 客户端处于活动状态。 |
| `-ENOTSUP` | 未启用 INIT-REBOOT 支持。 |

<a id="gafa2ddaa5cf17fbe5c4a3ca6fbf883cbe"></a>

### `net_dhcpv4_start()`

```c
void net_dhcpv4_start ( struct net_if * iface)
```

```c
#include <zephyr/net/dhcpv4.h>
```

在接口（Interface）上启动 DHCPv4 客户端（Client）。

在指定接口上启动 DHCPv4 客户端。客户端开始协商 IPv4 地址；协商成功后，将 IPv4 地址详情添加到接口。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 指向接口（Interface）的有效指针。 |

<a id="ga910a416e25c2878b84319f6884883d8e"></a>

### `net_dhcpv4_stop()`

```c
void net_dhcpv4_stop ( struct net_if * iface)
```

```c
#include <zephyr/net/dhcpv4.h>
```

在接口（Interface）上停止 DHCPv4 客户端（Client）。

在指定接口上停止 DHCPv4 客户端。客户端从接口移除由 DHCP 服务器获取的全部配置，并停止与服务器的后续协商。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 指向接口（Interface）的有效指针。 |


## 5.5\_原页交叉引用（Cross References）

- [net_if](../network_core_model_reference/P079_net_if_结构体.md)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [net_in_addr](../network_core_model_reference/P096_net_in_addr_结构体.md)
- [zephyr/net/dhcpv4.h](../api_file_transfer_device_reference/P003_zephyr__net__dhcpv4.h_文件参考.md)
- [CONTAINER_OF()](../util_reference/P001_通用工具公共接口.md#gac5bc561d1bfd1bf68877fe577779bd2f)
- [RFC 2132, section-9.6](https://datatracker.ietf.org/doc/html/rfc2132#section-9.6)
- [CONFIG_NET_DHCPV4_INIT_REBOOT](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_DHCPV4_INIT_REBOOT)

<a id="header-details"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="ggacc66584b0776e5a79b1f4ceea479a7f8ab8cb4caf5ae9de5bf79f791630475f1d"></a>
<a id="ggacc66584b0776e5a79b1f4ceea479a7f8a7e2888c4bb7cd85e3fb99b72d1a90a4a"></a>
<a id="ggacc66584b0776e5a79b1f4ceea479a7f8a4ec90153e2775f013099541acc15b14e"></a>
<a id="ggacc66584b0776e5a79b1f4ceea479a7f8ad5e45accf00132a16a3c6042a21e7b9f"></a>
<a id="ggacc66584b0776e5a79b1f4ceea479a7f8a77932735abd547927ed8eef61c9f4925"></a>
<a id="ggacc66584b0776e5a79b1f4ceea479a7f8a95d3e660ab59bdfb9de09e95493055c4"></a>
<a id="ggacc66584b0776e5a79b1f4ceea479a7f8a9255fce7b8a52f290f6406e039b298c5"></a>
<a id="ggacc66584b0776e5a79b1f4ceea479a7f8aba941cf50fabac68e5d0e07fa923b866"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P004_蓝牙HCI数据包辅助接口（Packet Helpers）。.md) · [返回大纲](大纲.md) · [下一章](P006_错误检测与纠正（EDAC）.md)
