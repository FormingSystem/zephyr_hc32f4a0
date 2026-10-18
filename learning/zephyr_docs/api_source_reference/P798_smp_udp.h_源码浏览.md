---
id: learning.zephyr-docs.api-source-reference.page-798
title: smp_udp.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/smp__udp_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第798章\_smp\_udp.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/smp__udp_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/smp__udp_8h.html)。

## 798.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00018"></a>
<a id="l00019"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="l00050"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="l00061"></a>
<a id="l00062"></a>
<a id="l00063"></a>
<a id="l00064"></a>
<a id="l00065"></a>
<a id="l00066"></a>
<a id="l00067"></a>
<a id="l00071"></a>
<a id="l00072"></a>
<a id="agroup__mcumgr__transport__udp_html_ga768f36cea02d7d7781113d36516e1763"></a>
<a id="agroup__mcumgr__transport__udp_html_gab11963f5889b4180b6a50e3e2cf46614"></a>
<a id="agroup__mcumgr__transport__udp_html_gadd428f3ed2ae0d9e580e45897a98a293"></a>
<a id="anet__ip_8h_html"></a>
<a id="asmp__client_8h_html"></a>
<a id="astructnet__sockaddr_html"></a>
<a id="astructsmp__client__object_html"></a>

```c
/*
 * Copyright (c) 2019, Prevas A/S
 * Copyright (c) 2023 Nordic Semiconductor ASA
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_MGMT_MCUMGR_TRANSPORT_SMP_UDP_H_
#define ZEPHYR_INCLUDE_MGMT_MCUMGR_TRANSPORT_SMP_UDP_H_

#include <zephyr/mgmt/mcumgr/smp/smp_client.h>
#include <zephyr/net/net_ip.h>


#ifdef __cplusplus
extern "C" {
#endif

int smp_udp_open(void);

int smp_udp_close(void);

#if defined(CONFIG_SMP_CLIENT) || defined(__DOXYGEN__)
int smp_client_udp_set_host_addr(struct smp_client_object *obj, struct net_sockaddr *addr);
#endif

#ifdef __cplusplus
}
#endif


#endif /* ZEPHYR_INCLUDE_MGMT_MCUMGR_TRANSPORT_SMP_UDP_H_ */
```

## 798.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2019, Prevas A/S。

版权（Copyright）：© 2023 Nordic Semiconductor ASA。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 72 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_MGMT_MCUMGR_TRANSPORT_SMP_UDP_H_`。

## 798.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/smp__udp_8h.html)
- [zephyr/mgmt/mcumgr/smp/smp_client.h](https://docs.zephyrproject.org/latest/doxygen/html/smp__client_8h.html)
- [zephyr/net/net_ip.h](https://docs.zephyrproject.org/latest/doxygen/html/net__ip_8h.html)
- [smp_udp_open](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__udp.html#ga768f36cea02d7d7781113d36516e1763)
- [smp_udp_close](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__udp.html#gadd428f3ed2ae0d9e580e45897a98a293)
- [smp_client_udp_set_host_addr](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__udp.html#gab11963f5889b4180b6a50e3e2cf46614)
- [smp_client_object](../system_service_model_reference/P078_smp_client_object_结构体.md)
- [net_sockaddr](../network_core_model_reference/P117_net_sockaddr_结构体.md)
- [net_ip.h](https://docs.zephyrproject.org/latest/doxygen/html/net__ip_8h.html)
- [smp_client.h](https://docs.zephyrproject.org/latest/doxygen/html/smp__client_8h.html)

---

[上一章](P797_smp_raw_dummy.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P799_snps-designware-gpio.h_源码浏览.md)
