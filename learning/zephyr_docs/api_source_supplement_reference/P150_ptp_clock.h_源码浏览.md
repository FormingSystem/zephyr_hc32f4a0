---
id: learning.zephyr-docs.api-source-supplement-reference.page-150
title: ptp_clock.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/ptp__clock_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第150章\_ptp\_clock.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/ptp__clock_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/ptp__clock_8h.html)。

## 150.1\_原始可见代码（Source Code）

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
<a id="l00044"></a>
<a id="l00049"></a>
<a id="l00050"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="l00061"></a>
<a id="l00062"></a>
<a id="l00067"></a>
<a id="l00068"></a>
<a id="foldopen00072"></a>
<a id="l00072"></a>
<a id="l00076"></a>
<a id="l00080"></a>
<a id="l00084"></a>
<a id="l00088"></a>
<a id="l00089"></a>
<a id="l00090"></a>
<a id="l00092"></a>
<a id="foldopen00101"></a>
<a id="l00101"></a>
<a id="l00102"></a>
<a id="l00103"></a>
<a id="l00104"></a>
<a id="l00105"></a>
<a id="l00106"></a>
<a id="l00115"></a>
<a id="l00116"></a>
<a id="l00117"></a>
<a id="l00118"></a>
<a id="l00119"></a>
<a id="l00120"></a>
<a id="l00121"></a>
<a id="l00122"></a>
<a id="foldopen00131"></a>
<a id="l00131"></a>
<a id="l00132"></a>
<a id="l00133"></a>
<a id="l00134"></a>
<a id="l00135"></a>
<a id="foldopen00144"></a>
<a id="l00144"></a>
<a id="l00145"></a>
<a id="l00146"></a>
<a id="l00147"></a>
<a id="l00148"></a>
<a id="l00149"></a>
<a id="l00150"></a>
<a id="l00151"></a>
<a id="l00152"></a>
<a id="l00153"></a>
<a id="l00154"></a>
<a id="l00158"></a>
<a id="l00159"></a>
<a id="adevice_8h_html"></a>
<a id="adevice_8h_html_a9907e8ee5e7be8c3b5d52b13bd33970a"></a>
<a id="agroup__ptp__clock__interface__backend_html_ga59a1c7530e59fd19b3fa25ff6f4e346c"></a>
<a id="agroup__ptp__clock__interface__backend_html_gad3b345ba7db470f274cffa33b1128810"></a>
<a id="agroup__ptp__clock__interface__backend_html_gae94ee94813969d15f8dc841814562ac3"></a>
<a id="agroup__ptp__clock__interface__backend_html_gaeda56e624ddc47b5f23ebd090031982a"></a>
<a id="agroup__ptp__clock__interface_html_ga310ee4974e6f3b01c4aa1b985194e57a"></a>
<a id="agroup__ptp__clock__interface_html_ga41123183be722b3423d5e993d3cde7c2"></a>
<a id="agroup__ptp__clock__interface_html_ga443f97ef2766e87c0b42c6ad6f7b63b4"></a>
<a id="agroup__ptp__clock__interface_html_gabd11d19b5ec5491e5813bf7cb74ab9b0"></a>
<a id="akernel_8h_html"></a>
<a id="aptp__time_8h_html"></a>
<a id="astdint_8h_html"></a>
<a id="astructdevice_html"></a>
<a id="astructnet__ptp__time_html"></a>
<a id="astructptp__clock__driver__api_html"></a>
<a id="astructptp__clock__driver__api_html_a9ef8a7a3ece8012c12fcb4510fa20e71"></a>
<a id="astructptp__clock__driver__api_html_aaf9ba9cb7af6c77a0cf53e2c576f7106"></a>
<a id="astructptp__clock__driver__api_html_aef67c906d97a1b9453ffd5d0e35d44c9"></a>
<a id="astructptp__clock__driver__api_html_af0bb3479e2b165500cbe602bd71e9e84"></a>
<a id="astructtm_html"></a>
<a id="asys_2util_8h_html"></a>

```c
/*
 * Copyright (c) 2018 Intel Corporation.
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DRIVERS_PTP_CLOCK_H_
#define ZEPHYR_INCLUDE_DRIVERS_PTP_CLOCK_H_


#include <zephyr/kernel.h>
#include <stdint.h>
#include <zephyr/device.h>
#include <zephyr/sys/util.h>
#include <zephyr/net/ptp_time.h>

#ifdef __cplusplus
extern "C" {
#endif

/* Name of the PTP clock driver */
#if !defined(PTP_CLOCK_NAME)
#define PTP_CLOCK_NAME "PTP_CLOCK"
#endif


typedef int (*ptp_clock_api_set_t)(const struct device *dev, struct net_ptp_time *tm);

typedef int (*ptp_clock_api_get_t)(const struct device *dev, struct net_ptp_time *tm);

typedef int (*ptp_clock_api_adjust_t)(const struct device *dev, int increment);

typedef int (*ptp_clock_api_rate_adjust_t)(const struct device *dev, double ratio);

__subsystem struct ptp_clock_driver_api {
        ptp_clock_api_set_t set;
        ptp_clock_api_get_t get;
        ptp_clock_api_adjust_t adjust;
        ptp_clock_api_rate_adjust_t rate_adjust;
};


static inline int ptp_clock_set(const struct device *dev,
                                struct net_ptp_time *tm)
{
        return DEVICE_API_GET(ptp_clock, dev)->set(dev, tm);
}

__syscall int ptp_clock_get(const struct device *dev, struct net_ptp_time *tm);

static inline int z_impl_ptp_clock_get(const struct device *dev,
                                       struct net_ptp_time *tm)
{
        return DEVICE_API_GET(ptp_clock, dev)->get(dev, tm);
}

static inline int ptp_clock_adjust(const struct device *dev, int increment)
{
        return DEVICE_API_GET(ptp_clock, dev)->adjust(dev, increment);
}

static inline int ptp_clock_rate_adjust(const struct device *dev, double rate)
{
        return DEVICE_API_GET(ptp_clock, dev)->rate_adjust(dev, rate);
}

#ifdef __cplusplus
}
#endif

#include <zephyr/syscalls/ptp_clock.h>


#endif /* ZEPHYR_INCLUDE_DRIVERS_PTP_CLOCK_H_ */
```

## 150.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2018 Intel Corporation.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 35 行

精确时间协议（PTP）时钟驱动的名称。

### 注释 3：原第 159 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_PTP_CLOCK_H_`。

## 150.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/ptp__clock_8h.html)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html)
- [zephyr/device.h](../device_reference/P007_设备模型头文件参考.md)
- [zephyr/sys/util.h](../util_reference/P002_通用工具头文件参考.md)
- [zephyr/net/ptp_time.h](https://docs.zephyrproject.org/latest/doxygen/html/ptp__time_8h.html)
- [ptp_clock_api_set_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ptp__clock__interface__backend.html#gaeda56e624ddc47b5f23ebd090031982a)
- [device](../device_reference/P002_设备对象结构.md)
- [net_ptp_time](../network_core_model_reference/P116_net_ptp_time_结构体.md)
- [tm](../posix_system_model_reference/P025_tm_结构体.md)
- [ptp_clock_api_get_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ptp__clock__interface__backend.html#ga59a1c7530e59fd19b3fa25ff6f4e346c)
- [ptp_clock_api_adjust_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ptp__clock__interface__backend.html#gad3b345ba7db470f274cffa33b1128810)
- [ptp_clock_api_rate_adjust_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ptp__clock__interface__backend.html#gae94ee94813969d15f8dc841814562ac3)
- [ptp_clock_driver_api](../network_service_model_reference/P054_ptp_clock_driver_api_结构体.md)
- [set](../network_service_model_reference/P054_ptp_clock_driver_api_结构体.md#a9ef8a7a3ece8012c12fcb4510fa20e71)
- [get](../network_service_model_reference/P054_ptp_clock_driver_api_结构体.md#aaf9ba9cb7af6c77a0cf53e2c576f7106)
- [adjust](../network_service_model_reference/P054_ptp_clock_driver_api_结构体.md#af0bb3479e2b165500cbe602bd71e9e84)
- [rate_adjust](../network_service_model_reference/P054_ptp_clock_driver_api_结构体.md#aef67c906d97a1b9453ffd5d0e35d44c9)
- [ptp_clock_set](https://docs.zephyrproject.org/latest/doxygen/html/group__ptp__clock__interface.html#ga41123183be722b3423d5e993d3cde7c2)
- [DEVICE_API_GET](../device_reference/P007_设备模型头文件参考.md#a9907e8ee5e7be8c3b5d52b13bd33970a)
- [ptp_clock_get](https://docs.zephyrproject.org/latest/doxygen/html/group__ptp__clock__interface.html#ga443f97ef2766e87c0b42c6ad6f7b63b4)
- [ptp_clock_adjust](https://docs.zephyrproject.org/latest/doxygen/html/group__ptp__clock__interface.html#gabd11d19b5ec5491e5813bf7cb74ab9b0)
- [ptp_clock_rate_adjust](https://docs.zephyrproject.org/latest/doxygen/html/group__ptp__clock__interface.html#ga310ee4974e6f3b01c4aa1b985194e57a)
- [device.h](../device_reference/P007_设备模型头文件参考.md)
- [kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [ptp_time.h](https://docs.zephyrproject.org/latest/doxygen/html/ptp__time_8h.html)
- [ptp_clock_driver_api::set](../network_service_model_reference/P054_ptp_clock_driver_api_结构体.md#a9ef8a7a3ece8012c12fcb4510fa20e71)
- [ptp_clock_driver_api::get](../network_service_model_reference/P054_ptp_clock_driver_api_结构体.md#aaf9ba9cb7af6c77a0cf53e2c576f7106)
- [ptp_clock_driver_api::rate_adjust](../network_service_model_reference/P054_ptp_clock_driver_api_结构体.md#aef67c906d97a1b9453ffd5d0e35d44c9)
- [ptp_clock_driver_api::adjust](../network_service_model_reference/P054_ptp_clock_driver_api_结构体.md#af0bb3479e2b165500cbe602bd71e9e84)
- [util.h](../util_reference/P002_通用工具头文件参考.md)

---

[上一章](P149_pstate.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P151_pwm_ifx_tcpwm.h_源码浏览.md)
