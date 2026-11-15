---
id: learning.zephyr-docs.api-source-reference.page-413
title: ism330dhcx.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/ism330dhcx_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第413章\_ism330dhcx.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/ism330dhcx_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/ism330dhcx_8h.html)。

## 413.1\_原始可见代码（Source Code）

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
<a id="l00022"></a>
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
<a id="l00042"></a>
<a id="l00044"></a>
<a id="l00045"></a>

```c
/*
 * Copyright (c) 2023 STMicroelectronics
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_SENSOR_ISM330DHCX_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_SENSOR_ISM330DHCX_H_


#define ISM330DHCX_DT_ODR_OFF                   0x0
#define ISM330DHCX_DT_ODR_12Hz5                 0x1
#define ISM330DHCX_DT_ODR_26H                   0x2
#define ISM330DHCX_DT_ODR_52Hz                  0x3
#define ISM330DHCX_DT_ODR_104Hz                 0x4
#define ISM330DHCX_DT_ODR_208Hz                 0x5
#define ISM330DHCX_DT_ODR_416Hz                 0x6
#define ISM330DHCX_DT_ODR_833Hz                 0x7
#define ISM330DHCX_DT_ODR_1666Hz                0x8
#define ISM330DHCX_DT_ODR_3332Hz                0x9
#define ISM330DHCX_DT_ODR_6667Hz                0xa
#define ISM330DHCX_DT_ODR_1Hz6                  0xb


#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_SENSOR_ISM330DHCX_H_ */
```

## 413.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2023 STMicroelectronics。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 45 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_SENSOR_ISM330DHCX_H_`。

## 413.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/ism330dhcx_8h.html)

---

[上一章](P412_is31fl3733.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P414_ism6hg256x.h_源码浏览.md)
