---
id: learning.zephyr-docs.api-source-reference.page-838
title: stmod-plus-connector.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/stmod-plus-connector_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第838章\_stmod-plus-connector.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/stmod-plus-connector_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/stmod-plus-connector_8h.html)。

## 838.1\_原始可见代码（Source Code）

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
<a id="l00023"></a>
<a id="l00024"></a>
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
<a id="l00041"></a>
<a id="l00042"></a>

```c
/*
 * SPDX-FileCopyrightText: Copyright The Zephyr Project Contributors
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_GPIO_STMOD_PLUS_CONNECTOR_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_GPIO_STMOD_PLUS_CONNECTOR_H_


#define STMOD_PLUS_NSS_CTS  1
#define STMOD_PLUS_MOSI_TX  2
#define STMOD_PLUS_MISO_RX  3
#define STMOD_PLUS_SCK_RTS  4
#define STMOD_PLUS_SCL      7
#define STMOD_PLUS_MOSIS    8
#define STMOD_PLUS_MISOS    9
#define STMOD_PLUS_SDA      10
#define STMOD_PLUS_INT      11
#define STMOD_PLUS_RESET    12
#define STMOD_PLUS_ADC      13
#define STMOD_PLUS_PWM      14
#define STMOD_PLUS_GPIO17   17
#define STMOD_PLUS_GPIO18   18
#define STMOD_PLUS_GPIO19   19
#define STMOD_PLUS_GPIO20   20


#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_GPIO_STMOD_PLUS_CONNECTOR_H_ */
```

## 838.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

SPDX 文件版权声明（FileCopyrightText）：Copyright The Zephyr Project Contributors。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 42 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_GPIO_STMOD_PLUS_CONNECTOR_H_`。

## 838.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/stmod-plus-connector_8h.html)

---

[上一章](P837_stm32n6_iocell.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P839_storage_common.h_源码浏览.md)
