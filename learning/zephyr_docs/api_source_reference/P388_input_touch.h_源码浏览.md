---
id: learning.zephyr-docs.api-source-reference.page-388
title: input_touch.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/input__touch_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第388章\_input\_touch.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/input__touch_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/input__touch_8h.html)。

## 388.1\_原始可见代码（Source Code）

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
<a id="l00023"></a>
<a id="l00024"></a>
<a id="l00025"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="l00029"></a>
<a id="foldopen00037"></a>
<a id="l00037"></a>
<a id="l00039"></a>
<a id="l00041"></a>
<a id="l00043"></a>
<a id="l00045"></a>
<a id="l00047"></a>
<a id="l00049"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="foldopen00065"></a>
<a id="l00065"></a>
<a id="l00066"></a>
<a id="l00067"></a>
<a id="l00068"></a>
<a id="l00069"></a>
<a id="foldopen00075"></a>
<a id="l00075"></a>
<a id="l00076"></a>
<a id="l00077"></a>
<a id="l00078"></a>
<a id="l00079"></a>
<a id="l00080"></a>
<a id="l00081"></a>
<a id="l00082"></a>
<a id="l00083"></a>
<a id="l00084"></a>
<a id="l00085"></a>
<a id="foldopen00091"></a>
<a id="l00091"></a>
<a id="l00092"></a>
<a id="l00093"></a>
<a id="foldopen00099"></a>
<a id="l00099"></a>
<a id="l00100"></a>
<a id="l00101"></a>
<a id="l00102"></a>
<a id="l00111"></a>
<a id="l00112"></a>
<a id="l00113"></a>
<a id="l00114"></a>
<a id="l00115"></a>
<a id="l00116"></a>
<a id="l00117"></a>
<a id="l00118"></a>
<a id="l00120"></a>
<a id="l00121"></a>
<a id="agroup__touch__events_html_ga646bb86aa9f942fc3065381bd19e545c"></a>
<a id="ainput_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astructdevice_html"></a>
<a id="astructinput__touchscreen__common__config_html"></a>
<a id="astructinput__touchscreen__common__config_html_a147cc66f165b5bf9e42b591ad77824c5"></a>
<a id="astructinput__touchscreen__common__config_html_a35b6d8ccd36aa95d46cc24be2f94144b"></a>
<a id="astructinput__touchscreen__common__config_html_a408e21f2a9e57267d87d24f8a054f999"></a>
<a id="astructinput__touchscreen__common__config_html_abba0c9353f867287b047635ea358e057"></a>
<a id="astructinput__touchscreen__common__config_html_ac7e996d150c9fef15ec733f4515bbf48"></a>
<a id="astructinput__touchscreen__common__config_html_ad93cf875b2f1db32a8d4790296ccc6a3"></a>
<a id="astructinput__touchscreen__common__config_html_ae534425e6069853cb80a3925fce8e2ad"></a>
<a id="astructk__timeout__t_html"></a>

```c
/*
 * Copyright (c) 2024 Antmicro <www.antmicro.com>
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_INPUT_INPUT_TOUCH_H_
#define ZEPHYR_INCLUDE_INPUT_INPUT_TOUCH_H_


#include <zephyr/input/input.h>

#ifdef __cplusplus
extern "C" {
#endif

struct input_touchscreen_common_config {
        uint32_t screen_width;
        uint32_t screen_height;
        bool inverted_x;
        bool inverted_y;
        bool swapped_x_y;
        uint32_t output_width;
        uint32_t output_height;
};

#define INPUT_TOUCH_OUTPUT_DIM(node_id, dim, prop)                      \
        COND_CODE_1(DT_NODE_HAS_PROP(node_id, display),                 \
                (DT_PROP(DT_PHANDLE(node_id, display), dim)),           \
                (DT_PROP_OR(node_id, prop, 0)))

#define INPUT_TOUCH_DT_COMMON_CONFIG_INIT(node_id)                      \
        {                                                               \
                .screen_width = DT_PROP(node_id, screen_width),         \
                .screen_height = DT_PROP(node_id, screen_height),       \
                .inverted_x = DT_PROP(node_id, inverted_x),             \
                .inverted_y = DT_PROP(node_id, inverted_y),             \
                .swapped_x_y = DT_PROP(node_id, swapped_x_y),           \
                .output_width = INPUT_TOUCH_OUTPUT_DIM(node_id, width, output_width),   \
                .output_height = INPUT_TOUCH_OUTPUT_DIM(node_id, height, output_height),        \
        }

#define INPUT_TOUCH_DT_INST_COMMON_CONFIG_INIT(inst) \
        INPUT_TOUCH_DT_COMMON_CONFIG_INIT(DT_DRV_INST(inst))

#define INPUT_TOUCH_STRUCT_CHECK(config) \
        BUILD_ASSERT(offsetof(config, common) == 0, \
                     "struct input_touchscreen_common_config must be placed first");

void input_touchscreen_report_pos(const struct device *dev,
                uint32_t x, uint32_t y,
                k_timeout_t timeout);

#ifdef __cplusplus
}
#endif


#endif /* ZEPHYR_INCLUDE_INPUT_INPUT_TOUCH_H_ */
```

## 388.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2024 Antmicro <www.antmicro.com>。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 121 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_INPUT_INPUT_TOUCH_H_`。

## 388.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/input__touch_8h.html)
- [zephyr/input/input.h](https://docs.zephyrproject.org/latest/doxygen/html/input_8h.html)
- [input_touchscreen_common_config](../system_service_model_reference/P057_input_touchscreen_common_config_结构体.md)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [screen_width](../system_service_model_reference/P057_input_touchscreen_common_config_结构体.md#a35b6d8ccd36aa95d46cc24be2f94144b)
- [screen_height](../system_service_model_reference/P057_input_touchscreen_common_config_结构体.md#ae534425e6069853cb80a3925fce8e2ad)
- [inverted_x](../system_service_model_reference/P057_input_touchscreen_common_config_结构体.md#a147cc66f165b5bf9e42b591ad77824c5)
- [inverted_y](../system_service_model_reference/P057_input_touchscreen_common_config_结构体.md#abba0c9353f867287b047635ea358e057)
- [swapped_x_y](../system_service_model_reference/P057_input_touchscreen_common_config_结构体.md#a408e21f2a9e57267d87d24f8a054f999)
- [output_width](../system_service_model_reference/P057_input_touchscreen_common_config_结构体.md#ac7e996d150c9fef15ec733f4515bbf48)
- [output_height](../system_service_model_reference/P057_input_touchscreen_common_config_结构体.md#ad93cf875b2f1db32a8d4790296ccc6a3)
- [input_touchscreen_report_pos](https://docs.zephyrproject.org/latest/doxygen/html/group__touch__events.html#ga646bb86aa9f942fc3065381bd19e545c)
- [device](../device_reference/P002_设备对象结构.md)
- [k_timeout_t](../timer_reference/P087_内核超时类型.md)
- [input.h](https://docs.zephyrproject.org/latest/doxygen/html/input_8h.html)
- [input_touchscreen_common_config::inverted_x](../system_service_model_reference/P057_input_touchscreen_common_config_结构体.md#a147cc66f165b5bf9e42b591ad77824c5)
- [input_touchscreen_common_config::screen_width](../system_service_model_reference/P057_input_touchscreen_common_config_结构体.md#a35b6d8ccd36aa95d46cc24be2f94144b)
- [input_touchscreen_common_config::swapped_x_y](../system_service_model_reference/P057_input_touchscreen_common_config_结构体.md#a408e21f2a9e57267d87d24f8a054f999)
- [input_touchscreen_common_config::inverted_y](../system_service_model_reference/P057_input_touchscreen_common_config_结构体.md#abba0c9353f867287b047635ea358e057)
- [input_touchscreen_common_config::output_width](../system_service_model_reference/P057_input_touchscreen_common_config_结构体.md#ac7e996d150c9fef15ec733f4515bbf48)
- [input_touchscreen_common_config::output_height](../system_service_model_reference/P057_input_touchscreen_common_config_结构体.md#ad93cf875b2f1db32a8d4790296ccc6a3)
- [input_touchscreen_common_config::screen_height](../system_service_model_reference/P057_input_touchscreen_common_config_结构体.md#ae534425e6069853cb80a3925fce8e2ad)

---

[上一章](P387_input_renesas_rx_ctsu.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P389_inputmux_trigger_ports.h_源码浏览.md)
