---
id: learning.zephyr-docs.api-source-reference.page-247
title: ethernet_vlan.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/ethernet__vlan_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第247章\_ethernet\_vlan.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/ethernet__vlan_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/ethernet__vlan_8h.html)。

## 247.1\_原始可见代码（Source Code）

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
<a id="l00024"></a>
<a id="l00025"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="l00035"></a>
<a id="l00036"></a>
<a id="foldopen00044"></a>
<a id="l00044"></a>
<a id="l00045"></a>
<a id="l00046"></a>
<a id="l00047"></a>
<a id="l00048"></a>
<a id="foldopen00056"></a>
<a id="l00056"></a>
<a id="l00057"></a>
<a id="l00058"></a>
<a id="l00059"></a>
<a id="l00060"></a>
<a id="foldopen00068"></a>
<a id="l00068"></a>
<a id="l00069"></a>
<a id="l00070"></a>
<a id="l00071"></a>
<a id="l00072"></a>
<a id="foldopen00081"></a>
<a id="l00081"></a>
<a id="l00082"></a>
<a id="l00083"></a>
<a id="l00084"></a>
<a id="l00085"></a>
<a id="foldopen00094"></a>
<a id="l00094"></a>
<a id="l00095"></a>
<a id="l00096"></a>
<a id="l00097"></a>
<a id="l00098"></a>
<a id="foldopen00107"></a>
<a id="l00107"></a>
<a id="l00108"></a>
<a id="l00109"></a>
<a id="l00110"></a>
<a id="l00111"></a>
<a id="l00112"></a>
<a id="l00113"></a>
<a id="l00114"></a>
<a id="l00115"></a>
<a id="l00119"></a>
<a id="l00120"></a>
<a id="l00121"></a>
<a id="agroup__vlan__api_html_ga06b2977281f627ebb9529512aecc20dd"></a>
<a id="agroup__vlan__api_html_ga090648b166db1dc5ee9db71bfba1f97b"></a>
<a id="agroup__vlan__api_html_ga6fcea099258c6be9c7cbfbd92fd4e8ab"></a>
<a id="agroup__vlan__api_html_gad12123bb6c9920f21a6faed0e9bf70a6"></a>
<a id="agroup__vlan__api_html_gadee54f9a2af345dd3981f39d73e1bc10"></a>
<a id="agroup__vlan__api_html_gafc746a075a23e4ad2c1c76328a8d773a"></a>
<a id="ainclude_2zephyr_2types_8h_html"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>

```c


/*
 * Copyright (c) 2018 Intel Corporation
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_NET_ETHERNET_VLAN_H_
#define ZEPHYR_INCLUDE_NET_ETHERNET_VLAN_H_


#include <zephyr/types.h>

#ifdef __cplusplus
extern "C" {
#endif

#define NET_VLAN_TAG_UNSPEC 0x0fff

#define NET_VLAN_TAG_PRIORITY 0x0000

static inline uint16_t net_eth_vlan_get_vid(uint16_t tci)
{
        return tci & 0x0fff;
}

static inline uint8_t net_eth_vlan_get_dei(uint16_t tci)
{
        return (tci >> 12) & 0x01;
}

static inline uint8_t net_eth_vlan_get_pcp(uint16_t tci)
{
        return (tci >> 13) & 0x07;
}

static inline uint16_t net_eth_vlan_set_vid(uint16_t tci, uint16_t vid)
{
        return (tci & 0xf000) | (vid & 0x0fff);
}

static inline uint16_t net_eth_vlan_set_dei(uint16_t tci, bool dei)
{
        return (tci & 0xefff) | ((!!dei) << 12);
}

static inline uint16_t net_eth_vlan_set_pcp(uint16_t tci, uint8_t pcp)
{
        return (tci & 0x1fff) | ((pcp & 0x07) << 13);
}

#ifdef __cplusplus
}
#endif



#endif /* ZEPHYR_INCLUDE_NET_ETHERNET_VLAN_H_ */
```

## 247.2\_可见注释译文（Comments）

### 注释 1：原第 7 行

版权（Copyright）：© 2018 Intel Corporation。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 121 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_NET_ETHERNET_VLAN_H_`。

## 247.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/ethernet__vlan_8h.html)
- [zephyr/types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [net_eth_vlan_get_vid](https://docs.zephyrproject.org/latest/doxygen/html/group__vlan__api.html#gad12123bb6c9920f21a6faed0e9bf70a6)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [net_eth_vlan_get_dei](https://docs.zephyrproject.org/latest/doxygen/html/group__vlan__api.html#ga090648b166db1dc5ee9db71bfba1f97b)
- [net_eth_vlan_get_pcp](https://docs.zephyrproject.org/latest/doxygen/html/group__vlan__api.html#gafc746a075a23e4ad2c1c76328a8d773a)
- [net_eth_vlan_set_vid](https://docs.zephyrproject.org/latest/doxygen/html/group__vlan__api.html#ga06b2977281f627ebb9529512aecc20dd)
- [net_eth_vlan_set_dei](https://docs.zephyrproject.org/latest/doxygen/html/group__vlan__api.html#ga6fcea099258c6be9c7cbfbd92fd4e8ab)
- [net_eth_vlan_set_pcp](https://docs.zephyrproject.org/latest/doxygen/html/group__vlan__api.html#gadee54f9a2af345dd3981f39d73e1bc10)
- [types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)

---

[上一章](P246_ethernet_mgmt.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P248_ets.h_源码浏览.md)
