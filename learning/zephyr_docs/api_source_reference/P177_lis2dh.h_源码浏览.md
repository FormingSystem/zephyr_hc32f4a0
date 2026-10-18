---
id: learning.zephyr-docs.api-source-reference.page-177
title: lis2dh.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/drivers_2sensor_2lis2dh_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第177章\_lis2dh.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2sensor_2lis2dh_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2sensor_2lis2dh_8h.html)。

## 177.1\_原始可见代码（Source Code）

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
<a id="l00029"></a>
<a id="l00030"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="foldopen00037"></a>
<a id="l00037"></a>
<a id="l00046"></a>
<a id="l00047"></a>
<a id="l00048"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="agroup__lis2dh__interface_html_ga3a36ff9fb1f811eb0c1ac853f8c27ddb"></a>
<a id="agroup__lis2dh__interface_html_gaffedeefeb4d8ceda71760226eef1b5cd"></a>
<a id="agroup__lis2dh__interface_html_gga3a36ff9fb1f811eb0c1ac853f8c27ddbaa1db870964cb2d719449484cd26f0b26"></a>
<a id="agroup__lis2dh__interface_html_gga3a36ff9fb1f811eb0c1ac853f8c27ddbab79d3f8c64da49e84f2be95507a05e69"></a>
<a id="agroup__lis2dh__interface_html_gga3a36ff9fb1f811eb0c1ac853f8c27ddbabc46ce24eeb0bfdf8093de3806cf841e"></a>
<a id="agroup__lis2dh__interface_html_ggaffedeefeb4d8ceda71760226eef1b5cdaad1fac97ac7266eee389dff93cb9d8e6"></a>
<a id="agroup__sensor__interface_html_gga0dcb6842bc969492bd1c9eb49708940bafb4b5859bc369f817f60eaa161bcefc3"></a>
<a id="asensor_8h_html"></a>

```c
/*
 * Copyright The Zephyr Project Contributors
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DRIVERS_SENSOR_LIS2DH_H_
#define ZEPHYR_INCLUDE_DRIVERS_SENSOR_LIS2DH_H_


#include <zephyr/drivers/sensor.h>

enum lis2dh_self_test {
        LIS2DH_SELF_TEST_DISABLE = 0,
        LIS2DH_SELF_TEST_POSITIVE = 1,
        LIS2DH_SELF_TEST_NEGATIVE = 2,
};

enum sensor_attribute_lis2dh {
        SENSOR_ATTR_LIS2DH_SELF_TEST = SENSOR_ATTR_PRIV_START,
};


#endif /* ZEPHYR_INCLUDE_DRIVERS_SENSOR_LIS2DH_H_ */
```

## 177.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：The Zephyr Project Contributors。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 53 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_SENSOR_LIS2DH_H_`。

## 177.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2sensor_2lis2dh_8h.html)
- [zephyr/drivers/sensor.h](https://docs.zephyrproject.org/latest/doxygen/html/sensor_8h.html)
- [lis2dh_self_test](https://docs.zephyrproject.org/latest/doxygen/html/group__lis2dh__interface.html#ga3a36ff9fb1f811eb0c1ac853f8c27ddb)
- [LIS2DH_SELF_TEST_DISABLE](https://docs.zephyrproject.org/latest/doxygen/html/group__lis2dh__interface.html#gga3a36ff9fb1f811eb0c1ac853f8c27ddbab79d3f8c64da49e84f2be95507a05e69)
- [LIS2DH_SELF_TEST_POSITIVE](https://docs.zephyrproject.org/latest/doxygen/html/group__lis2dh__interface.html#gga3a36ff9fb1f811eb0c1ac853f8c27ddbabc46ce24eeb0bfdf8093de3806cf841e)
- [LIS2DH_SELF_TEST_NEGATIVE](https://docs.zephyrproject.org/latest/doxygen/html/group__lis2dh__interface.html#gga3a36ff9fb1f811eb0c1ac853f8c27ddbaa1db870964cb2d719449484cd26f0b26)
- [sensor_attribute_lis2dh](https://docs.zephyrproject.org/latest/doxygen/html/group__lis2dh__interface.html#gaffedeefeb4d8ceda71760226eef1b5cd)
- [SENSOR_ATTR_LIS2DH_SELF_TEST](https://docs.zephyrproject.org/latest/doxygen/html/group__lis2dh__interface.html#ggaffedeefeb4d8ceda71760226eef1b5cdaad1fac97ac7266eee389dff93cb9d8e6)
- [SENSOR_ATTR_PRIV_START](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gga0dcb6842bc969492bd1c9eb49708940bafb4b5859bc369f817f60eaa161bcefc3)
- [sensor.h](https://docs.zephyrproject.org/latest/doxygen/html/sensor_8h.html)

---

[上一章](P176_it8xxx2_vcmp.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P178_lsm6dsvxxx.h_源码浏览.md)
