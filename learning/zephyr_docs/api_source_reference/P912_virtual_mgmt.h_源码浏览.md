---
id: learning.zephyr-docs.api-source-reference.page-912
title: virtual_mgmt.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/virtual__mgmt_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第912章\_virtual\_mgmt.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/virtual__mgmt_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/virtual__mgmt_8h.html)。

## 912.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
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
<a id="l00030"></a>
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
<a id="l00084"></a>
<a id="l00085"></a>
<a id="l00086"></a>
<a id="l00087"></a>
<a id="l00088"></a>
<a id="l00089"></a>
<a id="l00090"></a>
<a id="l00091"></a>
<a id="l00092"></a>
<a id="l00093"></a>
<a id="l00094"></a>
<a id="l00095"></a>
<a id="l00096"></a>
<a id="l00097"></a>
<a id="l00098"></a>
<a id="l00099"></a>
<a id="l00100"></a>
<a id="l00101"></a>
<a id="l00102"></a>
<a id="l00103"></a>
<a id="l00104"></a>
<a id="l00105"></a>
<a id="l00106"></a>
<a id="l00107"></a>
<a id="l00108"></a>
<a id="l00109"></a>
<a id="l00110"></a>
<a id="l00111"></a>
<a id="l00112"></a>
<a id="l00113"></a>
<a id="l00114"></a>
<a id="l00115"></a>
<a id="l00116"></a>
<a id="l00117"></a>
<a id="l00118"></a>
<a id="l00119"></a>
<a id="l00120"></a>
<a id="l00122"></a>
<a id="l00126"></a>
<a id="l00127"></a>
<a id="l00128"></a>
<a id="l00129"></a>
<a id="l00130"></a>
<a id="l00131"></a>
<a id="agroup__ip__4__6_html_ga8b4cfadf1b284e52d6905ca88657b48a"></a>
<a id="agroup__net__mgmt_html_ga08bde8717fd8e12a338c517b22b87776"></a>
<a id="anet__mgmt_8h_html"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astructnet__if_html"></a>
<a id="avirtual_8h_html"></a>

```c
/*
 * Copyright (c) 2021 Intel Corporation.
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_NET_VIRTUAL_MGMT_H_
#define ZEPHYR_INCLUDE_NET_VIRTUAL_MGMT_H_

#include <zephyr/net/virtual.h>
#include <zephyr/net/net_mgmt.h>

#ifdef __cplusplus
extern "C" {
#endif



#define NET_VIRTUAL_INTERFACE_LAYER     NET_MGMT_LAYER_L2
#define NET_VIRTUAL_INTERFACE_CODE      NET_MGMT_LAYER_CODE_VIRTUAL
#define NET_VIRTUAL_INTERFACE_BASE                                      \
        (NET_MGMT_IFACE_BIT |                                           \
         NET_MGMT_LAYER(NET_VIRTUAL_INTERFACE_LAYER) |                  \
         NET_MGMT_LAYER_CODE(NET_VIRTUAL_INTERFACE_CODE))
#define NET_VIRTUAL_INTERFACE_EVENT                                     \
        (NET_VIRTUAL_INTERFACE_BASE | NET_MGMT_EVENT_BIT)

struct virtual_interface_req_params {
        net_sa_family_t family;
        union {
                struct net_in_addr peer4addr;
                struct net_in6_addr peer6addr;
                int mtu;
                struct virtual_interface_link_types link_types;
                struct {
                        size_t len;
                        uint8_t *data;
                } private_key;
                struct {
                        size_t len;
                        uint8_t data[NET_VIRTUAL_MAX_PUBLIC_KEY_LEN];
                } public_key;
        };
};

enum net_request_virtual_interface_cmd {
        NET_REQUEST_VIRTUAL_INTERFACE_CMD_SET_PEER_ADDR = 1,
        NET_REQUEST_VIRTUAL_INTERFACE_CMD_GET_PEER_ADDR,
        NET_REQUEST_VIRTUAL_INTERFACE_CMD_SET_MTU,
        NET_REQUEST_VIRTUAL_INTERFACE_CMD_GET_MTU,
        NET_REQUEST_VIRTUAL_INTERFACE_CMD_SET_LINK_TYPE,
        NET_REQUEST_VIRTUAL_INTERFACE_CMD_GET_LINK_TYPE,
        NET_REQUEST_VIRTUAL_INTERFACE_CMD_SET_PRIVATE_KEY,
        NET_REQUEST_VIRTUAL_INTERFACE_CMD_GET_PUBLIC_KEY,
};

#define NET_REQUEST_VIRTUAL_INTERFACE_SET_PEER_ADDRESS          \
        (NET_VIRTUAL_INTERFACE_BASE |                           \
         NET_REQUEST_VIRTUAL_INTERFACE_CMD_SET_PEER_ADDR)

NET_MGMT_DEFINE_REQUEST_HANDLER(NET_REQUEST_VIRTUAL_INTERFACE_SET_PEER_ADDRESS);

#define NET_REQUEST_VIRTUAL_INTERFACE_SET_MTU           \
        (NET_VIRTUAL_INTERFACE_BASE |                   \
         NET_REQUEST_VIRTUAL_INTERFACE_CMD_SET_MTU)

NET_MGMT_DEFINE_REQUEST_HANDLER(NET_REQUEST_VIRTUAL_INTERFACE_SET_MTU);

#define NET_REQUEST_VIRTUAL_INTERFACE_SET_LINK_TYPE     \
        (NET_VIRTUAL_INTERFACE_BASE |                   \
         NET_REQUEST_VIRTUAL_INTERFACE_CMD_SET_LINK_TYPE)

NET_MGMT_DEFINE_REQUEST_HANDLER(NET_REQUEST_VIRTUAL_INTERFACE_SET_LINK_TYPE);

#define NET_REQUEST_VIRTUAL_INTERFACE_GET_PEER_ADDRESS          \
        (NET_VIRTUAL_INTERFACE_BASE |                           \
         NET_REQUEST_VIRTUAL_INTERFACE_CMD_GET_PEER_ADDR)

NET_MGMT_DEFINE_REQUEST_HANDLER(NET_REQUEST_VIRTUAL_INTERFACE_GET_PEER_ADDRESS);

#define NET_REQUEST_VIRTUAL_INTERFACE_GET_MTU           \
        (NET_VIRTUAL_INTERFACE_BASE |                   \
         NET_REQUEST_VIRTUAL_INTERFACE_CMD_GET_MTU)

NET_MGMT_DEFINE_REQUEST_HANDLER(NET_REQUEST_VIRTUAL_INTERFACE_GET_MTU);

#define NET_REQUEST_VIRTUAL_INTERFACE_GET_LINK_TYPE     \
        (NET_VIRTUAL_INTERFACE_BASE |                   \
         NET_REQUEST_VIRTUAL_INTERFACE_CMD_GET_LINK_TYPE)

NET_MGMT_DEFINE_REQUEST_HANDLER(NET_REQUEST_VIRTUAL_INTERFACE_GET_LINK_TYPE);

#define NET_REQUEST_VIRTUAL_INTERFACE_SET_PRIVATE_KEY           \
        (NET_VIRTUAL_INTERFACE_BASE |                           \
         NET_REQUEST_VIRTUAL_INTERFACE_CMD_SET_PRIVATE_KEY)

NET_MGMT_DEFINE_REQUEST_HANDLER(NET_REQUEST_VIRTUAL_INTERFACE_SET_PRIVATE_KEY);

#define NET_REQUEST_VIRTUAL_INTERFACE_GET_PUBLIC_KEY            \
        (NET_VIRTUAL_INTERFACE_BASE |                           \
         NET_REQUEST_VIRTUAL_INTERFACE_CMD_GET_PUBLIC_KEY)

NET_MGMT_DEFINE_REQUEST_HANDLER(NET_REQUEST_VIRTUAL_INTERFACE_GET_PUBLIC_KEY);

struct net_if;



#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_NET_VIRTUAL_MGMT_H_ */
```

## 912.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2021 Intel Corporation.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 131 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_NET_VIRTUAL_MGMT_H_`。

## 912.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/virtual__mgmt_8h.html)
- [zephyr/net/virtual.h](https://docs.zephyrproject.org/latest/doxygen/html/virtual_8h.html)
- [zephyr/net/net_mgmt.h](https://docs.zephyrproject.org/latest/doxygen/html/net__mgmt_8h.html)
- [net_sa_family_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga8b4cfadf1b284e52d6905ca88657b48a)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [NET_MGMT_DEFINE_REQUEST_HANDLER](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#ga08bde8717fd8e12a338c517b22b87776)
- [net_if](../network_core_model_reference/P079_net_if_结构体.md)
- [net_mgmt.h](https://docs.zephyrproject.org/latest/doxygen/html/net__mgmt_8h.html)
- [virtual.h](https://docs.zephyrproject.org/latest/doxygen/html/virtual_8h.html)

---

[上一章](P911_virtiofs.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P913_vl53l0x.h_源码浏览.md)
