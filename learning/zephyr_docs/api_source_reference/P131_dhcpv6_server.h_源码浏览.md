---
id: learning.zephyr-docs.api-source-reference.page-131
title: dhcpv6_server.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/dhcpv6__server_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第131章\_dhcpv6\_server.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/dhcpv6__server_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/dhcpv6__server_8h.html)。

## 131.1\_原始可见代码（Source Code）

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
<a id="l00018"></a>
<a id="l00019"></a>
<a id="l00028"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="foldopen00032"></a>
<a id="l00032"></a>
<a id="l00037"></a>
<a id="l00038"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="l00045"></a>
<a id="l00046"></a>
<a id="l00050"></a>
<a id="l00051"></a>
<a id="l00053"></a>
<a id="l00054"></a>
<a id="l00056"></a>
<a id="l00057"></a>
<a id="l00059"></a>
<a id="l00060"></a>
<a id="l00061"></a>
<a id="l00070"></a>
<a id="l00071"></a>
<a id="l00072"></a>
<a id="l00080"></a>
<a id="l00081"></a>
<a id="l00083"></a>
<a id="l00085"></a>
<a id="l00087"></a>
<a id="l00089"></a>
<a id="l00091"></a>
<a id="l00095"></a>
<a id="l00097"></a>
<a id="l00099"></a>
<a id="l00101"></a>
<a id="l00103"></a>
<a id="l00104"></a>
<a id="l00105"></a>
<a id="l00107"></a>
<a id="l00116"></a>
<a id="l00117"></a>
<a id="l00118"></a>
<a id="l00119"></a>
<a id="l00133"></a>
<a id="l00134"></a>
<a id="l00135"></a>
<a id="l00136"></a>
<a id="l00140"></a>
<a id="l00141"></a>
<a id="l00142"></a>
<a id="l00143"></a>
<a id="l00144"></a>
<a id="l00145"></a>
<a id="agroup__dhcpv6__server_html_ga5fdf013a85ca7701ad92c8f50c1b0ed0"></a>
<a id="agroup__dhcpv6__server_html_ga86f2ef89515d47d8ba4fe9b45da1eca9"></a>
<a id="agroup__dhcpv6__server_html_gaaedb437385fa27b8454bfc670ff9aa71"></a>
<a id="agroup__dhcpv6__server_html_gae090b9103bc0110eca408d3a3989c574"></a>
<a id="anet__ip_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_ac714c0d2c1a4adb10e73cab29623314b"></a>
<a id="astructnet__dhcpv6__server__params_html"></a>
<a id="astructnet__dhcpv6__server__params_html_a18cb34a5b577bebac7217fa13be13a5f"></a>
<a id="astructnet__dhcpv6__server__params_html_a3cedeee330d5b1765757b4c45d9caf6c"></a>
<a id="astructnet__dhcpv6__server__params_html_a426d99918b620fdc614d5812bc130256"></a>
<a id="astructnet__dhcpv6__server__params_html_a809af0885a7bbd7860d699eebe7b9e08"></a>
<a id="astructnet__dhcpv6__server__params_html_a83e5a07233e7558c487fe6804d21fd09"></a>
<a id="astructnet__dhcpv6__server__params_html_ae22caa5aeceefbfec8abac15334b1d67"></a>
<a id="astructnet__dhcpv6__server__params_html_aeeaf66c9475df8dc0e948938228f08d7"></a>
<a id="astructnet__if_html"></a>
<a id="astructnet__in6__addr_html"></a>

```c
/*
 * Copyright The Zephyr Project Contributors
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_NET_DHCPV6_SERVER_H_
#define ZEPHYR_INCLUDE_NET_DHCPV6_SERVER_H_

#include <zephyr/net/net_ip.h>

#ifdef __cplusplus
extern "C" {
#endif


struct net_if;

struct net_dhcpv6_server_params {
        struct net_in6_addr prefix;

        struct net_in6_addr addr;

        uint32_t valid_lifetime;

        uint32_t preferred_lifetime;

        uint8_t prefix_len;

        bool offer_addr : 1;

        bool offer_prefix : 1;
};

int net_dhcpv6_server_start(struct net_if *iface,
                            struct net_dhcpv6_server_params *params);

int net_dhcpv6_server_stop(struct net_if *iface);


struct net_dhcpv6_server_lease {
        struct net_in6_addr addr;
        struct net_in6_addr prefix;
        const uint8_t *duid;
        int64_t expiry;
        uint8_t duid_len;
        uint8_t prefix_len;
        bool has_addr;
        bool has_prefix;
};


typedef void (*net_dhcpv6_server_lease_cb_t)(
        struct net_if *iface, struct net_dhcpv6_server_lease *lease,
        void *user_data);

int net_dhcpv6_server_foreach_lease(struct net_if *iface,
                                    net_dhcpv6_server_lease_cb_t cb,
                                    void *user_data);


#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_NET_DHCPV6_SERVER_H_ */
```

## 131.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：The Zephyr Project Contributors。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 145 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_NET_DHCPV6_SERVER_H_`。

## 131.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/dhcpv6__server_8h.html)
- [zephyr/net/net_ip.h](https://docs.zephyrproject.org/latest/doxygen/html/net__ip_8h.html)
- [net_if](../network_core_model_reference/P079_net_if_结构体.md)
- [net_dhcpv6_server_params](../network_core_model_reference/P057_net_dhcpv6_server_params_结构体.md)
- [net_in6_addr](../network_core_model_reference/P094_net_in6_addr_结构体.md)
- [prefix](../network_core_model_reference/P057_net_dhcpv6_server_params_结构体.md#a426d99918b620fdc614d5812bc130256)
- [addr](../network_core_model_reference/P057_net_dhcpv6_server_params_结构体.md#a83e5a07233e7558c487fe6804d21fd09)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [valid_lifetime](../network_core_model_reference/P057_net_dhcpv6_server_params_结构体.md#aeeaf66c9475df8dc0e948938228f08d7)
- [preferred_lifetime](../network_core_model_reference/P057_net_dhcpv6_server_params_结构体.md#a18cb34a5b577bebac7217fa13be13a5f)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [prefix_len](../network_core_model_reference/P057_net_dhcpv6_server_params_结构体.md#a3cedeee330d5b1765757b4c45d9caf6c)
- [offer_addr](../network_core_model_reference/P057_net_dhcpv6_server_params_结构体.md#ae22caa5aeceefbfec8abac15334b1d67)
- [offer_prefix](../network_core_model_reference/P057_net_dhcpv6_server_params_结构体.md#a809af0885a7bbd7860d699eebe7b9e08)
- [net_dhcpv6_server_start](https://docs.zephyrproject.org/latest/doxygen/html/group__dhcpv6__server.html#ga5fdf013a85ca7701ad92c8f50c1b0ed0)
- [net_dhcpv6_server_stop](https://docs.zephyrproject.org/latest/doxygen/html/group__dhcpv6__server.html#gae090b9103bc0110eca408d3a3989c574)
- [int64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#ac714c0d2c1a4adb10e73cab29623314b)
- [net_dhcpv6_server_lease_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__dhcpv6__server.html#ga86f2ef89515d47d8ba4fe9b45da1eca9)
- [net_dhcpv6_server_foreach_lease](https://docs.zephyrproject.org/latest/doxygen/html/group__dhcpv6__server.html#gaaedb437385fa27b8454bfc670ff9aa71)
- [net_ip.h](https://docs.zephyrproject.org/latest/doxygen/html/net__ip_8h.html)
- [net_dhcpv6_server_params::preferred_lifetime](../network_core_model_reference/P057_net_dhcpv6_server_params_结构体.md#a18cb34a5b577bebac7217fa13be13a5f)
- [net_dhcpv6_server_params::prefix_len](../network_core_model_reference/P057_net_dhcpv6_server_params_结构体.md#a3cedeee330d5b1765757b4c45d9caf6c)
- [net_dhcpv6_server_params::prefix](../network_core_model_reference/P057_net_dhcpv6_server_params_结构体.md#a426d99918b620fdc614d5812bc130256)
- [net_dhcpv6_server_params::offer_prefix](../network_core_model_reference/P057_net_dhcpv6_server_params_结构体.md#a809af0885a7bbd7860d699eebe7b9e08)
- [net_dhcpv6_server_params::addr](../network_core_model_reference/P057_net_dhcpv6_server_params_结构体.md#a83e5a07233e7558c487fe6804d21fd09)
- [net_dhcpv6_server_params::offer_addr](../network_core_model_reference/P057_net_dhcpv6_server_params_结构体.md#ae22caa5aeceefbfec8abac15334b1d67)
- [net_dhcpv6_server_params::valid_lifetime](../network_core_model_reference/P057_net_dhcpv6_server_params_结构体.md#aeeaf66c9475df8dc0e948938228f08d7)

---

[上一章](P130_dhcpv6.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P132_direction.h_源码浏览.md)
