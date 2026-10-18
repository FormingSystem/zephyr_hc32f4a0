---
id: learning.zephyr-docs.api-source-configuration-reference.page-100
title: shared_irq.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/shared__irq_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第100章\_shared\_irq.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/shared__irq_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/shared__irq_8h.html)。

## 100.1\_原始可见代码（Source Code）

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
<a id="foldopen00029"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="l00034"></a>
<a id="foldopen00041"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="l00044"></a>
<a id="l00045"></a>
<a id="l00046"></a>
<a id="l00047"></a>
<a id="foldopen00053"></a>
<a id="l00053"></a>
<a id="l00054"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="l00057"></a>
<a id="l00058"></a>
<a id="foldopen00064"></a>
<a id="l00064"></a>
<a id="l00065"></a>
<a id="l00066"></a>
<a id="l00067"></a>
<a id="l00068"></a>
<a id="l00069"></a>
<a id="l00070"></a>
<a id="l00071"></a>
<a id="l00072"></a>
<a id="l00073"></a>
<a id="l00074"></a>
<a id="adevice_8h_html"></a>
<a id="adevice_8h_html_a9907e8ee5e7be8c3b5d52b13bd33970a"></a>
<a id="ashared__irq_8h_html_a0ff7a6ee448eb3e889aa9a7bd63e49bc"></a>
<a id="ashared__irq_8h_html_a22cf2ce082fea27f2087cd1abd74934c"></a>
<a id="ashared__irq_8h_html_a6ef6d536da13ebd8aa75830516dc0696"></a>
<a id="ashared__irq_8h_html_adcdb9702c30ca0911103fc8b9857abb4"></a>
<a id="ashared__irq_8h_html_ae400920b45bedf3da66831597ebca841"></a>
<a id="ashared__irq_8h_html_af36534589858c1e02ea50ed3cc888d41"></a>
<a id="ashared__irq_8h_html_af6d98f7cd2cde7482b7276aa6e0b487c"></a>
<a id="astructdevice_html"></a>
<a id="astructshared__irq__driver__api_html"></a>
<a id="astructshared__irq__driver__api_html_a2e339779ddec773a536f681b9df9997e"></a>
<a id="astructshared__irq__driver__api_html_a5a4ef3888a3d35497c47b67f4511fd5e"></a>
<a id="astructshared__irq__driver__api_html_a8e908b0d6e596905f11a3de1a6f907ad"></a>

```c
/* shared_irq - Shared interrupt driver */

/*
 * Copyright (c) 2015 - 2023 Intel corporation
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_SHARED_IRQ_H_
#define ZEPHYR_INCLUDE_SHARED_IRQ_H_

#include <zephyr/device.h>

#ifdef __cplusplus
extern "C" {
#endif

typedef int (*isr_t)(const struct device *dev, unsigned int irq_number);

/* driver API definition */
typedef int (*shared_irq_register_t)(const struct device *dev,
                                     isr_t isr_func,
                                     const struct device *isr_dev);
typedef int (*shared_irq_enable_t)(const struct device *dev,
                                   const struct device *isr_dev);
typedef int (*shared_irq_disable_t)(const struct device *dev,
                                    const struct device *isr_dev);

__subsystem struct shared_irq_driver_api {
        shared_irq_register_t isr_register;
        shared_irq_enable_t enable;
        shared_irq_disable_t disable;
};

static inline int shared_irq_isr_register(const struct device *dev,
                                          isr_t isr_func,
                                          const struct device *isr_dev)
{
        return DEVICE_API_GET(shared_irq, dev)->isr_register(dev, isr_func, isr_dev);
}

static inline int shared_irq_enable(const struct device *dev,
                                    const struct device *isr_dev)
{
        return DEVICE_API_GET(shared_irq, dev)->enable(dev, isr_dev);
}

static inline int shared_irq_disable(const struct device *dev,
                                     const struct device *isr_dev)
{
        return DEVICE_API_GET(shared_irq, dev)->disable(dev, isr_dev);
}

#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_SHARED_IRQ_H_ */
```

## 100.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

`shared_irq`：共享中断驱动（Shared interrupt driver）。

### 注释 2：原第 3 行

版权（Copyright）：© 2015 - 2023 Intel corporation。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 3：原第 20 行

驱动 API 定义（Driver API definition）。

### 注释 4：原第 74 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_SHARED_IRQ_H_`。

## 100.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/shared__irq_8h.html)
- [zephyr/device.h](../device_reference/P007_设备模型头文件参考.md)
- [isr_t](https://docs.zephyrproject.org/latest/doxygen/html/shared__irq_8h.html#af6d98f7cd2cde7482b7276aa6e0b487c)
- [device](../device_reference/P002_设备对象结构.md)
- [shared_irq_register_t](https://docs.zephyrproject.org/latest/doxygen/html/shared__irq_8h.html#ae400920b45bedf3da66831597ebca841)
- [shared_irq_enable_t](https://docs.zephyrproject.org/latest/doxygen/html/shared__irq_8h.html#a0ff7a6ee448eb3e889aa9a7bd63e49bc)
- [shared_irq_disable_t](https://docs.zephyrproject.org/latest/doxygen/html/shared__irq_8h.html#a22cf2ce082fea27f2087cd1abd74934c)
- [shared_irq_driver_api](../platform_security_model_reference/P054_shared_irq_driver_api_结构体.md)
- [isr_register](../platform_security_model_reference/P054_shared_irq_driver_api_结构体.md#a8e908b0d6e596905f11a3de1a6f907ad)
- [enable](../platform_security_model_reference/P054_shared_irq_driver_api_结构体.md#a5a4ef3888a3d35497c47b67f4511fd5e)
- [disable](../platform_security_model_reference/P054_shared_irq_driver_api_结构体.md#a2e339779ddec773a536f681b9df9997e)
- [shared_irq_isr_register](https://docs.zephyrproject.org/latest/doxygen/html/shared__irq_8h.html#a6ef6d536da13ebd8aa75830516dc0696)
- [DEVICE_API_GET](../device_reference/P007_设备模型头文件参考.md#a9907e8ee5e7be8c3b5d52b13bd33970a)
- [shared_irq_enable](https://docs.zephyrproject.org/latest/doxygen/html/shared__irq_8h.html#af36534589858c1e02ea50ed3cc888d41)
- [shared_irq_disable](https://docs.zephyrproject.org/latest/doxygen/html/shared__irq_8h.html#adcdb9702c30ca0911103fc8b9857abb4)
- [device.h](../device_reference/P007_设备模型头文件参考.md)
- [shared_irq_driver_api::disable](../platform_security_model_reference/P054_shared_irq_driver_api_结构体.md#a2e339779ddec773a536f681b9df9997e)
- [shared_irq_driver_api::enable](../platform_security_model_reference/P054_shared_irq_driver_api_结构体.md#a5a4ef3888a3d35497c47b67f4511fd5e)
- [shared_irq_driver_api::isr_register](../platform_security_model_reference/P054_shared_irq_driver_api_结构体.md#a8e908b0d6e596905f11a3de1a6f907ad)

---

[上一章](P099_service.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P101_silabs-acmp.h_源码浏览.md)
