---
id: learning.zephyr-docs.api-source-reference.page-129
title: dhcpv4_server.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/dhcpv4__server_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第129章\_dhcpv4\_server.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/dhcpv4__server_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/dhcpv4__server_8h.html)。

## 129.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00004"></a>
<a id="l00005"></a>
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
<a id="l00029"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="l00034"></a>
<a id="l00035"></a>
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
<a id="l00066"></a>
<a id="l00081"></a>
<a id="l00082"></a>
<a id="l00093"></a>
<a id="l00094"></a>
<a id="l00103"></a>
<a id="l00104"></a>
<a id="l00105"></a>
<a id="l00106"></a>
<a id="l00119"></a>
<a id="l00120"></a>
<a id="l00121"></a>
<a id="l00122"></a>
<a id="l00138"></a>
<a id="l00139"></a>
<a id="l00140"></a>
<a id="l00141"></a>
<a id="l00148"></a>
<a id="l00149"></a>
<a id="l00150"></a>
<a id="l00166"></a>
<a id="l00167"></a>
<a id="l00168"></a>
<a id="l00169"></a>
<a id="l00176"></a>
<a id="l00177"></a>
<a id="l00178"></a>
<a id="l00182"></a>
<a id="l00183"></a>
<a id="l00184"></a>
<a id="l00185"></a>
<a id="l00186"></a>
<a id="l00187"></a>
<a id="aclock_8h_html"></a>
<a id="agroup__dhcpv4__server_html_ga1a56f6dbb4c900e9d5c25cc9c04acac5"></a>
<a id="agroup__dhcpv4__server_html_ga1db06c0bf6a5f79334c81472b0a37bb7"></a>
<a id="agroup__dhcpv4__server_html_ga240c9c47957ea66ba88cc2945f295e11"></a>
<a id="agroup__dhcpv4__server_html_ga4a35c423ca86cb324e983d07f6181691"></a>
<a id="agroup__dhcpv4__server_html_ga636b2c71a7d5f00997cba946c31c0c00"></a>
<a id="agroup__dhcpv4__server_html_ga7955e5f3ff357c292a8641c0385f34e4"></a>
<a id="agroup__dhcpv4__server_html_gabd37fd84bc25525d4f1aec4df8aef8b6"></a>
<a id="agroup__dhcpv4__server_html_gac2ff21f144101fb00a87be4ca6f6301e"></a>
<a id="anet__ip_8h_html"></a>
<a id="aparser__state_8h_html_adc6e5733fc3c22f0a7b2914188c49c90"></a>
<a id="astdbool_8h_html_abb452686968e48b67397da5f97445f5b"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astructnet__if_html"></a>
<a id="astructnet__in__addr_html"></a>

```c


/*
 * Copyright (c) 2024 Nordic Semiconductor ASA
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_NET_DHCPV4_SERVER_H_
#define ZEPHYR_INCLUDE_NET_DHCPV4_SERVER_H_

#include <zephyr/net/net_ip.h>
#include <zephyr/sys/clock.h>

#ifdef __cplusplus
extern "C" {
#endif



struct net_if;

#define DHCPV4_CLIENT_ID_MAX_SIZE 20

#define DHCPV4_HARDWARE_ADDRESS_MAX_SIZE 16

enum dhcpv4_server_addr_state {
        DHCPV4_SERVER_ADDR_FREE,
        DHCPV4_SERVER_ADDR_RESERVED,
        DHCPV4_SERVER_ADDR_ALLOCATED,
        DHCPV4_SERVER_ADDR_DECLINED,
};

struct dhcpv4_client_id {
        uint8_t hw_addr_type;
        uint8_t hw_addr_buf[DHCPV4_HARDWARE_ADDRESS_MAX_SIZE];
        uint8_t hw_addr_len;

        uint8_t buf[DHCPV4_CLIENT_ID_MAX_SIZE];
        uint8_t len;
};

struct dhcpv4_addr_slot {
        enum dhcpv4_server_addr_state state;
        struct dhcpv4_client_id client_id;
        struct net_in_addr addr;
        uint32_t lease_time;
        k_timepoint_t expiry;
};


int net_dhcpv4_server_start(struct net_if *iface, struct net_in_addr *base_addr);

int net_dhcpv4_server_stop(struct net_if *iface);

typedef void (*net_dhcpv4_lease_cb_t)(struct net_if *iface,
                                      struct dhcpv4_addr_slot *lease,
                                      void *user_data);

int net_dhcpv4_server_foreach_lease(struct net_if *iface,
                                    net_dhcpv4_lease_cb_t cb,
                                    void *user_data);

typedef int (*net_dhcpv4_server_provider_cb_t)(struct net_if *iface,
                                               const struct dhcpv4_client_id *client_id,
                                               struct net_in_addr *addr,
                                               void *user_data);
void net_dhcpv4_server_set_provider_cb(net_dhcpv4_server_provider_cb_t cb,
                                       void *user_data);

typedef bool (*net_dhcpv4_server_address_validator_cb_t)(struct net_if *iface,
                                                        const struct dhcpv4_client_id *client_id,
                                                        const struct net_in_addr *addr,
                                                        void *user_data);
void net_dhcpv4_server_set_address_validator_cb(net_dhcpv4_server_address_validator_cb_t cb,
                                                void *user_data);


#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_NET_DHCPV4_SERVER_H_ */
```

## 129.2\_可见注释译文（Comments）

### 注释 1：原第 5 行

版权（Copyright）：© 2024 Nordic Semiconductor ASA。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 187 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_NET_DHCPV4_SERVER_H_`。

## 129.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/dhcpv4__server_8h.html)
- [zephyr/net/net_ip.h](https://docs.zephyrproject.org/latest/doxygen/html/net__ip_8h.html)
- [zephyr/sys/clock.h](../timer_reference/P090_系统时钟头文件参考.md)
- [net_if](../network_core_model_reference/P079_net_if_结构体.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [state](https://docs.zephyrproject.org/latest/doxygen/html/parser__state_8h.html#adc6e5733fc3c22f0a7b2914188c49c90)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [net_dhcpv4_server_start](https://docs.zephyrproject.org/latest/doxygen/html/group__dhcpv4__server.html#ga1a56f6dbb4c900e9d5c25cc9c04acac5)
- [net_in_addr](../network_core_model_reference/P096_net_in_addr_结构体.md)
- [net_dhcpv4_server_stop](https://docs.zephyrproject.org/latest/doxygen/html/group__dhcpv4__server.html#ga7955e5f3ff357c292a8641c0385f34e4)
- [net_dhcpv4_lease_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__dhcpv4__server.html#gabd37fd84bc25525d4f1aec4df8aef8b6)
- [net_dhcpv4_server_foreach_lease](https://docs.zephyrproject.org/latest/doxygen/html/group__dhcpv4__server.html#ga636b2c71a7d5f00997cba946c31c0c00)
- [net_dhcpv4_server_provider_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__dhcpv4__server.html#ga4a35c423ca86cb324e983d07f6181691)
- [net_dhcpv4_server_set_provider_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__dhcpv4__server.html#ga1db06c0bf6a5f79334c81472b0a37bb7)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)
- [net_dhcpv4_server_address_validator_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__dhcpv4__server.html#gac2ff21f144101fb00a87be4ca6f6301e)
- [net_dhcpv4_server_set_address_validator_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__dhcpv4__server.html#ga240c9c47957ea66ba88cc2945f295e11)
- [clock.h](../timer_reference/P090_系统时钟头文件参考.md)
- [net_ip.h](https://docs.zephyrproject.org/latest/doxygen/html/net__ip_8h.html)

---

[上一章](P128_dhcpv4.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P130_dhcpv6.h_源码浏览.md)
