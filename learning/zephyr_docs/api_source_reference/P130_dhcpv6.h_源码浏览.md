---
id: learning.zephyr-docs.api-source-reference.page-130
title: dhcpv6.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/dhcpv6_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第130章\_dhcpv6.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/dhcpv6_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/dhcpv6_8h.html)。

## 130.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00010"></a>
<a id="l00011"></a>
<a id="l00012"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00026"></a>
<a id="l00028"></a>
<a id="l00030"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="l00034"></a>
<a id="l00035"></a>
<a id="l00036"></a>
<a id="l00037"></a>
<a id="l00038"></a>
<a id="l00039"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="l00044"></a>
<a id="l00045"></a>
<a id="l00046"></a>
<a id="l00047"></a>
<a id="l00048"></a>
<a id="l00049"></a>
<a id="l00050"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="l00054"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="l00057"></a>
<a id="l00058"></a>
<a id="l00059"></a>
<a id="l00060"></a>
<a id="l00061"></a>
<a id="l00062"></a>
<a id="l00063"></a>
<a id="l00064"></a>
<a id="l00065"></a>
<a id="l00066"></a>
<a id="l00067"></a>
<a id="l00069"></a>
<a id="foldopen00071"></a>
<a id="l00071"></a>
<a id="l00072"></a>
<a id="l00073"></a>
<a id="l00075"></a>
<a id="l00089"></a>
<a id="l00090"></a>
<a id="l00091"></a>
<a id="l00103"></a>
<a id="l00104"></a>
<a id="l00114"></a>
<a id="l00115"></a>
<a id="l00124"></a>
<a id="l00125"></a>
<a id="l00127"></a>
<a id="l00133"></a>
<a id="l00134"></a>
<a id="l00136"></a>
<a id="l00140"></a>
<a id="l00141"></a>
<a id="l00142"></a>
<a id="l00143"></a>
<a id="l00144"></a>
<a id="l00145"></a>
<a id="agroup__dhcpv6_html_ga99642b89c14cb17f35b45a03a2286441"></a>
<a id="agroup__dhcpv6_html_gab607a476c947d0335a254304e5dc2a24"></a>
<a id="agroup__dhcpv6_html_gaf0b903bdcd0becf06ed6b212c74097a0"></a>
<a id="aparser__state_8h_html_adc6e5733fc3c22f0a7b2914188c49c90"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astructnet__dhcpv6__params_html"></a>
<a id="astructnet__dhcpv6__params_html_a2549234454437b4316f863347236ef6c"></a>
<a id="astructnet__dhcpv6__params_html_a4bc3655ee2a830879667cdb554883573"></a>
<a id="astructnet__dhcpv6__params_html_ad66949eb34540dbe8808dc9aea9e6368"></a>
<a id="astructnet__dhcpv6__params_html_afd290d92fcc5ae3bac9a9c7030910e6b"></a>
<a id="astructnet__if_html"></a>

```c
/*
 * Copyright (c) 2023 Nordic Semiconductor ASA
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_NET_DHCPV6_H_
#define ZEPHYR_INCLUDE_NET_DHCPV6_H_

#ifdef __cplusplus
extern "C" {
#endif



enum net_dhcpv6_state {
        NET_DHCPV6_DISABLED,
        NET_DHCPV6_INIT,
        NET_DHCPV6_SOLICITING,
        NET_DHCPV6_REQUESTING,
        NET_DHCPV6_CONFIRMING,
        NET_DHCPV6_RENEWING,
        NET_DHCPV6_REBINDING,
        NET_DHCPV6_INFO_REQUESTING,
        NET_DHCPV6_BOUND,
} __packed;

#define DHCPV6_TID_SIZE 3

#ifdef CONFIG_NET_DHCPV6_DUID_MAX_LEN
#define NET_DHCPV6_DUID_MAX_LEN CONFIG_NET_DHCPV6_DUID_MAX_LEN
#else
#define NET_DHCPV6_DUID_MAX_LEN 22
#endif

struct net_dhcpv6_duid_raw {
        uint16_t type;
        uint8_t buf[NET_DHCPV6_DUID_MAX_LEN];
} __packed;

struct net_dhcpv6_duid_storage {
        struct net_dhcpv6_duid_raw duid;
        uint8_t length;
};

#ifdef CONFIG_NET_DHCPV6_MAX_DOWNSTREAM
#define NET_DHCPV6_MAX_DOWNSTREAM CONFIG_NET_DHCPV6_MAX_DOWNSTREAM
#else
#define NET_DHCPV6_MAX_DOWNSTREAM 1
#endif

struct net_if;


struct net_dhcpv6_params {
        bool request_addr : 1;
        bool request_prefix : 1;
        uint8_t downstream_count;
        int downstream_ifaces[NET_DHCPV6_MAX_DOWNSTREAM];
};

void net_dhcpv6_start(struct net_if *iface, struct net_dhcpv6_params *params);

void net_dhcpv6_stop(struct net_if *iface);

void net_dhcpv6_restart(struct net_if *iface);


const char *net_dhcpv6_state_name(enum net_dhcpv6_state state);



#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_NET_DHCPV6_H_ */
```

## 130.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2023 Nordic Semiconductor ASA。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 145 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_NET_DHCPV6_H_`。

## 130.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/dhcpv6_8h.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [net_if](../network_core_model_reference/P079_net_if_结构体.md)
- [net_dhcpv6_params](../network_core_model_reference/P056_net_dhcpv6_params_结构体.md)
- [request_addr](../network_core_model_reference/P056_net_dhcpv6_params_结构体.md#a4bc3655ee2a830879667cdb554883573)
- [request_prefix](../network_core_model_reference/P056_net_dhcpv6_params_结构体.md#afd290d92fcc5ae3bac9a9c7030910e6b)
- [downstream_count](../network_core_model_reference/P056_net_dhcpv6_params_结构体.md#a2549234454437b4316f863347236ef6c)
- [downstream_ifaces](../network_core_model_reference/P056_net_dhcpv6_params_结构体.md#ad66949eb34540dbe8808dc9aea9e6368)
- [net_dhcpv6_start](https://docs.zephyrproject.org/latest/doxygen/html/group__dhcpv6.html#gab607a476c947d0335a254304e5dc2a24)
- [net_dhcpv6_stop](https://docs.zephyrproject.org/latest/doxygen/html/group__dhcpv6.html#gaf0b903bdcd0becf06ed6b212c74097a0)
- [net_dhcpv6_restart](https://docs.zephyrproject.org/latest/doxygen/html/group__dhcpv6.html#ga99642b89c14cb17f35b45a03a2286441)
- [state](https://docs.zephyrproject.org/latest/doxygen/html/parser__state_8h.html#adc6e5733fc3c22f0a7b2914188c49c90)
- [net_dhcpv6_params::downstream_count](../network_core_model_reference/P056_net_dhcpv6_params_结构体.md#a2549234454437b4316f863347236ef6c)
- [net_dhcpv6_params::request_addr](../network_core_model_reference/P056_net_dhcpv6_params_结构体.md#a4bc3655ee2a830879667cdb554883573)
- [net_dhcpv6_params::downstream_ifaces](../network_core_model_reference/P056_net_dhcpv6_params_结构体.md#ad66949eb34540dbe8808dc9aea9e6368)
- [net_dhcpv6_params::request_prefix](../network_core_model_reference/P056_net_dhcpv6_params_结构体.md#afd290d92fcc5ae3bac9a9c7030910e6b)

---

[上一章](P129_dhcpv4_server.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P131_dhcpv6_server.h_源码浏览.md)
