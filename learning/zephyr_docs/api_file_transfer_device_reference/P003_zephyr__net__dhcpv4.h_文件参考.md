---
id: learning.zephyr-docs.api-file-transfer-device-reference.page-3
title: zephyr__net__dhcpv4.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/dhcpv4_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第3章\_zephyr\_\_net\_\_dhcpv4.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/dhcpv4_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

DHCPv4客户端处理程序（Client Handler）。

<a id="details"></a>

```c
#include <zephyr/sys/slist.h>
#include <zephyr/types.h>
```

查看此文件的源码。

DHCPv4客户端处理程序（Client Handler）。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 3.1\_类型定义（Typedefs）

<a id="r_ga75caf142c6c4e058f78c7be0a4a35a9d"></a>

```c
typedef void(* net_dhcpv4_option_callback_handler_t) (struct net_dhcpv4_option_callback *cb, size_t length, enum net_dhcpv4_msg_type msg_type, struct net_if *iface)
```

相关声明：[net_dhcpv4_option_callback_handler_t](https://docs.zephyrproject.org/latest/doxygen/html/group__dhcpv4.html#ga75caf142c6c4e058f78c7be0a4a35a9d)、[net_dhcpv4_msg_type](https://docs.zephyrproject.org/latest/doxygen/html/group__dhcpv4.html#gacc66584b0776e5a79b1f4ceea479a7f8)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

定义应用程序回调处理函数的签名（Function Signature）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 3.2\_枚举（Enumerations）

<a id="r_gacc66584b0776e5a79b1f4ceea479a7f8"></a>

```c
enum net_dhcpv4_msg_type { NET_DHCPV4_MSG_TYPE_DISCOVER = 1 , NET_DHCPV4_MSG_TYPE_OFFER = 2 , NET_DHCPV4_MSG_TYPE_REQUEST = 3 , NET_DHCPV4_MSG_TYPE_DECLINE = 4 , NET_DHCPV4_MSG_TYPE_ACK = 5 , NET_DHCPV4_MSG_TYPE_NAK = 6 , NET_DHCPV4_MSG_TYPE_RELEASE = 7 , NET_DHCPV4_MSG_TYPE_INFORM = 8 }
```

相关声明：[net_dhcpv4_msg_type](https://docs.zephyrproject.org/latest/doxygen/html/group__dhcpv4.html#gacc66584b0776e5a79b1f4ceea479a7f8)、[NET_DHCPV4_MSG_TYPE_DISCOVER](https://docs.zephyrproject.org/latest/doxygen/html/group__dhcpv4.html#ggacc66584b0776e5a79b1f4ceea479a7f8ab8cb4caf5ae9de5bf79f791630475f1d)、[NET_DHCPV4_MSG_TYPE_OFFER](https://docs.zephyrproject.org/latest/doxygen/html/group__dhcpv4.html#ggacc66584b0776e5a79b1f4ceea479a7f8a7e2888c4bb7cd85e3fb99b72d1a90a4a)、[NET_DHCPV4_MSG_TYPE_REQUEST](https://docs.zephyrproject.org/latest/doxygen/html/group__dhcpv4.html#ggacc66584b0776e5a79b1f4ceea479a7f8a4ec90153e2775f013099541acc15b14e)、[NET_DHCPV4_MSG_TYPE_DECLINE](https://docs.zephyrproject.org/latest/doxygen/html/group__dhcpv4.html#ggacc66584b0776e5a79b1f4ceea479a7f8ad5e45accf00132a16a3c6042a21e7b9f)、[NET_DHCPV4_MSG_TYPE_ACK](https://docs.zephyrproject.org/latest/doxygen/html/group__dhcpv4.html#ggacc66584b0776e5a79b1f4ceea479a7f8a77932735abd547927ed8eef61c9f4925)、[NET_DHCPV4_MSG_TYPE_NAK](https://docs.zephyrproject.org/latest/doxygen/html/group__dhcpv4.html#ggacc66584b0776e5a79b1f4ceea479a7f8a95d3e660ab59bdfb9de09e95493055c4)、[NET_DHCPV4_MSG_TYPE_RELEASE](https://docs.zephyrproject.org/latest/doxygen/html/group__dhcpv4.html#ggacc66584b0776e5a79b1f4ceea479a7f8a9255fce7b8a52f290f6406e039b298c5)、[NET_DHCPV4_MSG_TYPE_INFORM](https://docs.zephyrproject.org/latest/doxygen/html/group__dhcpv4.html#ggacc66584b0776e5a79b1f4ceea479a7f8aba941cf50fabac68e5d0e07fa923b866)。

DHCPv4 消息类型（Message Types）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 3.3\_函数（Functions）

<a id="r_ga84df76c84de248a43e3e26d422cdfc2f"></a>

```c
static void net_dhcpv4_init_option_callback (struct net_dhcpv4_option_callback *callback, net_dhcpv4_option_callback_handler_t handler, uint8_t option, void *data, size_t max_length)
```

相关声明：[net_dhcpv4_init_option_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__dhcpv4.html#ga84df76c84de248a43e3e26d422cdfc2f)、[net_dhcpv4_option_callback_handler_t](https://docs.zephyrproject.org/latest/doxygen/html/group__dhcpv4.html#ga75caf142c6c4e058f78c7be0a4a35a9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

正确初始化 `struct net_dhcpv4_option_callback` 的辅助接口（Helper）。

<a id="r_gaf073157fcd5cb2d18c40b8697d724a7c"></a>

```c
int net_dhcpv4_add_option_callback (struct net_dhcpv4_option_callback *cb)
```

相关声明：[net_dhcpv4_add_option_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__dhcpv4.html#gaf073157fcd5cb2d18c40b8697d724a7c)。

添加应用回调。

<a id="r_gaa90c4ba8010bcd2079512afe5f288dbb"></a>

```c
int net_dhcpv4_remove_option_callback (struct net_dhcpv4_option_callback *cb)
```

相关声明：[net_dhcpv4_remove_option_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__dhcpv4.html#gaa90c4ba8010bcd2079512afe5f288dbb)。

移除应用回调。

<a id="r_gaec0f1c87f5093767a4bb1c43b8e18e72"></a>

```c
static void net_dhcpv4_init_option_vendor_callback (struct net_dhcpv4_option_callback *callback, net_dhcpv4_option_callback_handler_t handler, uint8_t option, void *data, size_t max_length)
```

相关声明：[net_dhcpv4_init_option_vendor_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__dhcpv4.html#gaec0f1c87f5093767a4bb1c43b8e18e72)、[net_dhcpv4_option_callback_handler_t](https://docs.zephyrproject.org/latest/doxygen/html/group__dhcpv4.html#ga75caf142c6c4e058f78c7be0a4a35a9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

为封装的厂商专用选项（Encapsulated Vendor-specific Options）正确初始化 `struct net_dhcpv4_option_callback` 的辅助接口。

<a id="r_gabf3d97139fc4f7122c1bdee52cb003cb"></a>

```c
int net_dhcpv4_add_option_vendor_callback (struct net_dhcpv4_option_callback *cb)
```

相关声明：[net_dhcpv4_add_option_vendor_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__dhcpv4.html#gabf3d97139fc4f7122c1bdee52cb003cb)。

为封装的厂商专用选项（Encapsulated Vendor-specific Options）添加应用回调（Application Callback）。

<a id="r_ga1f362cce448226447d892f5ed8401db5"></a>

```c
int net_dhcpv4_remove_option_vendor_callback (struct net_dhcpv4_option_callback *cb)
```

相关声明：[net_dhcpv4_remove_option_vendor_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__dhcpv4.html#ga1f362cce448226447d892f5ed8401db5)。

移除封装的厂商专用选项（Encapsulated Vendor-specific Options）的应用回调（Application Callback）。

<a id="r_gafa2ddaa5cf17fbe5c4a3ca6fbf883cbe"></a>

```c
void net_dhcpv4_start (struct net_if *iface)
```

相关声明：[net_dhcpv4_start](https://docs.zephyrproject.org/latest/doxygen/html/group__dhcpv4.html#gafa2ddaa5cf17fbe5c4a3ca6fbf883cbe)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

在接口（Interface）上启动 DHCPv4 客户端（Client）。

<a id="r_ga910a416e25c2878b84319f6884883d8e"></a>

```c
void net_dhcpv4_stop (struct net_if *iface)
```

相关声明：[net_dhcpv4_stop](https://docs.zephyrproject.org/latest/doxygen/html/group__dhcpv4.html#ga910a416e25c2878b84319f6884883d8e)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

在接口（Interface）上停止 DHCPv4 客户端（Client）。

<a id="r_ga57979593bfb87d006e634b88a64bdf1a"></a>

```c
void net_dhcpv4_restart (struct net_if *iface)
```

相关声明：[net_dhcpv4_restart](https://docs.zephyrproject.org/latest/doxygen/html/group__dhcpv4.html#ga57979593bfb87d006e634b88a64bdf1a)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

在接口（Interface）上重新启动 DHCPv4 客户端（Client）。

<a id="r_ga167e66033d902d7ffcab801b738db224"></a>

```c
int net_dhcpv4_set_reboot_hint (struct net_if *iface, const struct net_in_addr *requested_ip)
```

相关声明：[net_dhcpv4_set_reboot_hint](https://docs.zephyrproject.org/latest/doxygen/html/group__dhcpv4.html#ga167e66033d902d7ffcab801b738db224)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_in_addr](../network_core_model_reference/P096_net_in_addr_结构体.md)。

设置在 `INIT-REBOOT` 中请求的地址（Requested Address）。

<a id="r_ga571124b93b5dfdf3377877aded0c374c"></a>

```c
const char * net_dhcpv4_msg_type_name (enum net_dhcpv4_msg_type msg_type)
```

相关声明：[net_dhcpv4_msg_type_name](https://docs.zephyrproject.org/latest/doxygen/html/group__dhcpv4.html#ga571124b93b5dfdf3377877aded0c374c)、[net_dhcpv4_msg_type](https://docs.zephyrproject.org/latest/doxygen/html/group__dhcpv4.html#gacc66584b0776e5a79b1f4ceea479a7f8)。

返回 `msg_type` 的文本表示（Text Representation）。


## 3.4\_原页交叉引用（Cross References）

- [zephyr/sys/slist.h](../slist_reference/P003_单向链表头文件源码.md)
- [zephyr/types.h](../api_source_compiler_device_reference/P014_types.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P128_dhcpv4.h_源码浏览.md)
- [net_dhcpv4_option_callback_handler_t](https://docs.zephyrproject.org/latest/doxygen/html/group__dhcpv4.html#ga75caf142c6c4e058f78c7be0a4a35a9d)
- [net_dhcpv4_msg_type](https://docs.zephyrproject.org/latest/doxygen/html/group__dhcpv4.html#gacc66584b0776e5a79b1f4ceea479a7f8)
- [net_if](../network_core_model_reference/P079_net_if_结构体.md)
- [NET_DHCPV4_MSG_TYPE_DISCOVER](https://docs.zephyrproject.org/latest/doxygen/html/group__dhcpv4.html#ggacc66584b0776e5a79b1f4ceea479a7f8ab8cb4caf5ae9de5bf79f791630475f1d)
- [NET_DHCPV4_MSG_TYPE_OFFER](https://docs.zephyrproject.org/latest/doxygen/html/group__dhcpv4.html#ggacc66584b0776e5a79b1f4ceea479a7f8a7e2888c4bb7cd85e3fb99b72d1a90a4a)
- [NET_DHCPV4_MSG_TYPE_REQUEST](https://docs.zephyrproject.org/latest/doxygen/html/group__dhcpv4.html#ggacc66584b0776e5a79b1f4ceea479a7f8a4ec90153e2775f013099541acc15b14e)
- [NET_DHCPV4_MSG_TYPE_DECLINE](https://docs.zephyrproject.org/latest/doxygen/html/group__dhcpv4.html#ggacc66584b0776e5a79b1f4ceea479a7f8ad5e45accf00132a16a3c6042a21e7b9f)
- [NET_DHCPV4_MSG_TYPE_ACK](https://docs.zephyrproject.org/latest/doxygen/html/group__dhcpv4.html#ggacc66584b0776e5a79b1f4ceea479a7f8a77932735abd547927ed8eef61c9f4925)
- [NET_DHCPV4_MSG_TYPE_NAK](https://docs.zephyrproject.org/latest/doxygen/html/group__dhcpv4.html#ggacc66584b0776e5a79b1f4ceea479a7f8a95d3e660ab59bdfb9de09e95493055c4)
- [NET_DHCPV4_MSG_TYPE_RELEASE](https://docs.zephyrproject.org/latest/doxygen/html/group__dhcpv4.html#ggacc66584b0776e5a79b1f4ceea479a7f8a9255fce7b8a52f290f6406e039b298c5)
- [NET_DHCPV4_MSG_TYPE_INFORM](https://docs.zephyrproject.org/latest/doxygen/html/group__dhcpv4.html#ggacc66584b0776e5a79b1f4ceea479a7f8aba941cf50fabac68e5d0e07fa923b866)
- [net_dhcpv4_init_option_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__dhcpv4.html#ga84df76c84de248a43e3e26d422cdfc2f)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [net_dhcpv4_add_option_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__dhcpv4.html#gaf073157fcd5cb2d18c40b8697d724a7c)
- [net_dhcpv4_remove_option_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__dhcpv4.html#gaa90c4ba8010bcd2079512afe5f288dbb)
- [net_dhcpv4_init_option_vendor_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__dhcpv4.html#gaec0f1c87f5093767a4bb1c43b8e18e72)
- [net_dhcpv4_add_option_vendor_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__dhcpv4.html#gabf3d97139fc4f7122c1bdee52cb003cb)
- [net_dhcpv4_remove_option_vendor_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__dhcpv4.html#ga1f362cce448226447d892f5ed8401db5)
- [net_dhcpv4_start](https://docs.zephyrproject.org/latest/doxygen/html/group__dhcpv4.html#gafa2ddaa5cf17fbe5c4a3ca6fbf883cbe)
- [net_dhcpv4_stop](https://docs.zephyrproject.org/latest/doxygen/html/group__dhcpv4.html#ga910a416e25c2878b84319f6884883d8e)
- [net_dhcpv4_restart](https://docs.zephyrproject.org/latest/doxygen/html/group__dhcpv4.html#ga57979593bfb87d006e634b88a64bdf1a)
- [net_dhcpv4_set_reboot_hint](https://docs.zephyrproject.org/latest/doxygen/html/group__dhcpv4.html#ga167e66033d902d7ffcab801b738db224)
- [net_in_addr](../network_core_model_reference/P096_net_in_addr_结构体.md)
- [net_dhcpv4_msg_type_name](https://docs.zephyrproject.org/latest/doxygen/html/group__dhcpv4.html#ga571124b93b5dfdf3377877aded0c374c)

<a id="header-details"></a>

---

[上一章](P002_zephyr__drivers__clock_control__sf32lb.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P004_zephyr__drivers__dma__sf32lb.h_文件参考.md)
