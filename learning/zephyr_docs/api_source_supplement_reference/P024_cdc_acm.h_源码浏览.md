---
id: learning.zephyr-docs.api-source-supplement-reference.page-24
title: cdc_acm.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/cdc__acm_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第24章\_cdc\_acm.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/cdc__acm_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/cdc__acm_8h.html)。

## 24.1\_原始可见代码（Source Code）

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
<a id="l00021"></a>
<a id="l00022"></a>
<a id="l00030"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="l00048"></a>
<a id="l00049"></a>
<a id="l00050"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="l00054"></a>
<a id="l00055"></a>
<a id="acdc__acm_8h_html_a0b2e4a171e5d56dba45c3d2e7cef72b4"></a>
<a id="acdc__acm_8h_html_a5b71bd70532ed059fb31a1ee3e73eaa5"></a>
<a id="adevice_8h_html"></a>
<a id="aerrno_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astructdevice_html"></a>

```c
/*
 * Copyright (c) 2020 Google LLC
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DRIVERS_UART_CDC_ACM_H_
#define ZEPHYR_INCLUDE_DRIVERS_UART_CDC_ACM_H_

#include <errno.h>

#include <zephyr/device.h>

#ifdef __cplusplus
extern "C" {
#endif /* __cplusplus */

typedef void (*cdc_dte_rate_callback_t)(const struct device *dev,
                                        uint32_t rate);

__deprecated int cdc_acm_dte_rate_callback_set(const struct device *dev,
                                  cdc_dte_rate_callback_t callback);

#ifdef __cplusplus
}
#endif /* __cplusplus */

#endif /* ZEPHYR_INCLUDE_DRIVERS_UART_CDC_ACM_H_ */
```

## 24.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2020 Google LLC。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 21 行

条件编译标记：`__cplusplus`。

### 注释 3：原第 53 行

条件编译标记：`__cplusplus`。

### 注释 4：原第 55 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_UART_CDC_ACM_H_`。

## 24.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/cdc__acm_8h.html)
- [errno.h](../error_reference/P004_错误号头文件参考.md)
- [zephyr/device.h](../device_reference/P007_设备模型头文件参考.md)
- [cdc_dte_rate_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/cdc__acm_8h.html#a0b2e4a171e5d56dba45c3d2e7cef72b4)
- [device](../device_reference/P002_设备对象结构.md)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [cdc_acm_dte_rate_callback_set](https://docs.zephyrproject.org/latest/doxygen/html/cdc__acm_8h.html#a5b71bd70532ed059fb31a1ee3e73eaa5)
- [device.h](../device_reference/P007_设备模型头文件参考.md)

---

[上一章](P023_ccc.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P025_cellular.h_源码浏览.md)
