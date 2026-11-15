---
id: learning.zephyr-docs.api-source-configuration-reference.page-55
title: mctp_i3c_common.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/mctp__i3c__common_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第55章\_mctp\_i3c\_common.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/mctp__i3c__common_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/mctp__i3c__common_8h.html)。

## 55.1\_原始可见代码（Source Code）

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
<a id="l00018"></a>
<a id="l00019"></a>
<a id="l00020"></a>
<a id="l00021"></a>
<a id="l00022"></a>
<a id="l00023"></a>
<a id="l00024"></a>
<a id="l00026"></a>
<a id="l00027"></a>

```c
/*
 * Copyright (c) 2025 Intel Corporation
 *
 * SPDX-License-Identifier: Apache-2.0
 *
 */


#ifndef ZEPHYR_INCLUDE_PMCI_MCTP_MCTP_I3C_COMMON_H_
#define ZEPHYR_INCLUDE_PMCI_MCTP_MCTP_I3C_COMMON_H_


/* Max packet size */
#define MCTP_I3C_MAX_PKT_SIZE 255

/* DMTF mandatory byte with IBI signaling a pending Read */
#define MCTP_I3C_MDB_PENDING_READ 0xAE


#endif /* ZEPHYR_INCLUDE_PMCI_MCTP_MCTP_I3C_COMMON_H_ */
```

## 55.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2025 Intel Corporation。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 19 行

最大分组大小（Max packet size）。

### 注释 3：原第 22 行

DMTF 规定的必需字节，其中带内中断（IBI）指示有待读取的数据。

### 注释 4：原第 27 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_PMCI_MCTP_MCTP_I3C_COMMON_H_`。

## 55.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/mctp__i3c__common_8h.html)

---

[上一章](P054_mctp_i2c_gpio_common.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P056_microchip_sam_pmc.h_源码浏览.md)
