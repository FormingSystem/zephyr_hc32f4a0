---
id: learning.zephyr-docs.api-source-reference.page-669
title: power.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/power_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第669章\_power.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/power_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/power_8h.html)。

## 669.1\_原始可见代码（Source Code）

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
<a id="l00035"></a>
<a id="l00037"></a>
<a id="l00038"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="foldopen00048"></a>
<a id="l00048"></a>
<a id="l00049"></a>
<a id="l00050"></a>
<a id="l00051"></a>
<a id="l00053"></a>
<a id="l00058"></a>
<a id="l00060"></a>
<a id="l00061"></a>
<a id="l00063"></a>
<a id="l00064"></a>
<a id="l00066"></a>
<a id="foldopen00073"></a>
<a id="l00073"></a>
<a id="l00075"></a>
<a id="l00077"></a>
<a id="l00079"></a>
<a id="l00080"></a>
<a id="l00081"></a>
<a id="l00089"></a>
<a id="l00098"></a>
<a id="l00099"></a>
<a id="l00103"></a>
<a id="l00104"></a>
<a id="adrivers_2firmware_2scmi_2protocol_8h_html"></a>
<a id="agroup__scmi__power_html_ga0969968c4d6b94868295172c0408031b"></a>
<a id="agroup__scmi__power_html_gadc7a2fbf0c4cab570d3a567ce548c947"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astructscmi__power__state__config_html"></a>
<a id="astructscmi__power__state__config_html_a742409967c5487aecbccf89347dd7ae4"></a>
<a id="astructscmi__power__state__config_html_a83743ab1270c319ab62148e2cf89741f"></a>
<a id="astructscmi__power__state__config_html_ae246faf5674e4d885d84e8ee782cccae"></a>

```c
/*
 * Copyright 2024 NXP
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DRIVERS_FIRMWARE_SCMI_POWER_H_
#define ZEPHYR_INCLUDE_DRIVERS_FIRMWARE_SCMI_POWER_H_

#include <zephyr/drivers/firmware/scmi/protocol.h>


#define SCMI_POWER_STATE_SET_FLAGS_ASYNC BIT(0)

#define SCMI_POWER_DOMAIN_PROTOCOL_SUPPORTED_VERSION    0x30001


#define SCMI_POWER_STATE_TYPE_SHIFT     30U

#define SCMI_POWER_STATE_ID_MASK        (BIT(28) - 1)

#define SCMI_POWER_STATE_PARAM(type, id) \
        ((((type) & BIT(0)) << SCMI_POWER_STATE_TYPE_SHIFT) | \
         ((id) & SCMI_POWER_STATE_ID_MASK))



#define SCMI_POWER_STATE_GENERIC_ON     SCMI_POWER_STATE_PARAM(0, 0)

#define SCMI_POWER_STATE_GENERIC_OFF    SCMI_POWER_STATE_PARAM(1, 0)


struct scmi_power_state_config {
        uint32_t flags;
        uint32_t domain_id;
        uint32_t power_state;
};

int scmi_power_state_set(struct scmi_power_state_config *cfg);
int scmi_power_state_get(uint32_t domain_id, uint32_t *power_state);


#endif /* ZEPHYR_INCLUDE_DRIVERS_FIRMWARE_SCMI_POWER_H_ */
```

## 669.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：2024 NXP。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 104 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_FIRMWARE_SCMI_POWER_H_`。

## 669.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/power_8h.html)
- [zephyr/drivers/firmware/scmi/protocol.h](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2firmware_2scmi_2protocol_8h.html)
- [scmi_power_state_config](../platform_security_model_reference/P046_scmi_power_state_config_结构体.md)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [flags](../platform_security_model_reference/P046_scmi_power_state_config_结构体.md#a83743ab1270c319ab62148e2cf89741f)
- [domain_id](../platform_security_model_reference/P046_scmi_power_state_config_结构体.md#ae246faf5674e4d885d84e8ee782cccae)
- [power_state](../platform_security_model_reference/P046_scmi_power_state_config_结构体.md#a742409967c5487aecbccf89347dd7ae4)
- [scmi_power_state_set](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__power.html#ga0969968c4d6b94868295172c0408031b)
- [scmi_power_state_get](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__power.html#gadc7a2fbf0c4cab570d3a567ce548c947)
- [protocol.h](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2firmware_2scmi_2protocol_8h.html)
- [scmi_power_state_config::power_state](../platform_security_model_reference/P046_scmi_power_state_config_结构体.md#a742409967c5487aecbccf89347dd7ae4)
- [scmi_power_state_config::flags](../platform_security_model_reference/P046_scmi_power_state_config_结构体.md#a83743ab1270c319ab62148e2cf89741f)
- [scmi_power_state_config::domain_id](../platform_security_model_reference/P046_scmi_power_state_config_结构体.md#ae246faf5674e4d885d84e8ee782cccae)

---

[上一章](P668_posix_arch_console.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P670_print_format.h_源码浏览.md)
