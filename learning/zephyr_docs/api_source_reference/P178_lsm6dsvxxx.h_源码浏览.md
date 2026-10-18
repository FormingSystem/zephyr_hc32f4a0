---
id: learning.zephyr-docs.api-source-reference.page-178
title: lsm6dsvxxx.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/drivers_2sensor_2lsm6dsvxxx_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第178章\_lsm6dsvxxx.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2sensor_2lsm6dsvxxx_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2sensor_2lsm6dsvxxx_8h.html)。

## 178.1\_原始可见代码（Source Code）

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
<a id="foldopen00028"></a>
<a id="l00028"></a>
<a id="l00034"></a>
<a id="l00035"></a>
<a id="l00036"></a>
<a id="foldopen00038"></a>
<a id="l00038"></a>
<a id="l00039"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="l00046"></a>
<a id="l00047"></a>
<a id="agroup__lsm6dsvxxx__interface_html_ga0e2d73310764e4ad782f20f9e2b2da46"></a>
<a id="agroup__lsm6dsvxxx__interface_html_gaa40abf78652db54d4b43b41c7750b558"></a>
<a id="agroup__lsm6dsvxxx__interface_html_gga0e2d73310764e4ad782f20f9e2b2da46a01c6e9bb517b46bd18e2d69b1eb02349"></a>
<a id="agroup__lsm6dsvxxx__interface_html_gga0e2d73310764e4ad782f20f9e2b2da46a18d5155644c60de23dde8bf2ca3f5a36"></a>
<a id="agroup__lsm6dsvxxx__interface_html_ggaa40abf78652db54d4b43b41c7750b558a3b1d8afe96e306670568008d1f8b5a5d"></a>
<a id="agroup__sensor__interface_html_gga0dcb6842bc969492bd1c9eb49708940bafb4b5859bc369f817f60eaa161bcefc3"></a>
<a id="asensor_8h_html"></a>

```c
/*
 * Copyright The Zephyr Project Contributors
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DRIVERS_SENSOR_LSM6DSVXXX_H_
#define ZEPHYR_INCLUDE_DRIVERS_SENSOR_LSM6DSVXXX_H_


#include <zephyr/drivers/sensor.h>

enum sensor_attribute_lsm6dsvxxx {
        SENSOR_ATTR_GET_SELF_TEST_RESULT = SENSOR_ATTR_PRIV_START,
};

enum lsm6dsvxxx_self_test_result {
        LSM6DSVXXX_ST_OK = 0,
        LSM6DSVXXX_ST_FAIL = 1,
};


#endif /* ZEPHYR_INCLUDE_DRIVERS_SENSOR_LSM6DSVXXX_H_ */
```

## 178.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：The Zephyr Project Contributors。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 47 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_SENSOR_LSM6DSVXXX_H_`。

## 178.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2sensor_2lsm6dsvxxx_8h.html)
- [zephyr/drivers/sensor.h](https://docs.zephyrproject.org/latest/doxygen/html/sensor_8h.html)
- [sensor_attribute_lsm6dsvxxx](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#gaa40abf78652db54d4b43b41c7750b558)
- [SENSOR_ATTR_GET_SELF_TEST_RESULT](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#ggaa40abf78652db54d4b43b41c7750b558a3b1d8afe96e306670568008d1f8b5a5d)
- [SENSOR_ATTR_PRIV_START](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gga0dcb6842bc969492bd1c9eb49708940bafb4b5859bc369f817f60eaa161bcefc3)
- [lsm6dsvxxx_self_test_result](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#ga0e2d73310764e4ad782f20f9e2b2da46)
- [LSM6DSVXXX_ST_OK](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#gga0e2d73310764e4ad782f20f9e2b2da46a01c6e9bb517b46bd18e2d69b1eb02349)
- [LSM6DSVXXX_ST_FAIL](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#gga0e2d73310764e4ad782f20f9e2b2da46a18d5155644c60de23dde8bf2ca3f5a36)
- [sensor.h](https://docs.zephyrproject.org/latest/doxygen/html/sensor_8h.html)

---

[上一章](P177_lis2dh.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P179_max30009.h_源码浏览.md)
