---
id: learning.zephyr-docs.api-source-reference.page-906
title: version.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/version_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第906章\_version.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/version_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/version_8h.html)。

## 906.1\_原始可见代码（Source Code）

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
<a id="l00026"></a>
<a id="l00035"></a>
<a id="l00036"></a>
<a id="l00049"></a>
<a id="l00050"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="ageneric_8h_html"></a>
<a id="agroup__xen__version__queries_html_ga1a790f668be1f721823419393a62201b"></a>
<a id="agroup__xen__version__queries_html_ga9ed44decd02728419b557c1db7d86635"></a>

```c
/*
 * Copyright (c) 2025 EPAM Systems
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_XEN_VERSION_H_
#define ZEPHYR_INCLUDE_XEN_VERSION_H_

#include <zephyr/xen/generic.h>
#include <xen/public/version.h>
#include <xen/public/xen.h>


int xen_version(void);

int xen_version_extraversion(char *extra, int len);


#endif /* ZEPHYR_INCLUDE_XEN_VERSION_H_ */
```

## 906.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2025 EPAM Systems。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 53 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_XEN_VERSION_H_`。

## 906.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/version_8h.html)
- [zephyr/xen/generic.h](https://docs.zephyrproject.org/latest/doxygen/html/generic_8h.html)
- [xen_version](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__version__queries.html#ga1a790f668be1f721823419393a62201b)
- [xen_version_extraversion](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__version__queries.html#ga9ed44decd02728419b557c1db7d86635)
- [generic.h](https://docs.zephyrproject.org/latest/doxygen/html/generic_8h.html)

---

[上一章](P905_veml6046.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P907_video-interfaces.h_源码浏览.md)
