---
id: learning.zephyr-docs.api-source-runtime-reference.page-15
title: dsa_tag.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/dsa__tag_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第15章\_dsa\_tag.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/dsa__tag_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/dsa__tag_8h.html)。

## 15.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00010"></a>
<a id="l00011"></a>
<a id="l00012"></a>
<a id="l00013"></a>
<a id="l00022"></a>
<a id="l00023"></a>
<a id="l00024"></a>
<a id="l00025"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="foldopen00032"></a>
<a id="l00032"></a>
<a id="l00034"></a>
<a id="l00035"></a>
<a id="l00037"></a>
<a id="l00038"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="foldopen00043"></a>
<a id="l00043"></a>
<a id="l00044"></a>
<a id="l00045"></a>
<a id="l00046"></a>
<a id="l00047"></a>
<a id="l00048"></a>
<a id="l00049"></a>
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
<a id="l00080"></a>
<a id="l00084"></a>
<a id="l00085"></a>
<a id="adsa__tag__proto_8h_html"></a>
<a id="astructdevice_html"></a>
<a id="astructdsa__tag__register_html"></a>
<a id="astructdsa__tag__register_html_a96f1ec63a5e0d1f11df75b3c1732fcad"></a>
<a id="astructnet__if_html"></a>
<a id="astructnet__pkt_html"></a>
<a id="astructnet__pkt_html_a7590eeacf06469206cb7e7949acfa7b2"></a>

```c
/*
 * SPDX-FileCopyrightText: Copyright 2025-2026 NXP
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_NET_DSA_TAG_H_
#define ZEPHYR_INCLUDE_NET_DSA_TAG_H_


#include <zephyr/dt-bindings/ethernet/dsa_tag_proto.h>

#ifdef __cplusplus
extern "C" {
#endif

struct dsa_tag_register {
        int proto;

        struct net_if *(*recv)(struct net_if *iface, struct net_pkt *pkt);

        struct net_pkt *(*xmit)(struct net_if *iface, struct net_pkt *pkt);
};

#define DSA_TAG_REGISTER(_proto, _recv, _xmit)                                                     \
        static const STRUCT_SECTION_ITERABLE(dsa_tag_register, __dsa_tag_register_##_proto) = {    \
                .proto = _proto,                                                                   \
                .recv = _recv,                                                                     \
                .xmit = _xmit,                                                                     \
        }


/*
 * DSA tag protocol handles packet received by untagging
 *
 * param iface: Interface of DSA conduit port on which receives the packet
 * param pkt: Network packet
 *
 * Returns: Interface of DSA user port to redirect
 */
struct net_if *dsa_tag_recv(struct net_if *iface, struct net_pkt *pkt);

/*
 * DSA tag protocol handles packet transmitted by tagging
 *
 * param iface: Interface of DSA user port to transmit
 * param pkt: Network packet
 *
 * Returns: Network packet tagged
 */
struct net_pkt *dsa_tag_xmit(struct net_if *iface, struct net_pkt *pkt);

/*
 * Set up DSA tag protocol
 *
 * param dev_cpu: Device of DSA CPU port
 */
void dsa_tag_setup(const struct device *dev_cpu);



#endif /* ZEPHYR_INCLUDE_NET_DSA_TAG_H_ */
```

## 15.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

SPDX 文件版权声明（FileCopyrightText）：Copyright 2025-2026 NXP。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 52 行

DSA 标签协议通过去标签（Untagging）处理收到的分组。

参数：`iface` 为接收分组的 DSA 通道端口（Conduit port）接口；`pkt` 为网络分组。

返回值：分组应重定向到的 DSA 用户端口（User port）接口。

### 注释 3：原第 62 行

DSA 标签协议通过加标签（Tagging）处理发送的分组。

参数：`iface` 为负责发送的 DSA 用户端口（User port）接口；`pkt` 为网络分组。

返回值：已加标签的网络分组。

### 注释 4：原第 72 行

设置 DSA 标签协议。

参数 `dev_cpu`：DSA CPU 端口设备。

### 注释 5：原第 85 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_NET_DSA_TAG_H_`。

## 15.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/dsa__tag_8h.html)
- [zephyr/dt-bindings/ethernet/dsa_tag_proto.h](https://docs.zephyrproject.org/latest/doxygen/html/dsa__tag__proto_8h.html)
- [dsa_tag_register](../network_service_model_reference/P005_dsa_tag_register_结构体.md)
- [proto](../network_service_model_reference/P005_dsa_tag_register_结构体.md#a96f1ec63a5e0d1f11df75b3c1732fcad)
- [net_if](../network_core_model_reference/P079_net_if_结构体.md)
- [net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)
- [iface](../network_core_model_reference/P114_net_pkt_结构体.md#a7590eeacf06469206cb7e7949acfa7b2)
- [device](../device_reference/P002_设备对象结构.md)
- [dsa_tag_proto.h](https://docs.zephyrproject.org/latest/doxygen/html/dsa__tag__proto_8h.html)
- [dsa_tag_register::proto](../network_service_model_reference/P005_dsa_tag_register_结构体.md#a96f1ec63a5e0d1f11df75b3c1732fcad)
- [net_pkt::iface](../network_core_model_reference/P114_net_pkt_结构体.md#a7590eeacf06469206cb7e7949acfa7b2)

---

[上一章](P014_battery.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P016_pcie.h_源码浏览.md)
