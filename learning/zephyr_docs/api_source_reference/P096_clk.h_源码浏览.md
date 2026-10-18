---
id: learning.zephyr-docs.api-source-reference.page-96
title: clk.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/clk_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第96章\_clk.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/clk_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/clk_8h.html)。

## 96.1\_原始可见代码（Source Code）

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
<a id="foldopen00028"></a>
<a id="l00028"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="l00035"></a>
<a id="l00037"></a>
<a id="l00039"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="l00044"></a>
<a id="l00045"></a>
<a id="l00053"></a>
<a id="l00054"></a>
<a id="l00061"></a>
<a id="l00062"></a>
<a id="l00064"></a>
<a id="l00065"></a>
<a id="l00067"></a>
<a id="l00068"></a>
<a id="l00070"></a>
<a id="l00071"></a>
<a id="l00073"></a>
<a id="l00074"></a>
<a id="foldopen00081"></a>
<a id="l00081"></a>
<a id="l00083"></a>
<a id="l00085"></a>
<a id="l00087"></a>
<a id="l00088"></a>
<a id="l00089"></a>
<a id="foldopen00096"></a>
<a id="l00096"></a>
<a id="l00098"></a>
<a id="l00100"></a>
<a id="l00102"></a>
<a id="l00103"></a>
<a id="l00104"></a>
<a id="foldopen00110"></a>
<a id="l00110"></a>
<a id="l00112"></a>
<a id="l00114"></a>
<a id="l00116"></a>
<a id="l00117"></a>
<a id="l00118"></a>
<a id="l00128"></a>
<a id="l00129"></a>
<a id="l00130"></a>
<a id="l00146"></a>
<a id="l00147"></a>
<a id="l00157"></a>
<a id="l00158"></a>
<a id="l00159"></a>
<a id="l00169"></a>
<a id="l00170"></a>
<a id="l00180"></a>
<a id="l00181"></a>
<a id="l00192"></a>
<a id="l00193"></a>
<a id="l00203"></a>
<a id="l00204"></a>
<a id="l00205"></a>
<a id="l00215"></a>
<a id="l00216"></a>
<a id="l00220"></a>
<a id="l00221"></a>
<a id="adrivers_2firmware_2scmi_2protocol_8h_html"></a>
<a id="agroup__scmi__clk_html_ga11fb749832c289730674fb111fdb6a18"></a>
<a id="agroup__scmi__clk_html_ga456618c04934490afffdcd8be71729b3"></a>
<a id="agroup__scmi__clk_html_ga57942effe001fdb62a435a51441108e6"></a>
<a id="agroup__scmi__clk_html_ga9803a171fc12c01b6f29822eb3ccaea7"></a>
<a id="agroup__scmi__clk_html_gaa0f54c7fba01045a89ef0fd3a0ff16fc"></a>
<a id="agroup__scmi__clk_html_gac69cff69cef158aebf5b40ba2c3c7bb4"></a>
<a id="agroup__scmi__clk_html_gac9fe7f4275895fd9e6a7eada26012efb"></a>
<a id="agroup__scmi__clk_html_gadac0bacc2404b6be066155c6ce4a0d28"></a>
<a id="agroup__scmi__clk_html_gaf50ba91139d4de1a7eab9d8b4cebf745"></a>
<a id="aparser_8h_html_ab6b306ef981f5e21bb41ea2c2dbe8cd9"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astructscmi__clock__attributes_html"></a>
<a id="astructscmi__clock__attributes_html_a799a83ff8c0de3c62da2d206c471a630"></a>
<a id="astructscmi__clock__attributes_html_ab8379494c52bc400a545ff6808dbbf97"></a>
<a id="astructscmi__clock__attributes_html_ae85727aa3446b3f3b2ccc173367a9396"></a>
<a id="astructscmi__clock__config_html"></a>
<a id="astructscmi__clock__config_html_a1f4acfb41d1b75448f96acad6cfd3498"></a>
<a id="astructscmi__clock__config_html_ae180ad04a48558130e26a268ec444297"></a>
<a id="astructscmi__clock__config_html_ae21186dde1af79f55bdce325d08cdc06"></a>
<a id="astructscmi__clock__rate__config_html"></a>
<a id="astructscmi__clock__rate__config_html_a240149068386c9da08236589186ba4d8"></a>
<a id="astructscmi__clock__rate__config_html_a784dfe157fad46cfa038be4cac21560c"></a>
<a id="astructscmi__clock__rate__config_html_ab9a77f5d0213008afc023ae3406cbb81"></a>
<a id="astructscmi__protocol_html"></a>

```c
/*
 * Copyright 2024 NXP
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DRIVERS_FIRMWARE_SCMI_CLK_H_
#define ZEPHYR_INCLUDE_DRIVERS_FIRMWARE_SCMI_CLK_H_

#include <zephyr/drivers/firmware/scmi/protocol.h>


#define SCMI_CLK_CONFIG_DISABLE_ENABLE_MASK GENMASK(1, 0)
#define SCMI_CLK_CONFIG_ENABLE_DISABLE(x)\
        ((uint32_t)(x) & SCMI_CLK_CONFIG_DISABLE_ENABLE_MASK)

#define SCMI_CLK_ATTRIBUTES_CLK_NUM(x) ((x) & GENMASK(15, 0))

#define SCMI_CLK_RATE_SET_FLAGS_ASYNC                BIT(0)
#define SCMI_CLK_RATE_SET_FLAGS_IGNORE_DELEAYED_RESP BIT(1)
#define SCMI_CLK_RATE_SET_FLAGS_ROUNDS_UP_DOWN       BIT(2)
#define SCMI_CLK_RATE_SET_FLAGS_ROUNDS_AUTO          BIT(3)

#define SCMI_CLK_PROTOCOL_SUPPORTED_VERSION     0x30000

#define SCMI_PROTO_VER_MAJOR(v) ((v) >> 16)

#define SCMI_PROTO_VER_MINOR(v) ((v) & 0xFFFF)

#define SCMI_CLK_NAME_LEN 16

#define SCMI_CLK_ENABLED(attributes) ((attributes) & BIT(0))

#define SCMI_CLK_HAS_RESTRICTIONS(attributes) ((attributes) & BIT(1))

#define SCMI_CLK_STATE_CONTROL_ALLOWED(permissions) ((permissions) & BIT(31))

struct scmi_clock_config {
        uint32_t clk_id;
        uint32_t attributes;
        uint32_t extended_cfg_val;
};

struct scmi_clock_rate_config {
        uint32_t flags;
        uint32_t clk_id;
        uint32_t rate[2];
};

struct scmi_clock_attributes {
        uint32_t attributes;
        uint8_t clock_name[SCMI_CLK_NAME_LEN];
        uint32_t clock_enable_delay;
};

int scmi_clock_config_set(struct scmi_protocol *proto,
                          struct scmi_clock_config *cfg);

int scmi_clock_config_get(struct scmi_protocol *proto, uint32_t clk_id,
                          uint32_t flags, uint32_t *config);
int scmi_clock_rate_get(struct scmi_protocol *proto,
                        uint32_t clk_id, uint32_t *rate);

int scmi_clock_rate_set(struct scmi_protocol *proto, struct scmi_clock_rate_config *cfg);

int scmi_clock_parent_get(struct scmi_protocol *proto, uint32_t clk_id, uint32_t *parent_id);

int scmi_clock_parent_set(struct scmi_protocol *proto, uint32_t clk_id, uint32_t parent_id);

int scmi_clock_attributes(struct scmi_protocol *proto, uint32_t clk_id,
                          struct scmi_clock_attributes *attributes);

int scmi_clock_get_permissions(struct scmi_protocol *proto, uint32_t clk_id,
                               uint32_t *permissions);

#endif /* ZEPHYR_INCLUDE_DRIVERS_FIRMWARE_SCMI_CLK_H_ */
```

## 96.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：2024 NXP。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 221 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_FIRMWARE_SCMI_CLK_H_`。

## 96.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/clk_8h.html)
- [zephyr/drivers/firmware/scmi/protocol.h](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2firmware_2scmi_2protocol_8h.html)
- [scmi_clock_config](../platform_security_model_reference/P035_scmi_clock_config_结构体.md)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [clk_id](../platform_security_model_reference/P035_scmi_clock_config_结构体.md#a1f4acfb41d1b75448f96acad6cfd3498)
- [attributes](../platform_security_model_reference/P035_scmi_clock_config_结构体.md#ae21186dde1af79f55bdce325d08cdc06)
- [extended_cfg_val](../platform_security_model_reference/P035_scmi_clock_config_结构体.md#ae180ad04a48558130e26a268ec444297)
- [scmi_clock_rate_config](../platform_security_model_reference/P036_scmi_clock_rate_config_结构体.md)
- [flags](../platform_security_model_reference/P036_scmi_clock_rate_config_结构体.md#a784dfe157fad46cfa038be4cac21560c)
- [clk_id](../platform_security_model_reference/P036_scmi_clock_rate_config_结构体.md#ab9a77f5d0213008afc023ae3406cbb81)
- [rate](../platform_security_model_reference/P036_scmi_clock_rate_config_结构体.md#a240149068386c9da08236589186ba4d8)
- [scmi_clock_attributes](../platform_security_model_reference/P034_scmi_clock_attributes_结构体.md)
- [attributes](../platform_security_model_reference/P034_scmi_clock_attributes_结构体.md#a799a83ff8c0de3c62da2d206c471a630)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [clock_name](../platform_security_model_reference/P034_scmi_clock_attributes_结构体.md#ae85727aa3446b3f3b2ccc173367a9396)
- [SCMI_CLK_NAME_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__clk.html#gadac0bacc2404b6be066155c6ce4a0d28)
- [clock_enable_delay](../platform_security_model_reference/P034_scmi_clock_attributes_结构体.md#ab8379494c52bc400a545ff6808dbbf97)
- [scmi_clock_config_set](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__clk.html#gac9fe7f4275895fd9e6a7eada26012efb)
- [scmi_protocol](../platform_security_model_reference/P047_scmi_protocol_结构体.md)
- [scmi_clock_config_get](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__clk.html#gaf50ba91139d4de1a7eab9d8b4cebf745)
- [flags](https://docs.zephyrproject.org/latest/doxygen/html/parser_8h.html#ab6b306ef981f5e21bb41ea2c2dbe8cd9)
- [scmi_clock_rate_get](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__clk.html#gac69cff69cef158aebf5b40ba2c3c7bb4)
- [scmi_clock_rate_set](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__clk.html#gaa0f54c7fba01045a89ef0fd3a0ff16fc)
- [scmi_clock_parent_get](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__clk.html#ga456618c04934490afffdcd8be71729b3)
- [scmi_clock_parent_set](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__clk.html#ga57942effe001fdb62a435a51441108e6)
- [scmi_clock_attributes](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__clk.html#ga9803a171fc12c01b6f29822eb3ccaea7)
- [scmi_clock_get_permissions](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__clk.html#ga11fb749832c289730674fb111fdb6a18)
- [protocol.h](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2firmware_2scmi_2protocol_8h.html)
- [scmi_clock_attributes::attributes](../platform_security_model_reference/P034_scmi_clock_attributes_结构体.md#a799a83ff8c0de3c62da2d206c471a630)
- [scmi_clock_attributes::clock_enable_delay](../platform_security_model_reference/P034_scmi_clock_attributes_结构体.md#ab8379494c52bc400a545ff6808dbbf97)
- [scmi_clock_attributes::clock_name](../platform_security_model_reference/P034_scmi_clock_attributes_结构体.md#ae85727aa3446b3f3b2ccc173367a9396)
- [scmi_clock_config::clk_id](../platform_security_model_reference/P035_scmi_clock_config_结构体.md#a1f4acfb41d1b75448f96acad6cfd3498)
- [scmi_clock_config::extended_cfg_val](../platform_security_model_reference/P035_scmi_clock_config_结构体.md#ae180ad04a48558130e26a268ec444297)
- [scmi_clock_config::attributes](../platform_security_model_reference/P035_scmi_clock_config_结构体.md#ae21186dde1af79f55bdce325d08cdc06)
- [scmi_clock_rate_config::rate](../platform_security_model_reference/P036_scmi_clock_rate_config_结构体.md#a240149068386c9da08236589186ba4d8)
- [scmi_clock_rate_config::flags](../platform_security_model_reference/P036_scmi_clock_rate_config_结构体.md#a784dfe157fad46cfa038be4cac21560c)
- [scmi_clock_rate_config::clk_id](../platform_security_model_reference/P036_scmi_clock_rate_config_结构体.md#ab9a77f5d0213008afc023ae3406cbb81)

---

[上一章](P095_classic.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P097_sf32lb.h_源码浏览.md)
