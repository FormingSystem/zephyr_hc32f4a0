---
id: learning.zephyr-docs.api-source-configuration-reference.page-8
title: canbus.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/canbus_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第8章\_canbus.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/canbus_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/canbus_8h.html)。

## 8.1\_原始可见代码（Source Code）

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
<a id="l00020"></a>
<a id="l00021"></a>
<a id="l00022"></a>
<a id="l00023"></a>
<a id="foldopen00027"></a>
<a id="l00027"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="l00035"></a>
<a id="l00036"></a>
<a id="l00038"></a>
<a id="l00039"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="l00044"></a>
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
<a id="l00068"></a>
<a id="l00069"></a>
<a id="l00070"></a>
<a id="l00071"></a>
<a id="l00072"></a>
<a id="l00073"></a>
<a id="l00074"></a>
<a id="l00075"></a>
<a id="l00076"></a>
<a id="l00077"></a>
<a id="l00078"></a>
<a id="l00079"></a>
<a id="l00080"></a>
<a id="l00081"></a>
<a id="l00082"></a>
<a id="l00083"></a>
<a id="l00085"></a>
<a id="l00086"></a>
<a id="l00087"></a>
<a id="l00088"></a>
<a id="l00089"></a>
<a id="l00090"></a>
<a id="adrivers_2can_8h_html"></a>
<a id="agroup__ip__4__6_html_ga361fe60d9b96001f74363788352858a0"></a>
<a id="ainclude_2zephyr_2types_8h_html"></a>
<a id="anet__if_8h_html"></a>
<a id="anet__ip_8h_html"></a>
<a id="asocketcan_8h_html"></a>
<a id="astructcanbus__api_html"></a>
<a id="astructcanbus__api_html_a03a36b089a813aecaab120acf66542d2"></a>
<a id="astructcanbus__api_html_a31fee4b60f4ab2f832e0599c23337b6c"></a>
<a id="astructcanbus__api_html_abff03e6144170f8f223e11a7f28b59b7"></a>
<a id="astructcanbus__api_html_ade7bbf8e2f366425ed4da89b78272885"></a>
<a id="astructcanbus__api_html_af8f809bf252a5d261209af2b7b3096f7"></a>
<a id="astructdevice_html"></a>
<a id="astructnet__if_html"></a>
<a id="astructnet__pkt_html"></a>

```c
/*
 * Copyright (c) 2019 Intel Corporation
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_NET_CANBUS_H_
#define ZEPHYR_INCLUDE_NET_CANBUS_H_

#include <zephyr/types.h>
#include <zephyr/net/net_ip.h>
#include <zephyr/net/net_if.h>
#include <zephyr/net/socketcan.h>
#include <zephyr/drivers/can.h>

#ifdef __cplusplus
extern "C" {
#endif

struct canbus_api {
        struct net_if_api iface_api;

        int (*send)(const struct device *dev, struct net_pkt *pkt);

        void (*close)(const struct device *dev, int filter_id);

        int (*setsockopt)(const struct device *dev, void *obj, int level,
                          int optname,
                          const void *optval, net_socklen_t optlen);

        int (*getsockopt)(const struct device *dev, void *obj, int level,
                          int optname,
                          const void *optval, net_socklen_t *optlen);
};

/* Make sure that the network interface API is properly setup inside
 * CANBUS API struct (it is the first one).
 */
BUILD_ASSERT(offsetof(struct canbus_api, iface_api) == 0);


struct z_net_canbus_context {
        struct net_if *iface;
};

struct z_net_canbus_config {
        const struct device *can_dev;
};

int z_net_canbus_init(const struct device *dev);

extern const struct canbus_api z_net_canbus_api;

/*
 * Network interface of a CAN controller, defined by CAN_DEVICE_DT_DEFINE() next to the
 * controller's device so that only controllers with a driver in the build get one.
 */
#define Z_NET_CANBUS_DEVICE_DT_DEFINE(node_id)                                                     \
        static struct z_net_canbus_context z_net_canbus_ctx_##node_id;                             \
        static const struct z_net_canbus_config z_net_canbus_cfg_##node_id = {                     \
                .can_dev = DEVICE_DT_GET(node_id),                                                 \
        };                                                                                         \
        NET_DEVICE_INIT(net_canbus_##node_id, DEVICE_DT_NAME(node_id), z_net_canbus_init, NULL,    \
                        &z_net_canbus_ctx_##node_id, &z_net_canbus_cfg_##node_id,                  \
                        CONFIG_NET_CANBUS_INIT_PRIORITY, &z_net_canbus_api, CANBUS_RAW_L2,         \
                        NET_L2_GET_CTX_TYPE(CANBUS_RAW_L2), CAN_MTU);


#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_NET_CANBUS_H_ */
```

## 8.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2019 Intel Corporation。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 51 行

确保网络接口 API 正确放置在 CANBUS API 结构体内，即作为其第一个成员。

### 注释 3：原第 70 行

CAN 控制器的网络接口，由 `CAN_DEVICE_DT_DEFINE()` 在控制器设备旁定义，因此只有驱动被纳入构建的控制器才会拥有该接口。

### 注释 4：原第 90 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_NET_CANBUS_H_`。

## 8.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/canbus_8h.html)
- [zephyr/types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)
- [zephyr/net/net_ip.h](https://docs.zephyrproject.org/latest/doxygen/html/net__ip_8h.html)
- [zephyr/net/net_if.h](https://docs.zephyrproject.org/latest/doxygen/html/net__if_8h.html)
- [zephyr/net/socketcan.h](https://docs.zephyrproject.org/latest/doxygen/html/socketcan_8h.html)
- [zephyr/drivers/can.h](../can_driver_reference/P001_CAN驱动头文件参考.md)
- [canbus_api](../network_service_model_reference/P001_canbus_api_结构体.md)
- [iface_api](../network_service_model_reference/P001_canbus_api_结构体.md#af8f809bf252a5d261209af2b7b3096f7)
- [send](../network_service_model_reference/P001_canbus_api_结构体.md#a31fee4b60f4ab2f832e0599c23337b6c)
- [device](../device_reference/P002_设备对象结构.md)
- [net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)
- [close](../network_service_model_reference/P001_canbus_api_结构体.md#abff03e6144170f8f223e11a7f28b59b7)
- [setsockopt](../network_service_model_reference/P001_canbus_api_结构体.md#a03a36b089a813aecaab120acf66542d2)
- [net_socklen_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga361fe60d9b96001f74363788352858a0)
- [getsockopt](../network_service_model_reference/P001_canbus_api_结构体.md#ade7bbf8e2f366425ed4da89b78272885)
- [net_if](../network_core_model_reference/P079_net_if_结构体.md)
- [can.h](../can_driver_reference/P001_CAN驱动头文件参考.md)
- [types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)
- [net_if.h](https://docs.zephyrproject.org/latest/doxygen/html/net__if_8h.html)
- [net_ip.h](https://docs.zephyrproject.org/latest/doxygen/html/net__ip_8h.html)
- [socketcan.h](https://docs.zephyrproject.org/latest/doxygen/html/socketcan_8h.html)
- [canbus_api::setsockopt](../network_service_model_reference/P001_canbus_api_结构体.md#a03a36b089a813aecaab120acf66542d2)
- [canbus_api::send](../network_service_model_reference/P001_canbus_api_结构体.md#a31fee4b60f4ab2f832e0599c23337b6c)
- [canbus_api::close](../network_service_model_reference/P001_canbus_api_结构体.md#abff03e6144170f8f223e11a7f28b59b7)
- [canbus_api::getsockopt](../network_service_model_reference/P001_canbus_api_结构体.md#ade7bbf8e2f366425ed4da89b78272885)
- [canbus_api::iface_api](../network_service_model_reference/P001_canbus_api_结构体.md#af8f809bf252a5d261209af2b7b3096f7)

---

[上一章](P007_arm-v2m_beetle-pinctrl.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P009_cc1200.h_源码浏览.md)
