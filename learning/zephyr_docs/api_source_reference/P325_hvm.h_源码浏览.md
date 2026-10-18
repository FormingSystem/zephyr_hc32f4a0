---
id: learning.zephyr-docs.api-source-reference.page-325
title: hvm.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/hvm_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第325章\_hvm.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/hvm_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/hvm_8h.html)。

## 325.1\_原始可见代码（Source Code）

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
<a id="l00027"></a>
<a id="l00037"></a>
<a id="l00038"></a>
<a id="l00048"></a>
<a id="l00049"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="agroup__xen__hvm_html_gaa4c66d130a846c3effc5ec3052d95f82"></a>
<a id="agroup__xen__hvm_html_gae375499424094b2f6f8059160456b53e"></a>
<a id="akernel_8h_html"></a>
<a id="astdint_8h_html_a2095b9bffea4b2656950c6c0419edbf1"></a>

```c
/*
 * Copyright (c) 2021 EPAM Systems
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_XEN_HVM_H_
#define ZEPHYR_INCLUDE_XEN_HVM_H_

#include <xen/public/hvm/hvm_op.h>
#include <xen/public/hvm/params.h>

#include <zephyr/kernel.h>


int hvm_set_parameter(int idx, int domid, uint64_t value);

int hvm_get_parameter(int idx, int domid, uint64_t *value);


#endif /* ZEPHYR_INCLUDE_XEN_HVM_H_ */
```

## 325.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2021 EPAM Systems。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 52 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_XEN_HVM_H_`。

## 325.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/hvm_8h.html)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [hvm_set_parameter](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__hvm.html#gae375499424094b2f6f8059160456b53e)
- [uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)
- [hvm_get_parameter](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__hvm.html#gaa4c66d130a846c3effc5ec3052d95f82)
- [kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)

---

[上一章](P324_htu31d.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P326_hx711.h_源码浏览.md)
