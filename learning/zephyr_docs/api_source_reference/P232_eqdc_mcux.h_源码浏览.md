---
id: learning.zephyr-docs.api-source-reference.page-232
title: eqdc_mcux.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/eqdc__mcux_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第232章\_eqdc\_mcux.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/eqdc__mcux_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/eqdc__mcux_8h.html)。

## 232.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00011"></a>
<a id="l00012"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00021"></a>
<a id="l00022"></a>
<a id="l00023"></a>
<a id="l00024"></a>
<a id="l00025"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="foldopen00031"></a>
<a id="l00031"></a>
<a id="l00033"></a>
<a id="l00034"></a>
<a id="l00036"></a>
<a id="l00037"></a>
<a id="l00038"></a>
<a id="l00039"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="l00046"></a>
<a id="l00047"></a>
<a id="agroup__sensor__eqdc__mcux_html_gadcc2ad717337d60cb4fc30950b098481"></a>
<a id="agroup__sensor__eqdc__mcux_html_ggadcc2ad717337d60cb4fc30950b098481a38fef6ef89d7c82444be247744fa9a1d"></a>
<a id="agroup__sensor__eqdc__mcux_html_ggadcc2ad717337d60cb4fc30950b098481ac90210723198bb8db0b0d5000bb3ce95"></a>
<a id="agroup__sensor__interface_html_gga0dcb6842bc969492bd1c9eb49708940bafb4b5859bc369f817f60eaa161bcefc3"></a>
<a id="asensor_8h_html"></a>

```c
/*
 * SPDX-FileCopyrightText: 2026 NXP
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DRIVERS_SENSOR_EQDC_MCUX_H_
#define ZEPHYR_INCLUDE_DRIVERS_SENSOR_EQDC_MCUX_H_


#include <zephyr/drivers/sensor.h>

#ifdef __cplusplus
extern "C" {
#endif

enum sensor_attribute_eqdc_mcux {
        SENSOR_ATTR_EQDC_COUNTS_PER_REVOLUTION = SENSOR_ATTR_PRIV_START,

        SENSOR_ATTR_EQDC_PRESCALED_FREQUENCY,
};

#ifdef __cplusplus
}
#endif


#endif /* ZEPHYR_INCLUDE_DRIVERS_SENSOR_EQDC_MCUX_H_ */
```

## 232.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

SPDX 文件版权声明（FileCopyrightText）：2026 NXP。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 47 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_SENSOR_EQDC_MCUX_H_`。

## 232.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/eqdc__mcux_8h.html)
- [zephyr/drivers/sensor.h](https://docs.zephyrproject.org/latest/doxygen/html/sensor_8h.html)
- [sensor_attribute_eqdc_mcux](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__eqdc__mcux.html#gadcc2ad717337d60cb4fc30950b098481)
- [SENSOR_ATTR_EQDC_COUNTS_PER_REVOLUTION](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__eqdc__mcux.html#ggadcc2ad717337d60cb4fc30950b098481ac90210723198bb8db0b0d5000bb3ce95)
- [SENSOR_ATTR_PRIV_START](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gga0dcb6842bc969492bd1c9eb49708940bafb4b5859bc369f817f60eaa161bcefc3)
- [SENSOR_ATTR_EQDC_PRESCALED_FREQUENCY](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__eqdc__mcux.html#ggadcc2ad717337d60cb4fc30950b098481a38fef6ef89d7c82444be247744fa9a1d)
- [sensor.h](https://docs.zephyrproject.org/latest/doxygen/html/sensor_8h.html)

---

[上一章](P231_enum_mgmt_callbacks.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P233_error_types.h_源码浏览.md)
