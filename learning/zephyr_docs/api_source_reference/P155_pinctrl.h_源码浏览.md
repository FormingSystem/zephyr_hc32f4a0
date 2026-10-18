---
id: learning.zephyr-docs.api-source-reference.page-155
title: pinctrl.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/drivers_2firmware_2scmi_2pinctrl_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第155章\_pinctrl.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2firmware_2scmi_2pinctrl_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2firmware_2scmi_2pinctrl_8h.html)。

## 155.1\_原始可见代码（Source Code）

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
<a id="l00024"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="foldopen00038"></a>
<a id="l00038"></a>
<a id="l00039"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="l00044"></a>
<a id="l00046"></a>
<a id="l00047"></a>
<a id="foldopen00049"></a>
<a id="l00049"></a>
<a id="l00050"></a>
<a id="l00051"></a>
<a id="foldopen00056"></a>
<a id="l00056"></a>
<a id="l00057"></a>
<a id="l00058"></a>
<a id="l00060"></a>
<a id="l00061"></a>
<a id="foldopen00065"></a>
<a id="l00065"></a>
<a id="l00067"></a>
<a id="l00069"></a>
<a id="l00071"></a>
<a id="l00073"></a>
<a id="l00075"></a>
<a id="l00077"></a>
<a id="l00079"></a>
<a id="l00081"></a>
<a id="l00083"></a>
<a id="l00085"></a>
<a id="l00087"></a>
<a id="l00089"></a>
<a id="l00091"></a>
<a id="l00093"></a>
<a id="l00095"></a>
<a id="l00097"></a>
<a id="l00099"></a>
<a id="l00101"></a>
<a id="l00103"></a>
<a id="l00105"></a>
<a id="l00107"></a>
<a id="l00109"></a>
<a id="l00111"></a>
<a id="l00113"></a>
<a id="l00114"></a>
<a id="l00115"></a>
<a id="foldopen00122"></a>
<a id="l00122"></a>
<a id="l00124"></a>
<a id="l00126"></a>
<a id="l00128"></a>
<a id="l00130"></a>
<a id="l00131"></a>
<a id="l00132"></a>
<a id="l00140"></a>
<a id="l00141"></a>
<a id="l00145"></a>
<a id="l00146"></a>
<a id="adrivers_2firmware_2scmi_2protocol_8h_html"></a>
<a id="agroup__scmi__pinctrl_html_ga5856f69a41daebeb67bc675549a94082"></a>
<a id="agroup__scmi__pinctrl_html_gab5208b8108578e82acfa5dd0c8a2a96b"></a>
<a id="agroup__scmi__pinctrl_html_gad7d9ca78b75cc32edefc1ea8e0e0c09e"></a>
<a id="agroup__scmi__pinctrl_html_ggab5208b8108578e82acfa5dd0c8a2a96ba02ef96841a54b7f55b784d4b5c8685d2"></a>
<a id="agroup__scmi__pinctrl_html_ggab5208b8108578e82acfa5dd0c8a2a96ba051880c89ea312541c87324c4d641727"></a>
<a id="agroup__scmi__pinctrl_html_ggab5208b8108578e82acfa5dd0c8a2a96ba0a19f087055a6d331b3a20a83e39c696"></a>
<a id="agroup__scmi__pinctrl_html_ggab5208b8108578e82acfa5dd0c8a2a96ba18ecf549efbf006475f3c0205bbea432"></a>
<a id="agroup__scmi__pinctrl_html_ggab5208b8108578e82acfa5dd0c8a2a96ba264ed5f09078fdd145effc6d0fe705d4"></a>
<a id="agroup__scmi__pinctrl_html_ggab5208b8108578e82acfa5dd0c8a2a96ba2668c9faec52f0cf124af5af3e62cbd5"></a>
<a id="agroup__scmi__pinctrl_html_ggab5208b8108578e82acfa5dd0c8a2a96ba3c5302df7906c502eb31e0956a982171"></a>
<a id="agroup__scmi__pinctrl_html_ggab5208b8108578e82acfa5dd0c8a2a96ba3c62801c73f96b5854edd952ce6e729b"></a>
<a id="agroup__scmi__pinctrl_html_ggab5208b8108578e82acfa5dd0c8a2a96ba4600bb6538330e7b0228e78c8b8c5e55"></a>
<a id="agroup__scmi__pinctrl_html_ggab5208b8108578e82acfa5dd0c8a2a96ba464371220816dbe642caf696e3b9b905"></a>
<a id="agroup__scmi__pinctrl_html_ggab5208b8108578e82acfa5dd0c8a2a96ba4c93a8dcc239793359a5d49087b6d378"></a>
<a id="agroup__scmi__pinctrl_html_ggab5208b8108578e82acfa5dd0c8a2a96ba709f0e20f862af2b2886825731125bf4"></a>
<a id="agroup__scmi__pinctrl_html_ggab5208b8108578e82acfa5dd0c8a2a96ba84ceb297de86593719a88cfd3aaa4691"></a>
<a id="agroup__scmi__pinctrl_html_ggab5208b8108578e82acfa5dd0c8a2a96ba88232491b6ec4dfc73d5c945413c860e"></a>
<a id="agroup__scmi__pinctrl_html_ggab5208b8108578e82acfa5dd0c8a2a96ba8f3390e1a61d025c3682d23ed13725e8"></a>
<a id="agroup__scmi__pinctrl_html_ggab5208b8108578e82acfa5dd0c8a2a96ba9a3efde347233010b1a21f7c2c244e54"></a>
<a id="agroup__scmi__pinctrl_html_ggab5208b8108578e82acfa5dd0c8a2a96baac8d42ee60b4251cb506b9c724d458be"></a>
<a id="agroup__scmi__pinctrl_html_ggab5208b8108578e82acfa5dd0c8a2a96babb038fbaa33b735fc8bb749f0cc59359"></a>
<a id="agroup__scmi__pinctrl_html_ggab5208b8108578e82acfa5dd0c8a2a96bac93aa772bcf931acdd3532774270db65"></a>
<a id="agroup__scmi__pinctrl_html_ggab5208b8108578e82acfa5dd0c8a2a96bae991c77daff7720e03c45b7738ec7692"></a>
<a id="agroup__scmi__pinctrl_html_ggab5208b8108578e82acfa5dd0c8a2a96baed811778f8586aeca201119a5b05fd1d"></a>
<a id="agroup__scmi__pinctrl_html_ggab5208b8108578e82acfa5dd0c8a2a96baefcb24ff6ca583f7925db6b962951629"></a>
<a id="agroup__scmi__pinctrl_html_ggab5208b8108578e82acfa5dd0c8a2a96baf0dd0db5fb4cdab56e4d580e0da2a0a3"></a>
<a id="agroup__scmi__pinctrl_html_ggab5208b8108578e82acfa5dd0c8a2a96bafcdffbc64f9648ae15f8bfa1d4d97227"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astructscmi__pinctrl__settings_html"></a>
<a id="astructscmi__pinctrl__settings_html_a36c8e49a42cb89d4117b9e90fe1a044e"></a>
<a id="astructscmi__pinctrl__settings_html_a5e92a3755d6dc8ccfecf696ca5eb8bd1"></a>
<a id="astructscmi__pinctrl__settings_html_a7c206eaf1a88e0d1e54d0d19c79e25c6"></a>
<a id="astructscmi__pinctrl__settings_html_ade79b6c3efc5b069f74ad6e12088d6c2"></a>

```c
/*
 * Copyright 2024 NXP
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DRIVERS_FIRMWARE_SCMI_PINCTRL_H_
#define ZEPHYR_INCLUDE_DRIVERS_FIRMWARE_SCMI_PINCTRL_H_

#include <zephyr/drivers/firmware/scmi/protocol.h>


#define ARM_SCMI_PINCTRL_MAX_CONFIG_SIZE (10 * 2)

#define SCMI_PINCTRL_NO_FUNCTION 0xFFFFFFFF

#define SCMI_PINCTRL_CONFIG_ATTRIBUTES(fid_valid, cfg_num, selector)    \
        (SCMI_FIELD_MAKE(fid_valid, BIT(0), 10) |                       \
         SCMI_FIELD_MAKE(cfg_num, GENMASK(7, 0), 2) |                   \
         SCMI_FIELD_MAKE(selector, GENMASK(1, 0), 0))

#define SCMI_PINCTRL_SELECTOR_PIN 0x0
#define SCMI_PINCTRL_SELECTOR_GROUP 0x1

#define SCMI_PINCTRL_ATTRIBUTES_CONFIG_NUM(attributes)\
        (((attributes) & GENMASK(9, 2)) >> 2)

#define SCMI_PINCTRL_ATTRIBUTES_FID_VALID(attributes)\
        FIELD_GET(BIT(10), attributes)

#define SCMI_PIN_CONTROL_PROTOCOL_SUPPORTED_VERSION     0x10000

enum scmi_pinctrl_config {
        SCMI_PINCTRL_DEFAULT = 0,
        SCMI_PINCTRL_BIAS_BUS_HOLD = 1,
        SCMI_PINCTRL_BIAS_DISABLE = 2,
        SCMI_PINCTRL_BIAS_HIGH_Z = 3,
        SCMI_PINCTRL_BIAS_PULL_UP = 4,
        SCMI_PINCTRL_BIAS_PULL_DEFAULT = 5,
        SCMI_PINCTRL_BIAS_PULL_DOWN = 6,
        SCMI_PINCTRL_DRIVE_OPEN_DRAIN = 7,
        SCMI_PINCTRL_DRIVE_OPEN_SOURCE = 8,
        SCMI_PCINTRL_DRIVE_PUSH_PULL = 9,
        SCMI_PCINTRL_DRIVE_STRENGTH = 10,
        SCMI_PINCTRL_INPUT_DEBOUNCE = 11,
        SCMI_PINCTRL_INPUT_MODE = 12,
        SCMI_PINCTRL_PULL_MODE = 13,
        SCMI_PINCTRL_INPUT_VALUE = 14,
        SCMI_PINCTRL_INPUT_SCHMITT = 15,
        SCMI_PINCTRL_LP_MODE = 16,
        SCMI_PINCTRL_OUTPUT_MODE = 17,
        SCMI_PINCTRL_OUTPUT_VALUE = 18,
        SCMI_PINCTRL_POWER_SOURCE = 19,
        SCMI_PINCTRL_SLEW_RATE = 20,
        SCMI_PINCTRL_RESERVED_START = 21,
        SCMI_PINCTRL_RESERVED_END = 191,
        SCMI_PINCTRL_VENDOR_START = 192,
};

struct scmi_pinctrl_settings {
        uint32_t id;
        uint32_t function;
        uint32_t attributes;
        uint32_t config[ARM_SCMI_PINCTRL_MAX_CONFIG_SIZE];
};

int scmi_pinctrl_settings_configure(struct scmi_pinctrl_settings *settings);


#endif /* ZEPHYR_INCLUDE_DRIVERS_FIRMWARE_SCMI_PINCTRL_H_ */
```

## 155.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：2024 NXP。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 146 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_FIRMWARE_SCMI_PINCTRL_H_`。

## 155.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2firmware_2scmi_2pinctrl_8h.html)
- [zephyr/drivers/firmware/scmi/protocol.h](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2firmware_2scmi_2protocol_8h.html)
- [scmi_pinctrl_config](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__pinctrl.html#gab5208b8108578e82acfa5dd0c8a2a96b)
- [SCMI_PINCTRL_DEFAULT](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__pinctrl.html#ggab5208b8108578e82acfa5dd0c8a2a96ba3c62801c73f96b5854edd952ce6e729b)
- [SCMI_PINCTRL_BIAS_BUS_HOLD](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__pinctrl.html#ggab5208b8108578e82acfa5dd0c8a2a96ba4600bb6538330e7b0228e78c8b8c5e55)
- [SCMI_PINCTRL_BIAS_DISABLE](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__pinctrl.html#ggab5208b8108578e82acfa5dd0c8a2a96ba8f3390e1a61d025c3682d23ed13725e8)
- [SCMI_PINCTRL_BIAS_HIGH_Z](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__pinctrl.html#ggab5208b8108578e82acfa5dd0c8a2a96ba18ecf549efbf006475f3c0205bbea432)
- [SCMI_PINCTRL_BIAS_PULL_UP](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__pinctrl.html#ggab5208b8108578e82acfa5dd0c8a2a96ba88232491b6ec4dfc73d5c945413c860e)
- [SCMI_PINCTRL_BIAS_PULL_DEFAULT](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__pinctrl.html#ggab5208b8108578e82acfa5dd0c8a2a96ba02ef96841a54b7f55b784d4b5c8685d2)
- [SCMI_PINCTRL_BIAS_PULL_DOWN](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__pinctrl.html#ggab5208b8108578e82acfa5dd0c8a2a96bae991c77daff7720e03c45b7738ec7692)
- [SCMI_PINCTRL_DRIVE_OPEN_DRAIN](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__pinctrl.html#ggab5208b8108578e82acfa5dd0c8a2a96baed811778f8586aeca201119a5b05fd1d)
- [SCMI_PINCTRL_DRIVE_OPEN_SOURCE](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__pinctrl.html#ggab5208b8108578e82acfa5dd0c8a2a96ba9a3efde347233010b1a21f7c2c244e54)
- [SCMI_PCINTRL_DRIVE_PUSH_PULL](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__pinctrl.html#ggab5208b8108578e82acfa5dd0c8a2a96bafcdffbc64f9648ae15f8bfa1d4d97227)
- [SCMI_PCINTRL_DRIVE_STRENGTH](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__pinctrl.html#ggab5208b8108578e82acfa5dd0c8a2a96baf0dd0db5fb4cdab56e4d580e0da2a0a3)
- [SCMI_PINCTRL_INPUT_DEBOUNCE](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__pinctrl.html#ggab5208b8108578e82acfa5dd0c8a2a96ba709f0e20f862af2b2886825731125bf4)
- [SCMI_PINCTRL_INPUT_MODE](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__pinctrl.html#ggab5208b8108578e82acfa5dd0c8a2a96ba264ed5f09078fdd145effc6d0fe705d4)
- [SCMI_PINCTRL_PULL_MODE](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__pinctrl.html#ggab5208b8108578e82acfa5dd0c8a2a96bac93aa772bcf931acdd3532774270db65)
- [SCMI_PINCTRL_INPUT_VALUE](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__pinctrl.html#ggab5208b8108578e82acfa5dd0c8a2a96ba2668c9faec52f0cf124af5af3e62cbd5)
- [SCMI_PINCTRL_INPUT_SCHMITT](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__pinctrl.html#ggab5208b8108578e82acfa5dd0c8a2a96baac8d42ee60b4251cb506b9c724d458be)
- [SCMI_PINCTRL_LP_MODE](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__pinctrl.html#ggab5208b8108578e82acfa5dd0c8a2a96ba84ceb297de86593719a88cfd3aaa4691)
- [SCMI_PINCTRL_OUTPUT_MODE](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__pinctrl.html#ggab5208b8108578e82acfa5dd0c8a2a96ba4c93a8dcc239793359a5d49087b6d378)
- [SCMI_PINCTRL_OUTPUT_VALUE](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__pinctrl.html#ggab5208b8108578e82acfa5dd0c8a2a96babb038fbaa33b735fc8bb749f0cc59359)
- [SCMI_PINCTRL_POWER_SOURCE](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__pinctrl.html#ggab5208b8108578e82acfa5dd0c8a2a96ba464371220816dbe642caf696e3b9b905)
- [SCMI_PINCTRL_SLEW_RATE](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__pinctrl.html#ggab5208b8108578e82acfa5dd0c8a2a96baefcb24ff6ca583f7925db6b962951629)
- [SCMI_PINCTRL_RESERVED_START](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__pinctrl.html#ggab5208b8108578e82acfa5dd0c8a2a96ba051880c89ea312541c87324c4d641727)
- [SCMI_PINCTRL_RESERVED_END](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__pinctrl.html#ggab5208b8108578e82acfa5dd0c8a2a96ba3c5302df7906c502eb31e0956a982171)
- [SCMI_PINCTRL_VENDOR_START](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__pinctrl.html#ggab5208b8108578e82acfa5dd0c8a2a96ba0a19f087055a6d331b3a20a83e39c696)
- [scmi_pinctrl_settings](../platform_security_model_reference/P044_scmi_pinctrl_settings_结构体.md)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [id](../platform_security_model_reference/P044_scmi_pinctrl_settings_结构体.md#a36c8e49a42cb89d4117b9e90fe1a044e)
- [function](../platform_security_model_reference/P044_scmi_pinctrl_settings_结构体.md#ade79b6c3efc5b069f74ad6e12088d6c2)
- [attributes](../platform_security_model_reference/P044_scmi_pinctrl_settings_结构体.md#a7c206eaf1a88e0d1e54d0d19c79e25c6)
- [config](../platform_security_model_reference/P044_scmi_pinctrl_settings_结构体.md#a5e92a3755d6dc8ccfecf696ca5eb8bd1)
- [ARM_SCMI_PINCTRL_MAX_CONFIG_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__pinctrl.html#ga5856f69a41daebeb67bc675549a94082)
- [scmi_pinctrl_settings_configure](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__pinctrl.html#gad7d9ca78b75cc32edefc1ea8e0e0c09e)
- [protocol.h](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2firmware_2scmi_2protocol_8h.html)
- [scmi_pinctrl_settings::id](../platform_security_model_reference/P044_scmi_pinctrl_settings_结构体.md#a36c8e49a42cb89d4117b9e90fe1a044e)
- [scmi_pinctrl_settings::config](../platform_security_model_reference/P044_scmi_pinctrl_settings_结构体.md#a5e92a3755d6dc8ccfecf696ca5eb8bd1)
- [scmi_pinctrl_settings::attributes](../platform_security_model_reference/P044_scmi_pinctrl_settings_结构体.md#a7c206eaf1a88e0d1e54d0d19c79e25c6)
- [scmi_pinctrl_settings::function](../platform_security_model_reference/P044_scmi_pinctrl_settings_结构体.md#ade79b6c3efc5b069f74ad6e12088d6c2)

---

[上一章](P154_cpu.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P156_protocol.h_源码浏览.md)
