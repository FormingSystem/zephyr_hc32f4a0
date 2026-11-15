---
id: learning.zephyr-docs.api-file-interface-reference.page-62
title: zephyr__drivers__usb_c__usbc_vbus.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/usbc__vbus_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第62章\_zephyr\_\_drivers\_\_usb\_c\_\_usbc\_vbus.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/usbc__vbus_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

USB-C VBUS的设备API。

<a id="details"></a>

```c
#include <zephyr/types.h>
#include <zephyr/device.h>
#include <zephyr/drivers/usb_c/usbc_tc.h>
```

查看此文件的源码。

USB-C VBUS 设备 API。本文件包含 USB-C VBUS 设备 API。所有 USB-C VBUS 测量与控制设备驱动程序均应实现本文件描述的 API。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 62.1\_数据结构（Data Structures）

<a id="r_usbc_5Fvbus_5Fdriver_5Fapi"></a>

```c
struct usbc_vbus_driver_api
```

相关声明：[usbc_vbus_driver_api](../device_power_control_model_reference/P101_usbc_vbus_driver_api_结构体.md)。

驱动操作（Driver Operations）：USB-C VBUS驱动操作。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 62.2\_函数（Functions）

<a id="r_ga421653274fe9b8e2e6237a4bbe47e3ad"></a>

```c
static bool usbc_vbus_check_level (const struct device *dev, enum tc_vbus_level level)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[usbc_vbus_check_level](https://docs.zephyrproject.org/latest/doxygen/html/group__usbc__vbus__api.html#ga421653274fe9b8e2e6237a4bbe47e3ad)、[device](../device_reference/P002_设备对象结构.md)、[tc_vbus_level](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c.html#ga015455a6c5620dfc96cfb713bbb72161)。

检查 VBUS 是否处于特定电平（level）。

<a id="r_ga0b6c561c5f74a30d54397294cb21660d"></a>

```c
static int usbc_vbus_measure (const struct device *dev, int *meas)
```

相关声明：[usbc_vbus_measure](https://docs.zephyrproject.org/latest/doxygen/html/group__usbc__vbus__api.html#ga0b6c561c5f74a30d54397294cb21660d)、[device](../device_reference/P002_设备对象结构.md)。

读取并返回 VBUS 电压，单位为 mV。

<a id="r_ga8414cfcfeee7799ea57854c59c0c1677"></a>

```c
static int usbc_vbus_discharge (const struct device *dev, bool enable)
```

相关声明：[usbc_vbus_discharge](https://docs.zephyrproject.org/latest/doxygen/html/group__usbc__vbus__api.html#ga8414cfcfeee7799ea57854c59c0c1677)、[device](../device_reference/P002_设备对象结构.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

控制用于对 VBUS 放电（discharge）的引脚。

<a id="r_ga7c94eac0f28be6cd12717d2f1a50ec54"></a>

```c
static int usbc_vbus_enable (const struct device *dev, bool enable)
```

相关声明：[usbc_vbus_enable](https://docs.zephyrproject.org/latest/doxygen/html/group__usbc__vbus__api.html#ga7c94eac0f28be6cd12717d2f1a50ec54)、[device](../device_reference/P002_设备对象结构.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

控制用于启用 VBUS 测量（measurement）的引脚。


## 62.3\_原页交叉引用（Cross References）

- [zephyr/types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h_source.html)
- [zephyr/device.h](../device_reference/P008_设备模型头文件源码.md)
- [zephyr/drivers/usb_c/usbc_tc.h](../api_source_reference/P891_usbc_tc.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P893_usbc_vbus.h_源码浏览.md)
- [usbc_vbus_driver_api](../device_power_control_model_reference/P101_usbc_vbus_driver_api_结构体.md)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [usbc_vbus_check_level](https://docs.zephyrproject.org/latest/doxygen/html/group__usbc__vbus__api.html#ga421653274fe9b8e2e6237a4bbe47e3ad)
- [device](../device_reference/P002_设备对象结构.md)
- [tc_vbus_level](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c.html#ga015455a6c5620dfc96cfb713bbb72161)
- [usbc_vbus_measure](https://docs.zephyrproject.org/latest/doxygen/html/group__usbc__vbus__api.html#ga0b6c561c5f74a30d54397294cb21660d)
- [usbc_vbus_discharge](https://docs.zephyrproject.org/latest/doxygen/html/group__usbc__vbus__api.html#ga8414cfcfeee7799ea57854c59c0c1677)
- [usbc_vbus_enable](https://docs.zephyrproject.org/latest/doxygen/html/group__usbc__vbus__api.html#ga7c94eac0f28be6cd12717d2f1a50ec54)

<a id="header-details"></a>

---

[上一章](P061_zephyr__usb__class__usb_hid.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P063_zephyr__usb__class__usbd_hid.h_文件参考.md)
