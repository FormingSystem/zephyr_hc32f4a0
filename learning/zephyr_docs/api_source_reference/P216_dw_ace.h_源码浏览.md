---
id: learning.zephyr-docs.api-source-reference.page-216
title: dw_ace.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/dw__ace_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第216章\_dw\_ace.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/dw__ace_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/dw__ace_8h.html)。

## 216.1\_原始可见代码（Source Code）

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
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00018"></a>
<a id="foldopen00019"></a>
<a id="l00019"></a>
<a id="l00020"></a>
<a id="l00021"></a>
<a id="l00022"></a>
<a id="l00023"></a>
<a id="l00024"></a>
<a id="l00025"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="adevice_8h_html"></a>
<a id="adw__ace_8h_html_a1e71aa00761ed1a478f92de8a1342564"></a>
<a id="adw__ace_8h_html_a5b6d1259c32080069df86d5e4fd506cb"></a>
<a id="adw__ace_8h_html_a99f66a0736502ea18deb13e0a5d9958e"></a>
<a id="adw__ace_8h_html_af94ebd4f440b084d94d42eed62e159cc"></a>
<a id="aparser_8h_html_ab6b306ef981f5e21bb41ea2c2dbe8cd9"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astructdevice_html"></a>
<a id="astructdw__ace__v1__ictl__driver__api_html"></a>
<a id="astructdw__ace__v1__ictl__driver__api_html_a549b3e3c36f4bd632ab52ec4eee5fd80"></a>
<a id="astructdw__ace__v1__ictl__driver__api_html_aa7984ba6960a07a33ae0746717bc45ac"></a>
<a id="astructdw__ace__v1__ictl__driver__api_html_ac2bbb8a07be14882b6763e58bf79be43"></a>

```c
/*
 * Copyright (c) 2022 Intel Corporation
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DRIVERS_INTERRUPT_CONTROLLER_DW_ACE_H_
#define ZEPHYR_INCLUDE_DRIVERS_INTERRUPT_CONTROLLER_DW_ACE_H_

#include <zephyr/device.h>

typedef void (*irq_enable_t)(const struct device *dev, uint32_t irq);
typedef void (*irq_disable_t)(const struct device *dev, uint32_t irq);
typedef int (*irq_is_enabled_t)(const struct device *dev, unsigned int irq);
typedef int (*irq_connect_dynamic_t)(const struct device *dev,
                                     unsigned int irq, unsigned int priority,
                                     void (*routine)(const void *parameter),
                                     const void *parameter, uint32_t flags);

struct dw_ace_v1_ictl_driver_api {
        irq_enable_t intr_enable;
        irq_disable_t intr_disable;
        irq_is_enabled_t intr_is_enabled;
#ifdef CONFIG_DYNAMIC_INTERRUPTS
        irq_connect_dynamic_t intr_connect_dynamic;
#endif
};

#endif /* ZEPHYR_INCLUDE_DRIVERS_INTERRUPT_CONTROLLER_DW_ACE_H_ */
```

## 216.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2022 Intel Corporation。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 28 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_INTERRUPT_CONTROLLER_DW_ACE_H_`。

## 216.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/dw__ace_8h.html)
- [zephyr/device.h](../device_reference/P007_设备模型头文件参考.md)
- [irq_enable_t](https://docs.zephyrproject.org/latest/doxygen/html/dw__ace_8h.html#a99f66a0736502ea18deb13e0a5d9958e)
- [device](../device_reference/P002_设备对象结构.md)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [irq_disable_t](https://docs.zephyrproject.org/latest/doxygen/html/dw__ace_8h.html#a1e71aa00761ed1a478f92de8a1342564)
- [irq_is_enabled_t](https://docs.zephyrproject.org/latest/doxygen/html/dw__ace_8h.html#af94ebd4f440b084d94d42eed62e159cc)
- [irq_connect_dynamic_t](https://docs.zephyrproject.org/latest/doxygen/html/dw__ace_8h.html#a5b6d1259c32080069df86d5e4fd506cb)
- [flags](https://docs.zephyrproject.org/latest/doxygen/html/parser_8h.html#ab6b306ef981f5e21bb41ea2c2dbe8cd9)
- [dw_ace_v1_ictl_driver_api](../platform_security_model_reference/P002_dw_ace_v1_ictl_driver_api_结构体.md)
- [intr_enable](../platform_security_model_reference/P002_dw_ace_v1_ictl_driver_api_结构体.md#aa7984ba6960a07a33ae0746717bc45ac)
- [intr_disable](../platform_security_model_reference/P002_dw_ace_v1_ictl_driver_api_结构体.md#a549b3e3c36f4bd632ab52ec4eee5fd80)
- [intr_is_enabled](../platform_security_model_reference/P002_dw_ace_v1_ictl_driver_api_结构体.md#ac2bbb8a07be14882b6763e58bf79be43)
- [device.h](../device_reference/P007_设备模型头文件参考.md)
- [dw_ace_v1_ictl_driver_api::intr_disable](../platform_security_model_reference/P002_dw_ace_v1_ictl_driver_api_结构体.md#a549b3e3c36f4bd632ab52ec4eee5fd80)
- [dw_ace_v1_ictl_driver_api::intr_enable](../platform_security_model_reference/P002_dw_ace_v1_ictl_driver_api_结构体.md#aa7984ba6960a07a33ae0746717bc45ac)
- [dw_ace_v1_ictl_driver_api::intr_is_enabled](../platform_security_model_reference/P002_dw_ace_v1_ictl_driver_api_结构体.md#ac2bbb8a07be14882b6763e58bf79be43)

---

[上一章](P215_dvp-20pin-connector.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P217_ead.h_源码浏览.md)
