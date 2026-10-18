---
id: learning.zephyr-docs.api-source-reference.page-680
title: ptp.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/ptp_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第680章\_ptp.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/ptp_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/ptp_8h.html)。

## 680.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00025"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="l00034"></a>
<a id="l00035"></a>
<a id="l00036"></a>
<a id="l00037"></a>
<a id="l00038"></a>
<a id="l00039"></a>
<a id="l00040"></a>
<a id="l00044"></a>
<a id="l00045"></a>
<a id="aptp__time_8h_html"></a>

```c
/*
 * Copyright (c) 2024 BayLibre SAS
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_NET_PTP_H_
#define ZEPHYR_INCLUDE_NET_PTP_H_


#include <zephyr/net/ptp_time.h>

#ifdef __cplusplus
extern "C" {
#endif

#define PTP_MAJOR_VERSION 2
#define PTP_MINOR_VERSION 1

#define PTP_VERSION (PTP_MINOR_VERSION << 4 | PTP_MAJOR_VERSION)

#ifdef __cplusplus
}
#endif


#endif /* ZEPHYR_INCLUDE_NET_PTP_H_ */
```

## 680.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2024 BayLibre SAS。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 45 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_NET_PTP_H_`。

## 680.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/ptp_8h.html)
- [zephyr/net/ptp_time.h](https://docs.zephyrproject.org/latest/doxygen/html/ptp__time_8h.html)
- [ptp_time.h](https://docs.zephyrproject.org/latest/doxygen/html/ptp__time_8h.html)

---

[上一章](P679_ptm.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P681_ptp_time.h_源码浏览.md)
