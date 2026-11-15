---
id: learning.zephyr-docs.api-source-reference.page-860
title: tdk_apex.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/tdk__apex_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第860章\_tdk\_apex.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/tdk__apex_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/tdk__apex_8h.html)。

## 860.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00008"></a>
<a id="l00009"></a>
<a id="l00010"></a>
<a id="l00011"></a>
<a id="l00019"></a>
<a id="l00023"></a>
<a id="l00025"></a>
<a id="l00027"></a>
<a id="l00029"></a>
<a id="l00031"></a>
<a id="l00033"></a>
<a id="l00035"></a>
<a id="foldopen00052"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="l00057"></a>
<a id="agroup__sensor__interface_html_ggaaa1b502bc029b10d7b23b0a25ef4e934ac1f260296289d93a13c5686ca11bdc12"></a>
<a id="asensor_8h_html"></a>
<a id="atdk__apex_8h_html_a944436d98a2aea1f93977a2d0738d959"></a>
<a id="atdk__apex_8h_html_a944436d98a2aea1f93977a2d0738d959a5181bce02684391a151723bbd7f86af5"></a>

```c
/*
 * Copyright (c) 2024 TDK Invensense
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DRIVERS_SENSOR_TDK_APEX_H_
#define ZEPHYR_INCLUDE_DRIVERS_SENSOR_TDK_APEX_H_

#include <zephyr/drivers/sensor.h>


#define TDK_APEX_DISABLE   (0)
#define TDK_APEX_PEDOMETER (1)
#define TDK_APEX_TILT      (2)
#define TDK_APEX_SMD       (3)
#define TDK_APEX_WOM       (4)
#define TDK_APEX_TAP       (5)

enum sensor_channel_tdk_apex {

        SENSOR_CHAN_APEX_MOTION = SENSOR_CHAN_PRIV_START,
};
#endif /* ZEPHYR_INCLUDE_DRIVERS_SENSOR_TDK_APEX_H_ */
```

## 860.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2024 TDK Invensense。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 57 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_SENSOR_TDK_APEX_H_`。

## 860.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/tdk__apex_8h.html)
- [zephyr/drivers/sensor.h](https://docs.zephyrproject.org/latest/doxygen/html/sensor_8h.html)
- [sensor_channel_tdk_apex](https://docs.zephyrproject.org/latest/doxygen/html/tdk__apex_8h.html#a944436d98a2aea1f93977a2d0738d959)
- [SENSOR_CHAN_APEX_MOTION](https://docs.zephyrproject.org/latest/doxygen/html/tdk__apex_8h.html#a944436d98a2aea1f93977a2d0738d959a5181bce02684391a151723bbd7f86af5)
- [SENSOR_CHAN_PRIV_START](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934ac1f260296289d93a13c5686ca11bdc12)
- [sensor.h](https://docs.zephyrproject.org/latest/doxygen/html/sensor_8h.html)

---

[上一章](P859_tcs34725.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P861_test_toolchain.h_源码浏览.md)
