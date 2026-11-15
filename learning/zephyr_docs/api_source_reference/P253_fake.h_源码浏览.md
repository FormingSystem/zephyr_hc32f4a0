---
id: learning.zephyr-docs.api-source-reference.page-253
title: fake.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/fake_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第253章\_fake.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/fake_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/fake_8h.html)。

## 253.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
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
<a id="l00039"></a>
<a id="l00041"></a>
<a id="l00043"></a>
<a id="l00045"></a>
<a id="l00046"></a>
<a id="l00048"></a>
<a id="l00049"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="l00054"></a>
<a id="l00055"></a>
<a id="l00057"></a>
<a id="l00059"></a>
<a id="l00060"></a>
<a id="l00062"></a>
<a id="l00063"></a>
<a id="l00065"></a>
<a id="l00066"></a>
<a id="l00068"></a>
<a id="l00069"></a>
<a id="l00071"></a>
<a id="l00072"></a>
<a id="l00074"></a>
<a id="l00075"></a>
<a id="l00077"></a>
<a id="l00078"></a>
<a id="l00080"></a>
<a id="l00081"></a>
<a id="l00082"></a>
<a id="l00084"></a>
<a id="l00085"></a>
<a id="l00087"></a>
<a id="l00088"></a>
<a id="l00089"></a>
<a id="l00093"></a>
<a id="l00094"></a>
<a id="l00095"></a>
<a id="l00096"></a>
<a id="l00097"></a>
<a id="l00098"></a>
<a id="agroup__regulator__fake_html_ga20e42c403dfbef4d77c6481c54b07a54"></a>
<a id="agroup__regulator__fake_html_ga3698eca47d504ade69bdf83c701790a3"></a>
<a id="agroup__regulator__fake_html_ga408d9f38ccfc124e37d493d7e28bc945"></a>
<a id="agroup__regulator__fake_html_ga440e1de9a526312b664ece361b69bb9c"></a>
<a id="agroup__regulator__fake_html_ga46fa15902ea00714aa55339a6dfb0118"></a>
<a id="agroup__regulator__fake_html_ga48dff2682962072c8cd94ac86438e187"></a>
<a id="agroup__regulator__fake_html_ga4cb6eb2be56aa8068ef2ae9535f10865"></a>
<a id="agroup__regulator__fake_html_gaaf5093c4e28539c4ae5d253c90d1c7bb"></a>
<a id="agroup__regulator__fake_html_gaafc47ff2195727115be0e4e98f040611"></a>
<a id="agroup__regulator__fake_html_gab4d6cbe6fec13d6adc544c7695974e30"></a>
<a id="agroup__regulator__fake_html_gac06d00e3355efcc21ec639af071791de"></a>
<a id="agroup__regulator__fake_html_gacdb5dd0dde7c62c46dfeecc25e364821"></a>
<a id="agroup__regulator__fake_html_gad87508f8ea72f48f347dc417c212a3aa"></a>
<a id="agroup__regulator__fake_html_gadf5c7522be1d9654c9cbed62354d14f0"></a>
<a id="agroup__regulator__fake_html_gae7b0b1f909b3bd6e82fdcd60436f2cb7"></a>
<a id="agroup__regulator__fake_html_gaf60c59ae80d397943b589e89414f1af4"></a>
<a id="agroup__regulator__fake_html_gaf76fea2e3aa81d36c102b2212e4f6f12"></a>
<a id="agroup__regulator__interface_html_ga1971bd21b504979a0cecab16048a0d03"></a>
<a id="agroup__regulator__interface_html_ga31dae130509d28ee41602ab16ab31a90"></a>
<a id="agroup__regulator__interface_html_ga9a15a21a532e497713724f42052b1dbd"></a>
<a id="aregulator_8h_html"></a>
<a id="astdint_8h_html_a0c18914b3041c2f583aba76f418399c2"></a>
<a id="astructdevice_html"></a>

```c
/*
 * Copyright (c) 2022 Nordic Semiconductor ASA
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DRIVERS_REGULATOR_FAKE_H_
#define ZEPHYR_INCLUDE_DRIVERS_REGULATOR_FAKE_H_

#include <zephyr/drivers/regulator.h>
#include <zephyr/fff.h>

#ifdef __cplusplus
extern "C" {
#endif


DECLARE_FAKE_VALUE_FUNC(int, regulator_fake_enable, const struct device *);
DECLARE_FAKE_VALUE_FUNC(int, regulator_fake_disable, const struct device *);
DECLARE_FAKE_VALUE_FUNC(unsigned int, regulator_fake_count_voltages,
                        const struct device *);
DECLARE_FAKE_VALUE_FUNC(int, regulator_fake_list_voltage, const struct device *,
                        unsigned int, int32_t *);
DECLARE_FAKE_VALUE_FUNC(int, regulator_fake_set_voltage, const struct device *,
                        int32_t, int32_t);
DECLARE_FAKE_VALUE_FUNC(int, regulator_fake_get_voltage, const struct device *,
                        int32_t *);
DECLARE_FAKE_VALUE_FUNC(unsigned int, regulator_fake_count_current_limits, const struct device *);
DECLARE_FAKE_VALUE_FUNC(int, regulator_fake_list_current_limit, const struct device *, unsigned int,
                        int32_t *);
DECLARE_FAKE_VALUE_FUNC(int, regulator_fake_set_current_limit,
                        const struct device *, int32_t, int32_t);
DECLARE_FAKE_VALUE_FUNC(int, regulator_fake_get_current_limit,
                        const struct device *, int32_t *);
DECLARE_FAKE_VALUE_FUNC(int, regulator_fake_set_mode, const struct device *,
                        regulator_mode_t);
DECLARE_FAKE_VALUE_FUNC(int, regulator_fake_get_mode, const struct device *,
                        regulator_mode_t *);
DECLARE_FAKE_VALUE_FUNC(int, regulator_fake_set_active_discharge, const struct device *,
                        bool);
DECLARE_FAKE_VALUE_FUNC(int, regulator_fake_get_active_discharge, const struct device *,
                        bool *);
DECLARE_FAKE_VALUE_FUNC(int, regulator_fake_get_error_flags,
                        const struct device *, regulator_error_flags_t *);

DECLARE_FAKE_VALUE_FUNC(int, regulator_parent_fake_dvs_state_set,
                        const struct device *, regulator_dvs_state_t);
DECLARE_FAKE_VALUE_FUNC(int, regulator_parent_fake_ship_mode,
                        const struct device *);


#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_DRIVERS_REGULATOR_FAKE_H_ */
```

## 253.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2022 Nordic Semiconductor ASA。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 98 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_REGULATOR_FAKE_H_`。

## 253.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/fake_8h.html)
- [zephyr/drivers/regulator.h](../power/P082_稳压器头文件.md)
- [regulator_fake_enable](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__fake.html#gae7b0b1f909b3bd6e82fdcd60436f2cb7)
- [device](../device_reference/P002_设备对象结构.md)
- [regulator_fake_disable](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__fake.html#gaf60c59ae80d397943b589e89414f1af4)
- [regulator_fake_count_voltages](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__fake.html#gaafc47ff2195727115be0e4e98f040611)
- [regulator_fake_list_voltage](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__fake.html#ga20e42c403dfbef4d77c6481c54b07a54)
- [int32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0c18914b3041c2f583aba76f418399c2)
- [regulator_fake_set_voltage](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__fake.html#gaaf5093c4e28539c4ae5d253c90d1c7bb)
- [regulator_fake_get_voltage](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__fake.html#gab4d6cbe6fec13d6adc544c7695974e30)
- [regulator_fake_count_current_limits](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__fake.html#gacdb5dd0dde7c62c46dfeecc25e364821)
- [regulator_fake_list_current_limit](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__fake.html#ga46fa15902ea00714aa55339a6dfb0118)
- [regulator_fake_set_current_limit](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__fake.html#gaf76fea2e3aa81d36c102b2212e4f6f12)
- [regulator_fake_get_current_limit](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__fake.html#gac06d00e3355efcc21ec639af071791de)
- [regulator_fake_set_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__fake.html#gadf5c7522be1d9654c9cbed62354d14f0)
- [regulator_mode_t](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__interface.html#ga1971bd21b504979a0cecab16048a0d03)
- [regulator_fake_get_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__fake.html#ga440e1de9a526312b664ece361b69bb9c)
- [regulator_fake_set_active_discharge](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__fake.html#ga48dff2682962072c8cd94ac86438e187)
- [regulator_fake_get_active_discharge](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__fake.html#gad87508f8ea72f48f347dc417c212a3aa)
- [regulator_fake_get_error_flags](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__fake.html#ga408d9f38ccfc124e37d493d7e28bc945)
- [regulator_error_flags_t](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__interface.html#ga31dae130509d28ee41602ab16ab31a90)
- [regulator_parent_fake_dvs_state_set](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__fake.html#ga3698eca47d504ade69bdf83c701790a3)
- [regulator_dvs_state_t](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__interface.html#ga9a15a21a532e497713724f42052b1dbd)
- [regulator_parent_fake_ship_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__fake.html#ga4cb6eb2be56aa8068ef2ae9535f10865)
- [regulator.h](../power/P082_稳压器头文件.md)

---

[上一章](P252_f75303.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P254_fake_comp.h_源码浏览.md)
