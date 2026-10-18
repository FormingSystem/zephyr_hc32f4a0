---
id: learning.zephyr-docs.api-source-reference.page-801
title: sntp_server.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/sntp__server_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第801章\_sntp\_server.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/sntp__server_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/sntp__server_8h.html)。

## 801.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00011"></a>
<a id="l00012"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00018"></a>
<a id="l00019"></a>
<a id="l00020"></a>
<a id="l00029"></a>
<a id="l00043"></a>
<a id="l00044"></a>
<a id="l00048"></a>
<a id="l00049"></a>
<a id="l00050"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="agroup__sntp__server_html_ga36c5b4a695294c7ad6777fe79d08b798"></a>
<a id="astdint_8h_html"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_accbd6432732c88ad6adc5365800433b6"></a>

```c
/*
 * SPDX-FileCopyrightText: Copyright 2025 L. Felten <lothar.felten@gmail.com>
 * SPDX-FileCopyrightText: Copyright The Zephyr Project Contributors
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_NET_SNTP_SERVER_H_
#define ZEPHYR_INCLUDE_NET_SNTP_SERVER_H_

#include <stdint.h>

#ifdef __cplusplus
extern "C" {
#endif


void sntp_server_clock_source(const uint8_t ref_id[4], uint8_t stratum, int8_t precision);


#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_NET_SNTP_SERVER_H_ */
```

## 801.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

SPDX 文件版权声明（FileCopyrightText）：Copyright 2025 L. Felten <lothar.felten@gmail.com>。

SPDX 文件版权声明（FileCopyrightText）：Copyright The Zephyr Project Contributors。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 53 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_NET_SNTP_SERVER_H_`。

## 801.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/sntp__server_8h.html)
- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html)
- [sntp_server_clock_source](https://docs.zephyrproject.org/latest/doxygen/html/group__sntp__server.html#ga36c5b4a695294c7ad6777fe79d08b798)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [int8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#accbd6432732c88ad6adc5365800433b6)

---

[上一章](P800_sntp.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P802_socket_select.h_源码浏览.md)
