---
id: learning.zephyr-docs.api-source-reference.page-932
title: sched.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/xen_2sched_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第932章\_sched.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/xen_2sched_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/xen_2sched_8h.html)。

## 932.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00012"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00023"></a>
<a id="l00024"></a>
<a id="l00030"></a>
<a id="l00031"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="l00048"></a>
<a id="l00049"></a>
<a id="l00057"></a>
<a id="l00058"></a>
<a id="l00065"></a>
<a id="l00066"></a>
<a id="l00073"></a>
<a id="l00074"></a>
<a id="l00089"></a>
<a id="l00090"></a>
<a id="l00091"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a0c18914b3041c2f583aba76f418399c2"></a>
<a id="astdint_8h_html_a2095b9bffea4b2656950c6c0419edbf1"></a>
<a id="axen_2sched_8h_html_a0222b5101cec4a985cec20219fdab238"></a>
<a id="axen_2sched_8h_html_a3450b645f99cb336c24ef2835911f1fd"></a>
<a id="axen_2sched_8h_html_a354226bfab2b158b1b7a597ad8336432"></a>
<a id="axen_2sched_8h_html_a7d2814d9797a0f1f65819fd774a87bad"></a>
<a id="axen_2sched_8h_html_ad487cde3d2523420a468bbdbd074382a"></a>
<a id="axen_2sched_8h_html_ae35f7ea4d4b340ea35fdb10bbea977f0"></a>
<a id="axen_2sched_8h_html_afb585cc82ac5851d5ad82de7a15d81f0"></a>
<a id="axen_2sched_8h_html_afe72a62c01c49764514ad62400f19d36"></a>

```c
/*
 * SPDX-FileCopyrightText: Copyright (c) 2026 EPAM Systems
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_XEN_SCHED_H_
#define ZEPHYR_INCLUDE_XEN_SCHED_H_

#include <xen/public/sched.h>

int xen_sched_yield(void);

int xen_sched_block(void);

int xen_sched_poll(evtchn_port_t *ports, unsigned int nr_ports, uint64_t timeout);

int xen_sched_shutdown(unsigned int reason);

int xen_sched_remote_shutdown(domid_t domid, unsigned int reason);

int xen_sched_shutdown_code(unsigned int reason);

int xen_sched_pin_override(int32_t pcpu);

int xen_sched_watchdog(uint32_t *id, uint32_t timeout);

#endif /* ZEPHYR_INCLUDE_XEN_SCHED_H_ */
```

## 932.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

SPDX 文件版权声明（FileCopyrightText）：Copyright (c) 2026 EPAM Systems。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 91 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_XEN_SCHED_H_`。

## 932.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/xen_2sched_8h.html)
- [xen_sched_yield](https://docs.zephyrproject.org/latest/doxygen/html/xen_2sched_8h.html#ae35f7ea4d4b340ea35fdb10bbea977f0)
- [xen_sched_block](https://docs.zephyrproject.org/latest/doxygen/html/xen_2sched_8h.html#afb585cc82ac5851d5ad82de7a15d81f0)
- [xen_sched_poll](https://docs.zephyrproject.org/latest/doxygen/html/xen_2sched_8h.html#a7d2814d9797a0f1f65819fd774a87bad)
- [uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)
- [xen_sched_shutdown](https://docs.zephyrproject.org/latest/doxygen/html/xen_2sched_8h.html#a3450b645f99cb336c24ef2835911f1fd)
- [xen_sched_remote_shutdown](https://docs.zephyrproject.org/latest/doxygen/html/xen_2sched_8h.html#a0222b5101cec4a985cec20219fdab238)
- [xen_sched_shutdown_code](https://docs.zephyrproject.org/latest/doxygen/html/xen_2sched_8h.html#afe72a62c01c49764514ad62400f19d36)
- [xen_sched_pin_override](https://docs.zephyrproject.org/latest/doxygen/html/xen_2sched_8h.html#ad487cde3d2523420a468bbdbd074382a)
- [int32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0c18914b3041c2f583aba76f418399c2)
- [xen_sched_watchdog](https://docs.zephyrproject.org/latest/doxygen/html/xen_2sched_8h.html#a354226bfab2b158b1b7a597ad8336432)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)

---

[上一章](P931_xbr818.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P933_xg21-dma.h_源码浏览.md)
