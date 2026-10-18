---
id: learning.zephyr-docs.api-source-reference.page-146
title: dplpmtud.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/dplpmtud_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第146章\_dplpmtud.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/dplpmtud_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/dplpmtud_8h.html)。

## 146.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
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
<a id="l00048"></a>
<a id="l00049"></a>
<a id="foldopen00051"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="l00054"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="l00057"></a>
<a id="foldopen00059"></a>
<a id="l00059"></a>
<a id="l00061"></a>
<a id="l00062"></a>
<a id="l00064"></a>
<a id="l00065"></a>
<a id="l00067"></a>
<a id="l00068"></a>
<a id="l00069"></a>
<a id="l00081"></a>
<a id="l00082"></a>
<a id="l00083"></a>
<a id="l00084"></a>
<a id="l00091"></a>
<a id="l00092"></a>
<a id="l00093"></a>
<a id="l00111"></a>
<a id="l00112"></a>
<a id="l00123"></a>
<a id="l00124"></a>
<a id="l00135"></a>
<a id="l00136"></a>
<a id="l00147"></a>
<a id="l00148"></a>
<a id="l00160"></a>
<a id="l00161"></a>
<a id="l00162"></a>
<a id="l00172"></a>
<a id="l00173"></a>
<a id="l00174"></a>
<a id="l00184"></a>
<a id="l00185"></a>
<a id="l00186"></a>
<a id="l00196"></a>
<a id="l00197"></a>
<a id="l00198"></a>
<a id="l00199"></a>
<a id="l00200"></a>
<a id="l00201"></a>
<a id="l00203"></a>
<a id="l00204"></a>
<a id="agroup__net__dplpmtud_html_ga4be5d1abe82e1bf2591d1804eacb401e"></a>
<a id="agroup__net__dplpmtud_html_ga5db1cdda7708b3186670a9c176fa1384"></a>
<a id="agroup__net__dplpmtud_html_ga7d1720efbd54fe04bdbfae5ffd53f4f1"></a>
<a id="agroup__net__dplpmtud_html_ga86037b3a53ee6fc5cb9c9d57a8e3a69c"></a>
<a id="agroup__net__dplpmtud_html_ga8ad5c097467be2001f385f1f403b4376"></a>
<a id="agroup__net__dplpmtud_html_ga8cb73dde5eff26e8fc6e8af967e7877f"></a>
<a id="agroup__net__dplpmtud_html_ga90b9864def9a47bb48783629ab5017fc"></a>
<a id="agroup__net__dplpmtud_html_ga9ac65913e3237c9b66c1c0ab5a4ced56"></a>
<a id="agroup__net__dplpmtud_html_gaa36c73f87f48f1ce43d1ab96aa7328e5"></a>
<a id="agroup__net__dplpmtud_html_gac5d971f112c15245febec53c6220ade9"></a>
<a id="agroup__net__dplpmtud_html_gaca014d4c339c7152805055bac4fc033a"></a>
<a id="agroup__net__dplpmtud_html_gga8ad5c097467be2001f385f1f403b4376a04e0fec02aef8095e5f0f42982d823e2"></a>
<a id="agroup__net__dplpmtud_html_gga8ad5c097467be2001f385f1f403b4376a8562af32b8a2e8575aa8ab5715a9dae7"></a>
<a id="agroup__net__dplpmtud_html_gga8ad5c097467be2001f385f1f403b4376a901a51fd4db48131cf11e62a4cc72b09"></a>
<a id="agroup__net__dplpmtud_html_gga8ad5c097467be2001f385f1f403b4376ab880e0ba1bdb2307566711cdcf95bab7"></a>
<a id="anet__ip_8h_html"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astructnet__dplpmtud__path_html"></a>
<a id="astructnet__dplpmtud__path_html_a54087b52e2fdb7a79c600fe746e8233c"></a>
<a id="astructnet__dplpmtud__path_html_a899fb7ac2822e8921a8b1232c5315dd0"></a>
<a id="astructnet__dplpmtud__path_html_a96f94f2f1ef88dfbe010fb1df74e101e"></a>
<a id="astructnet__sockaddr_html"></a>

```c
/*
 * SPDX-FileCopyrightText: Copyright The Zephyr Project Contributors
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_NET_DPLPMTUD_H_
#define ZEPHYR_INCLUDE_NET_DPLPMTUD_H_

#include <zephyr/net/net_ip.h>

#ifdef __cplusplus
extern "C" {
#endif

#define NET_DPLPMTUD_BASE_PLPMTU 1200U

enum net_dplpmtud_state {
        NET_DPLPMTUD_STATE_BASE = 0,
        NET_DPLPMTUD_STATE_SEARCHING,
        NET_DPLPMTUD_STATE_SEARCH_COMPLETE,
        NET_DPLPMTUD_STATE_ERROR,
};

struct net_dplpmtud_path {
        struct net_sockaddr_storage dst;

        uint16_t max_plpmtu;

        bool in_use;
};

int net_dplpmtud_init_path(struct net_dplpmtud_path *path,
                           const struct net_sockaddr *dst,
                           uint16_t max_plpmtu);

void net_dplpmtud_set_path_max_plpmtu(struct net_dplpmtud_path *path,
                                      uint16_t max_plpmtu);

void net_dplpmtud_reopen_path_search(struct net_dplpmtud_path *path);

int net_dplpmtud_get_path_mtu(struct net_dplpmtud_path *path);

int net_dplpmtud_get_path_probe_size(struct net_dplpmtud_path *path);

bool net_dplpmtud_path_probe_in_flight(struct net_dplpmtud_path *path);

int net_dplpmtud_on_path_probe_sent(struct net_dplpmtud_path *path,
                                    uint16_t probe_size);

int net_dplpmtud_on_path_probe_acked(struct net_dplpmtud_path *path,
                                     uint16_t probe_size);

int net_dplpmtud_on_path_probe_lost(struct net_dplpmtud_path *path,
                                    uint16_t probe_size);

void net_dplpmtud_note_path_blackhole(struct net_dplpmtud_path *path);

#ifdef __cplusplus
}
#endif


#endif /* ZEPHYR_INCLUDE_NET_DPLPMTUD_H_ */
```

## 146.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

SPDX 文件版权声明（FileCopyrightText）：Copyright The Zephyr Project Contributors。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 204 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_NET_DPLPMTUD_H_`。

## 146.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/dplpmtud_8h.html)
- [zephyr/net/net_ip.h](https://docs.zephyrproject.org/latest/doxygen/html/net__ip_8h.html)
- [net_dplpmtud_state](https://docs.zephyrproject.org/latest/doxygen/html/group__net__dplpmtud.html#ga8ad5c097467be2001f385f1f403b4376)
- [NET_DPLPMTUD_STATE_BASE](https://docs.zephyrproject.org/latest/doxygen/html/group__net__dplpmtud.html#gga8ad5c097467be2001f385f1f403b4376a8562af32b8a2e8575aa8ab5715a9dae7)
- [NET_DPLPMTUD_STATE_SEARCHING](https://docs.zephyrproject.org/latest/doxygen/html/group__net__dplpmtud.html#gga8ad5c097467be2001f385f1f403b4376a901a51fd4db48131cf11e62a4cc72b09)
- [NET_DPLPMTUD_STATE_SEARCH_COMPLETE](https://docs.zephyrproject.org/latest/doxygen/html/group__net__dplpmtud.html#gga8ad5c097467be2001f385f1f403b4376a04e0fec02aef8095e5f0f42982d823e2)
- [NET_DPLPMTUD_STATE_ERROR](https://docs.zephyrproject.org/latest/doxygen/html/group__net__dplpmtud.html#gga8ad5c097467be2001f385f1f403b4376ab880e0ba1bdb2307566711cdcf95bab7)
- [net_dplpmtud_path](../network_core_model_reference/P058_net_dplpmtud_path_结构体.md)
- [dst](../network_core_model_reference/P058_net_dplpmtud_path_结构体.md#a54087b52e2fdb7a79c600fe746e8233c)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [max_plpmtu](../network_core_model_reference/P058_net_dplpmtud_path_结构体.md#a96f94f2f1ef88dfbe010fb1df74e101e)
- [in_use](../network_core_model_reference/P058_net_dplpmtud_path_结构体.md#a899fb7ac2822e8921a8b1232c5315dd0)
- [net_dplpmtud_init_path](https://docs.zephyrproject.org/latest/doxygen/html/group__net__dplpmtud.html#ga90b9864def9a47bb48783629ab5017fc)
- [net_sockaddr](../network_core_model_reference/P117_net_sockaddr_结构体.md)
- [net_dplpmtud_set_path_max_plpmtu](https://docs.zephyrproject.org/latest/doxygen/html/group__net__dplpmtud.html#ga7d1720efbd54fe04bdbfae5ffd53f4f1)
- [net_dplpmtud_reopen_path_search](https://docs.zephyrproject.org/latest/doxygen/html/group__net__dplpmtud.html#gaca014d4c339c7152805055bac4fc033a)
- [net_dplpmtud_get_path_mtu](https://docs.zephyrproject.org/latest/doxygen/html/group__net__dplpmtud.html#gac5d971f112c15245febec53c6220ade9)
- [net_dplpmtud_get_path_probe_size](https://docs.zephyrproject.org/latest/doxygen/html/group__net__dplpmtud.html#gaa36c73f87f48f1ce43d1ab96aa7328e5)
- [net_dplpmtud_path_probe_in_flight](https://docs.zephyrproject.org/latest/doxygen/html/group__net__dplpmtud.html#ga86037b3a53ee6fc5cb9c9d57a8e3a69c)
- [net_dplpmtud_on_path_probe_sent](https://docs.zephyrproject.org/latest/doxygen/html/group__net__dplpmtud.html#ga5db1cdda7708b3186670a9c176fa1384)
- [net_dplpmtud_on_path_probe_acked](https://docs.zephyrproject.org/latest/doxygen/html/group__net__dplpmtud.html#ga4be5d1abe82e1bf2591d1804eacb401e)
- [net_dplpmtud_on_path_probe_lost](https://docs.zephyrproject.org/latest/doxygen/html/group__net__dplpmtud.html#ga8cb73dde5eff26e8fc6e8af967e7877f)
- [net_dplpmtud_note_path_blackhole](https://docs.zephyrproject.org/latest/doxygen/html/group__net__dplpmtud.html#ga9ac65913e3237c9b66c1c0ab5a4ced56)
- [net_ip.h](https://docs.zephyrproject.org/latest/doxygen/html/net__ip_8h.html)
- [net_dplpmtud_path::dst](../network_core_model_reference/P058_net_dplpmtud_path_结构体.md#a54087b52e2fdb7a79c600fe746e8233c)
- [net_dplpmtud_path::in_use](../network_core_model_reference/P058_net_dplpmtud_path_结构体.md#a899fb7ac2822e8921a8b1232c5315dd0)
- [net_dplpmtud_path::max_plpmtu](../network_core_model_reference/P058_net_dplpmtud_path_结构体.md#a96f94f2f1ef88dfbe010fb1df74e101e)

---

[上一章](P145_domctl.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P147_emul.h_源码浏览.md)
