---
id: learning.zephyr-docs.api-source-reference.page-508
title: mctp_i3c_endpoint.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/mctp__i3c__endpoint_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第508章\_mctp\_i3c\_endpoint.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/mctp__i3c__endpoint_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/mctp__i3c__endpoint_8h.html)。

## 508.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00018"></a>
<a id="l00019"></a>
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
<a id="l00045"></a>
<a id="l00046"></a>
<a id="adevice_8h_html"></a>
<a id="ai3c_8h_html"></a>
<a id="aposix_2sys_2socket_8h_html_a05b4e957a092db3e68281988ceb32df8"></a>
<a id="astructdevice_html"></a>
<a id="astructdevice_html_a4a2e6a2cfeb6efed7d5383c33458f46d"></a>
<a id="astructi3c__device__desc_html"></a>
<a id="astructmctp__binding__i3c__controller_html"></a>

```c
/*
 * Copyright (c) 2025 Intel Corporation
 *
 * SPDX-License-Identifier: Apache-2.0
 *
 */


#ifndef ZEPHYR_INCLUDE_PMCI_MCTP_MCTP_I3C_ENDPOINT_H_
#define ZEPHYR_INCLUDE_PMCI_MCTP_MCTP_I3C_ENDPOINT_H_

#include <zephyr/device.h>
#include <zephyr/drivers/i3c.h>

struct mctp_binding_i3c_controller;

struct mctp_i3c_endpoint_api {
        void (*bind)(const struct device *dev, struct mctp_binding_i3c_controller *ctlr,
                    struct i3c_device_desc **i3c_dev);
        struct mctp_binding_i3c_controller *(*binding)(const struct device *dev);
};

static inline void mctp_i3c_endpoint_bind(const struct device *dev,
                                          struct mctp_binding_i3c_controller *ctlr,
                                          struct i3c_device_desc **i3c_dev)
{
        const struct mctp_i3c_endpoint_api *api = dev->api;

        api->bind(dev, ctlr, i3c_dev);
}

static inline struct mctp_binding_i3c_controller *mctp_i3c_endpoint_binding(const struct device *d)
{
        const struct mctp_i3c_endpoint_api *api = d->api;

        return api->binding(d);
}

#endif /* ZEPHYR_INCLUDE_PMCI_MCTP_MCTP_I3C_ENDPOINT_H_ */
```

## 508.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2025 Intel Corporation。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 46 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_PMCI_MCTP_MCTP_I3C_ENDPOINT_H_`。

## 508.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/mctp__i3c__endpoint_8h.html)
- [zephyr/device.h](../device_reference/P007_设备模型头文件参考.md)
- [zephyr/drivers/i3c.h](https://docs.zephyrproject.org/latest/doxygen/html/i3c_8h.html)
- [mctp_binding_i3c_controller](../peripheral_bus_storage_model_reference/P028_mctp_binding_i3c_controller_结构体.md)
- [bind](https://docs.zephyrproject.org/latest/doxygen/html/posix_2sys_2socket_8h.html#a05b4e957a092db3e68281988ceb32df8)
- [device](../device_reference/P002_设备对象结构.md)
- [i3c_device_desc](../hardware/P401_I3C设备描述符.md)
- [api](../device_reference/P002_设备对象结构.md#a4a2e6a2cfeb6efed7d5383c33458f46d)
- [device.h](../device_reference/P007_设备模型头文件参考.md)
- [i3c.h](https://docs.zephyrproject.org/latest/doxygen/html/i3c_8h.html)
- [device::api](../device_reference/P002_设备对象结构.md#a4a2e6a2cfeb6efed7d5383c33458f46d)

---

[上一章](P507_mchp_xec_pcr.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P509_mctp_i3c_pec.h_源码浏览.md)
