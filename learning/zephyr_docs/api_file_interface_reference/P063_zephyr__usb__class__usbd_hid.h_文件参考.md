---
id: learning.zephyr-docs.api-file-interface-reference.page-63
title: zephyr__usb__class__usbd_hid.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/usbd__hid_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第63章\_zephyr\_\_usb\_\_class\_\_usbd\_hid.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/usbd__hid_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

USB设备（USBD）HID设备API的头文件。

<a id="details"></a>

```c
#include <stdint.h>
#include <zephyr/device.h>
#include <zephyr/usb/class/hid.h>
```

查看此文件的源码。

USB设备（USBD）HID设备API的头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 63.1\_数据结构（Data Structures）

<a id="r_hid_5Fdevice_5Fops"></a>

```c
struct hid_device_ops
```

相关声明：[hid_device_ops](../usb/P043_HID设备回调接口.md)。

人机接口设备（HID）的用户回调。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 63.2\_枚举（Enumerations）

<a id="r_gabfdd923d3dea1fc17d6c21f4ad7dab1d"></a>

```c
enum { HID_REPORT_TYPE_INPUT = 1 , HID_REPORT_TYPE_OUTPUT , HID_REPORT_TYPE_FEATURE }
```

相关声明：[HID_REPORT_TYPE_INPUT](../usb/P042_新版HID设备API.md#ggabfdd923d3dea1fc17d6c21f4ad7dab1da451c0c5bb29aa79f5ce554ac9a914acd)、[HID_REPORT_TYPE_OUTPUT](../usb/P042_新版HID设备API.md#ggabfdd923d3dea1fc17d6c21f4ad7dab1dac019f1ccb72d64b8ce9dc5c5d952f8a3)、[HID_REPORT_TYPE_FEATURE](../usb/P042_新版HID设备API.md#ggabfdd923d3dea1fc17d6c21f4ad7dab1dadb047f4ed99575941ca9d857244f5aea)。

HID 报告类型（report types）：用于 Get/Set Report 请求的报告类型。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 63.3\_函数（Functions）

<a id="r_gabb4502a7c3ab5d2400c039549577f4d0"></a>

```c
int hid_device_register (const struct device *dev, const uint8_t *const rdesc, const uint16_t rsize, const struct hid_device_ops *const ops)
```

相关声明：[hid_device_register](../usb/P042_新版HID设备API.md#gabb4502a7c3ab5d2400c039549577f4d0)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[hid_device_ops](../usb/P043_HID设备回调接口.md)。

注册 HID 设备报告描述符（report descriptor）及用户回调。

<a id="r_ga547f99b1089a4d65a297faa5d6e8edd8"></a>

```c
int hid_device_submit_report (const struct device *dev, const uint16_t size, const uint8_t *const report)
```

相关声明：[hid_device_submit_report](../usb/P042_新版HID设备API.md#ga547f99b1089a4d65a297faa5d6e8edd8)、[device](../device_reference/P002_设备对象结构.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

提交新的输入报告（input report）。

<a id="r_gaa5d319acba8a671537f1ee6a2ea7559e"></a>

```c
int hid_device_set_in_polling (const struct device *dev, const unsigned int period_us)
```

相关声明：[hid_device_set_in_polling](../usb/P042_新版HID设备API.md#gaa5d319acba8a671537f1ee6a2ea7559e)、[device](../device_reference/P002_设备对象结构.md)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)。

设置输入报告的轮询周期（polling period）。

<a id="r_gac5b27822922030734341db4b41435cb6"></a>

```c
int hid_device_set_out_polling (const struct device *dev, const unsigned int period_us)
```

相关声明：[hid_device_set_out_polling](../usb/P042_新版HID设备API.md#gac5b27822922030734341db4b41435cb6)、[device](../device_reference/P002_设备对象结构.md)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)。

设置输出报告（output report）的轮询周期。


## 63.4\_原页交叉引用（Cross References）

- [stdint.h](../api_source_device_reference/P036_stdint.h_源码浏览.md)
- [zephyr/device.h](../device_reference/P008_设备模型头文件源码.md)
- [zephyr/usb/class/hid.h](https://docs.zephyrproject.org/latest/doxygen/html/usb_2class_2hid_8h_source.html)
- [查看此文件的源码。](../api_source_supplement_reference/P239_usbd_hid.h_源码浏览.md)
- [hid_device_ops](../usb/P043_HID设备回调接口.md)
- [HID_REPORT_TYPE_INPUT](../usb/P042_新版HID设备API.md#ggabfdd923d3dea1fc17d6c21f4ad7dab1da451c0c5bb29aa79f5ce554ac9a914acd)
- [HID_REPORT_TYPE_OUTPUT](../usb/P042_新版HID设备API.md#ggabfdd923d3dea1fc17d6c21f4ad7dab1dac019f1ccb72d64b8ce9dc5c5d952f8a3)
- [HID_REPORT_TYPE_FEATURE](../usb/P042_新版HID设备API.md#ggabfdd923d3dea1fc17d6c21f4ad7dab1dadb047f4ed99575941ca9d857244f5aea)
- [hid_device_register](../usb/P042_新版HID设备API.md#gabb4502a7c3ab5d2400c039549577f4d0)
- [device](../device_reference/P002_设备对象结构.md)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [hid_device_submit_report](../usb/P042_新版HID设备API.md#ga547f99b1089a4d65a297faa5d6e8edd8)
- [hid_device_set_in_polling](../usb/P042_新版HID设备API.md#gaa5d319acba8a671537f1ee6a2ea7559e)
- [unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)
- [hid_device_set_out_polling](../usb/P042_新版HID设备API.md#gac5b27822922030734341db4b41435cb6)

<a id="header-details"></a>

---

[上一章](P062_zephyr__drivers__usb_c__usbc_vbus.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P064_zephyr__net__wireguard.h_文件参考.md)
