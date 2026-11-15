---
id: learning.zephyr-docs.api-source-supplement-reference.page-152
title: qdec_nxp_tpm.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/qdec__nxp__tpm_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第152章\_qdec\_nxp\_tpm.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/qdec__nxp__tpm_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/qdec__nxp__tpm_8h.html)。

## 152.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00008"></a>
<a id="l00009"></a>
<a id="l00010"></a>
<a id="l00011"></a>
<a id="l00012"></a>
<a id="foldopen00013"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00018"></a>
<a id="agroup__sensor__interface_html_gga0dcb6842bc969492bd1c9eb49708940bafb4b5859bc369f817f60eaa161bcefc3"></a>
<a id="agroup__sensor__qdec__mcux_html_gga93f4f84af3e5a42381e9152750c46286adeea574ce5fbed87ca34dc26860428b2"></a>
<a id="aqdec__nxp__tpm_8h_html_adab9169b39efa0b7ecbe1f5ae9c69830"></a>
<a id="asensor_8h_html"></a>

```c
/*
 * Copyright (c) 2022, Prevas A/S
 * Copyright (c) 2025 NXP
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DRIVERS_SENSOR_QDEC_NXP_TPM_H_
#define ZEPHYR_INCLUDE_DRIVERS_SENSOR_QDEC_NXP_TPM_H_

#include <zephyr/drivers/sensor.h>

enum sensor_attribute_qdec_tpm {
        /* Number of counts per revolution */
        SENSOR_ATTR_QDEC_MOD_VAL = SENSOR_ATTR_PRIV_START,
};

#endif /* ZEPHYR_INCLUDE_DRIVERS_SENSOR_QDEC_NXP_TPM_H_ */
```

## 152.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2022, Prevas A/S。

版权（Copyright）：© 2025 NXP。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 14 行

每转计数（Counts per revolution）。

### 注释 3：原第 18 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_SENSOR_QDEC_NXP_TPM_H_`。

## 152.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/qdec__nxp__tpm_8h.html)
- [zephyr/drivers/sensor.h](https://docs.zephyrproject.org/latest/doxygen/html/sensor_8h.html)
- [sensor_attribute_qdec_tpm](https://docs.zephyrproject.org/latest/doxygen/html/qdec__nxp__tpm_8h.html#adab9169b39efa0b7ecbe1f5ae9c69830)
- [SENSOR_ATTR_QDEC_MOD_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__qdec__mcux.html#gga93f4f84af3e5a42381e9152750c46286adeea574ce5fbed87ca34dc26860428b2)
- [SENSOR_ATTR_PRIV_START](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gga0dcb6842bc969492bd1c9eb49708940bafb4b5859bc369f817f60eaa161bcefc3)
- [sensor.h](https://docs.zephyrproject.org/latest/doxygen/html/sensor_8h.html)

---

[上一章](P151_pwm_ifx_tcpwm.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P153_r8a779f0_cpg_mssr.h_源码浏览.md)
