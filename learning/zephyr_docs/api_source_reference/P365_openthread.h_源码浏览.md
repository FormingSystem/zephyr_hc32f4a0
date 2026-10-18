---
id: learning.zephyr-docs.api-source-reference.page-365
title: openthread.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2net_2openthread_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第365章\_openthread.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2net_2openthread_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2net_2openthread_8h.html)。

## 365.1\_原始可见代码（Source Code）

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
<a id="l00022"></a>
<a id="l00023"></a>
<a id="l00024"></a>
<a id="l00025"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="l00039"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="l00046"></a>
<a id="l00048"></a>
<a id="l00049"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="l00054"></a>
<a id="l00055"></a>
<a id="l00057"></a>
<a id="l00058"></a>
<a id="l00060"></a>
<a id="l00061"></a>
<a id="l00065"></a>
<a id="l00072"></a>
<a id="l00073"></a>
<a id="l00075"></a>
<a id="l00076"></a>
<a id="l00077"></a>
<a id="l00079"></a>
<a id="l00080"></a>
<a id="l00081"></a>
<a id="l00082"></a>
<a id="l00083"></a>
<a id="l00087"></a>
<a id="l00088"></a>
<a id="agroup__openthread_html_gad975528c91de66cd1054f3584bfcc957"></a>
<a id="ainclude_2zephyr_2net_2openthread_8h_html"></a>
<a id="akernel_2thread_8h_html"></a>
<a id="akernel_8h_html"></a>
<a id="anet__if_8h_html"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>

```c
/*
 * Copyright (c) 2017 Nordic Semiconductor ASA
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_NET_OPENTHREAD_H_
#define ZEPHYR_INCLUDE_NET_OPENTHREAD_H_


#include <zephyr/kernel.h>
#include <zephyr/net/net_if.h>
#include <zephyr/kernel/thread.h>

#include <openthread.h>

#ifdef __cplusplus
extern "C" {
#endif

struct pkt_list_elem {
        struct net_pkt *pkt;
};

struct openthread_context {
        struct net_if *iface;

        uint16_t pkt_list_in_idx;

        uint16_t pkt_list_out_idx;

        uint8_t pkt_list_full;

        struct pkt_list_elem pkt_list[CONFIG_OPENTHREAD_PKT_LIST_SIZE];
};

struct openthread_context *openthread_get_default_context(void);


#define OPENTHREAD_L2_CTX_TYPE struct openthread_context


#ifdef __cplusplus
}
#endif


#endif /* ZEPHYR_INCLUDE_NET_OPENTHREAD_H_ */
```

## 365.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2017 Nordic Semiconductor ASA。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 88 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_NET_OPENTHREAD_H_`。

## 365.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2net_2openthread_8h.html)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [zephyr/net/net_if.h](https://docs.zephyrproject.org/latest/doxygen/html/net__if_8h.html)
- [zephyr/kernel/thread.h](../thread_core_reference/P002_线程头文件参考.md)
- [openthread.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2net_2openthread_8h.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [openthread_get_default_context](https://docs.zephyrproject.org/latest/doxygen/html/group__openthread.html#gad975528c91de66cd1054f3584bfcc957)
- [thread.h](../thread_core_reference/P002_线程头文件参考.md)
- [kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [net_if.h](https://docs.zephyrproject.org/latest/doxygen/html/net__if_8h.html)

---

[上一章](P364_types.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P366_inet.h_源码浏览.md)
