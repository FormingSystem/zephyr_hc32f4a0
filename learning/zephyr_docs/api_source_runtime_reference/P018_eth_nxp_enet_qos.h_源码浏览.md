---
id: learning.zephyr-docs.api-source-runtime-reference.page-18
title: eth_nxp_enet_qos.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/eth__nxp__enet__qos_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第18章\_eth\_nxp\_enet\_qos.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/eth__nxp__enet__qos_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/eth__nxp__enet__qos_8h.html)。

## 18.1\_原始可见代码（Source Code）

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
<a id="l00020"></a>
<a id="l00021"></a>
<a id="l00022"></a>
<a id="l00023"></a>
<a id="l00024"></a>
<a id="l00025"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="l00034"></a>
<a id="l00035"></a>
<a id="l00036"></a>
<a id="l00037"></a>
<a id="l00038"></a>
<a id="l00039"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="l00044"></a>
<a id="l00045"></a>
<a id="l00046"></a>
<a id="l00047"></a>
<a id="l00048"></a>
<a id="l00049"></a>
<a id="l00050"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="l00054"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="l00057"></a>
<a id="l00058"></a>
<a id="l00059"></a>
<a id="l00060"></a>
<a id="l00061"></a>
<a id="l00063"></a>
<a id="l00064"></a>
<a id="aclock__control_8h_html"></a>
<a id="agroup__clock__control__interface_html_gaa7d3935eaaf18902801a7d94859483db"></a>

```c
/*
 * Copyright 2023-2026 NXP
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DRIVERS_ETH_NXP_ENET_QOS_H__
#define ZEPHYR_INCLUDE_DRIVERS_ETH_NXP_ENET_QOS_H__

#include <fsl_device_registers.h>
#include <zephyr/drivers/clock_control.h>


/* Different platforms named the peripheral different in the register definitions */
#if defined(CONFIG_SOC_FAMILY_MCXN) || defined(CONFIG_SOC_FAMILY_MCXA)
#undef ENET
#define ENET_QOS_NAME ENET
#define ENET_QOS_ALIGNMENT 4
typedef ENET_Type enet_qos_t;
#else
#error "ENET_QOS not enabled on this SOC series"
#endif

#define _PREFIX_UNDERLINE(x) _##x
#define _ENET_QOS_REG_FIELD(reg, field) MACRO_MAP_CAT(_PREFIX_UNDERLINE, reg, field, MASK)
#define _ENET_QOS_REG_MASK(reg, field) CONCAT(ENET_QOS_NAME, _ENET_QOS_REG_FIELD(reg, field))

/* Deciphers value of a field from a read value of an enet qos register
 *
 * reg: name of the register
 * field: name of the bit field within the register
 * val: value that had been read from the register
 */
#define ENET_QOS_REG_GET(reg, field, val) FIELD_GET(_ENET_QOS_REG_MASK(reg, field), val)

/* Prepares value of a field for a write to an enet qos register
 *
 * reg: name of the register
 * field: name of the bit field within the register
 * val: value to put into the field
 */
#define ENET_QOS_REG_PREP(reg, field, val) FIELD_PREP(_ENET_QOS_REG_MASK(reg, field), val)


#define ENET_QOS_ALIGN_ADDR_SHIFT(x) (x >> (ENET_QOS_ALIGNMENT >> 1))

struct nxp_enet_qos_config {
        const struct pinctrl_dev_config *pincfg;
        const struct device *clock_dev;
        clock_control_subsys_t clock_subsys;
        enet_qos_t *base;
};
#define ENET_QOS_MODULE_CFG(module_dev) ((struct nxp_enet_qos_config *) module_dev->config)


#endif /* ZEPHYR_INCLUDE_DRIVERS_ETH_NXP_ENET_H__ */
```

## 18.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：2023-2026 NXP。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 21 行

不同平台在寄存器定义中对该外设采用不同名称。

### 注释 3：原第 35 行

从读取到的 ENET QoS 寄存器值中解析某字段的值。

- `reg`：寄存器名称。
- `field`：寄存器中的位域名称。
- `val`：从寄存器读取的值。

### 注释 4：原第 43 行

准备写入 ENET QoS 寄存器的某字段值。

- `reg`：寄存器名称。
- `field`：寄存器中的位域名称。
- `val`：要放入该字段的值。

### 注释 5：原第 64 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_ETH_NXP_ENET_H__`。

## 18.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/eth__nxp__enet__qos_8h.html)
- [zephyr/drivers/clock_control.h](../timer_reference/P095_时钟控制头文件参考.md)
- [clock_control_subsys_t](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__interface.html#gaa7d3935eaaf18902801a7d94859483db)
- [clock_control.h](../timer_reference/P095_时钟控制头文件参考.md)

---

[上一章](P017_esp32-touch-sensor-input.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P019_fcb.h_源码浏览.md)
