---
id: learning.zephyr-docs.api-source-reference.page-128
title: dhcpv4.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/dhcpv4_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第128章\_dhcpv4.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/dhcpv4_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/dhcpv4_8h.html)。

## 128.1\_原始可见代码（Source Code）

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
<a id="l00050"></a>
<a id="foldopen00060"></a>
<a id="l00060"></a>
<a id="l00061"></a>
<a id="l00062"></a>
<a id="l00063"></a>
<a id="l00064"></a>
<a id="l00065"></a>
<a id="l00066"></a>
<a id="l00067"></a>
<a id="l00068"></a>
<a id="l00069"></a>
<a id="l00070"></a>
<a id="l00071"></a>
<a id="l00072"></a>
<a id="l00073"></a>
<a id="l00089"></a>
<a id="l00090"></a>
<a id="l00091"></a>
<a id="l00092"></a>
<a id="l00093"></a>
<a id="l00095"></a>
<a id="l00106"></a>
<a id="l00110"></a>
<a id="l00111"></a>
<a id="l00113"></a>
<a id="l00114"></a>
<a id="l00116"></a>
<a id="l00117"></a>
<a id="l00119"></a>
<a id="l00120"></a>
<a id="l00124"></a>
<a id="l00125"></a>
<a id="l00126"></a>
<a id="l00128"></a>
<a id="foldopen00137"></a>
<a id="l00137"></a>
<a id="l00138"></a>
<a id="l00139"></a>
<a id="l00140"></a>
<a id="l00141"></a>
<a id="l00142"></a>
<a id="l00143"></a>
<a id="l00144"></a>
<a id="l00145"></a>
<a id="l00146"></a>
<a id="l00147"></a>
<a id="l00148"></a>
<a id="l00149"></a>
<a id="l00150"></a>
<a id="l00151"></a>
<a id="l00152"></a>
<a id="l00158"></a>
<a id="l00159"></a>
<a id="l00165"></a>
<a id="l00166"></a>
<a id="l00176"></a>
<a id="foldopen00177"></a>
<a id="l00177"></a>
<a id="l00178"></a>
<a id="l00179"></a>
<a id="l00180"></a>
<a id="l00181"></a>
<a id="l00182"></a>
<a id="l00183"></a>
<a id="l00184"></a>
<a id="l00185"></a>
<a id="l00186"></a>
<a id="l00187"></a>
<a id="l00188"></a>
<a id="l00189"></a>
<a id="l00190"></a>
<a id="l00196"></a>
<a id="l00197"></a>
<a id="l00203"></a>
<a id="l00204"></a>
<a id="l00214"></a>
<a id="l00215"></a>
<a id="l00225"></a>
<a id="l00226"></a>
<a id="l00236"></a>
<a id="l00237"></a>
<a id="l00257"></a>
<a id="l00258"></a>
<a id="l00259"></a>
<a id="l00261"></a>
<a id="l00267"></a>
<a id="l00268"></a>
<a id="l00270"></a>
<a id="l00277"></a>
<a id="l00278"></a>
<a id="l00282"></a>
<a id="l00283"></a>
<a id="l00284"></a>
<a id="l00285"></a>
<a id="l00286"></a>
<a id="l00287"></a>
<a id="agroup__dhcpv4_html_ga167e66033d902d7ffcab801b738db224"></a>
<a id="agroup__dhcpv4_html_ga1f362cce448226447d892f5ed8401db5"></a>
<a id="agroup__dhcpv4_html_ga571124b93b5dfdf3377877aded0c374c"></a>
<a id="agroup__dhcpv4_html_ga57979593bfb87d006e634b88a64bdf1a"></a>
<a id="agroup__dhcpv4_html_ga75caf142c6c4e058f78c7be0a4a35a9d"></a>
<a id="agroup__dhcpv4_html_ga84df76c84de248a43e3e26d422cdfc2f"></a>
<a id="agroup__dhcpv4_html_ga910a416e25c2878b84319f6884883d8e"></a>
<a id="agroup__dhcpv4_html_gaa90c4ba8010bcd2079512afe5f288dbb"></a>
<a id="agroup__dhcpv4_html_gabf3d97139fc4f7122c1bdee52cb003cb"></a>
<a id="agroup__dhcpv4_html_gacc66584b0776e5a79b1f4ceea479a7f8"></a>
<a id="agroup__dhcpv4_html_gaec0f1c87f5093767a4bb1c43b8e18e72"></a>
<a id="agroup__dhcpv4_html_gaf073157fcd5cb2d18c40b8697d724a7c"></a>
<a id="agroup__dhcpv4_html_gafa2ddaa5cf17fbe5c4a3ca6fbf883cbe"></a>
<a id="agroup__dhcpv4_html_ggacc66584b0776e5a79b1f4ceea479a7f8a4ec90153e2775f013099541acc15b14e"></a>
<a id="agroup__dhcpv4_html_ggacc66584b0776e5a79b1f4ceea479a7f8a77932735abd547927ed8eef61c9f4925"></a>
<a id="agroup__dhcpv4_html_ggacc66584b0776e5a79b1f4ceea479a7f8a7e2888c4bb7cd85e3fb99b72d1a90a4a"></a>
<a id="agroup__dhcpv4_html_ggacc66584b0776e5a79b1f4ceea479a7f8a9255fce7b8a52f290f6406e039b298c5"></a>
<a id="agroup__dhcpv4_html_ggacc66584b0776e5a79b1f4ceea479a7f8a95d3e660ab59bdfb9de09e95493055c4"></a>
<a id="agroup__dhcpv4_html_ggacc66584b0776e5a79b1f4ceea479a7f8ab8cb4caf5ae9de5bf79f791630475f1d"></a>
<a id="agroup__dhcpv4_html_ggacc66584b0776e5a79b1f4ceea479a7f8aba941cf50fabac68e5d0e07fa923b866"></a>
<a id="agroup__dhcpv4_html_ggacc66584b0776e5a79b1f4ceea479a7f8ad5e45accf00132a16a3c6042a21e7b9f"></a>
<a id="agroup__single-linked-list__apis_html_ga69bf43aad81e3ee2d55250c59b857493"></a>
<a id="ainclude_2zephyr_2types_8h_html"></a>
<a id="aparser__state_8h_html_adc6e5733fc3c22f0a7b2914188c49c90"></a>
<a id="aslist_8h_html"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astructnet__if_html"></a>
<a id="astructnet__in__addr_html"></a>

```c


/*
 * Copyright (c) 2016 Intel Corporation
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_NET_DHCPV4_H_
#define ZEPHYR_INCLUDE_NET_DHCPV4_H_

#include <zephyr/sys/slist.h>
#include <zephyr/types.h>

#ifdef __cplusplus
extern "C" {
#endif



enum net_dhcpv4_state {
        NET_DHCPV4_DISABLED,
        NET_DHCPV4_INIT,
        NET_DHCPV4_INIT_REBOOT,
        NET_DHCPV4_SELECTING,
        NET_DHCPV4_REQUESTING,
        NET_DHCPV4_RENEWING,
        NET_DHCPV4_REBINDING,
        NET_DHCPV4_BOUND,
        NET_DHCPV4_DECLINE,
} __packed;


enum net_dhcpv4_msg_type {
        NET_DHCPV4_MSG_TYPE_DISCOVER    = 1,
        NET_DHCPV4_MSG_TYPE_OFFER       = 2,
        NET_DHCPV4_MSG_TYPE_REQUEST     = 3,
        NET_DHCPV4_MSG_TYPE_DECLINE     = 4,
        NET_DHCPV4_MSG_TYPE_ACK         = 5,
        NET_DHCPV4_MSG_TYPE_NAK         = 6,
        NET_DHCPV4_MSG_TYPE_RELEASE     = 7,
        NET_DHCPV4_MSG_TYPE_INFORM      = 8,
};

struct net_dhcpv4_option_callback;
struct net_in_addr;

typedef void (*net_dhcpv4_option_callback_handler_t)(struct net_dhcpv4_option_callback *cb,
                                                     size_t length,
                                                     enum net_dhcpv4_msg_type msg_type,
                                                     struct net_if *iface);


struct net_dhcpv4_option_callback {
        sys_snode_t node;

        net_dhcpv4_option_callback_handler_t handler;

        uint8_t option;

        size_t max_length;

        void *data;
};


static inline void net_dhcpv4_init_option_callback(struct net_dhcpv4_option_callback *callback,
                                                   net_dhcpv4_option_callback_handler_t handler,
                                                   uint8_t option,
                                                   void *data,
                                                   size_t max_length)
{
        __ASSERT(callback, "Callback pointer should not be NULL");
        __ASSERT(handler, "Callback handler pointer should not be NULL");
        __ASSERT(data, "Data pointer should not be NULL");

        callback->handler = handler;
        callback->option = option;
        callback->data = data;
        callback->max_length = max_length;
}

int net_dhcpv4_add_option_callback(struct net_dhcpv4_option_callback *cb);

int net_dhcpv4_remove_option_callback(struct net_dhcpv4_option_callback *cb);

static inline void
net_dhcpv4_init_option_vendor_callback(struct net_dhcpv4_option_callback *callback,
                                       net_dhcpv4_option_callback_handler_t handler, uint8_t option,
                                       void *data, size_t max_length)
{
        __ASSERT(callback, "Callback pointer should not be NULL");
        __ASSERT(handler, "Callback handler pointer should not be NULL");
        __ASSERT(data, "Data pointer should not be NULL");

        callback->handler = handler;
        callback->option = option;
        callback->data = data;
        callback->max_length = max_length;
}

int net_dhcpv4_add_option_vendor_callback(struct net_dhcpv4_option_callback *cb);

int net_dhcpv4_remove_option_vendor_callback(struct net_dhcpv4_option_callback *cb);

void net_dhcpv4_start(struct net_if *iface);

void net_dhcpv4_stop(struct net_if *iface);

void net_dhcpv4_restart(struct net_if *iface);

int net_dhcpv4_set_reboot_hint(struct net_if *iface,
                               const struct net_in_addr *requested_ip);


const char *net_dhcpv4_state_name(enum net_dhcpv4_state state);


const char *net_dhcpv4_msg_type_name(enum net_dhcpv4_msg_type msg_type);


#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_NET_DHCPV4_H_ */
```

## 128.2\_可见注释译文（Comments）

### 注释 1：原第 5 行

版权（Copyright）：© 2016 Intel Corporation。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 287 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_NET_DHCPV4_H_`。

## 128.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/dhcpv4_8h.html)
- [zephyr/sys/slist.h](../slist_reference/P002_单向链表头文件参考.md)
- [zephyr/types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)
- [net_dhcpv4_msg_type](https://docs.zephyrproject.org/latest/doxygen/html/group__dhcpv4.html#gacc66584b0776e5a79b1f4ceea479a7f8)
- [NET_DHCPV4_MSG_TYPE_DISCOVER](https://docs.zephyrproject.org/latest/doxygen/html/group__dhcpv4.html#ggacc66584b0776e5a79b1f4ceea479a7f8ab8cb4caf5ae9de5bf79f791630475f1d)
- [NET_DHCPV4_MSG_TYPE_OFFER](https://docs.zephyrproject.org/latest/doxygen/html/group__dhcpv4.html#ggacc66584b0776e5a79b1f4ceea479a7f8a7e2888c4bb7cd85e3fb99b72d1a90a4a)
- [NET_DHCPV4_MSG_TYPE_REQUEST](https://docs.zephyrproject.org/latest/doxygen/html/group__dhcpv4.html#ggacc66584b0776e5a79b1f4ceea479a7f8a4ec90153e2775f013099541acc15b14e)
- [NET_DHCPV4_MSG_TYPE_DECLINE](https://docs.zephyrproject.org/latest/doxygen/html/group__dhcpv4.html#ggacc66584b0776e5a79b1f4ceea479a7f8ad5e45accf00132a16a3c6042a21e7b9f)
- [NET_DHCPV4_MSG_TYPE_ACK](https://docs.zephyrproject.org/latest/doxygen/html/group__dhcpv4.html#ggacc66584b0776e5a79b1f4ceea479a7f8a77932735abd547927ed8eef61c9f4925)
- [NET_DHCPV4_MSG_TYPE_NAK](https://docs.zephyrproject.org/latest/doxygen/html/group__dhcpv4.html#ggacc66584b0776e5a79b1f4ceea479a7f8a95d3e660ab59bdfb9de09e95493055c4)
- [NET_DHCPV4_MSG_TYPE_RELEASE](https://docs.zephyrproject.org/latest/doxygen/html/group__dhcpv4.html#ggacc66584b0776e5a79b1f4ceea479a7f8a9255fce7b8a52f290f6406e039b298c5)
- [NET_DHCPV4_MSG_TYPE_INFORM](https://docs.zephyrproject.org/latest/doxygen/html/group__dhcpv4.html#ggacc66584b0776e5a79b1f4ceea479a7f8aba941cf50fabac68e5d0e07fa923b866)
- [net_in_addr](../network_core_model_reference/P096_net_in_addr_结构体.md)
- [net_dhcpv4_option_callback_handler_t](https://docs.zephyrproject.org/latest/doxygen/html/group__dhcpv4.html#ga75caf142c6c4e058f78c7be0a4a35a9d)
- [net_if](../network_core_model_reference/P079_net_if_结构体.md)
- [sys_snode_t](../slist_reference/P001_单向链表公共接口.md#ga69bf43aad81e3ee2d55250c59b857493)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [net_dhcpv4_init_option_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__dhcpv4.html#ga84df76c84de248a43e3e26d422cdfc2f)
- [net_dhcpv4_add_option_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__dhcpv4.html#gaf073157fcd5cb2d18c40b8697d724a7c)
- [net_dhcpv4_remove_option_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__dhcpv4.html#gaa90c4ba8010bcd2079512afe5f288dbb)
- [net_dhcpv4_init_option_vendor_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__dhcpv4.html#gaec0f1c87f5093767a4bb1c43b8e18e72)
- [net_dhcpv4_add_option_vendor_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__dhcpv4.html#gabf3d97139fc4f7122c1bdee52cb003cb)
- [net_dhcpv4_remove_option_vendor_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__dhcpv4.html#ga1f362cce448226447d892f5ed8401db5)
- [net_dhcpv4_start](https://docs.zephyrproject.org/latest/doxygen/html/group__dhcpv4.html#gafa2ddaa5cf17fbe5c4a3ca6fbf883cbe)
- [net_dhcpv4_stop](https://docs.zephyrproject.org/latest/doxygen/html/group__dhcpv4.html#ga910a416e25c2878b84319f6884883d8e)
- [net_dhcpv4_restart](https://docs.zephyrproject.org/latest/doxygen/html/group__dhcpv4.html#ga57979593bfb87d006e634b88a64bdf1a)
- [net_dhcpv4_set_reboot_hint](https://docs.zephyrproject.org/latest/doxygen/html/group__dhcpv4.html#ga167e66033d902d7ffcab801b738db224)
- [state](https://docs.zephyrproject.org/latest/doxygen/html/parser__state_8h.html#adc6e5733fc3c22f0a7b2914188c49c90)
- [net_dhcpv4_msg_type_name](https://docs.zephyrproject.org/latest/doxygen/html/group__dhcpv4.html#ga571124b93b5dfdf3377877aded0c374c)
- [types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)
- [slist.h](../slist_reference/P002_单向链表头文件参考.md)

---

[上一章](P127_dfu_metadata.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P129_dhcpv4_server.h_源码浏览.md)
