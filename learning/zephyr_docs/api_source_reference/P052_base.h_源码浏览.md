---
id: learning.zephyr-docs.api-source-reference.page-52
title: base.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/base_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第52章\_base.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/base_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/base_8h.html)。

## 52.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00008"></a>
<a id="l00009"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00024"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="foldopen00034"></a>
<a id="l00034"></a>
<a id="l00036"></a>
<a id="l00038"></a>
<a id="l00040"></a>
<a id="l00042"></a>
<a id="l00044"></a>
<a id="l00045"></a>
<a id="l00046"></a>
<a id="foldopen00052"></a>
<a id="l00052"></a>
<a id="l00054"></a>
<a id="l00056"></a>
<a id="l00057"></a>
<a id="l00058"></a>
<a id="l00065"></a>
<a id="l00066"></a>
<a id="l00073"></a>
<a id="l00074"></a>
<a id="l00083"></a>
<a id="l00084"></a>
<a id="l00093"></a>
<a id="l00094"></a>
<a id="l00102"></a>
<a id="l00103"></a>
<a id="l00107"></a>
<a id="l00108"></a>
<a id="adrivers_2firmware_2scmi_2protocol_8h_html"></a>
<a id="agroup__scmi__base_html_ga161b383297fe35f90d9d25d02f30633d"></a>
<a id="agroup__scmi__base_html_ga286e1a0dff35750c88b2ffe9372aae0d"></a>
<a id="agroup__scmi__base_html_ga9be1e92e28837b9ee64d8b792897bacf"></a>
<a id="agroup__scmi__base_html_gacb8772d6c7b59168ab2ae043dc4852f1"></a>
<a id="agroup__scmi__base_html_gaf4c82d6c1faffae9fc3f2070de52d11a"></a>
<a id="agroup__scmi__interface_html_gaff6ceb886b06b1187018d8a2b8dd73e3"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astructscmi__agent__info_html"></a>
<a id="astructscmi__agent__info_html_a137145e77dd29b54815295d0951a5263"></a>
<a id="astructscmi__agent__info_html_aed61e021c94d0a5efb05f14daf47077b"></a>
<a id="astructscmi__platform__info_html"></a>
<a id="astructscmi__platform__info_html_a050a3fb299aa893da67e32874b565d20"></a>
<a id="astructscmi__platform__info_html_a550fb1e5b313df82e7ad54741228abb6"></a>
<a id="astructscmi__platform__info_html_aa06c3dd53958c3cbe389f682b5ded16c"></a>
<a id="astructscmi__platform__info_html_ade42f3a6c6e97bce2695072a39ec21bd"></a>
<a id="astructscmi__platform__info_html_ae6327a38864e1247b382a76259562c92"></a>

```c
/*
 * Copyright (c) 2026 EPAM Systems
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DRIVERS_FIRMWARE_SCMI_BASE_H_
#define ZEPHYR_INCLUDE_DRIVERS_FIRMWARE_SCMI_BASE_H_


#include <zephyr/drivers/firmware/scmi/protocol.h>


#define SCMI_BASE_PROTOCOL_SUPPORTED_VERSION 0x20001

#define SCMI_BASE_AGENT_ID_OWN 0xFFFFFFFF

struct scmi_platform_info {
        uint8_t num_protocols;
        uint8_t num_agents;
        uint32_t impl_ver;
        char vendor_id[SCMI_SHORT_NAME_MAX_SIZE];
        char sub_vendor_id[SCMI_SHORT_NAME_MAX_SIZE];
};

struct scmi_agent_info {
        uint32_t agent_id;
        char name[SCMI_SHORT_NAME_MAX_SIZE];
};

int scmi_base_get_num_agents(uint8_t *num_agents);

int scmi_base_get_platform_info(struct scmi_platform_info *rev);

int scmi_base_discover_agent(uint32_t agent_id, struct scmi_agent_info *agent_inf);

int scmi_base_device_permission(uint32_t agent_id, uint32_t device_id, bool allow);

int scmi_base_reset_agent_cfg(uint32_t agent_id, bool reset_perm);


#endif /* ZEPHYR_INCLUDE_DRIVERS_FIRMWARE_SCMI_BASE_H_ */
```

## 52.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2026 EPAM Systems。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 108 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_FIRMWARE_SCMI_BASE_H_`。

## 52.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/base_8h.html)
- [zephyr/drivers/firmware/scmi/protocol.h](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2firmware_2scmi_2protocol_8h.html)
- [scmi_platform_info](../platform_security_model_reference/P045_scmi_platform_info_结构体.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [num_protocols](../platform_security_model_reference/P045_scmi_platform_info_结构体.md#aa06c3dd53958c3cbe389f682b5ded16c)
- [num_agents](../platform_security_model_reference/P045_scmi_platform_info_结构体.md#ade42f3a6c6e97bce2695072a39ec21bd)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [impl_ver](../platform_security_model_reference/P045_scmi_platform_info_结构体.md#ae6327a38864e1247b382a76259562c92)
- [vendor_id](../platform_security_model_reference/P045_scmi_platform_info_结构体.md#a550fb1e5b313df82e7ad54741228abb6)
- [SCMI_SHORT_NAME_MAX_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__interface.html#gaff6ceb886b06b1187018d8a2b8dd73e3)
- [sub_vendor_id](../platform_security_model_reference/P045_scmi_platform_info_结构体.md#a050a3fb299aa893da67e32874b565d20)
- [scmi_agent_info](../platform_security_model_reference/P032_scmi_agent_info_结构体.md)
- [agent_id](../platform_security_model_reference/P032_scmi_agent_info_结构体.md#a137145e77dd29b54815295d0951a5263)
- [name](../platform_security_model_reference/P032_scmi_agent_info_结构体.md#aed61e021c94d0a5efb05f14daf47077b)
- [scmi_base_get_num_agents](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__base.html#ga286e1a0dff35750c88b2ffe9372aae0d)
- [scmi_base_get_platform_info](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__base.html#ga9be1e92e28837b9ee64d8b792897bacf)
- [scmi_base_discover_agent](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__base.html#gaf4c82d6c1faffae9fc3f2070de52d11a)
- [scmi_base_device_permission](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__base.html#gacb8772d6c7b59168ab2ae043dc4852f1)
- [scmi_base_reset_agent_cfg](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__base.html#ga161b383297fe35f90d9d25d02f30633d)
- [protocol.h](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2firmware_2scmi_2protocol_8h.html)
- [scmi_agent_info::agent_id](../platform_security_model_reference/P032_scmi_agent_info_结构体.md#a137145e77dd29b54815295d0951a5263)
- [scmi_agent_info::name](../platform_security_model_reference/P032_scmi_agent_info_结构体.md#aed61e021c94d0a5efb05f14daf47077b)
- [scmi_platform_info::sub_vendor_id](../platform_security_model_reference/P045_scmi_platform_info_结构体.md#a050a3fb299aa893da67e32874b565d20)
- [scmi_platform_info::vendor_id](../platform_security_model_reference/P045_scmi_platform_info_结构体.md#a550fb1e5b313df82e7ad54741228abb6)
- [scmi_platform_info::num_protocols](../platform_security_model_reference/P045_scmi_platform_info_结构体.md#aa06c3dd53958c3cbe389f682b5ded16c)
- [scmi_platform_info::num_agents](../platform_security_model_reference/P045_scmi_platform_info_结构体.md#ade42f3a6c6e97bce2695072a39ec21bd)
- [scmi_platform_info::impl_ver](../platform_security_model_reference/P045_scmi_platform_info_结构体.md#ae6327a38864e1247b382a76259562c92)

---

[上一章](P051_bas.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P053_basicmath.h_源码浏览.md)
