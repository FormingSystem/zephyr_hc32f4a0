---
id: learning.zephyr-docs.api-source-reference.page-678
title: ps_ids.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/ps__ids_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第678章\_ps\_ids.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/ps__ids_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/ps__ids_8h.html)。

## 678.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00008"></a>
<a id="l00016"></a>
<a id="l00018"></a>
<a id="l00019"></a>
<a id="l00020"></a>
<a id="l00022"></a>
<a id="l00023"></a>
<a id="l00024"></a>
<a id="l00025"></a>

```c
/*
 * Copyright (c) 2025 Analog Devices, Inc.
 *
 * SPDX-License-Identifier: Apache-2.0
 */
#ifndef ZEPHYR_INCLUDE_PSA_PS_IDS_H_
#define ZEPHYR_INCLUDE_PSA_PS_IDS_H_


#define ZEPHYR_PSA_SETTINGS_TFM_PS_UID_RANGE_BEGIN 0x2C000000
#define ZEPHYR_PSA_SETTINGS_TFM_PS_UID_RANGE_SIZE  0x10000

#define ZEPHYR_PSA_TLS_CREDENTIALS_PS_UID_RANGE_BEGIN 0xC2E0000000000000
#define ZEPHYR_PSA_TLS_CREDENTIALS_PS_UID_RANGE_SIZE  0x0001000000000000

#endif /* ZEPHYR_INCLUDE_PSA_PS_IDS_H_ */
```

## 678.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2025 Analog Devices, Inc.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 25 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_PSA_PS_IDS_H_`。

## 678.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/ps__ids_8h.html)

---

[上一章](P677_ps.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P679_ptm.h_源码浏览.md)
