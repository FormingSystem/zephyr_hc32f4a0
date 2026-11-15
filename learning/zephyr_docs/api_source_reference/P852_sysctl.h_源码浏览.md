---
id: learning.zephyr-docs.api-source-reference.page-852
title: sysctl.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/sysctl_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第852章\_sysctl.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/sysctl_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/sysctl_8h.html)。

## 852.1\_原始可见代码（Source Code）

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
<a id="l00018"></a>
<a id="l00019"></a>
<a id="l00020"></a>
<a id="l00026"></a>
<a id="l00033"></a>
<a id="l00044"></a>
<a id="l00045"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="l00070"></a>
<a id="l00071"></a>
<a id="l00072"></a>
<a id="l00082"></a>
<a id="l00083"></a>
<a id="l00085"></a>
<a id="l00086"></a>
<a id="ageneric_8h_html"></a>
<a id="agroup__xen__dom0__domain__control_html_ga4848541359c3e13358dc39b42b3c142f"></a>
<a id="agroup__xen__dom0__sysctl_html_ga4241e03d02285724a6b47a9c5338ad8f"></a>
<a id="agroup__xen__dom0__sysctl_html_gaaf1c2e7bdef408008b3cee7fd380e2eb"></a>
<a id="agroup__xen__dom0__sysctl_html_gabae81727f21c359faa8325d094606fcc"></a>
<a id="agroup__xen__dom0__sysctl_html_gabf15e75ba751c107f3ba9e86b67820c7"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>

```c
/*
 * Copyright (c) 2025 EPAM Systems
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_XEN_DOM0_SYSCTL_H_
#define ZEPHYR_INCLUDE_XEN_DOM0_SYSCTL_H_

#include <xen/public/xen.h>
#include <xen/public/sysctl.h>

#include <zephyr/xen/generic.h>



int xen_sysctl_physinfo(struct xen_sysctl_physinfo *info);

int xen_sysctl_tbuf_op(struct xen_sysctl_tbuf_op *tbuf_op);

int xen_sysctl_getdomaininfo(struct xen_domctl_getdomaininfo *domaininfo,
                             uint16_t first, uint16_t num);

int xen_sysctl_cpu_hotplug(uint32_t cpu, bool enable);


#endif /* ZEPHYR_INCLUDE_XEN_DOM0_SYSCTL_H_ */
```

## 852.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2025 EPAM Systems。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 86 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_XEN_DOM0_SYSCTL_H_`。

## 852.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/sysctl_8h.html)
- [zephyr/xen/generic.h](https://docs.zephyrproject.org/latest/doxygen/html/generic_8h.html)
- [xen_sysctl_physinfo](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__dom0__sysctl.html#ga4241e03d02285724a6b47a9c5338ad8f)
- [xen_sysctl_tbuf_op](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__dom0__sysctl.html#gaaf1c2e7bdef408008b3cee7fd380e2eb)
- [xen_sysctl_getdomaininfo](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__dom0__sysctl.html#gabae81727f21c359faa8325d094606fcc)
- [xen_domctl_getdomaininfo](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__dom0__domain__control.html#ga4848541359c3e13358dc39b42b3c142f)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [xen_sysctl_cpu_hotplug](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__dom0__sysctl.html#gabf15e75ba751c107f3ba9e86b67820c7)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [generic.h](https://docs.zephyrproject.org/latest/doxygen/html/generic_8h.html)

---

[上一章](P851_dirent.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P853_system.h_源码浏览.md)
