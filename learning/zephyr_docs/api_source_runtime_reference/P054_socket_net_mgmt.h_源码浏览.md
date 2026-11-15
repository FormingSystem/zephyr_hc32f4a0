---
id: learning.zephyr-docs.api-source-runtime-reference.page-54
title: socket_net_mgmt.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/socket__net__mgmt_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第54章\_socket\_net\_mgmt.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/socket__net__mgmt_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/socket__net__mgmt_8h.html)。

## 54.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00008"></a>
<a id="l00009"></a>
<a id="l00010"></a>
<a id="l00011"></a>
<a id="l00012"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00018"></a>
<a id="l00019"></a>
<a id="l00020"></a>
<a id="l00021"></a>
<a id="l00022"></a>
<a id="l00023"></a>
<a id="l00024"></a>
<a id="l00033"></a>
<a id="l00035"></a>
<a id="l00036"></a>
<a id="l00037"></a>
<a id="l00038"></a>
<a id="l00039"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="l00044"></a>
<a id="l00049"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="l00054"></a>
<a id="l00055"></a>
<a id="l00057"></a>
<a id="l00058"></a>
<a id="foldopen00062"></a>
<a id="l00062"></a>
<a id="l00064"></a>
<a id="l00065"></a>
<a id="l00067"></a>
<a id="l00068"></a>
<a id="l00070"></a>
<a id="l00071"></a>
<a id="l00072"></a>
<a id="l00082"></a>
<a id="l00083"></a>
<a id="l00087"></a>
<a id="l00088"></a>
<a id="l00089"></a>
<a id="l00090"></a>
<a id="l00091"></a>
<a id="l00092"></a>
<a id="ainclude_2zephyr_2types_8h_html"></a>
<a id="anet__if_8h_html"></a>
<a id="anet__ip_8h_html"></a>
<a id="anet__mgmt_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astructnet__mgmt__msghdr_html"></a>
<a id="astructnet__mgmt__msghdr_html_a09e1bc6f985b8fcc3397aa447b1d8e94"></a>
<a id="astructnet__mgmt__msghdr_html_a6867379b1ab13c504ee9884cc386c05e"></a>
<a id="astructnet__mgmt__msghdr_html_ad7f4caefa6b3d8d93a480cd8210d7a4d"></a>

```c


/*
 * Copyright (c) 2019 Intel Corporation
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_NET_SOCKET_NET_MGMT_H_
#define ZEPHYR_INCLUDE_NET_SOCKET_NET_MGMT_H_

#include <zephyr/types.h>
#include <zephyr/net/net_ip.h>
#include <zephyr/net/net_if.h>
#include <zephyr/net/net_mgmt.h>

#ifdef __cplusplus
extern "C" {
#endif



/* Protocols of the protocol family PF_NET_MGMT */
#define NET_MGMT_EVENT_PROTO 0x01

/* Socket NET_MGMT options */
#define SOL_NET_MGMT_BASE 100
#define SOL_NET_MGMT_RAW (SOL_NET_MGMT_BASE + 1)



#define SO_NET_MGMT_ETHERNET_SET_QAV_PARAM 1

#define SO_NET_MGMT_ETHERNET_GET_QAV_PARAM 2
 /* for @name */


struct net_mgmt_msghdr {
        uint32_t nm_msg_version;

        uint32_t nm_msg_len;

        uint8_t nm_msg[];
};

#define NET_MGMT_SOCKET_VERSION_1 0x0001


#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_NET_SOCKET_NET_MGMT_H_ */
```

## 54.2\_可见注释译文（Comments）

### 注释 1：原第 7 行

版权（Copyright）：© 2019 Intel Corporation。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 36 行

协议族 `PF_NET_MGMT` 中的协议。

### 注释 3：原第 39 行

NET_MGMT 套接字选项。

### 注释 4：原第 55 行

供 Doxygen 的 `@name` 使用。

### 注释 5：原第 92 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_NET_SOCKET_NET_MGMT_H_`。

## 54.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/socket__net__mgmt_8h.html)
- [zephyr/types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)
- [zephyr/net/net_ip.h](https://docs.zephyrproject.org/latest/doxygen/html/net__ip_8h.html)
- [zephyr/net/net_if.h](https://docs.zephyrproject.org/latest/doxygen/html/net__if_8h.html)
- [zephyr/net/net_mgmt.h](https://docs.zephyrproject.org/latest/doxygen/html/net__mgmt_8h.html)
- [net_mgmt_msghdr](../network_core_model_reference/P111_net_mgmt_msghdr_结构体.md)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [nm_msg_version](../network_core_model_reference/P111_net_mgmt_msghdr_结构体.md#a6867379b1ab13c504ee9884cc386c05e)
- [nm_msg_len](../network_core_model_reference/P111_net_mgmt_msghdr_结构体.md#ad7f4caefa6b3d8d93a480cd8210d7a4d)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [nm_msg](../network_core_model_reference/P111_net_mgmt_msghdr_结构体.md#a09e1bc6f985b8fcc3397aa447b1d8e94)
- [types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)
- [net_if.h](https://docs.zephyrproject.org/latest/doxygen/html/net__if_8h.html)
- [net_ip.h](https://docs.zephyrproject.org/latest/doxygen/html/net__ip_8h.html)
- [net_mgmt.h](https://docs.zephyrproject.org/latest/doxygen/html/net__mgmt_8h.html)
- [net_mgmt_msghdr::nm_msg](../network_core_model_reference/P111_net_mgmt_msghdr_结构体.md#a09e1bc6f985b8fcc3397aa447b1d8e94)
- [net_mgmt_msghdr::nm_msg_version](../network_core_model_reference/P111_net_mgmt_msghdr_结构体.md#a6867379b1ab13c504ee9884cc386c05e)
- [net_mgmt_msghdr::nm_msg_len](../network_core_model_reference/P111_net_mgmt_msghdr_结构体.md#ad7f4caefa6b3d8d93a480cd8210d7a4d)

---

[上一章](P053_rfcomm.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P055_stm32c0_clock.h_源码浏览.md)
