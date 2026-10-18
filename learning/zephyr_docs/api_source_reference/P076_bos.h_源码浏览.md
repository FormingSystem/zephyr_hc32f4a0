---
id: learning.zephyr-docs.api-source-reference.page-76
title: bos.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/bos_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第76章\_bos.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/bos_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](../usb/P151_USBBOS公共头文件.md)。

## 76.1\_原始可见代码（Source Code）

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
<a id="l00027"></a>
<a id="foldopen00029"></a>
<a id="l00029"></a>
<a id="l00031"></a>
<a id="l00033"></a>
<a id="l00038"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="foldopen00044"></a>
<a id="l00044"></a>
<a id="l00046"></a>
<a id="l00048"></a>
<a id="l00049"></a>
<a id="l00050"></a>
<a id="foldopen00057"></a>
<a id="l00057"></a>
<a id="l00059"></a>
<a id="l00060"></a>
<a id="l00062"></a>
<a id="l00063"></a>
<a id="l00065"></a>
<a id="l00066"></a>
<a id="l00070"></a>
<a id="l00071"></a>
<a id="l00072"></a>
<a id="foldopen00078"></a>
<a id="l00078"></a>
<a id="l00080"></a>
<a id="l00082"></a>
<a id="l00084"></a>
<a id="l00086"></a>
<a id="l00088"></a>
<a id="l00089"></a>
<a id="l00090"></a>
<a id="foldopen00096"></a>
<a id="l00096"></a>
<a id="l00098"></a>
<a id="l00102"></a>
<a id="l00103"></a>
<a id="l00108"></a>
<a id="l00109"></a>
<a id="l00110"></a>
<a id="foldopen00117"></a>
<a id="l00117"></a>
<a id="l00119"></a>
<a id="l00121"></a>
<a id="l00125"></a>
<a id="l00127"></a>
<a id="l00128"></a>
<a id="l00129"></a>
<a id="l00133"></a>
<a id="l00134"></a>
<a id="agroup__usb__bos_html_ga0bddefd6b9373068cd4ff8e6fc47950d"></a>
<a id="agroup__usb__bos_html_gga0bddefd6b9373068cd4ff8e6fc47950da2ca67045883d490b849193d4a5a29862"></a>
<a id="agroup__usb__bos_html_gga0bddefd6b9373068cd4ff8e6fc47950da5eb29e64487aa25625305f0b4595394b"></a>
<a id="astdint_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astructusb__bos__capability__lpm_html"></a>
<a id="astructusb__bos__capability__lpm_html_a09ec679e05e7b848800ab63220109bef"></a>
<a id="astructusb__bos__capability__lpm_html_a1ceea07e81970d684a6c1586364a0c90"></a>
<a id="astructusb__bos__capability__lpm_html_a880b1f6efecf7d1e8e9076680c74f9c2"></a>
<a id="astructusb__bos__capability__lpm_html_a8a643af1e99eafdecc006cf714cb0af7"></a>
<a id="astructusb__bos__capability__msos_html"></a>
<a id="astructusb__bos__capability__msos_html_a0945c68d9e7911add0c0586b000c90d3"></a>
<a id="astructusb__bos__capability__msos_html_a4da7539d3bc58fe1da48e3d4d8c965e2"></a>
<a id="astructusb__bos__capability__msos_html_a5e10aed83d93d2ddc1278245aab9cb0a"></a>
<a id="astructusb__bos__capability__msos_html_adbf37ee9a5d7479d59cd1a44ab8d8ca5"></a>
<a id="astructusb__bos__capability__webusb_html"></a>
<a id="astructusb__bos__capability__webusb_html_a068861c7ee1abfdb03e52b8269db30b5"></a>
<a id="astructusb__bos__capability__webusb_html_a1ebbfa1bdca4ad783000c67419552e54"></a>
<a id="astructusb__bos__capability__webusb_html_a3ae4aada1ab7b28d9bac6294467e93ff"></a>
<a id="astructusb__bos__descriptor_html"></a>
<a id="astructusb__bos__descriptor_html_a2c0e68a49d6904d32413f3b3598bb926"></a>
<a id="astructusb__bos__descriptor_html_aa3a661440a4b6d6a2ecf27da740c4121"></a>
<a id="astructusb__bos__descriptor_html_ab45b26a3249589469a53b2cfb99ddd1d"></a>
<a id="astructusb__bos__descriptor_html_afd74417a44821690051d50cd5ffdd581"></a>
<a id="astructusb__bos__platform__descriptor_html"></a>
<a id="astructusb__bos__platform__descriptor_html_a09f10af1f29bccdd300be504cd2dda10"></a>
<a id="astructusb__bos__platform__descriptor_html_a26a748945b0223d369a05ad06a2c6d05"></a>
<a id="astructusb__bos__platform__descriptor_html_a477719191468cec83d2a92a5d6f1231d"></a>
<a id="astructusb__bos__platform__descriptor_html_a477ab8e85845e8809ff7f4bd1bcc0f8a"></a>
<a id="astructusb__bos__platform__descriptor_html_a8e8e95a1648e6bba7568c519158de917"></a>

```c
/*
 * Copyright (c) 2018 Intel Corporation
 * Copyright (c) 2023 Nordic Semiconductor ASA
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_USB_BOS_H_
#define ZEPHYR_INCLUDE_USB_BOS_H_

#include <stdint.h>


struct usb_bos_descriptor {
        uint8_t bLength;
        uint8_t bDescriptorType;
        uint16_t wTotalLength;
        uint8_t bNumDeviceCaps;
} __packed;

enum usb_bos_capability_types {
        USB_BOS_CAPABILITY_EXTENSION = 0x02,
        USB_BOS_CAPABILITY_PLATFORM = 0x05,
};

struct usb_bos_capability_lpm {
        uint8_t bLength;

        uint8_t bDescriptorType;

        uint8_t bDevCapabilityType;

        uint32_t bmAttributes;
} __packed;

struct usb_bos_platform_descriptor {
        uint8_t bLength;
        uint8_t bDescriptorType;
        uint8_t bDevCapabilityType;
        uint8_t bReserved;
        uint8_t PlatformCapabilityUUID[16];
} __packed;

struct usb_bos_capability_webusb {
        uint16_t bcdVersion;
        uint8_t bVendorCode;

        uint8_t iLandingPage;
} __packed;

struct usb_bos_capability_msos {
        uint32_t dwWindowsVersion;
        uint16_t wMSOSDescriptorSetTotalLength;
        uint8_t bMS_VendorCode;
        uint8_t bAltEnumCode;
} __packed;


#endif  /* ZEPHYR_INCLUDE_USB_BOS_H_ */
```

## 76.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2018 Intel Corporation。

版权（Copyright）：© 2023 Nordic Semiconductor ASA。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 134 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_USB_BOS_H_`。

## 76.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](../usb/P151_USBBOS公共头文件.md)
- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html)
- [usb_bos_descriptor](../usb/P146_USBBOS描述符.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bLength](../usb/P146_USBBOS描述符.md#aa3a661440a4b6d6a2ecf27da740c4121)
- [bDescriptorType](../usb/P146_USBBOS描述符.md#afd74417a44821690051d50cd5ffdd581)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [wTotalLength](../usb/P146_USBBOS描述符.md#ab45b26a3249589469a53b2cfb99ddd1d)
- [bNumDeviceCaps](../usb/P146_USBBOS描述符.md#a2c0e68a49d6904d32413f3b3598bb926)
- [usb_bos_capability_types](../usb/P145_USBBOS支持API.md#ga0bddefd6b9373068cd4ff8e6fc47950d)
- [USB_BOS_CAPABILITY_EXTENSION](../usb/P145_USBBOS支持API.md#gga0bddefd6b9373068cd4ff8e6fc47950da2ca67045883d490b849193d4a5a29862)
- [USB_BOS_CAPABILITY_PLATFORM](../usb/P145_USBBOS支持API.md#gga0bddefd6b9373068cd4ff8e6fc47950da5eb29e64487aa25625305f0b4595394b)
- [usb_bos_capability_lpm](../usb/P148_USB链路电源管理能力.md)
- [bLength](../usb/P148_USB链路电源管理能力.md#a09ec679e05e7b848800ab63220109bef)
- [bDescriptorType](../usb/P148_USB链路电源管理能力.md#a880b1f6efecf7d1e8e9076680c74f9c2)
- [bDevCapabilityType](../usb/P148_USB链路电源管理能力.md#a1ceea07e81970d684a6c1586364a0c90)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [bmAttributes](../usb/P148_USB链路电源管理能力.md#a8a643af1e99eafdecc006cf714cb0af7)
- [usb_bos_platform_descriptor](../usb/P147_USB平台能力描述符.md)
- [bLength](../usb/P147_USB平台能力描述符.md#a477ab8e85845e8809ff7f4bd1bcc0f8a)
- [bDescriptorType](../usb/P147_USB平台能力描述符.md#a26a748945b0223d369a05ad06a2c6d05)
- [bDevCapabilityType](../usb/P147_USB平台能力描述符.md#a8e8e95a1648e6bba7568c519158de917)
- [bReserved](../usb/P147_USB平台能力描述符.md#a477719191468cec83d2a92a5d6f1231d)
- [PlatformCapabilityUUID](../usb/P147_USB平台能力描述符.md#a09f10af1f29bccdd300be504cd2dda10)
- [usb_bos_capability_webusb](../usb/P150_USB网页访问能力.md)
- [bcdVersion](../usb/P150_USB网页访问能力.md#a1ebbfa1bdca4ad783000c67419552e54)
- [bVendorCode](../usb/P150_USB网页访问能力.md#a3ae4aada1ab7b28d9bac6294467e93ff)
- [iLandingPage](../usb/P150_USB网页访问能力.md#a068861c7ee1abfdb03e52b8269db30b5)
- [usb_bos_capability_msos](../usb/P149_USB微软操作系统能力.md)
- [dwWindowsVersion](../usb/P149_USB微软操作系统能力.md#a5e10aed83d93d2ddc1278245aab9cb0a)
- [wMSOSDescriptorSetTotalLength](../usb/P149_USB微软操作系统能力.md#adbf37ee9a5d7479d59cd1a44ab8d8ca5)
- [bMS_VendorCode](../usb/P149_USB微软操作系统能力.md#a4da7539d3bc58fe1da48e3d4d8c965e2)
- [bAltEnumCode](../usb/P149_USB微软操作系统能力.md#a0945c68d9e7911add0c0586b000c90d3)
- [usb_bos_capability_lpm::bLength](../usb/P148_USB链路电源管理能力.md#a09ec679e05e7b848800ab63220109bef)
- [usb_bos_capability_lpm::bDevCapabilityType](../usb/P148_USB链路电源管理能力.md#a1ceea07e81970d684a6c1586364a0c90)
- [usb_bos_capability_lpm::bDescriptorType](../usb/P148_USB链路电源管理能力.md#a880b1f6efecf7d1e8e9076680c74f9c2)
- [usb_bos_capability_lpm::bmAttributes](../usb/P148_USB链路电源管理能力.md#a8a643af1e99eafdecc006cf714cb0af7)
- [usb_bos_capability_msos::bAltEnumCode](../usb/P149_USB微软操作系统能力.md#a0945c68d9e7911add0c0586b000c90d3)
- [usb_bos_capability_msos::bMS_VendorCode](../usb/P149_USB微软操作系统能力.md#a4da7539d3bc58fe1da48e3d4d8c965e2)
- [usb_bos_capability_msos::dwWindowsVersion](../usb/P149_USB微软操作系统能力.md#a5e10aed83d93d2ddc1278245aab9cb0a)
- [usb_bos_capability_msos::wMSOSDescriptorSetTotalLength](../usb/P149_USB微软操作系统能力.md#adbf37ee9a5d7479d59cd1a44ab8d8ca5)
- [usb_bos_capability_webusb::iLandingPage](../usb/P150_USB网页访问能力.md#a068861c7ee1abfdb03e52b8269db30b5)
- [usb_bos_capability_webusb::bcdVersion](../usb/P150_USB网页访问能力.md#a1ebbfa1bdca4ad783000c67419552e54)
- [usb_bos_capability_webusb::bVendorCode](../usb/P150_USB网页访问能力.md#a3ae4aada1ab7b28d9bac6294467e93ff)
- [usb_bos_descriptor::bNumDeviceCaps](../usb/P146_USBBOS描述符.md#a2c0e68a49d6904d32413f3b3598bb926)
- [usb_bos_descriptor::bLength](../usb/P146_USBBOS描述符.md#aa3a661440a4b6d6a2ecf27da740c4121)
- [usb_bos_descriptor::wTotalLength](../usb/P146_USBBOS描述符.md#ab45b26a3249589469a53b2cfb99ddd1d)
- [usb_bos_descriptor::bDescriptorType](../usb/P146_USBBOS描述符.md#afd74417a44821690051d50cd5ffdd581)
- [usb_bos_platform_descriptor::PlatformCapabilityUUID](../usb/P147_USB平台能力描述符.md#a09f10af1f29bccdd300be504cd2dda10)
- [usb_bos_platform_descriptor::bDescriptorType](../usb/P147_USB平台能力描述符.md#a26a748945b0223d369a05ad06a2c6d05)
- [usb_bos_platform_descriptor::bReserved](../usb/P147_USB平台能力描述符.md#a477719191468cec83d2a92a5d6f1231d)
- [usb_bos_platform_descriptor::bLength](../usb/P147_USB平台能力描述符.md#a477ab8e85845e8809ff7f4bd1bcc0f8a)
- [usb_bos_platform_descriptor::bDevCapabilityType](../usb/P147_USB平台能力描述符.md#a8e8e95a1648e6bba7568c519158de917)

---

[上一章](P075_bmp581.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P077_brg_cfg_cli.h_源码浏览.md)
