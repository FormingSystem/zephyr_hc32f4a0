---
id: learning.zephyr-docs.api-source-configuration-reference.page-19
title: reset.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/drivers_2firmware_2scmi_2reset_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第19章\_reset.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2firmware_2scmi_2reset_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2firmware_2scmi_2reset_8h.html)。

## 19.1\_原始可见代码（Source Code）

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
<a id="l00025"></a>
<a id="l00027"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="l00031"></a>
<a id="l00033"></a>
<a id="l00035"></a>
<a id="l00037"></a>
<a id="l00038"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="l00043"></a>
<a id="l00044"></a>
<a id="foldopen00049"></a>
<a id="l00049"></a>
<a id="l00051"></a>
<a id="l00053"></a>
<a id="l00055"></a>
<a id="l00057"></a>
<a id="l00059"></a>
<a id="l00060"></a>
<a id="l00061"></a>
<a id="l00071"></a>
<a id="l00072"></a>
<a id="l00073"></a>
<a id="l00084"></a>
<a id="l00085"></a>
<a id="l00086"></a>
<a id="l00090"></a>
<a id="l00091"></a>
<a id="adrivers_2firmware_2scmi_2protocol_8h_html"></a>
<a id="agroup__scmi__interface_html_gaff6ceb886b06b1187018d8a2b8dd73e3"></a>
<a id="agroup__scmi__reset_html_gaa0d948bb949e0ef8066bccd243948044"></a>
<a id="agroup__scmi__reset_html_gab79cf3b45fec93a8eba5dd0d6377b21e"></a>
<a id="aparser_8h_html_ab6b306ef981f5e21bb41ea2c2dbe8cd9"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astructscmi__protocol_html"></a>
<a id="astructscmi__reset__domain__attr_html"></a>
<a id="astructscmi__reset__domain__attr_html_a23258ab925ea86f304d49fdb5c562fd3"></a>
<a id="astructscmi__reset__domain__attr_html_a47e672531778348a1da1b835374a7b1b"></a>
<a id="astructscmi__reset__domain__attr_html_a5a64c890789e2e9fb273cca050e24ade"></a>
<a id="astructscmi__reset__domain__attr_html_a5f130ce02cc05af0caa6abbdb9affea4"></a>
<a id="astructscmi__reset__domain__attr_html_a8b8d31eba1f64f0f5cef64dea229848d"></a>

```c
/*
 * Copyright (c) 2026 EPAM Systems
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DRIVERS_FIRMWARE_SCMI_RESET_H_
#define ZEPHYR_INCLUDE_DRIVERS_FIRMWARE_SCMI_RESET_H_

#include <zephyr/drivers/firmware/scmi/protocol.h>


/* PROTOCOL_ATTRIBUTES */
#define SCMI_RESET_ATTR_NUM_DOMAINS           GENMASK(15, 0)
#define SCMI_RESET_ATTR_GET_NUM_DOMAINS(attr) FIELD_GET(SCMI_RESET_ATTR_NUM_DOMAINS, (attr))

/* RESET Domain Attributes Flags */
#define SCMI_RESET_AUTONOMOUS         BIT(0)
#define SCMI_RESET_EXPLICIT_ASSERT    BIT(1)
#define SCMI_RESET_ASYNCHRONOUS_RESET BIT(2)

#define SCMI_RESET_ARCH_COLD_RESET 0

#define SCMI_RESET_PROTOCOL_SUPPORTED_VERSION 0x30001

struct scmi_reset_domain_attr {
        uint32_t latency;
        char name[SCMI_SHORT_NAME_MAX_SIZE];
        bool is_async_sup:1;
        bool is_notifications_sup:1;
        bool is_latency_valid:1;
};

int scmi_reset_domain_get_attr(struct scmi_protocol *proto, uint32_t id,
                               struct scmi_reset_domain_attr *dom_attr);

int scmi_reset_domain(struct scmi_protocol *proto, uint32_t id, uint32_t flags,
                      uint32_t reset_state);


#endif /* ZEPHYR_INCLUDE_DRIVERS_FIRMWARE_SCMI_RESET_H_ */
```

## 19.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2026 EPAM Systems。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 25 行

协议属性（`PROTOCOL_ATTRIBUTES`）。

### 注释 3：原第 31 行

复位域属性标志（RESET Domain Attributes Flags）。

### 注释 4：原第 91 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_FIRMWARE_SCMI_RESET_H_`。

## 19.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2firmware_2scmi_2reset_8h.html)
- [zephyr/drivers/firmware/scmi/protocol.h](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2firmware_2scmi_2protocol_8h.html)
- [scmi_reset_domain_attr](../platform_security_model_reference/P050_scmi_reset_domain_attr_结构体.md)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [latency](../platform_security_model_reference/P050_scmi_reset_domain_attr_结构体.md#a47e672531778348a1da1b835374a7b1b)
- [name](../platform_security_model_reference/P050_scmi_reset_domain_attr_结构体.md#a23258ab925ea86f304d49fdb5c562fd3)
- [SCMI_SHORT_NAME_MAX_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__interface.html#gaff6ceb886b06b1187018d8a2b8dd73e3)
- [is_async_sup](../platform_security_model_reference/P050_scmi_reset_domain_attr_结构体.md#a5f130ce02cc05af0caa6abbdb9affea4)
- [is_notifications_sup](../platform_security_model_reference/P050_scmi_reset_domain_attr_结构体.md#a5a64c890789e2e9fb273cca050e24ade)
- [is_latency_valid](../platform_security_model_reference/P050_scmi_reset_domain_attr_结构体.md#a8b8d31eba1f64f0f5cef64dea229848d)
- [scmi_reset_domain_get_attr](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__reset.html#gaa0d948bb949e0ef8066bccd243948044)
- [scmi_protocol](../platform_security_model_reference/P047_scmi_protocol_结构体.md)
- [scmi_reset_domain](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__reset.html#gab79cf3b45fec93a8eba5dd0d6377b21e)
- [flags](https://docs.zephyrproject.org/latest/doxygen/html/parser_8h.html#ab6b306ef981f5e21bb41ea2c2dbe8cd9)
- [protocol.h](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2firmware_2scmi_2protocol_8h.html)
- [scmi_reset_domain_attr::name](../platform_security_model_reference/P050_scmi_reset_domain_attr_结构体.md#a23258ab925ea86f304d49fdb5c562fd3)
- [scmi_reset_domain_attr::latency](../platform_security_model_reference/P050_scmi_reset_domain_attr_结构体.md#a47e672531778348a1da1b835374a7b1b)
- [scmi_reset_domain_attr::is_notifications_sup](../platform_security_model_reference/P050_scmi_reset_domain_attr_结构体.md#a5a64c890789e2e9fb273cca050e24ade)
- [scmi_reset_domain_attr::is_async_sup](../platform_security_model_reference/P050_scmi_reset_domain_attr_结构体.md#a5f130ce02cc05af0caa6abbdb9affea4)
- [scmi_reset_domain_attr::is_latency_valid](../platform_security_model_reference/P050_scmi_reset_domain_attr_结构体.md#a8b8d31eba1f64f0f5cef64dea229848d)

---

[上一章](P018_dma_npcx_gdma.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P020_dsa_tag_proto.h_源码浏览.md)
