---
id: learning.zephyr-docs.api-source-supplement-reference.page-139
title: offloaded_netdev.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/offloaded__netdev_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第139章\_offloaded\_netdev.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/offloaded__netdev_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/offloaded__netdev_8h.html)。

## 139.1\_原始可见代码（Source Code）

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
<a id="foldopen00035"></a>
<a id="l00035"></a>
<a id="l00037"></a>
<a id="l00038"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="l00043"></a>
<a id="l00044"></a>
<a id="l00046"></a>
<a id="l00047"></a>
<a id="l00048"></a>
<a id="foldopen00053"></a>
<a id="l00053"></a>
<a id="l00058"></a>
<a id="l00059"></a>
<a id="l00061"></a>
<a id="l00062"></a>
<a id="l00064"></a>
<a id="l00065"></a>
<a id="l00066"></a>
<a id="l00067"></a>
<a id="l00068"></a>
<a id="l00069"></a>
<a id="foldopen00077"></a>
<a id="l00077"></a>
<a id="l00078"></a>
<a id="l00079"></a>
<a id="l00080"></a>
<a id="l00081"></a>
<a id="l00082"></a>
<a id="l00083"></a>
<a id="l00084"></a>
<a id="l00085"></a>
<a id="l00086"></a>
<a id="l00087"></a>
<a id="l00088"></a>
<a id="l00089"></a>
<a id="l00090"></a>
<a id="l00094"></a>
<a id="l00095"></a>
<a id="l00096"></a>
<a id="l00097"></a>
<a id="l00098"></a>
<a id="l00099"></a>
<a id="agroup__net__if_html_gaeb8c703f273bc07ae9bb7a0d8bfe6f3d"></a>
<a id="agroup__offloaded__netdev_html_gac1980977f6da3ace33ede7949d43f81f"></a>
<a id="agroup__offloaded__netdev_html_gad1076eacf1b1e82f70759f9b54937ced"></a>
<a id="agroup__offloaded__netdev_html_ggac1980977f6da3ace33ede7949d43f81fa46a984d855ea5731207274149b12de1d"></a>
<a id="agroup__offloaded__netdev_html_ggac1980977f6da3ace33ede7949d43f81fa532f2d2684118c1c7e78064b5bd7920a"></a>
<a id="agroup__offloaded__netdev_html_ggac1980977f6da3ace33ede7949d43f81fa85328162750725aae17aa0d84a4dab21"></a>
<a id="agroup__offloaded__netdev_html_ggac1980977f6da3ace33ede7949d43f81fab764b4fe8932593599bd26b9ebf11f24"></a>
<a id="ainclude_2zephyr_2types_8h_html"></a>
<a id="akernel_8h_html"></a>
<a id="anet__if_8h_html"></a>
<a id="aparser__state_8h_html_adc6e5733fc3c22f0a7b2914188c49c90"></a>
<a id="astdbool_8h_html"></a>
<a id="astructdevice_html"></a>
<a id="astructdevice_html_a4a2e6a2cfeb6efed7d5383c33458f46d"></a>
<a id="astructnet__if_html"></a>
<a id="astructoffloaded__if__api_html"></a>
<a id="astructoffloaded__if__api_html_a24cc2bd70d18075731be617955e3e1a8"></a>
<a id="astructoffloaded__if__api_html_a5ae87a9ed455f62958e1f2fa8cb715e7"></a>
<a id="astructoffloaded__if__api_html_aadf471a8e3ae22f3294df1cab090a7a3"></a>

```c


/*
 * Copyright (c) 2022 Nordic Semiconductor ASA
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_NET_OFFLOADED_NETDEV_H_
#define ZEPHYR_INCLUDE_NET_OFFLOADED_NETDEV_H_

#include <zephyr/kernel.h>
#include <zephyr/types.h>
#include <stdbool.h>
#include <zephyr/net/net_if.h>

#ifdef __cplusplus
extern "C" {
#endif


enum offloaded_net_if_types {
        L2_OFFLOADED_NET_IF_TYPE_UNKNOWN,

        L2_OFFLOADED_NET_IF_TYPE_ETHERNET,

        L2_OFFLOADED_NET_IF_TYPE_MODEM,

        L2_OFFLOADED_NET_IF_TYPE_WIFI,
};

struct offloaded_if_api {
        struct net_if_api iface_api;

        int (*enable)(const struct net_if *iface, bool state);

        enum offloaded_net_if_types (*get_type)(void);
};

/* Ensure offloaded_if_api is compatible with net_if_api */
BUILD_ASSERT(offsetof(struct offloaded_if_api, iface_api) == 0);

static inline bool net_off_is_wifi_offloaded(struct net_if *iface)
{
        const struct device *dev = net_if_get_device(iface);
        const struct offloaded_if_api *api;

        NET_ASSERT(dev != NULL);

        api = (const struct offloaded_if_api *)dev->api;

        NET_ASSERT(api != NULL);

        return api->get_type && api->get_type() == L2_OFFLOADED_NET_IF_TYPE_WIFI;
}


#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_NET_OFFLOADED_NETDEV_H_ */
```

## 139.2\_可见注释译文（Comments）

### 注释 1：原第 7 行

版权（Copyright）：© 2022 Nordic Semiconductor ASA。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 67 行

确保 `offloaded_if_api` 与 `net_if_api` 兼容。

### 注释 3：原第 99 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_NET_OFFLOADED_NETDEV_H_`。

## 139.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/offloaded__netdev_8h.html)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [zephyr/types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)
- [stdbool.h](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html)
- [zephyr/net/net_if.h](https://docs.zephyrproject.org/latest/doxygen/html/net__if_8h.html)
- [offloaded_net_if_types](https://docs.zephyrproject.org/latest/doxygen/html/group__offloaded__netdev.html#gac1980977f6da3ace33ede7949d43f81f)
- [L2_OFFLOADED_NET_IF_TYPE_UNKNOWN](https://docs.zephyrproject.org/latest/doxygen/html/group__offloaded__netdev.html#ggac1980977f6da3ace33ede7949d43f81fa46a984d855ea5731207274149b12de1d)
- [L2_OFFLOADED_NET_IF_TYPE_ETHERNET](https://docs.zephyrproject.org/latest/doxygen/html/group__offloaded__netdev.html#ggac1980977f6da3ace33ede7949d43f81fa532f2d2684118c1c7e78064b5bd7920a)
- [L2_OFFLOADED_NET_IF_TYPE_MODEM](https://docs.zephyrproject.org/latest/doxygen/html/group__offloaded__netdev.html#ggac1980977f6da3ace33ede7949d43f81fa85328162750725aae17aa0d84a4dab21)
- [L2_OFFLOADED_NET_IF_TYPE_WIFI](https://docs.zephyrproject.org/latest/doxygen/html/group__offloaded__netdev.html#ggac1980977f6da3ace33ede7949d43f81fab764b4fe8932593599bd26b9ebf11f24)
- [offloaded_if_api](../network_service_model_reference/P038_offloaded_if_api_结构体.md)
- [iface_api](../network_service_model_reference/P038_offloaded_if_api_结构体.md#a24cc2bd70d18075731be617955e3e1a8)
- [enable](../network_service_model_reference/P038_offloaded_if_api_结构体.md#aadf471a8e3ae22f3294df1cab090a7a3)
- [net_if](../network_core_model_reference/P079_net_if_结构体.md)
- [state](https://docs.zephyrproject.org/latest/doxygen/html/parser__state_8h.html#adc6e5733fc3c22f0a7b2914188c49c90)
- [get_type](../network_service_model_reference/P038_offloaded_if_api_结构体.md#a5ae87a9ed455f62958e1f2fa8cb715e7)
- [net_off_is_wifi_offloaded](https://docs.zephyrproject.org/latest/doxygen/html/group__offloaded__netdev.html#gad1076eacf1b1e82f70759f9b54937ced)
- [device](../device_reference/P002_设备对象结构.md)
- [net_if_get_device](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#gaeb8c703f273bc07ae9bb7a0d8bfe6f3d)
- [api](../device_reference/P002_设备对象结构.md#a4a2e6a2cfeb6efed7d5383c33458f46d)
- [types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)
- [kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [net_if.h](https://docs.zephyrproject.org/latest/doxygen/html/net__if_8h.html)
- [device::api](../device_reference/P002_设备对象结构.md#a4a2e6a2cfeb6efed7d5383c33458f46d)
- [offloaded_if_api::iface_api](../network_service_model_reference/P038_offloaded_if_api_结构体.md#a24cc2bd70d18075731be617955e3e1a8)
- [offloaded_if_api::get_type](../network_service_model_reference/P038_offloaded_if_api_结构体.md#a5ae87a9ed455f62958e1f2fa8cb715e7)
- [offloaded_if_api::enable](../network_service_model_reference/P038_offloaded_if_api_结构体.md#aadf471a8e3ae22f3294df1cab090a7a3)

---

[上一章](P138_nxp_nx20p3483.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P140_paj7620.h_源码浏览.md)
