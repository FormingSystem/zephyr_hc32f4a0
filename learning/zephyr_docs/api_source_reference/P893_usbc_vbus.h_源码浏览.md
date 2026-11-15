---
id: learning.zephyr-docs.api-source-reference.page-893
title: usbc_vbus.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/usbc__vbus_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第893章\_usbc\_vbus.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/usbc__vbus_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/usbc__vbus_8h.html)。

## 893.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00018"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="l00034"></a>
<a id="l00035"></a>
<a id="l00041"></a>
<a id="foldopen00045"></a>
<a id="l00045"></a>
<a id="l00047"></a>
<a id="l00049"></a>
<a id="l00051"></a>
<a id="l00053"></a>
<a id="l00054"></a>
<a id="l00055"></a>
<a id="l00057"></a>
<a id="foldopen00067"></a>
<a id="l00067"></a>
<a id="l00068"></a>
<a id="l00069"></a>
<a id="l00070"></a>
<a id="l00071"></a>
<a id="foldopen00081"></a>
<a id="l00081"></a>
<a id="l00082"></a>
<a id="l00083"></a>
<a id="l00084"></a>
<a id="l00085"></a>
<a id="foldopen00096"></a>
<a id="l00096"></a>
<a id="l00097"></a>
<a id="l00098"></a>
<a id="l00099"></a>
<a id="l00100"></a>
<a id="foldopen00111"></a>
<a id="l00111"></a>
<a id="l00112"></a>
<a id="l00113"></a>
<a id="l00114"></a>
<a id="l00115"></a>
<a id="l00119"></a>
<a id="l00120"></a>
<a id="l00121"></a>
<a id="l00122"></a>
<a id="l00123"></a>
<a id="l00124"></a>
<a id="adevice_8h_html"></a>
<a id="adevice_8h_html_a9907e8ee5e7be8c3b5d52b13bd33970a"></a>
<a id="agroup__usb__type__c_html_ga015455a6c5620dfc96cfb713bbb72161"></a>
<a id="agroup__usbc__vbus__api_html_ga0b6c561c5f74a30d54397294cb21660d"></a>
<a id="agroup__usbc__vbus__api_html_ga421653274fe9b8e2e6237a4bbe47e3ad"></a>
<a id="agroup__usbc__vbus__api_html_ga7c94eac0f28be6cd12717d2f1a50ec54"></a>
<a id="agroup__usbc__vbus__api_html_ga8414cfcfeee7799ea57854c59c0c1677"></a>
<a id="ainclude_2zephyr_2types_8h_html"></a>
<a id="astdbool_8h_html_abb452686968e48b67397da5f97445f5b"></a>
<a id="astructdevice_html"></a>
<a id="astructusbc__vbus__driver__api_html"></a>
<a id="astructusbc__vbus__driver__api_html_a164ae753995e293460fc408edebe21df"></a>
<a id="astructusbc__vbus__driver__api_html_a373b4435b3e4a1a88a78a15d24bdcbab"></a>
<a id="astructusbc__vbus__driver__api_html_a5a7e6383279dc17c01d478a063efcac0"></a>
<a id="astructusbc__vbus__driver__api_html_adce9dc1f3065a029b53ee954d734cfac"></a>
<a id="ausbc__tc_8h_html"></a>

```c
/*
 * Copyright 2022 The Chromium OS Authors
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DRIVERS_USB_C_USBC_VBUS_H_
#define ZEPHYR_INCLUDE_DRIVERS_USB_C_USBC_VBUS_H_


#include <zephyr/types.h>
#include <zephyr/device.h>
#include <zephyr/drivers/usb_c/usbc_tc.h>

#ifdef __cplusplus
extern "C" {
#endif


__subsystem struct usbc_vbus_driver_api {
        bool (*check_level)(const struct device *dev, enum tc_vbus_level level);
        int (*measure)(const struct device *dev, int *vbus_meas);
        int (*discharge)(const struct device *dev, bool enable);
        int (*enable)(const struct device *dev, bool enable);
};


static inline bool usbc_vbus_check_level(const struct device *dev, enum tc_vbus_level level)
{
        return DEVICE_API_GET(usbc_vbus, dev)->check_level(dev, level);
}

static inline int usbc_vbus_measure(const struct device *dev, int *meas)
{
        return DEVICE_API_GET(usbc_vbus, dev)->measure(dev, meas);
}

static inline int usbc_vbus_discharge(const struct device *dev, bool enable)
{
        return DEVICE_API_GET(usbc_vbus, dev)->discharge(dev, enable);
}

static inline int usbc_vbus_enable(const struct device *dev, bool enable)
{
        return DEVICE_API_GET(usbc_vbus, dev)->enable(dev, enable);
}


#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_DRIVERS_USB_C_USBC_VBUS_H_ */
```

## 893.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：2022 The Chromium OS Authors。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 124 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_USB_C_USBC_VBUS_H_`。

## 893.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/usbc__vbus_8h.html)
- [zephyr/types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)
- [zephyr/device.h](../device_reference/P007_设备模型头文件参考.md)
- [zephyr/drivers/usb_c/usbc_tc.h](https://docs.zephyrproject.org/latest/doxygen/html/usbc__tc_8h.html)
- [usbc_vbus_driver_api](../device_power_control_model_reference/P101_usbc_vbus_driver_api_结构体.md)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)
- [check_level](../device_power_control_model_reference/P101_usbc_vbus_driver_api_结构体.md#adce9dc1f3065a029b53ee954d734cfac)
- [device](../device_reference/P002_设备对象结构.md)
- [tc_vbus_level](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c.html#ga015455a6c5620dfc96cfb713bbb72161)
- [measure](../device_power_control_model_reference/P101_usbc_vbus_driver_api_结构体.md#a373b4435b3e4a1a88a78a15d24bdcbab)
- [discharge](../device_power_control_model_reference/P101_usbc_vbus_driver_api_结构体.md#a164ae753995e293460fc408edebe21df)
- [enable](../device_power_control_model_reference/P101_usbc_vbus_driver_api_结构体.md#a5a7e6383279dc17c01d478a063efcac0)
- [usbc_vbus_check_level](https://docs.zephyrproject.org/latest/doxygen/html/group__usbc__vbus__api.html#ga421653274fe9b8e2e6237a4bbe47e3ad)
- [DEVICE_API_GET](../device_reference/P007_设备模型头文件参考.md#a9907e8ee5e7be8c3b5d52b13bd33970a)
- [usbc_vbus_measure](https://docs.zephyrproject.org/latest/doxygen/html/group__usbc__vbus__api.html#ga0b6c561c5f74a30d54397294cb21660d)
- [usbc_vbus_discharge](https://docs.zephyrproject.org/latest/doxygen/html/group__usbc__vbus__api.html#ga8414cfcfeee7799ea57854c59c0c1677)
- [usbc_vbus_enable](https://docs.zephyrproject.org/latest/doxygen/html/group__usbc__vbus__api.html#ga7c94eac0f28be6cd12717d2f1a50ec54)
- [device.h](../device_reference/P007_设备模型头文件参考.md)
- [types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)
- [usbc_vbus_driver_api::discharge](../device_power_control_model_reference/P101_usbc_vbus_driver_api_结构体.md#a164ae753995e293460fc408edebe21df)
- [usbc_vbus_driver_api::measure](../device_power_control_model_reference/P101_usbc_vbus_driver_api_结构体.md#a373b4435b3e4a1a88a78a15d24bdcbab)
- [usbc_vbus_driver_api::enable](../device_power_control_model_reference/P101_usbc_vbus_driver_api_结构体.md#a5a7e6383279dc17c01d478a063efcac0)
- [usbc_vbus_driver_api::check_level](../device_power_control_model_reference/P101_usbc_vbus_driver_api_结构体.md#adce9dc1f3065a029b53ee954d734cfac)
- [usbc_tc.h](https://docs.zephyrproject.org/latest/doxygen/html/usbc__tc_8h.html)

---

[上一章](P892_usbc_tcpc.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P894_usbd_midi2.h_源码浏览.md)
