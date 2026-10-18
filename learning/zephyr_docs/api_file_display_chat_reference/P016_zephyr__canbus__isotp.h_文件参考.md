---
id: learning.zephyr-docs.api-file-display-chat-reference.page-16
title: zephyr__canbus__isotp.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/isotp_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第16章\_zephyr\_\_canbus\_\_isotp.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/isotp_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

ISO-TP（ISO 15765-2:2016）的公共API。

<a id="details"></a>

```c
#include <zephyr/drivers/can.h>
#include <zephyr/types.h>
#include <zephyr/net_buf.h>
```

查看此文件的源码。

ISO-TP（ISO 15765-2:2016）公共 API。ISO-TP 是用于控制器局域网（Controller Area Network，CAN）的传输协议（Transport Protocol）。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 16.1\_数据结构（Data Structures）

<a id="r_isotp_5Fmsg_5Fid"></a>

```c
struct isotp_msg_id
```

相关声明：[isotp_msg_id](../hardware/P381_ISO-TP消息标识.md)。

ISO-TP消息标识（Message ID）结构。

<a id="r_isotp_5Ffc_5Fopts"></a>

```c
struct isotp_fc_opts
```

相关声明：[isotp_fc_opts](../hardware/P382_ISO-TP流控选项.md)。

ISO-TP帧控制选项（Frame Control Options）结构。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 16.2\_宏定义（Macros）

<a id="r_gab7daaebbc303665beb2946ce077d5312"></a>

```c
#define ISOTP_N_OK 0
```

相关声明：[ISOTP_N_OK](https://docs.zephyrproject.org/latest/doxygen/html/group__can__isotp.html#gab7daaebbc303665beb2946ce077d5312)。

成功完成（Completed Successfully）。

<a id="r_ga8298423e96932f94308f3064755d18fb"></a>

```c
#define ISOTP_N_TIMEOUT_A -1
```

相关声明：[ISOTP_N_TIMEOUT_A](https://docs.zephyrproject.org/latest/doxygen/html/group__can__isotp.html#ga8298423e96932f94308f3064755d18fb)。

Ar/As 已超时（Timed Out）。

<a id="r_ga9e525bb24928a2656e7cd2842b306553"></a>

```c
#define ISOTP_N_TIMEOUT_BS -2
```

相关声明：[ISOTP_N_TIMEOUT_BS](https://docs.zephyrproject.org/latest/doxygen/html/group__can__isotp.html#ga9e525bb24928a2656e7cd2842b306553)。

接收下一个流控帧（FC）已超时。

<a id="r_ga77b802df46c66ed6002f143b57f73b7a"></a>

```c
#define ISOTP_N_TIMEOUT_CR -3
```

相关声明：[ISOTP_N_TIMEOUT_CR](https://docs.zephyrproject.org/latest/doxygen/html/group__can__isotp.html#ga77b802df46c66ed6002f143b57f73b7a)。

Cr 已超时（Timed Out）。

<a id="r_ga9caa5677a171e1bd0be06ebb6b006046"></a>

```c
#define ISOTP_N_WRONG_SN -4
```

相关声明：[ISOTP_N_WRONG_SN](https://docs.zephyrproject.org/latest/doxygen/html/group__can__isotp.html#ga9caa5677a171e1bd0be06ebb6b006046)。

非预期的序列号（Unexpected Sequence Number）。

<a id="r_ga99312831df8e1822f02b41e3fccc0661"></a>

```c
#define ISOTP_N_INVALID_FS -5
```

相关声明：[ISOTP_N_INVALID_FS](https://docs.zephyrproject.org/latest/doxygen/html/group__can__isotp.html#ga99312831df8e1822f02b41e3fccc0661)。

收到无效的流状态（Flow Status）。

<a id="r_ga45e3bfdd3948be6ccb3daec5db412b78"></a>

```c
#define ISOTP_N_UNEXP_PDU -6
```

相关声明：[ISOTP_N_UNEXP_PDU](https://docs.zephyrproject.org/latest/doxygen/html/group__can__isotp.html#ga45e3bfdd3948be6ccb3daec5db412b78)。

收到非预期的协议数据单元（PDU）。

<a id="r_gad6bcb7b6fb8ab30da1a4ddeabe3e3178"></a>

```c
#define ISOTP_N_WFT_OVRN -7
```

相关声明：[ISOTP_N_WFT_OVRN](https://docs.zephyrproject.org/latest/doxygen/html/group__can__isotp.html#gad6bcb7b6fb8ab30da1a4ddeabe3e3178)。

超过 WAIT flowStatus 协议数据单元（PDUs）的最大数量。

<a id="r_ga1b8e6b35a637b5f98e7a2ab4270efd41"></a>

```c
#define ISOTP_N_BUFFER_OVERFLW -8
```

相关声明：[ISOTP_N_BUFFER_OVERFLW](https://docs.zephyrproject.org/latest/doxygen/html/group__can__isotp.html#ga1b8e6b35a637b5f98e7a2ab4270efd41)。

收到 FlowStatus OVFLW 协议数据单元（PDU）。

<a id="r_ga0805646e65d39a9e2f15e110720887ca"></a>

```c
#define ISOTP_N_ERROR -9
```

相关声明：[ISOTP_N_ERROR](https://docs.zephyrproject.org/latest/doxygen/html/group__can__isotp.html#ga0805646e65d39a9e2f15e110720887ca)。

一般错误（General Error）。

<a id="r_gaf0624cd5e7d12e94f4a739bc47ee0361"></a>

```c
#define ISOTP_NO_FREE_FILTER -10
```

相关声明：[ISOTP_NO_FREE_FILTER](https://docs.zephyrproject.org/latest/doxygen/html/group__can__isotp.html#gaf0624cd5e7d12e94f4a739bc47ee0361)。

实现特定的错误（Implementation-specific Errors）。

<a id="r_ga901f61175e228a70c2f882bc999caea6"></a>

```c
#define ISOTP_NO_NET_BUF_LEFT -11
```

相关声明：[ISOTP_NO_NET_BUF_LEFT](https://docs.zephyrproject.org/latest/doxygen/html/group__can__isotp.html#ga901f61175e228a70c2f882bc999caea6)。

没有剩余网络缓冲区（Net Buffer）可供分配。

<a id="r_gaed5270f0ee489128adb8c2ea481c6c77"></a>

```c
#define ISOTP_NO_BUF_DATA_LEFT -12
```

相关声明：[ISOTP_NO_BUF_DATA_LEFT](https://docs.zephyrproject.org/latest/doxygen/html/group__can__isotp.html#gaed5270f0ee489128adb8c2ea481c6c77)。

缓冲区剩余空间不足以容纳数据。

<a id="r_gac5cb1fafeb8aa5cf9fe1695612671c7d"></a>

```c
#define ISOTP_NO_CTX_LEFT -13
```

相关声明：[ISOTP_NO_CTX_LEFT](https://docs.zephyrproject.org/latest/doxygen/html/group__can__isotp.html#gac5cb1fafeb8aa5cf9fe1695612671c7d)。

没有剩余上下文缓冲区（Context Buffer）可供分配。

<a id="r_gaa3e873d4a80ee128f1858520874f93b6"></a>

```c
#define ISOTP_RECV_TIMEOUT -14
```

相关声明：[ISOTP_RECV_TIMEOUT](https://docs.zephyrproject.org/latest/doxygen/html/group__can__isotp.html#gaa3e873d4a80ee128f1858520874f93b6)。

接收（recv）超时。

<a id="r_gaedb0e7330d19b1cdc380c0b36cabf2f5"></a>

```c
#define ISOTP_FIXED_ADDR_SA_POS (CONFIG_ISOTP_FIXED_ADDR_SA_POS)
```

相关声明：[ISOTP_FIXED_ADDR_SA_POS](https://docs.zephyrproject.org/latest/doxygen/html/group__can__isotp.html#gaedb0e7330d19b1cdc380c0b36cabf2f5)。

固定源地址（Source Address，SA）的位置。

<a id="r_ga2a9cbfd95bae05a9f7433f3b1c58689e"></a>

```c
#define ISOTP_FIXED_ADDR_SA_MASK (CONFIG_ISOTP_FIXED_ADDR_SA_MASK)
```

相关声明：[ISOTP_FIXED_ADDR_SA_MASK](https://docs.zephyrproject.org/latest/doxygen/html/group__can__isotp.html#ga2a9cbfd95bae05a9f7433f3b1c58689e)。

提取固定源地址（Source Address，SA）的掩码。

<a id="r_ga2b64d4dffde99159ae5120586364e1c6"></a>

```c
#define ISOTP_FIXED_ADDR_TA_POS (CONFIG_ISOTP_FIXED_ADDR_TA_POS)
```

相关声明：[ISOTP_FIXED_ADDR_TA_POS](https://docs.zephyrproject.org/latest/doxygen/html/group__can__isotp.html#ga2b64d4dffde99159ae5120586364e1c6)。

固定目标地址（Target Address，TA）的位置。

<a id="r_ga5d5415982e04e506c9b045bfbe2be337"></a>

```c
#define ISOTP_FIXED_ADDR_TA_MASK (CONFIG_ISOTP_FIXED_ADDR_TA_MASK)
```

相关声明：[ISOTP_FIXED_ADDR_TA_MASK](https://docs.zephyrproject.org/latest/doxygen/html/group__can__isotp.html#ga5d5415982e04e506c9b045bfbe2be337)。

提取固定目标地址（Target Address，TA）的掩码。

<a id="r_ga29f8806889f4e41c1529c35a56ee98a9"></a>

```c
#define ISOTP_FIXED_ADDR_PRIO_POS (CONFIG_ISOTP_FIXED_ADDR_PRIO_POS)
```

相关声明：[ISOTP_FIXED_ADDR_PRIO_POS](https://docs.zephyrproject.org/latest/doxygen/html/group__can__isotp.html#ga29f8806889f4e41c1529c35a56ee98a9)。

固定寻址模式（Fixed Addressing Mode）中优先级的位置。

<a id="r_gab5dc33148923e7cd58b438a8906d1ace"></a>

```c
#define ISOTP_FIXED_ADDR_PRIO_MASK (CONFIG_ISOTP_FIXED_ADDR_PRIO_MASK)
```

相关声明：[ISOTP_FIXED_ADDR_PRIO_MASK](https://docs.zephyrproject.org/latest/doxygen/html/group__can__isotp.html#gab5dc33148923e7cd58b438a8906d1ace)。

固定寻址模式（Fixed Addressing Mode）中优先级的掩码。

<a id="r_gac27b3210cb754b4621c54923696bfe2d"></a>

```c
#define ISOTP_FIXED_ADDR_RX_MASK (CONFIG_ISOTP_FIXED_ADDR_RX_MASK)
```

相关声明：[ISOTP_FIXED_ADDR_RX_MASK](https://docs.zephyrproject.org/latest/doxygen/html/group__can__isotp.html#gac27b3210cb754b4621c54923696bfe2d)。

用于匹配任意优先级和源地址（SA）的 CAN 接收过滤掩码（Filter RX Mask）。

<a id="define-members-0"></a>

### ISO-TP 消息标识符标志（Message ID Flags）



<a id="r_ga903d326b3bfb05151b9d5d0a0ace59b9"></a>

```c
#define ISOTP_MSG_EXT_ADDR BIT(0)
```

相关声明：[ISOTP_MSG_EXT_ADDR](https://docs.zephyrproject.org/latest/doxygen/html/group__can__isotp.html#ga903d326b3bfb05151b9d5d0a0ace59b9)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

消息使用 ISO-TP 扩展寻址（Extended Addressing），地址位于 CAN 帧负载的第一个字节。

<a id="r_ga998ae9b1645485f567e692bfbaa50cbe"></a>

```c
#define ISOTP_MSG_FIXED_ADDR BIT(1)
```

相关声明：[ISOTP_MSG_FIXED_ADDR](https://docs.zephyrproject.org/latest/doxygen/html/group__can__isotp.html#ga998ae9b1645485f567e692bfbaa50cbe)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

消息使用 ISO-TP 固定寻址（Fixed Addressing），遵循 SAE J1939。

<a id="r_ga16935466c1a543c03d11b71b8944d0b8"></a>

```c
#define ISOTP_MSG_IDE BIT(2)
```

相关声明：[ISOTP_MSG_IDE](https://docs.zephyrproject.org/latest/doxygen/html/group__can__isotp.html#ga16935466c1a543c03d11b71b8944d0b8)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

消息使用扩展（29 位）CAN 标识符（Extended CAN ID）。

<a id="r_ga70b485a2e576b1b0fec2cc8037215bd9"></a>

```c
#define ISOTP_MSG_FDF BIT(3)
```

相关声明：[ISOTP_MSG_FDF](https://docs.zephyrproject.org/latest/doxygen/html/group__can__isotp.html#ga70b485a2e576b1b0fec2cc8037215bd9)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

消息使用 CAN FD 格式（FDF）。

<a id="r_ga9275708b5afba61c8b5c98c718ec4635"></a>

```c
#define ISOTP_MSG_BRS BIT(4)
```

相关声明：[ISOTP_MSG_BRS](https://docs.zephyrproject.org/latest/doxygen/html/group__can__isotp.html#ga9275708b5afba61c8b5c98c718ec4635)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

消息使用 CAN FD 波特率切换（Baud Rate Switch，BRS）。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 16.3\_类型定义（Typedefs）

<a id="r_gad4f9c0d3f847d453ea662128db2603bb"></a>

```c
typedef void(* isotp_tx_callback_t) (int error_nr, void *arg)
```

相关声明：[isotp_tx_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__can__isotp.html#gad4f9c0d3f847d453ea662128db2603bb)。

发送回调（Transmission Callback）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 16.4\_函数（Functions）

<a id="r_ga725696a26c3bdc0c99e3c4e611a897f9"></a>

```c
int isotp_bind (struct isotp_recv_ctx *rctx, const struct device *can_dev, const struct isotp_msg_id *rx_addr, const struct isotp_msg_id *tx_addr, const struct isotp_fc_opts *opts, k_timeout_t timeout)
```

相关声明：[isotp_bind](https://docs.zephyrproject.org/latest/doxygen/html/group__can__isotp.html#ga725696a26c3bdc0c99e3c4e611a897f9)、[device](../device_reference/P002_设备对象结构.md)、[isotp_msg_id](../hardware/P381_ISO-TP消息标识.md)、[isotp_msg_id](../hardware/P381_ISO-TP消息标识.md)、[isotp_fc_opts](../hardware/P382_ISO-TP流控选项.md)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

将地址绑定到接收上下文（Receiving Context）。

<a id="r_ga622293da5564203bf6dcb993410d21ba"></a>

```c
void isotp_unbind (struct isotp_recv_ctx *rctx)
```

相关声明：[isotp_unbind](https://docs.zephyrproject.org/latest/doxygen/html/group__can__isotp.html#ga622293da5564203bf6dcb993410d21ba)。

从接口解除上下文（Context）的绑定。

<a id="r_ga79c9cad7f39802c5c80af743717e22c6"></a>

```c
int isotp_recv (struct isotp_recv_ctx *rctx, uint8_t *data, size_t len, k_timeout_t timeout)
```

相关声明：[isotp_recv](https://docs.zephyrproject.org/latest/doxygen/html/group__can__isotp.html#ga79c9cad7f39802c5c80af743717e22c6)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

从 FIFO 读出收到的数据。

<a id="r_ga4fb0ef794b7c4104d6e6b17bc68e09d8"></a>

```c
int isotp_recv_net (struct isotp_recv_ctx *rctx, struct net_buf **buffer, k_timeout_t timeout)
```

相关声明：[isotp_recv_net](https://docs.zephyrproject.org/latest/doxygen/html/group__can__isotp.html#ga4fb0ef794b7c4104d6e6b17bc68e09d8)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

接收数据时获取网络缓冲区（Net Buffer）。

<a id="r_ga3723fae583a1d7deabc2deee475ba756"></a>

```c
int isotp_send (struct isotp_send_ctx *sctx, const struct device *can_dev, const uint8_t *data, size_t len, const struct isotp_msg_id *tx_addr, const struct isotp_msg_id *rx_addr, isotp_tx_callback_t complete_cb, void *cb_arg)
```

相关声明：[isotp_send](https://docs.zephyrproject.org/latest/doxygen/html/group__can__isotp.html#ga3723fae583a1d7deabc2deee475ba756)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[isotp_msg_id](../hardware/P381_ISO-TP消息标识.md)、[isotp_msg_id](../hardware/P381_ISO-TP消息标识.md)、[isotp_tx_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__can__isotp.html#gad4f9c0d3f847d453ea662128db2603bb)。

发送数据（Send Data）。


## 16.5\_原页交叉引用（Cross References）

- [zephyr/drivers/can.h](../can_driver_reference/P002_CAN驱动头文件源码.md)
- [zephyr/types.h](../api_source_compiler_device_reference/P014_types.h_源码浏览.md)
- [zephyr/net_buf.h](../api_source_system_reference/P021_net_buf.h_源码浏览.md)
- [查看此文件的源码。](../api_source_system_reference/P015_isotp.h_源码浏览.md)
- [isotp_msg_id](../hardware/P381_ISO-TP消息标识.md)
- [isotp_fc_opts](../hardware/P382_ISO-TP流控选项.md)
- [ISOTP_N_OK](https://docs.zephyrproject.org/latest/doxygen/html/group__can__isotp.html#gab7daaebbc303665beb2946ce077d5312)
- [ISOTP_N_TIMEOUT_A](https://docs.zephyrproject.org/latest/doxygen/html/group__can__isotp.html#ga8298423e96932f94308f3064755d18fb)
- [ISOTP_N_TIMEOUT_BS](https://docs.zephyrproject.org/latest/doxygen/html/group__can__isotp.html#ga9e525bb24928a2656e7cd2842b306553)
- [ISOTP_N_TIMEOUT_CR](https://docs.zephyrproject.org/latest/doxygen/html/group__can__isotp.html#ga77b802df46c66ed6002f143b57f73b7a)
- [ISOTP_N_WRONG_SN](https://docs.zephyrproject.org/latest/doxygen/html/group__can__isotp.html#ga9caa5677a171e1bd0be06ebb6b006046)
- [ISOTP_N_INVALID_FS](https://docs.zephyrproject.org/latest/doxygen/html/group__can__isotp.html#ga99312831df8e1822f02b41e3fccc0661)
- [ISOTP_N_UNEXP_PDU](https://docs.zephyrproject.org/latest/doxygen/html/group__can__isotp.html#ga45e3bfdd3948be6ccb3daec5db412b78)
- [ISOTP_N_WFT_OVRN](https://docs.zephyrproject.org/latest/doxygen/html/group__can__isotp.html#gad6bcb7b6fb8ab30da1a4ddeabe3e3178)
- [ISOTP_N_BUFFER_OVERFLW](https://docs.zephyrproject.org/latest/doxygen/html/group__can__isotp.html#ga1b8e6b35a637b5f98e7a2ab4270efd41)
- [ISOTP_N_ERROR](https://docs.zephyrproject.org/latest/doxygen/html/group__can__isotp.html#ga0805646e65d39a9e2f15e110720887ca)
- [ISOTP_NO_FREE_FILTER](https://docs.zephyrproject.org/latest/doxygen/html/group__can__isotp.html#gaf0624cd5e7d12e94f4a739bc47ee0361)
- [ISOTP_NO_NET_BUF_LEFT](https://docs.zephyrproject.org/latest/doxygen/html/group__can__isotp.html#ga901f61175e228a70c2f882bc999caea6)
- [ISOTP_NO_BUF_DATA_LEFT](https://docs.zephyrproject.org/latest/doxygen/html/group__can__isotp.html#gaed5270f0ee489128adb8c2ea481c6c77)
- [ISOTP_NO_CTX_LEFT](https://docs.zephyrproject.org/latest/doxygen/html/group__can__isotp.html#gac5cb1fafeb8aa5cf9fe1695612671c7d)
- [ISOTP_RECV_TIMEOUT](https://docs.zephyrproject.org/latest/doxygen/html/group__can__isotp.html#gaa3e873d4a80ee128f1858520874f93b6)
- [ISOTP_FIXED_ADDR_SA_POS](https://docs.zephyrproject.org/latest/doxygen/html/group__can__isotp.html#gaedb0e7330d19b1cdc380c0b36cabf2f5)
- [ISOTP_FIXED_ADDR_SA_MASK](https://docs.zephyrproject.org/latest/doxygen/html/group__can__isotp.html#ga2a9cbfd95bae05a9f7433f3b1c58689e)
- [ISOTP_FIXED_ADDR_TA_POS](https://docs.zephyrproject.org/latest/doxygen/html/group__can__isotp.html#ga2b64d4dffde99159ae5120586364e1c6)
- [ISOTP_FIXED_ADDR_TA_MASK](https://docs.zephyrproject.org/latest/doxygen/html/group__can__isotp.html#ga5d5415982e04e506c9b045bfbe2be337)
- [ISOTP_FIXED_ADDR_PRIO_POS](https://docs.zephyrproject.org/latest/doxygen/html/group__can__isotp.html#ga29f8806889f4e41c1529c35a56ee98a9)
- [ISOTP_FIXED_ADDR_PRIO_MASK](https://docs.zephyrproject.org/latest/doxygen/html/group__can__isotp.html#gab5dc33148923e7cd58b438a8906d1ace)
- [ISOTP_FIXED_ADDR_RX_MASK](https://docs.zephyrproject.org/latest/doxygen/html/group__can__isotp.html#gac27b3210cb754b4621c54923696bfe2d)
- [ISOTP_MSG_EXT_ADDR](https://docs.zephyrproject.org/latest/doxygen/html/group__can__isotp.html#ga903d326b3bfb05151b9d5d0a0ace59b9)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)
- [ISOTP_MSG_FIXED_ADDR](https://docs.zephyrproject.org/latest/doxygen/html/group__can__isotp.html#ga998ae9b1645485f567e692bfbaa50cbe)
- [ISOTP_MSG_IDE](https://docs.zephyrproject.org/latest/doxygen/html/group__can__isotp.html#ga16935466c1a543c03d11b71b8944d0b8)
- [ISOTP_MSG_FDF](https://docs.zephyrproject.org/latest/doxygen/html/group__can__isotp.html#ga70b485a2e576b1b0fec2cc8037215bd9)
- [ISOTP_MSG_BRS](https://docs.zephyrproject.org/latest/doxygen/html/group__can__isotp.html#ga9275708b5afba61c8b5c98c718ec4635)
- [isotp_tx_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__can__isotp.html#gad4f9c0d3f847d453ea662128db2603bb)
- [isotp_bind](https://docs.zephyrproject.org/latest/doxygen/html/group__can__isotp.html#ga725696a26c3bdc0c99e3c4e611a897f9)
- [device](../device_reference/P002_设备对象结构.md)
- [k_timeout_t](../timer_reference/P087_内核超时类型.md)
- [isotp_unbind](https://docs.zephyrproject.org/latest/doxygen/html/group__can__isotp.html#ga622293da5564203bf6dcb993410d21ba)
- [isotp_recv](https://docs.zephyrproject.org/latest/doxygen/html/group__can__isotp.html#ga79c9cad7f39802c5c80af743717e22c6)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [isotp_recv_net](https://docs.zephyrproject.org/latest/doxygen/html/group__can__isotp.html#ga4fb0ef794b7c4104d6e6b17bc68e09d8)
- [net_buf](../network_core_model_reference/P046_net_buf_结构体.md)
- [isotp_send](https://docs.zephyrproject.org/latest/doxygen/html/group__can__isotp.html#ga3723fae583a1d7deabc2deee475ba756)

<a id="ISOTP_MSG_FLAGS"></a>
<a id="header-details"></a>

---

[上一章](P015_zephyr__irq_multilevel.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P017_zephyr__lorawan__lorawan.h_文件参考.md)
