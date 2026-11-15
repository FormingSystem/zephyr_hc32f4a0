---
id: learning.zephyr-docs.api-source-reference.page-699
title: regions.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/regions_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第699章\_regions.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/regions_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/regions_8h.html)。

## 699.1\_原始可见代码（Source Code）

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
<a id="l00025"></a>
<a id="l00036"></a>
<a id="l00037"></a>
<a id="l00047"></a>
<a id="l00048"></a>
<a id="l00060"></a>
<a id="l00061"></a>
<a id="l00073"></a>
<a id="l00074"></a>
<a id="l00086"></a>
<a id="l00087"></a>
<a id="l00089"></a>
<a id="l00090"></a>
<a id="agroup__xen__regions_html_ga4853ade09ca37b66ad484ad1cbab6cf3"></a>
<a id="agroup__xen__regions_html_ga65b8fda79f7b6e4db26cccc818c69c79"></a>
<a id="agroup__xen__regions_html_gaa82b399b305dc279da8fb8206da77d3b"></a>
<a id="agroup__xen__regions_html_gabe293a88ca167b9a52709c7e94af73b3"></a>
<a id="agroup__xen__regions_html_gaf576c75a5b01b1a8b6f2be3b48a25886"></a>
<a id="astdbool_8h_html"></a>

```c
/*
 * Copyright (c) 2026 EPAM Systems
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_XEN_REGIONS_H_
#define ZEPHYR_INCLUDE_XEN_REGIONS_H_

#include <stdbool.h>
#include <stddef.h>


bool xen_region_is_addr_extreg(void *ptr);

void *xen_region_get_pages(size_t nr_pages);

int xen_region_put_pages(void *ptr, size_t nr_pages);

int xen_region_map(void *ptr, size_t nr_pages);

int xen_region_unmap(void *ptr, size_t nr_pages);


#endif /* ZEPHYR_INCLUDE_XEN_REGIONS_H_ */
```

## 699.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2026 EPAM Systems。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 90 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_XEN_REGIONS_H_`。

## 699.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/regions_8h.html)
- [stdbool.h](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html)
- [xen_region_is_addr_extreg](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__regions.html#gabe293a88ca167b9a52709c7e94af73b3)
- [xen_region_get_pages](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__regions.html#ga4853ade09ca37b66ad484ad1cbab6cf3)
- [xen_region_put_pages](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__regions.html#gaa82b399b305dc279da8fb8206da77d3b)
- [xen_region_map](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__regions.html#ga65b8fda79f7b6e4db26cccc818c69c79)
- [xen_region_unmap](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__regions.html#gaf576c75a5b01b1a8b6f2be3b48a25886)

---

[上一章](P698_realtek-rts5817-gpio.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P700_regset_target_lib.h_源码浏览.md)
