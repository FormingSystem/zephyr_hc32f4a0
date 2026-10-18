---
id: learning.zephyr-docs.api-source-visible-fragment-reference.page-2
title: gpio_bl61x_wo.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/gpio__bl61x__wo_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第2章\_gpio\_bl61x\_wo.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/gpio__bl61x__wo_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/gpio__bl61x__wo_8h.html)。

## 2.1\_原始可见代码（Source Code）

> 译注：官方源码浏览页保留了部分缺少起始标记的注释尾段。下方代码保持原样；这些可见尾段也逐项翻译，不补写页面中已经省略的注释。

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
<a id="l00029"></a>
<a id="l00030"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="l00034"></a>
<a id="l00036"></a>
<a id="l00038"></a>
<a id="l00039"></a>
<a id="l00040"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="l00044"></a>
<a id="l00045"></a>
<a id="l00046"></a>
<a id="l00048"></a>
<a id="l00049"></a>
<a id="l00050"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="l00057"></a>
<a id="l00058"></a>
<a id="l00059"></a>
<a id="l00060"></a>
<a id="l00061"></a>
<a id="l00062"></a>
<a id="l00063"></a>
<a id="l00065"></a>
<a id="l00066"></a>
<a id="l00068"></a>
<a id="l00077"></a>
<a id="l00078"></a>
<a id="foldopen00110"></a>
<a id="l00110"></a>
<a id="l00111"></a>
<a id="l00112"></a>
<a id="l00113"></a>
<a id="l00114"></a>
<a id="l00115"></a>
<a id="l00116"></a>
<a id="l00117"></a>
<a id="l00118"></a>
<a id="l00119"></a>
<a id="l00127"></a>
<a id="l00128"></a>
<a id="l00136"></a>
<a id="l00137"></a>
<a id="l00148"></a>
<a id="l00149"></a>
<a id="l00150"></a>
<a id="l00160"></a>
<a id="l00161"></a>
<a id="l00162"></a>
<a id="l00171"></a>
<a id="l00172"></a>
<a id="l00183"></a>
<a id="l00184"></a>
<a id="l00185"></a>
<a id="l00189"></a>
<a id="l00190"></a>
<a id="l00191"></a>
<a id="l00192"></a>
<a id="l00193"></a>
<a id="l00194"></a>
<a id="adrivers_2gpio_8h_html"></a>
<a id="agroup__gpio__bl61x__wo__interface_html_ga257585afa07fddec00f680d7aef38cc7"></a>
<a id="agroup__gpio__bl61x__wo__interface_html_ga4644ddfda65420dbe21900d31da85828"></a>
<a id="agroup__gpio__bl61x__wo__interface_html_ga49ba177988201217332721e06af7308e"></a>
<a id="agroup__gpio__bl61x__wo__interface_html_gabab8d53092752f0fecd864bbcaa1bb56"></a>
<a id="agroup__gpio__bl61x__wo__interface_html_gac2c0c4a647d13039f7a90c56c804b5a0"></a>
<a id="agroup__gpio__bl61x__wo__interface_html_gac45b67106001a4cdb5c1c6703c764fcd"></a>
<a id="agroup__gpio__bl61x__wo__interface_html_gae3412749c6176638bc5a8fc417ba2aab"></a>
<a id="agroup__gpio__interface_html_ga5f5cb5e7dae6d58e072bb450af029d2e"></a>
<a id="agroup__sys-util_html_ga111fe4e9d63758262fc6810a782cb32a"></a>
<a id="alib_2libc_2minimal_2include_2time_8h_html_a99ef1cb2c789827dd5db3886dccf9067"></a>
<a id="aparser_8h_html_ab6b306ef981f5e21bb41ea2c2dbe8cd9"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astructbl61x__wo__config_html"></a>
<a id="astructbl61x__wo__config_html_a008fe193acd73529d2cdb1a681209ce3"></a>
<a id="astructbl61x__wo__config_html_a2fd1a2bdbb7603b86d39fcb885013630"></a>
<a id="astructbl61x__wo__config_html_a4aca055fbb5f0b5db088489297590b83"></a>
<a id="astructbl61x__wo__config_html_a58ee7556887d3b80ffe68312d69915f0"></a>
<a id="astructbl61x__wo__config_html_ac0c5d20792b3d3e1c6ff919980b5918f"></a>
<a id="astructbl61x__wo__config_html_adff7e30b46544eb722cd9380a2bc3367"></a>
<a id="astructgpio__dt__spec_html"></a>
<a id="autil__macro_8h_html"></a>

```c
/*
 * Copyright (c) 2026 MASSDRIVER EI (massdriver.space)
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DRIVERS_GPIO_GPIO_BL61X_WO_H_
#define ZEPHYR_INCLUDE_DRIVERS_GPIO_GPIO_BL61X_WO_H_

#ifdef __cplusplus
extern "C" {
#endif


#include <zephyr/drivers/gpio.h>
#include <zephyr/sys/util_macro.h>

#define BL61X_WO_PIN_CNT        16


BUILD_ASSERT(IS_ENABLED(CONFIG_GPIO_BL61X_808_WO),
             "BFLB Wire Out must be activated to use this header");

#define BL61X_WO_VALIDATE_TIME(_node)                                                           \
        BUILD_ASSERT((DT_PROP(_node, time_t0h) < DT_PROP(_node, time_total)),                   \
                     "BFLB WO device time-t0h must be smaller than time-total");                \
        BUILD_ASSERT((DT_PROP(_node, time_t1h) < DT_PROP(_node, time_total)),                   \
                     "BFLB WO device time-t1h must be smaller than time-total")
#define BL61X_WO_VALIDATE_FREQ(_node)                                                           \
        BUILD_ASSERT((DT_PROP(_node, time_t0h) < (Z_HZ_ns / DT_PROP(_node, frequency))),        \
                     "BFLB WO device time-t0h must be smaller than the frequency's period");    \
        BUILD_ASSERT((DT_PROP(_node, time_t1h) < (Z_HZ_ns / DT_PROP(_node, frequency))),        \
                     "BFLB WO device time-t1h must be smaller than the frequency's period")

#define BL61X_WO_VALIDATE(_node)                                                                \
        BUILD_ASSERT((DT_PROP_OR(_node, frequency, 0) | DT_PROP_OR(_node, time_total, 0)) != 0, \
                     "BFLB WO device must have frequency or time_total set");                   \
        BUILD_ASSERT(DT_NODE_HAS_PROP(_node, time_t0h),                                         \
                "BFLB WO device must have time-t0h, device binding is bad if this was allowed");\
        BUILD_ASSERT(DT_NODE_HAS_PROP(_node, time_t1h),                                         \
                "BFLB WO device must have time-t1h, device binding is bad if this was allowed");\
        IF_ENABLED(DT_NODE_HAS_PROP(_node, time_total), (BL61X_WO_VALIDATE_TIME(_node)));       \
        IF_ENABLED(DT_NODE_HAS_PROP(_node, frequency), (BL61X_WO_VALIDATE_FREQ(_node)))
#define BL61X_WO_VALIDATE_INST(_inst, _compat) BL61X_WO_VALIDATE(DT_INST(_inst, _compat))


typedef void (*bl61x_wo_callback_t) (void *user_data);

 */
struct bl61x_wo_config {
        uint16_t total_cycles;
        uint8_t set_cycles;
        uint8_t unset_cycles;
        bool set_invert;
        bool unset_invert;
        bool park_high;
};

uint16_t bl61x_wo_frequency_to_cycles(const uint32_t frequency, const bool exact);

uint16_t bl61x_wo_time_to_cycles(const uint32_t time, const bool exact);

int bl61x_wo_configure(const struct bl61x_wo_config *const config,
                       const uint8_t *pins, const gpio_flags_t *flags, const size_t pin_cnt);

int bl61x_wo_configure_dt(const struct bl61x_wo_config *const config,
                          const struct gpio_dt_spec *pins, const size_t pin_cnt);

int bl61x_wo_write(const uint16_t *const data, const size_t len);

int bl61x_wo_write_async(const uint16_t *const data, const size_t len,
                         bl61x_wo_callback_t cb, void *user_data);


#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_DRIVERS_GPIO_GPIO_BL61X_WO_H_ */
```

## 2.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权所有（Copyright）2026 MASSDRIVER EI（massdriver.space）。

SPDX-License-Identifier: Apache-2.0。

### 注释 2：原第 110 行

原页此处仅保留注释结束标记 `*/`，没有可译正文。

### 注释 3：原第 194 行

头文件包含保护（Include Guard）：`ZEPHYR_INCLUDE_DRIVERS_GPIO_GPIO_BL61X_WO_H_`。

## 2.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/gpio__bl61x__wo_8h.html)
- [zephyr/drivers/gpio.h](../gpio_driver_reference/P001_GPIO驱动头文件参考.md)
- [zephyr/sys/util_macro.h](../util_reference/P004_宏工具头文件参考.md)
- [IS_ENABLED](../util_reference/P001_通用工具公共接口.md#ga111fe4e9d63758262fc6810a782cb32a)
- [bl61x_wo_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__bl61x__wo__interface.html#gac45b67106001a4cdb5c1c6703c764fcd)
- [bl61x_wo_config](../hardware/P289_BL61x线输出配置.md)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [total_cycles](https://docs.zephyrproject.org/latest/doxygen/html/structbl61x__wo__config.html#a4aca055fbb5f0b5db088489297590b83)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [set_cycles](https://docs.zephyrproject.org/latest/doxygen/html/structbl61x__wo__config.html#ac0c5d20792b3d3e1c6ff919980b5918f)
- [unset_cycles](https://docs.zephyrproject.org/latest/doxygen/html/structbl61x__wo__config.html#a58ee7556887d3b80ffe68312d69915f0)
- [set_invert](https://docs.zephyrproject.org/latest/doxygen/html/structbl61x__wo__config.html#adff7e30b46544eb722cd9380a2bc3367)
- [unset_invert](https://docs.zephyrproject.org/latest/doxygen/html/structbl61x__wo__config.html#a2fd1a2bdbb7603b86d39fcb885013630)
- [park_high](https://docs.zephyrproject.org/latest/doxygen/html/structbl61x__wo__config.html#a008fe193acd73529d2cdb1a681209ce3)
- [bl61x_wo_frequency_to_cycles](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__bl61x__wo__interface.html#gac2c0c4a647d13039f7a90c56c804b5a0)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [bl61x_wo_time_to_cycles](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__bl61x__wo__interface.html#ga4644ddfda65420dbe21900d31da85828)
- [time](../api_file_reference/P187_____w__zephyr__zephyr__lib__libc__minimal__include__time.h_文件参考.md#a99ef1cb2c789827dd5db3886dccf9067)
- [bl61x_wo_configure](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__bl61x__wo__interface.html#gae3412749c6176638bc5a8fc417ba2aab)
- [gpio_flags_t](../hardware/P266_GPIO公共接口.md#ga5f5cb5e7dae6d58e072bb450af029d2e)
- [flags](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)
- [bl61x_wo_configure_dt](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__bl61x__wo__interface.html#gabab8d53092752f0fecd864bbcaa1bb56)
- [gpio_dt_spec](../hardware/P267_GPIO设备树描述.md)
- [bl61x_wo_write](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__bl61x__wo__interface.html#ga49ba177988201217332721e06af7308e)
- [bl61x_wo_write_async](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__bl61x__wo__interface.html#ga257585afa07fddec00f680d7aef38cc7)
- [gpio.h](../gpio_driver_reference/P001_GPIO驱动头文件参考.md)
- [bl61x_wo_config::park_high](https://docs.zephyrproject.org/latest/doxygen/html/structbl61x__wo__config.html#a008fe193acd73529d2cdb1a681209ce3)
- [bl61x_wo_config::unset_invert](https://docs.zephyrproject.org/latest/doxygen/html/structbl61x__wo__config.html#a2fd1a2bdbb7603b86d39fcb885013630)
- [bl61x_wo_config::total_cycles](https://docs.zephyrproject.org/latest/doxygen/html/structbl61x__wo__config.html#a4aca055fbb5f0b5db088489297590b83)
- [bl61x_wo_config::unset_cycles](https://docs.zephyrproject.org/latest/doxygen/html/structbl61x__wo__config.html#a58ee7556887d3b80ffe68312d69915f0)
- [bl61x_wo_config::set_cycles](https://docs.zephyrproject.org/latest/doxygen/html/structbl61x__wo__config.html#ac0c5d20792b3d3e1c6ff919980b5918f)
- [bl61x_wo_config::set_invert](https://docs.zephyrproject.org/latest/doxygen/html/structbl61x__wo__config.html#adff7e30b46544eb722cd9380a2bc3367)
- [util_macro.h](../util_reference/P004_宏工具头文件参考.md)

---

[上一章](P001_addr.h_源码浏览.md) · [返回大纲](大纲.md)
