---
id: learning.zephyr-docs.api-file-kernel-network-reference.page-13
title: zephyr__usb__class__hid.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/usb_2class_2hid_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第13章\_zephyr\_\_usb\_\_class\_\_hid.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/usb_2class_2hid_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

USB人机接口设备（Human Interface Device，HID）通用定义的头文件。

查看此文件的源码。

<a id="details"></a>

USB 人机接口设备（Human Interface Device，HID）通用定义头文件。本头文件遵循《人机接口设备（HID）设备类定义》（Device Class Definition for Human Interface Devices）1.11 版文档（`HID1_11-1.pdf`）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 13.1\_宏定义（Macros）

<a id="r_ga4e9dc6652402e0b87e1313c143737ed4"></a>

```c
#define HID_ITEM(bTag, bType, bSize)
```

相关声明：[HID_ITEM](../usb/P049_HID报告项目定义.md#ga4e9dc6652402e0b87e1313c143737ed4)。

定义 HID 短条目（Short Item）。

<a id="r_ga8646699330c45fb008d50b54be339c6c"></a>

```c
#define HID_INPUT(a)
```

相关声明：[HID_INPUT](../usb/P049_HID报告项目定义.md#ga8646699330c45fb008d50b54be339c6c)。

定义数据长度为 1 字节的 HID 输入项（Input Item）。

<a id="r_ga6ef7aa576bf69f9ba5f93df500a1403c"></a>

```c
#define HID_OUTPUT(a)
```

相关声明：[HID_OUTPUT](../usb/P049_HID报告项目定义.md#ga6ef7aa576bf69f9ba5f93df500a1403c)。

定义数据长度为 1 字节的 HID 输出项（Output Item）。

<a id="r_ga951a415e05e95492250d4fb43a37090d"></a>

```c
#define HID_FEATURE(a)
```

相关声明：[HID_FEATURE](../usb/P049_HID报告项目定义.md#ga951a415e05e95492250d4fb43a37090d)。

定义数据长度为 1 字节的 HID 特征项（Feature Item）。

<a id="r_gad010ed98662b0e653754caff1dfd352f"></a>

```c
#define HID_COLLECTION(a)
```

相关声明：[HID_COLLECTION](../usb/P049_HID报告项目定义.md#gad010ed98662b0e653754caff1dfd352f)。

定义数据长度为 1 字节的 HID 集合项（Collection Item）。

<a id="r_ga6cd6affb9d52e0bf98c7a5c83d03a764"></a>

```c
#define HID_END_COLLECTION HID_ITEM(HID_ITEM_TAG_COLLECTION_END, HID_ITEM_TYPE_MAIN, 0)
```

相关声明：[HID_END_COLLECTION](../usb/P049_HID报告项目定义.md#ga6cd6affb9d52e0bf98c7a5c83d03a764)、[HID_ITEM](../usb/P049_HID报告项目定义.md#ga4e9dc6652402e0b87e1313c143737ed4)、[HID_ITEM_TAG_COLLECTION_END](../usb/P048_HID通用定义.md#ga3f4fe1817887966f0d05aa597cd0ab79)、[HID_ITEM_TYPE_MAIN](../usb/P048_HID通用定义.md#ga9a71248c522943951b5af70ec9c14c02)。

定义 HID 结束集合（End Collection）条目，即非数据条目（Non-data Item）。

<a id="r_ga30dc3f62583822ba27edd984dc2dec39"></a>

```c
#define HID_USAGE_PAGE(page)
```

相关声明：[HID_USAGE_PAGE](../usb/P049_HID报告项目定义.md#ga30dc3f62583822ba27edd984dc2dec39)。

定义 HID 用法页项（Usage Page Item）。

<a id="r_ga4ab727e3407dc5c0b11d998314ab27de"></a>

```c
#define HID_USAGE_PAGE16(page)
```

相关声明：[HID_USAGE_PAGE16](../usb/P049_HID报告项目定义.md#ga4ab727e3407dc5c0b11d998314ab27de)。

定义数据长度为 2 字节的 HID 用法页项（Usage Page Item）。

<a id="r_gacd141f6ede5122f260cd50338649d458"></a>

```c
#define HID_LOGICAL_MIN8(a)
```

相关声明：[HID_LOGICAL_MIN8](../usb/P049_HID报告项目定义.md#gacd141f6ede5122f260cd50338649d458)。

定义数据长度为 1 字节的 HID 逻辑最小值项（Logical Minimum Item）。

<a id="r_ga2f6b809ae85b6716ade8c52da4fa56af"></a>

```c
#define HID_LOGICAL_MAX8(a)
```

相关声明：[HID_LOGICAL_MAX8](../usb/P049_HID报告项目定义.md#ga2f6b809ae85b6716ade8c52da4fa56af)。

定义数据长度为 1 字节的 HID 逻辑最大值项（Logical Maximum Item）。

<a id="r_ga5e290798d55bccd7474dbfb6bc2d1033"></a>

```c
#define HID_LOGICAL_MIN16(a, b)
```

相关声明：[HID_LOGICAL_MIN16](../usb/P049_HID报告项目定义.md#ga5e290798d55bccd7474dbfb6bc2d1033)。

定义数据长度为 2 字节的 HID 逻辑最小值项（Logical Minimum Item）。

<a id="r_ga9b804d676812dcfb0ec12f3aa887e37f"></a>

```c
#define HID_LOGICAL_MAX16(a, b)
```

相关声明：[HID_LOGICAL_MAX16](../usb/P049_HID报告项目定义.md#ga9b804d676812dcfb0ec12f3aa887e37f)。

定义数据长度为 2 字节的 HID 逻辑最大值项（Logical Maximum Item）。

<a id="r_gad4b2ff8642676d692fd0d56ab0cbeaa7"></a>

```c
#define HID_LOGICAL_MIN32(a, b, c, d)
```

相关声明：[HID_LOGICAL_MIN32](../usb/P049_HID报告项目定义.md#gad4b2ff8642676d692fd0d56ab0cbeaa7)。

定义数据长度为 4 字节的 HID 逻辑最小值项（Logical Minimum Item）。

<a id="r_gae9d17e753685b0df6c53f942ce9c95d2"></a>

```c
#define HID_LOGICAL_MAX32(a, b, c, d)
```

相关声明：[HID_LOGICAL_MAX32](../usb/P049_HID报告项目定义.md#gae9d17e753685b0df6c53f942ce9c95d2)。

定义数据长度为 4 字节的 HID 逻辑最大值项（Logical Maximum Item）。

<a id="r_ga3135a21a63c491daf8647fa771def0e7"></a>

```c
#define HID_REPORT_SIZE(size)
```

相关声明：[HID_REPORT_SIZE](../usb/P049_HID报告项目定义.md#ga3135a21a63c491daf8647fa771def0e7)。

定义数据长度为 1 字节的 HID 报告大小项（Report Size Item）。

<a id="r_ga1b45fce2c7df2847b1326fca29cef389"></a>

```c
#define HID_REPORT_ID(id)
```

相关声明：[HID_REPORT_ID](../usb/P049_HID报告项目定义.md#ga1b45fce2c7df2847b1326fca29cef389)。

定义数据长度为 1 字节的 HID 报告ID项（Report ID Item）。

<a id="r_ga71192f2a55f05456b893069ebfbc5b98"></a>

```c
#define HID_REPORT_COUNT(count)
```

相关声明：[HID_REPORT_COUNT](../usb/P049_HID报告项目定义.md#ga71192f2a55f05456b893069ebfbc5b98)。

定义数据长度为 1 字节的 HID 报告计数项（Report Count Item）。

<a id="r_gac8429a70866a898887ead55664e04bd7"></a>

```c
#define HID_USAGE(idx)
```

相关声明：[HID_USAGE](../usb/P049_HID报告项目定义.md#gac8429a70866a898887ead55664e04bd7)。

定义数据长度为 1 字节的 HID 用法索引项（Usage Index Item）。

<a id="r_gaf2e338747f22f75256e57de1cf055200"></a>

```c
#define HID_USAGE16(idx)
```

相关声明：[HID_USAGE16](../usb/P049_HID报告项目定义.md#gaf2e338747f22f75256e57de1cf055200)。

定义数据长度为 2 字节的 HID 用法索引项（Usage Index Item）。

<a id="r_gabf53f1e2eae6d686aeb7d62cc46b22ad"></a>

```c
#define HID_USAGE_MIN8(a)
```

相关声明：[HID_USAGE_MIN8](../usb/P049_HID报告项目定义.md#gabf53f1e2eae6d686aeb7d62cc46b22ad)。

定义数据长度为 1 字节的 HID 用法最小值项（Usage Minimum Item）。

<a id="r_gae7fc9684ef10f50d69df6f495cc09e91"></a>

```c
#define HID_USAGE_MAX8(a)
```

相关声明：[HID_USAGE_MAX8](../usb/P049_HID报告项目定义.md#gae7fc9684ef10f50d69df6f495cc09e91)。

定义数据长度为 1 字节的 HID 用法最大值项（Usage Maximum Item）。

<a id="r_ga0dbc847d11cf64676f7cfc51b54150fa"></a>

```c
#define HID_USAGE_MIN16(a, b)
```

相关声明：[HID_USAGE_MIN16](../usb/P049_HID报告项目定义.md#ga0dbc847d11cf64676f7cfc51b54150fa)。

定义数据长度为 2 字节的 HID 用法最小值项（Usage Minimum Item）。

<a id="r_gadd11a09546bc275c82e7a992cb9441cc"></a>

```c
#define HID_USAGE_MAX16(a, b)
```

相关声明：[HID_USAGE_MAX16](../usb/P049_HID报告项目定义.md#gadd11a09546bc275c82e7a992cb9441cc)。

定义数据长度为 2 字节的 HID 用法最大值项（Usage Maximum Item）。

<a id="r_ga2147820c08a9b4a18d3aa162460f3967"></a>

```c
#define HID_UNIT_EXPONENT(exp)
```

相关声明：[HID_UNIT_EXPONENT](../usb/P049_HID报告项目定义.md#ga2147820c08a9b4a18d3aa162460f3967)。

定义 HID 单位指数项（Unit Exponent Item）。

<a id="r_ga3696f0782268d504b0c8bb540236779f"></a>

```c
#define HID_MOUSE_REPORT_DESC(bcnt)
```

相关声明：[HID_MOUSE_REPORT_DESC](../usb/P050_HID报告描述符构造宏.md#ga3696f0782268d504b0c8bb540236779f)。

适用于具有 `n` 个按键的鼠标的简单 HID 鼠标报告描述符（Mouse Report Descriptor）。

<a id="r_gaea973ffbe1612187c90614133956cfd6"></a>

```c
#define HID_KEYBOARD_REPORT_DESC()
```

相关声明：[HID_KEYBOARD_REPORT_DESC](../usb/P050_HID报告描述符构造宏.md#gaea973ffbe1612187c90614133956cfd6)。

简单的 HID 键盘报告描述符（Keyboard Report Descriptor）。

<a id="define-members-0"></a>

### USB HID 类型与值（USB HID types and values）

<a id="r_ga77f649cbc5ab446b2cfe3e68eb88ac91"></a>

```c
#define USB_HID_VERSION 0x0111
```

相关声明：[USB_HID_VERSION](../usb/P048_HID通用定义.md#ga77f649cbc5ab446b2cfe3e68eb88ac91)。

HID 规范版本（Specification Release）v1.11。

<a id="r_ga07e8028979ff1c3d30408b08778bfd3d"></a>

```c
#define USB_DESC_HID 0x21
```

相关声明：[USB_DESC_HID](../usb/P048_HID通用定义.md#ga07e8028979ff1c3d30408b08778bfd3d)。

USB HID 类的 HID 描述符类型（HID Descriptor Type）。

<a id="r_gaca594a2caf9cb5ebac863c6c2f233f31"></a>

```c
#define USB_DESC_HID_REPORT 0x22
```

相关声明：[USB_DESC_HID_REPORT](../usb/P048_HID通用定义.md#gaca594a2caf9cb5ebac863c6c2f233f31)。

USB HID 类的报告描述符类型（Report Descriptor Type）。

<a id="r_ga2d543337d798d1c85436d2fee1c5be3f"></a>

```c
#define USB_DESC_HID_PHYSICAL 0x23
```

相关声明：[USB_DESC_HID_PHYSICAL](../usb/P048_HID通用定义.md#ga2d543337d798d1c85436d2fee1c5be3f)。

USB HID 类的物理描述符类型（Physical Descriptor Type）。

<a id="r_ga3d4f67db0b3531f3493cde381110809d"></a>

```c
#define USB_HID_GET_REPORT 0x01
```

相关声明：[USB_HID_GET_REPORT](../usb/P048_HID通用定义.md#ga3d4f67db0b3531f3493cde381110809d)。

USB HID 类的获取报告（GetReport）请求的 `bRequest` 值。

<a id="r_ga9d69e0dae00cf3c6c5dc5602f63b2f2f"></a>

```c
#define USB_HID_GET_IDLE 0x02
```

相关声明：[USB_HID_GET_IDLE](../usb/P048_HID通用定义.md#ga9d69e0dae00cf3c6c5dc5602f63b2f2f)。

USB HID 类的获取空闲率（GetIdle）请求的 `bRequest` 值。

<a id="r_ga09469e20036a4c3df8281a2575358747"></a>

```c
#define USB_HID_GET_PROTOCOL 0x03
```

相关声明：[USB_HID_GET_PROTOCOL](../usb/P048_HID通用定义.md#ga09469e20036a4c3df8281a2575358747)。

USB HID 类的获取协议（GetProtocol）请求的 `bRequest` 值。

<a id="r_gaed6de2caf14f9caa049fab82902299cf"></a>

```c
#define USB_HID_SET_REPORT 0x09
```

相关声明：[USB_HID_SET_REPORT](../usb/P048_HID通用定义.md#gaed6de2caf14f9caa049fab82902299cf)。

USB HID 类的设置报告（SetReport）请求的 `bRequest` 值。

<a id="r_ga1cbc5f99d9bd85fca7b9a624efb41078"></a>

```c
#define USB_HID_SET_IDLE 0x0A
```

相关声明：[USB_HID_SET_IDLE](../usb/P048_HID通用定义.md#ga1cbc5f99d9bd85fca7b9a624efb41078)。

USB HID 类的设置空闲率（SetIdle）请求的 `bRequest` 值。

<a id="r_ga2058ed723b6a4613b4dcb8040b739684"></a>

```c
#define USB_HID_SET_PROTOCOL 0x0B
```

相关声明：[USB_HID_SET_PROTOCOL](../usb/P048_HID通用定义.md#ga2058ed723b6a4613b4dcb8040b739684)。

USB HID 类的设置协议（SetProtocol）请求的 `bRequest` 值。

<a id="r_ga953074178d707cd3538da80f36a96ff6"></a>

```c
#define HID_BOOT_IFACE_CODE_NONE 0
```

相关声明：[HID_BOOT_IFACE_CODE_NONE](../usb/P048_HID通用定义.md#ga953074178d707cd3538da80f36a96ff6)。

USB HID 引导接口协议（Boot Interface Protocol，`bInterfaceProtocol`）的无协议（None）编码。

<a id="r_ga6e6276ae88c414e10c602d5e041738ab"></a>

```c
#define HID_BOOT_IFACE_CODE_KEYBOARD 1
```

相关声明：[HID_BOOT_IFACE_CODE_KEYBOARD](../usb/P048_HID通用定义.md#ga6e6276ae88c414e10c602d5e041738ab)。

USB HID 引导接口协议（Boot Interface Protocol，`bInterfaceProtocol`）的键盘（Keyboard）编码。

<a id="r_ga900873d4834ea511a08b08debe62bedf"></a>

```c
#define HID_BOOT_IFACE_CODE_MOUSE 2
```

相关声明：[HID_BOOT_IFACE_CODE_MOUSE](../usb/P048_HID通用定义.md#ga900873d4834ea511a08b08debe62bedf)。

USB HID 引导接口协议（Boot Interface Protocol，`bInterfaceProtocol`）的鼠标（Mouse）编码。

<a id="r_gafd24e87747c82293e689f58157f06128"></a>

```c
#define HID_PROTOCOL_BOOT 0
```

相关声明：[HID_PROTOCOL_BOOT](../usb/P048_HID通用定义.md#gafd24e87747c82293e689f58157f06128)。

USB HID 类的引导协议（Boot Protocol）编码。

<a id="r_ga982c0da911cbda6e09bd48a5e4ab85f1"></a>

```c
#define HID_PROTOCOL_REPORT 1
```

相关声明：[HID_PROTOCOL_REPORT](../usb/P048_HID通用定义.md#ga982c0da911cbda6e09bd48a5e4ab85f1)。

USB HID 类的报告协议（Report Protocol）编码。

<a id="r_ga9a71248c522943951b5af70ec9c14c02"></a>

```c
#define HID_ITEM_TYPE_MAIN 0x0
```

相关声明：[HID_ITEM_TYPE_MAIN](../usb/P048_HID通用定义.md#ga9a71248c522943951b5af70ec9c14c02)。

HID 主条目类型（Main Item Type）。

<a id="r_ga8e56e8090f1af7aae473e8a8b6832fb8"></a>

```c
#define HID_ITEM_TYPE_GLOBAL 0x1
```

相关声明：[HID_ITEM_TYPE_GLOBAL](../usb/P048_HID通用定义.md#ga8e56e8090f1af7aae473e8a8b6832fb8)。

HID 全局条目类型（Global Item Type）。

<a id="r_ga0bfb0e326d9a01072c029cba788d6456"></a>

```c
#define HID_ITEM_TYPE_LOCAL 0x2
```

相关声明：[HID_ITEM_TYPE_LOCAL](../usb/P048_HID通用定义.md#ga0bfb0e326d9a01072c029cba788d6456)。

HID 局部条目类型（Local Item Type）。

<a id="r_ga66e1c50fe814fd05d61dce12ce3888c1"></a>

```c
#define HID_ITEM_TAG_INPUT 0x8
```

相关声明：[HID_ITEM_TAG_INPUT](../usb/P048_HID通用定义.md#ga66e1c50fe814fd05d61dce12ce3888c1)。

HID 输入项标记（Input Item Tag）。

<a id="r_ga70c32518a6b538831e821ad30022679b"></a>

```c
#define HID_ITEM_TAG_OUTPUT 0x9
```

相关声明：[HID_ITEM_TAG_OUTPUT](../usb/P048_HID通用定义.md#ga70c32518a6b538831e821ad30022679b)。

HID 输出项标记（Output Item Tag）。

<a id="r_ga2c06052593b060466f4c338a88319485"></a>

```c
#define HID_ITEM_TAG_COLLECTION 0xA
```

相关声明：[HID_ITEM_TAG_COLLECTION](../usb/P048_HID通用定义.md#ga2c06052593b060466f4c338a88319485)。

HID 集合项标记（Collection Item Tag）。

<a id="r_gaeadcca849f0a0923d9a70605c44464a6"></a>

```c
#define HID_ITEM_TAG_FEATURE 0xB
```

相关声明：[HID_ITEM_TAG_FEATURE](../usb/P048_HID通用定义.md#gaeadcca849f0a0923d9a70605c44464a6)。

HID 特征项标记（Feature Item Tag）。

<a id="r_ga3f4fe1817887966f0d05aa597cd0ab79"></a>

```c
#define HID_ITEM_TAG_COLLECTION_END 0xC
```

相关声明：[HID_ITEM_TAG_COLLECTION_END](../usb/P048_HID通用定义.md#ga3f4fe1817887966f0d05aa597cd0ab79)。

HID 集合结束项标记（End Collection Item Tag）。

<a id="r_ga73f58fa37c0bf6698463b9d31c8a511f"></a>

```c
#define HID_ITEM_TAG_USAGE_PAGE 0x0
```

相关声明：[HID_ITEM_TAG_USAGE_PAGE](../usb/P048_HID通用定义.md#ga73f58fa37c0bf6698463b9d31c8a511f)。

HID 用法页项标记（Usage Page Item Tag）。

<a id="r_ga034033b1ae6f4677aef82d4243c6f712"></a>

```c
#define HID_ITEM_TAG_LOGICAL_MIN 0x1
```

相关声明：[HID_ITEM_TAG_LOGICAL_MIN](../usb/P048_HID通用定义.md#ga034033b1ae6f4677aef82d4243c6f712)。

HID 逻辑最小值项标记（Logical Minimum Item Tag）。

<a id="r_gaab6aec72cca41670464605d6970ad553"></a>

```c
#define HID_ITEM_TAG_LOGICAL_MAX 0x2
```

相关声明：[HID_ITEM_TAG_LOGICAL_MAX](../usb/P048_HID通用定义.md#gaab6aec72cca41670464605d6970ad553)。

HID 逻辑最大值项标记（Logical Maximum Item Tag）。

<a id="r_ga6dfdd60d0b985d683a58ad752d3ef3c3"></a>

```c
#define HID_ITEM_TAG_PHYSICAL_MIN 0x3
```

相关声明：[HID_ITEM_TAG_PHYSICAL_MIN](../usb/P048_HID通用定义.md#ga6dfdd60d0b985d683a58ad752d3ef3c3)。

HID 物理最小值项标记（Physical Minimum Item Tag）。

<a id="r_gaa68bd8a73cee33d810484f4aa3f30e92"></a>

```c
#define HID_ITEM_TAG_PHYSICAL_MAX 0x4
```

相关声明：[HID_ITEM_TAG_PHYSICAL_MAX](../usb/P048_HID通用定义.md#gaa68bd8a73cee33d810484f4aa3f30e92)。

HID 物理最大值项标记（Physical Maximum Item Tag）。

<a id="r_ga7c6d81ee211814ec9b5d17f95e57639b"></a>

```c
#define HID_ITEM_TAG_UNIT_EXPONENT 0x5
```

相关声明：[HID_ITEM_TAG_UNIT_EXPONENT](../usb/P048_HID通用定义.md#ga7c6d81ee211814ec9b5d17f95e57639b)。

HID 单位指数项标记（Unit Exponent Item Tag）。

<a id="r_ga98267b4ff28f435d67d2a7bf1055fc7c"></a>

```c
#define HID_ITEM_TAG_UNIT 0x6
```

相关声明：[HID_ITEM_TAG_UNIT](../usb/P048_HID通用定义.md#ga98267b4ff28f435d67d2a7bf1055fc7c)。

HID 单位项标记（Unit Item Tag）。

<a id="r_ga0e6d7a56593bd25a5e15683e9271bb19"></a>

```c
#define HID_ITEM_TAG_REPORT_SIZE 0x7
```

相关声明：[HID_ITEM_TAG_REPORT_SIZE](../usb/P048_HID通用定义.md#ga0e6d7a56593bd25a5e15683e9271bb19)。

HID 报告大小项标记（Report Size Item Tag）。

<a id="r_ga76cd3a266ae5d5e29292d93caceece72"></a>

```c
#define HID_ITEM_TAG_REPORT_ID 0x8
```

相关声明：[HID_ITEM_TAG_REPORT_ID](../usb/P048_HID通用定义.md#ga76cd3a266ae5d5e29292d93caceece72)。

HID 报告ID项标记（Report ID Item Tag）。

<a id="r_ga1847701703130ce8f57547811f28b2b4"></a>

```c
#define HID_ITEM_TAG_REPORT_COUNT 0x9
```

相关声明：[HID_ITEM_TAG_REPORT_COUNT](../usb/P048_HID通用定义.md#ga1847701703130ce8f57547811f28b2b4)。

HID 报告计数项标记（Report count Item Tag）。

<a id="r_gaefd616ecaa8fc8762e65ec9d7b01f0cd"></a>

```c
#define HID_ITEM_TAG_USAGE 0x0
```

相关声明：[HID_ITEM_TAG_USAGE](../usb/P048_HID通用定义.md#gaefd616ecaa8fc8762e65ec9d7b01f0cd)。

HID 用法项标记（Usage Item Tag）。

<a id="r_ga4e6f4133f12276f4f9fa51ab06580676"></a>

```c
#define HID_ITEM_TAG_USAGE_MIN 0x1
```

相关声明：[HID_ITEM_TAG_USAGE_MIN](../usb/P048_HID通用定义.md#ga4e6f4133f12276f4f9fa51ab06580676)。

HID 用法最小值项标记（Usage Minimum Item Tag）。

<a id="r_gac2a0aff74caff6c03511fc0b6db6167b"></a>

```c
#define HID_ITEM_TAG_USAGE_MAX 0x2
```

相关声明：[HID_ITEM_TAG_USAGE_MAX](../usb/P048_HID通用定义.md#gac2a0aff74caff6c03511fc0b6db6167b)。

HID 用法最大值项标记（Usage Maximum Item Tag）。

<a id="r_gaca1e227f9241c217b8b1aeae6c4bd672"></a>

```c
#define HID_COLLECTION_PHYSICAL 0x00
```

相关声明：[HID_COLLECTION_PHYSICAL](../usb/P048_HID通用定义.md#gaca1e227f9241c217b8b1aeae6c4bd672)。

物理集合类型（Physical Collection Type）。

<a id="r_ga2e5e5ad0919fbaea0e6f8e5d86f4c2fd"></a>

```c
#define HID_COLLECTION_APPLICATION 0x01
```

相关声明：[HID_COLLECTION_APPLICATION](../usb/P048_HID通用定义.md#ga2e5e5ad0919fbaea0e6f8e5d86f4c2fd)。

应用集合类型（Application Collection Type）。

<a id="r_ga904a372a663bd7d9205402a3a014c04b"></a>

```c
#define HID_COLLECTION_LOGICAL 0x02
```

相关声明：[HID_COLLECTION_LOGICAL](../usb/P048_HID通用定义.md#ga904a372a663bd7d9205402a3a014c04b)。

逻辑集合类型（Logical Collection Type）。

<a id="r_gac58ab4780c054754b7f94ff97a152694"></a>

```c
#define HID_COLLECTION_REPORT 0x03
```

相关声明：[HID_COLLECTION_REPORT](../usb/P048_HID通用定义.md#gac58ab4780c054754b7f94ff97a152694)。

报告集合类型（Report Collection Type）。

<a id="r_ga8e1610365a1556adf7121cc3b1f83080"></a>

```c
#define HID_COLLECTION_NAMED_ARRAY 0x04
```

相关声明：[HID_COLLECTION_NAMED_ARRAY](../usb/P048_HID通用定义.md#ga8e1610365a1556adf7121cc3b1f83080)。

命名数组集合类型（Named Array Collection Type）。

<a id="r_ga64af797e424ea1e2c02c745f30721e48"></a>

```c
#define HID_COLLECTION_USAGE_SWITCH 0x05
```

相关声明：[HID_COLLECTION_USAGE_SWITCH](../usb/P048_HID通用定义.md#ga64af797e424ea1e2c02c745f30721e48)。

用法切换集合类型（Usage Switch Collection Type）。

<a id="r_gaabc1c6bed23b88f4cdc89d5347595d4f"></a>

```c
#define HID_COLLECTION_MODIFIER 0x06
```

相关声明：[HID_COLLECTION_MODIFIER](../usb/P048_HID通用定义.md#gaabc1c6bed23b88f4cdc89d5347595d4f)。

修饰符集合类型（Modifier Collection Type）。

<a id="r_gacb3fc5b0f838dfa5eb95e9e1bf52b589"></a>

```c
#define HID_USAGE_GEN_DESKTOP 0x01
```

相关声明：[HID_USAGE_GEN_DESKTOP](../usb/P048_HID通用定义.md#gacb3fc5b0f838dfa5eb95e9e1bf52b589)。

HID 通用桌面控制用途页（Generic Desktop Controls Usage Page）。

<a id="r_ga1fdbfffd0b343cec1480e9f0347efa5d"></a>

```c
#define HID_USAGE_GEN_KEYBOARD 0x07
```

相关声明：[HID_USAGE_GEN_KEYBOARD](../usb/P048_HID通用定义.md#ga1fdbfffd0b343cec1480e9f0347efa5d)。

HID 键盘用途页（Keyboard Usage Page）。

<a id="r_gae632e9a37203506c051c3cacfdf0c2c7"></a>

```c
#define HID_USAGE_GEN_LEDS 0x08
```

相关声明：[HID_USAGE_GEN_LEDS](../usb/P048_HID通用定义.md#gae632e9a37203506c051c3cacfdf0c2c7)。

HID LED 用途页（LEDs Usage Page）。

<a id="r_ga13401731a0ead5448a0823d0f6142404"></a>

```c
#define HID_USAGE_GEN_BUTTON 0x09
```

相关声明：[HID_USAGE_GEN_BUTTON](../usb/P048_HID通用定义.md#ga13401731a0ead5448a0823d0f6142404)。

HID 按键用途页（Button Usage Page）。

<a id="r_gab5d07369bed290a78a119d54240db567"></a>

```c
#define HID_USAGE_SENSORS 0x20
```

相关声明：[HID_USAGE_SENSORS](../usb/P048_HID通用定义.md#gab5d07369bed290a78a119d54240db567)。

HID 传感器用途页（Sensors Usage Page）。

<a id="r_ga1441517d7c57529dcf726a1dd8b09a07"></a>

```c
#define HID_USAGE_GEN_DESKTOP_UNDEFINED 0x00
```

相关声明：[HID_USAGE_GEN_DESKTOP_UNDEFINED](../usb/P048_HID通用定义.md#ga1441517d7c57529dcf726a1dd8b09a07)。

HID 通用桌面（Generic Desktop）的未定义用法 ID（Undefined Usage ID）。

<a id="r_ga77a7162980a77efa1e2e7b21942bb7dd"></a>

```c
#define HID_USAGE_GEN_DESKTOP_POINTER 0x01
```

相关声明：[HID_USAGE_GEN_DESKTOP_POINTER](../usb/P048_HID通用定义.md#ga77a7162980a77efa1e2e7b21942bb7dd)。

HID 通用桌面（Generic Desktop）的指针用法 ID（Pointer Usage ID）。

<a id="r_ga983274dd50058de26e0e86d10d50e81a"></a>

```c
#define HID_USAGE_GEN_DESKTOP_MOUSE 0x02
```

相关声明：[HID_USAGE_GEN_DESKTOP_MOUSE](../usb/P048_HID通用定义.md#ga983274dd50058de26e0e86d10d50e81a)。

HID 通用桌面（Generic Desktop）的鼠标用法 ID（Mouse Usage ID）。

<a id="r_gada59a9f3aeaeaefc6112c7d9902b2d6d"></a>

```c
#define HID_USAGE_GEN_DESKTOP_JOYSTICK 0x04
```

相关声明：[HID_USAGE_GEN_DESKTOP_JOYSTICK](../usb/P048_HID通用定义.md#gada59a9f3aeaeaefc6112c7d9902b2d6d)。

HID 通用桌面（Generic Desktop）的操纵杆用法 ID（Joystick Usage ID）。

<a id="r_ga17404e33133204a538f976d321c84ff0"></a>

```c
#define HID_USAGE_GEN_DESKTOP_GAMEPAD 0x05
```

相关声明：[HID_USAGE_GEN_DESKTOP_GAMEPAD](../usb/P048_HID通用定义.md#ga17404e33133204a538f976d321c84ff0)。

HID 通用桌面（Generic Desktop）的游戏手柄用法 ID（Gamepad Usage ID）。

<a id="r_ga0bdaa3d23c79204a1064cb53b279bd77"></a>

```c
#define HID_USAGE_GEN_DESKTOP_KEYBOARD 0x06
```

相关声明：[HID_USAGE_GEN_DESKTOP_KEYBOARD](../usb/P048_HID通用定义.md#ga0bdaa3d23c79204a1064cb53b279bd77)。

HID 通用桌面（Generic Desktop）的键盘用法 ID（Keyboard Usage ID）。

<a id="r_ga69f8e44306828b3f44d3a7704ff07807"></a>

```c
#define HID_USAGE_GEN_DESKTOP_KEYPAD 0x07
```

相关声明：[HID_USAGE_GEN_DESKTOP_KEYPAD](../usb/P048_HID通用定义.md#ga69f8e44306828b3f44d3a7704ff07807)。

HID 通用桌面（Generic Desktop）的小键盘用法 ID（Keypad Usage ID）。

<a id="r_gae283a3558ba536e163140a3b6cdbb273"></a>

```c
#define HID_USAGE_GEN_DESKTOP_X 0x30
```

相关声明：[HID_USAGE_GEN_DESKTOP_X](../usb/P048_HID通用定义.md#gae283a3558ba536e163140a3b6cdbb273)。

HID 通用桌面（Generic Desktop）的X轴用法 ID（X Usage ID）。

<a id="r_gad1ab1f8f9c8a4a80bfc8e3a327e3b2fb"></a>

```c
#define HID_USAGE_GEN_DESKTOP_Y 0x31
```

相关声明：[HID_USAGE_GEN_DESKTOP_Y](../usb/P048_HID通用定义.md#gad1ab1f8f9c8a4a80bfc8e3a327e3b2fb)。

HID 通用桌面（Generic Desktop）的Y轴用法 ID（Y Usage ID）。

<a id="r_gaa8c772d412ac1ac7a36739c52f04c0a9"></a>

```c
#define HID_USAGE_GEN_DESKTOP_WHEEL 0x38
```

相关声明：[HID_USAGE_GEN_DESKTOP_WHEEL](../usb/P048_HID通用定义.md#gaa8c772d412ac1ac7a36739c52f04c0a9)。

HID 通用桌面（Generic Desktop）的滚轮用法 ID（Wheel Usage ID）。

<a id="r_ga85a9547841ea4a2e4b56ba2a58e9d0ee"></a>

```c
#define HID_USAGE_SENSOR_TYPE_COLLECTION 0x001
```

相关声明：[HID_USAGE_SENSOR_TYPE_COLLECTION](../usb/P048_HID通用定义.md#ga85a9547841ea4a2e4b56ba2a58e9d0ee)。

HID 传感器（Sensors）的集合用法 ID（Collection Usage ID）。

<a id="r_ga00b6e4c7d3eb1576c9f3eb7bae076bab"></a>

```c
#define HID_USAGE_SENSORS_TYPE_ENVIRONMENTAL_TEMPERATURE 0x033
```

相关声明：[HID_USAGE_SENSORS_TYPE_ENVIRONMENTAL_TEMPERATURE](../usb/P048_HID通用定义.md#ga00b6e4c7d3eb1576c9f3eb7bae076bab)。

HID 传感器（Sensors）的环境温度类型用法 ID（Environmental Temperature Type Usage ID）。

<a id="r_ga062651fd2ce433819e1d61d0488e4b7f"></a>

```c
#define HID_USAGE_SENSORS_EVENT_SENSOR_STATE 0x201
```

相关声明：[HID_USAGE_SENSORS_EVENT_SENSOR_STATE](../usb/P048_HID通用定义.md#ga062651fd2ce433819e1d61d0488e4b7f)。

HID 传感器（Sensors）的事件传感器状态用法 ID（Event Sensor State Usage ID）。

<a id="r_gaf5d0cd096b1a0591002a6438a977710c"></a>

```c
#define HID_USAGE_SENSORS_PROPERTY_FRIENDLY_NAME 0x301
```

相关声明：[HID_USAGE_SENSORS_PROPERTY_FRIENDLY_NAME](../usb/P048_HID通用定义.md#gaf5d0cd096b1a0591002a6438a977710c)。

HID 传感器（Sensors）的友好名称属性用法 ID（Friendly Name Property Usage ID）。

<a id="r_ga2108b2634377a0f8860b2f7de50f21e8"></a>

```c
#define HID_USAGE_SENSORS_DATA_ENVIRONMENTAL_TEMPERATURE 0x434
```

相关声明：[HID_USAGE_SENSORS_DATA_ENVIRONMENTAL_TEMPERATURE](../usb/P048_HID通用定义.md#ga2108b2634377a0f8860b2f7de50f21e8)。

HID 传感器（Sensors）的环境温度数据用法 ID（Environmental Temperature Data Usage ID）。

<a id="r_ga0f907ba7b85ff784dde9a14b38ed6fbb"></a>

```c
#define HID_USAGE_SENSORS_PROPERTY_TIMESTAMP 0x529
```

相关声明：[HID_USAGE_SENSORS_PROPERTY_TIMESTAMP](../usb/P048_HID通用定义.md#ga0f907ba7b85ff784dde9a14b38ed6fbb)。

HID 传感器（Sensors）的时间戳属性用法 ID（Timestamp Property Usage ID）。

<a id="r_gaa5a61c460035086e103a4fa97b89efb6"></a>

```c
#define HID_USAGE_SENSORS_SENSOR_STATE_UNDEFINED 0x800
```

相关声明：[HID_USAGE_SENSORS_SENSOR_STATE_UNDEFINED](../usb/P048_HID通用定义.md#gaa5a61c460035086e103a4fa97b89efb6)。

HID 传感器（Sensors）的传感器状态未定义用法 ID（Sensor State Undefined Usage ID）。

<a id="r_gae37e00681768e24a1995a6766bd5ba77"></a>

```c
#define HID_USAGE_SENSORS_SENSOR_STATE_READY 0x801
```

相关声明：[HID_USAGE_SENSORS_SENSOR_STATE_READY](../usb/P048_HID通用定义.md#gae37e00681768e24a1995a6766bd5ba77)。

HID 传感器（Sensors）的传感器状态就绪用法 ID（Sensor State Ready Usage ID）。

<a id="r_ga5c897b459ec0f68d0825b6f454a49355"></a>

```c
#define HID_USAGE_SENSORS_SENSOR_STATE_NOT_AVAILABLE 0x802
```

相关声明：[HID_USAGE_SENSORS_SENSOR_STATE_NOT_AVAILABLE](../usb/P048_HID通用定义.md#ga5c897b459ec0f68d0825b6f454a49355)。

HID 传感器（Sensors）的传感器状态不可用用法 ID（Sensor State Not Available Usage ID）。

<a id="r_ga6948d4190e58386e184b0376b6c67584"></a>

```c
#define HID_USAGE_SENSORS_SENSOR_STATE_NO_DATA 0x803
```

相关声明：[HID_USAGE_SENSORS_SENSOR_STATE_NO_DATA](../usb/P048_HID通用定义.md#ga6948d4190e58386e184b0376b6c67584)。

HID 传感器（Sensors）的传感器状态无数据用法 ID（Sensor State No Data Usage ID）。

<a id="r_ga347b9f96fc87f3e7f6540961e240ef5e"></a>

```c
#define HID_USAGE_SENSORS_SENSOR_STATE_INITIALIZING 0x804
```

相关声明：[HID_USAGE_SENSORS_SENSOR_STATE_INITIALIZING](../usb/P048_HID通用定义.md#ga347b9f96fc87f3e7f6540961e240ef5e)。

HID 传感器（Sensors）的传感器状态初始化中用法 ID（Sensor State Initializing Usage ID）。

<a id="r_gacd020e8f8e80bf1592b750542684d915"></a>

```c
#define HID_USAGE_SENSORS_SENSOR_STATE_ACCESS_DENIED 0x805
```

相关声明：[HID_USAGE_SENSORS_SENSOR_STATE_ACCESS_DENIED](../usb/P048_HID通用定义.md#gacd020e8f8e80bf1592b750542684d915)。

HID 传感器（Sensors）的传感器状态访问被拒绝用法 ID（Sensor State Access Denied Usage ID）。

<a id="r_gaabb092d4a50f1f60298079d3e5a82242"></a>

```c
#define HID_USAGE_SENSORS_SENSOR_STATE_ERROR 0x806
```

相关声明：[HID_USAGE_SENSORS_SENSOR_STATE_ERROR](../usb/P048_HID通用定义.md#gaabb092d4a50f1f60298079d3e5a82242)。

HID 传感器（Sensors）的传感器状态错误用法 ID（Sensor State Error Usage ID）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 13.2\_枚举（Enumerations）

<a id="r_ga4f2bb15109c64695f852afd6bd99e3bf"></a>

```c
enum hid_kbd_code { HID_KEY_A = 4 , HID_KEY_B = 5 , HID_KEY_C = 6 , HID_KEY_D = 7 , HID_KEY_E = 8 , HID_KEY_F = 9 , HID_KEY_G = 10 , HID_KEY_H = 11 , HID_KEY_I = 12 , HID_KEY_J = 13 , HID_KEY_K = 14 , HID_KEY_L = 15 , HID_KEY_M = 16 , HID_KEY_N = 17 , HID_KEY_O = 18 , HID_KEY_P = 19 , HID_KEY_Q = 20 , HID_KEY_R = 21 , HID_KEY_S = 22 , HID_KEY_T = 23 , HID_KEY_U = 24 , HID_KEY_V = 25 , HID_KEY_W = 26 , HID_KEY_X = 27 , HID_KEY_Y = 28 , HID_KEY_Z = 29 , HID_KEY_1 = 30 , HID_KEY_2 = 31 , HID_KEY_3 = 32 , HID_KEY_4 = 33 , HID_KEY_5 = 34 , HID_KEY_6 = 35 , HID_KEY_7 = 36 , HID_KEY_8 = 37 , HID_KEY_9 = 38 , HID_KEY_0 = 39 , HID_KEY_ENTER = 40 , HID_KEY_ESC = 41 , HID_KEY_BACKSPACE = 42 , HID_KEY_TAB = 43 , HID_KEY_SPACE = 44 , HID_KEY_MINUS = 45 , HID_KEY_EQUAL = 46 , HID_KEY_LEFTBRACE = 47 , HID_KEY_RIGHTBRACE = 48 , HID_KEY_BACKSLASH = 49 , HID_KEY_HASH = 50 , HID_KEY_SEMICOLON = 51 , HID_KEY_APOSTROPHE = 52 , HID_KEY_GRAVE = 53 , HID_KEY_COMMA = 54 , HID_KEY_DOT = 55 , HID_KEY_SLASH = 56 , HID_KEY_CAPSLOCK = 57 , HID_KEY_F1 = 58 , HID_KEY_F2 = 59 , HID_KEY_F3 = 60 , HID_KEY_F4 = 61 , HID_KEY_F5 = 62 , HID_KEY_F6 = 63 , HID_KEY_F7 = 64 , HID_KEY_F8 = 65 , HID_KEY_F9 = 66 , HID_KEY_F10 = 67 , HID_KEY_F11 = 68 , HID_KEY_F12 = 69 , HID_KEY_SYSRQ = 70 , HID_KEY_SCROLLLOCK = 71 , HID_KEY_PAUSE = 72 , HID_KEY_INSERT = 73 , HID_KEY_HOME = 74 , HID_KEY_PAGEUP = 75 , HID_KEY_DELETE = 76 , HID_KEY_END = 77 , HID_KEY_PAGEDOWN = 78 , HID_KEY_RIGHT = 79 , HID_KEY_LEFT = 80 , HID_KEY_DOWN = 81 , HID_KEY_UP = 82 , HID_KEY_NUMLOCK = 83 , HID_KEY_KPSLASH = 84 , HID_KEY_KPASTERISK = 85 , HID_KEY_KPMINUS = 86 , HID_KEY_KPPLUS = 87 , HID_KEY_KPENTER = 88 , HID_KEY_KP_1 = 89 , HID_KEY_KP_2 = 90 , HID_KEY_KP_3 = 91 , HID_KEY_KP_4 = 92 , HID_KEY_KP_5 = 93 , HID_KEY_KP_6 = 94 , HID_KEY_KP_7 = 95 , HID_KEY_KP_8 = 96 , HID_KEY_KP_9 = 97 , HID_KEY_KP_0 = 98 , HID_KEY_KPDOT = 99 , HID_KEY_MENU = 101 }
```

相关声明：[hid_kbd_code](../usb/P050_HID报告描述符构造宏.md#ga4f2bb15109c64695f852afd6bd99e3bf)、[HID_KEY_A](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa5413afa6a28a21dd52f07db101f2d139)、[HID_KEY_B](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfabb0b25fe8c201dc75b72c7b078f745d6)、[HID_KEY_C](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa932c610512cc99157654c3997bc2b922)、[HID_KEY_D](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfabc172093417a4c40a7443eee551e9700)、[HID_KEY_E](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfaff7192b9ddd4228e02c44b6fb2d7bf85)、[HID_KEY_F](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfacc002ca9f0f3bdc01b4de42d00e5560b)、[HID_KEY_G](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa1eadd56346bbd64b1c33fa5393f65bda)、[HID_KEY_H](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa4bfc341fccde664ec9267af6e705ba0c)、[HID_KEY_I](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfafcd25dc5bba218f7097698f8f49fdc45)、[HID_KEY_J](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa2a78196208c634941d63429cd1e1df7a)、[HID_KEY_K](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa4ceddaaaa90d84f0afb3e1ee9a35a976)、[HID_KEY_L](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfaf5de66adc9eb2aa183eab1e23f977894)、[HID_KEY_M](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa4f8174feca1eb72901576c4e24c8f8a9)、[HID_KEY_N](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfab4d202043e8b0b7a8c2d4c519fd1eb07)、[HID_KEY_O](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfad8884ef7e77722099e6bd61265f6564c)、[HID_KEY_P](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfaca0480331288d15eccec9f072f123817)、[HID_KEY_Q](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa05fb920f8129f57dd350036f17fbe519)、[HID_KEY_R](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa037de00c763ae6b270895b7a5f0f57a7)、[HID_KEY_S](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfae6a84e8474b6c3e8f9f7d344408cfa0b)、[HID_KEY_T](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa893799f48b30c438349335556a0e15b6)、[HID_KEY_U](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfab3c7c9f3a73e83623c651cdfddddeb05)、[HID_KEY_V](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa02f14e6303b4d2e4e46747324d649dda)、[HID_KEY_W](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfadf81a88f3f92f15e2abec83911bf3732)、[HID_KEY_X](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa9f3b8bb63f6628db9a1678b72ec12b6d)、[HID_KEY_Y](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa4ca2ebe26c09f2400a8ebc0aa445ce89)、[HID_KEY_Z](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfaa5cd01ad23ede98de1ae176920b8fc8f)、[HID_KEY_1](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa039ced168420140b97e2d0676e1bb12a)、[HID_KEY_2](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfae98dd71460def5e66fcf32e9783b96ea)、[HID_KEY_3](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfaf58d848786f8d2dfac702f7fae178311)、[HID_KEY_4](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa17019d72e84302486f72f7d8101baca5)、[HID_KEY_5](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfaf32ab36da2e30066c9ed2816596011c8)、[HID_KEY_6](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfae16b76c1bf9f7aa58a1b1c556a6b6022)、[HID_KEY_7](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa5887a1854f7d0787121bd75034cdd726)、[HID_KEY_8](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa1761228849d7dc2b84d0565d3337b2e2)、[HID_KEY_9](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa758aec2540a6a2153702d6905c44ce52)、[HID_KEY_0](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa856ca663233681e789ef4aa94c44ebaf)、[HID_KEY_ENTER](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfaeeab6ddad27c449cbc44ca2458912a75)、[HID_KEY_ESC](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa763b39fe76a92c4cc1fc32f47d2a760a)、[HID_KEY_BACKSPACE](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfafd6cf6a44966d518b173df4ed57ae720)、[HID_KEY_TAB](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa5a6c79e8ea85f6593c06d19098d69a03)、[HID_KEY_SPACE](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfaf4fc3d7b4b86f9f095cec624d190ebec)、[HID_KEY_MINUS](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfaa59864204064d3e8fac5271b69a7da23)、[HID_KEY_EQUAL](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfac8d82858905175ba79c24b0be1b1b1a8)、[HID_KEY_LEFTBRACE](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfac232473666b21ca772c84b68be6c1f3d)、[HID_KEY_RIGHTBRACE](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfaef692bd882621d292255cb99d4697513)、[HID_KEY_BACKSLASH](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa25ba5457bc128593b1624d95ec536182)、[HID_KEY_HASH](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa0d57ce7c99d06ee9b15fef880af075eb)、[HID_KEY_SEMICOLON](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa3743f920856a12e726e1be05932c7411)、[HID_KEY_APOSTROPHE](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa7325a5bd52e9dc0cc38a85609b1c55ab)、[HID_KEY_GRAVE](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa8b84c64da5b8c5f5d99b86c1cfe09ffc)、[HID_KEY_COMMA](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfaa81aa5b3424f02fdf02295de47b11b19)、[HID_KEY_DOT](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa403fe927ebb0014e2c1b3dc25e1d9779)、[HID_KEY_SLASH](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa24c2c93a1c895745828311affc011dea)、[HID_KEY_CAPSLOCK](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa4d40549a59fdcfdd0b2d592a6675bc89)、[HID_KEY_F1](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa9642163abbbad8aa5c7088c8529aadd7)、[HID_KEY_F2](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa9ce331f5f41ba3e3e05f485bc2d4138e)、[HID_KEY_F3](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa76adde1d9295cf62e7efb35e27911a1e)、[HID_KEY_F4](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfaa9956a2b95afe1a05fda65db5cc66467)、[HID_KEY_F5](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bface9e8d409d981f193f69fc5b29f38ca7)、[HID_KEY_F6](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfabc92147e725c8108c18f4e03005afbdc)、[HID_KEY_F7](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa1e2eabf8b9fa6cbfea613696b2c4122a)、[HID_KEY_F8](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa5092add2863231d273ba60cd583ebe33)、[HID_KEY_F9](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa5a09deabde1a3a44378b7de44dad27b6)、[HID_KEY_F10](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfac2c4a3aec85b4d8171de4429ccabbe19)、[HID_KEY_F11](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa76bb35a0f71733b0a0f1bd7e3837064c)、[HID_KEY_F12](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfab44ba4426c1574f4b296794b7bfe2172)、[HID_KEY_SYSRQ](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfae5405b62cb20962cb5864ba6e90a4ab2)、[HID_KEY_SCROLLLOCK](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfae16bd57629c7aba96a554d0446e83d98)、[HID_KEY_PAUSE](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa1905733a0fe81f78e0752e3b0bb99c69)、[HID_KEY_INSERT](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa1e1c320cea0644c3dc38da06c865837b)、[HID_KEY_HOME](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa5fc1127fe9014018f4831cbf272c883b)、[HID_KEY_PAGEUP](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa2468ac3b37d38b6158cd989ed54bcd8c)、[HID_KEY_DELETE](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfae8f5051cb476c3e9253b008094c431fc)、[HID_KEY_END](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa8f933f0f6e5a1a3c3cdc1819ffcdce63)、[HID_KEY_PAGEDOWN](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfaf7615ff4f608d64ae20a61540d939065)、[HID_KEY_RIGHT](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa4c203feb452e3212089e8246b8d75f6c)、[HID_KEY_LEFT](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfaf7d3c678a8ac31916068a0c5aff54d4b)、[HID_KEY_DOWN](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa9e2597c2a109abda1c63c8d5ca5376b3)、[HID_KEY_UP](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfaf5fe431b55adf16d82604e0fc2239090)、[HID_KEY_NUMLOCK](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfafec8c71efd5ee9decd156f0d33739fbe)、[HID_KEY_KPSLASH](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa44e83040efab214dcfe462ac0d338e0c)、[HID_KEY_KPASTERISK](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfaff47eb8157a7118183573e3aefb7df08)、[HID_KEY_KPMINUS](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa6fb35c78b12ae434cb7a7280501886e9)、[HID_KEY_KPPLUS](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa2cb7852467d2ebd785e2f7556383a883)、[HID_KEY_KPENTER](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfab5b923992d0bdc176f716cd8ace3a66e)、[HID_KEY_KP_1](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa7eea75b0eb4b4f0306daa3e6fccf09e4)、[HID_KEY_KP_2](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa68db65e7002e7cc599394a7eea116e3c)、[HID_KEY_KP_3](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa4210f9a5ae469c8b863b28b9b2d8189d)、[HID_KEY_KP_4](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa48eefeeb48a942eaaa0726bd4a2df01d)、[HID_KEY_KP_5](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa1b8d299d56a0289ae15cbf8c67e36a7c)、[HID_KEY_KP_6](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa90f2c51ad42e335a474061c4d5e4e5a9)、[HID_KEY_KP_7](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa1e191017084fadf830a7394de0e1cc05)、[HID_KEY_KP_8](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfadd7c795e2c9c212a4adeaba904bda447)、[HID_KEY_KP_9](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bface8d41615c6afd45724f4b6d16238c36)、[HID_KEY_KP_0](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa4ae4af2b06f6f2585a598353bfef9af7)、[HID_KEY_KPDOT](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa9f26dd9d2aaa5d328481715764dbb1b9)、[HID_KEY_MENU](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa4b07b1bbe7695f2f67ce9df298c1d3c7)。

HID 键盘按键编码（Keyboard Button Codes）。

<a id="r_ga12f11556b697518b00fa86eb040f9eb8"></a>

```c
enum hid_kbd_modifier { HID_KBD_MODIFIER_NONE = 0x00 , HID_KBD_MODIFIER_LEFT_CTRL = 0x01 , HID_KBD_MODIFIER_LEFT_SHIFT = 0x02 , HID_KBD_MODIFIER_LEFT_ALT = 0x04 , HID_KBD_MODIFIER_LEFT_UI = 0x08 , HID_KBD_MODIFIER_RIGHT_CTRL = 0x10 , HID_KBD_MODIFIER_RIGHT_SHIFT = 0x20 , HID_KBD_MODIFIER_RIGHT_ALT = 0x40 , HID_KBD_MODIFIER_RIGHT_UI = 0x80 }
```

相关声明：[hid_kbd_modifier](../usb/P050_HID报告描述符构造宏.md#ga12f11556b697518b00fa86eb040f9eb8)、[HID_KBD_MODIFIER_NONE](../usb/P050_HID报告描述符构造宏.md#gga12f11556b697518b00fa86eb040f9eb8a79b0eb4f485bedb745180f1b8798c603)、[HID_KBD_MODIFIER_LEFT_CTRL](../usb/P050_HID报告描述符构造宏.md#gga12f11556b697518b00fa86eb040f9eb8a4df663509a05599fd66657cfc90a37c7)、[HID_KBD_MODIFIER_LEFT_SHIFT](../usb/P050_HID报告描述符构造宏.md#gga12f11556b697518b00fa86eb040f9eb8aba69ca183306d3d1427b66666803e57f)、[HID_KBD_MODIFIER_LEFT_ALT](../usb/P050_HID报告描述符构造宏.md#gga12f11556b697518b00fa86eb040f9eb8a829d884291b546c0e276afa4ad92ac18)、[HID_KBD_MODIFIER_LEFT_UI](../usb/P050_HID报告描述符构造宏.md#gga12f11556b697518b00fa86eb040f9eb8a718c92a2d0ca9dd6603825b97a99fc77)、[HID_KBD_MODIFIER_RIGHT_CTRL](../usb/P050_HID报告描述符构造宏.md#gga12f11556b697518b00fa86eb040f9eb8a8e346c0e9c7d5b58e4b8748380423a92)、[HID_KBD_MODIFIER_RIGHT_SHIFT](../usb/P050_HID报告描述符构造宏.md#gga12f11556b697518b00fa86eb040f9eb8affdba298e8860b000a0916be7495c2dc)、[HID_KBD_MODIFIER_RIGHT_ALT](../usb/P050_HID报告描述符构造宏.md#gga12f11556b697518b00fa86eb040f9eb8a85ce29a6ab9feef68350deca92001db2)、[HID_KBD_MODIFIER_RIGHT_UI](../usb/P050_HID报告描述符构造宏.md#gga12f11556b697518b00fa86eb040f9eb8a1b4b75cd0364824cbfc80dfc68e294dd)。

HID 键盘修饰键（Keyboard Modifiers）。

<a id="r_ga8cef56ba216d0a01c6cc89f723d1740b"></a>

```c
enum hid_kbd_led { HID_KBD_LED_NUM_LOCK = 0x01 , HID_KBD_LED_CAPS_LOCK = 0x02 , HID_KBD_LED_SCROLL_LOCK = 0x04 , HID_KBD_LED_COMPOSE = 0x08 , HID_KBD_LED_KANA = 0x10 }
```

相关声明：[hid_kbd_led](../usb/P050_HID报告描述符构造宏.md#ga8cef56ba216d0a01c6cc89f723d1740b)、[HID_KBD_LED_NUM_LOCK](../usb/P050_HID报告描述符构造宏.md#gga8cef56ba216d0a01c6cc89f723d1740ba6cb2e1acb52cc5bab8dd3aa6ef6ac01b)、[HID_KBD_LED_CAPS_LOCK](../usb/P050_HID报告描述符构造宏.md#gga8cef56ba216d0a01c6cc89f723d1740baa17e5130bd8c45eb21661d8783517266)、[HID_KBD_LED_SCROLL_LOCK](../usb/P050_HID报告描述符构造宏.md#gga8cef56ba216d0a01c6cc89f723d1740ba6ea943f59b98680aefd0d5be4ef22e36)、[HID_KBD_LED_COMPOSE](../usb/P050_HID报告描述符构造宏.md#gga8cef56ba216d0a01c6cc89f723d1740bad62692e71ae45351311c8bf2ce13e3c9)、[HID_KBD_LED_KANA](../usb/P050_HID报告描述符构造宏.md#gga8cef56ba216d0a01c6cc89f723d1740bafd5d599c1955bdb1c62c7b17286b37f1)。

HID 键盘 LED（Keyboard LEDs）。


## 13.3\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_pcie_hid_reference/P009_hid.h_源码浏览.md)
- [HID_ITEM](../usb/P049_HID报告项目定义.md#ga4e9dc6652402e0b87e1313c143737ed4)
- [HID_INPUT](../usb/P049_HID报告项目定义.md#ga8646699330c45fb008d50b54be339c6c)
- [HID_OUTPUT](../usb/P049_HID报告项目定义.md#ga6ef7aa576bf69f9ba5f93df500a1403c)
- [HID_FEATURE](../usb/P049_HID报告项目定义.md#ga951a415e05e95492250d4fb43a37090d)
- [HID_COLLECTION](../usb/P049_HID报告项目定义.md#gad010ed98662b0e653754caff1dfd352f)
- [HID_END_COLLECTION](../usb/P049_HID报告项目定义.md#ga6cd6affb9d52e0bf98c7a5c83d03a764)
- [HID_ITEM_TAG_COLLECTION_END](../usb/P048_HID通用定义.md#ga3f4fe1817887966f0d05aa597cd0ab79)
- [HID_ITEM_TYPE_MAIN](../usb/P048_HID通用定义.md#ga9a71248c522943951b5af70ec9c14c02)
- [HID_USAGE_PAGE](../usb/P049_HID报告项目定义.md#ga30dc3f62583822ba27edd984dc2dec39)
- [HID_USAGE_PAGE16](../usb/P049_HID报告项目定义.md#ga4ab727e3407dc5c0b11d998314ab27de)
- [HID_LOGICAL_MIN8](../usb/P049_HID报告项目定义.md#gacd141f6ede5122f260cd50338649d458)
- [HID_LOGICAL_MAX8](../usb/P049_HID报告项目定义.md#ga2f6b809ae85b6716ade8c52da4fa56af)
- [HID_LOGICAL_MIN16](../usb/P049_HID报告项目定义.md#ga5e290798d55bccd7474dbfb6bc2d1033)
- [HID_LOGICAL_MAX16](../usb/P049_HID报告项目定义.md#ga9b804d676812dcfb0ec12f3aa887e37f)
- [HID_LOGICAL_MIN32](../usb/P049_HID报告项目定义.md#gad4b2ff8642676d692fd0d56ab0cbeaa7)
- [HID_LOGICAL_MAX32](../usb/P049_HID报告项目定义.md#gae9d17e753685b0df6c53f942ce9c95d2)
- [HID_REPORT_SIZE](../usb/P049_HID报告项目定义.md#ga3135a21a63c491daf8647fa771def0e7)
- [HID_REPORT_ID](../usb/P049_HID报告项目定义.md#ga1b45fce2c7df2847b1326fca29cef389)
- [HID_REPORT_COUNT](../usb/P049_HID报告项目定义.md#ga71192f2a55f05456b893069ebfbc5b98)
- [HID_USAGE](../usb/P049_HID报告项目定义.md#gac8429a70866a898887ead55664e04bd7)
- [HID_USAGE16](../usb/P049_HID报告项目定义.md#gaf2e338747f22f75256e57de1cf055200)
- [HID_USAGE_MIN8](../usb/P049_HID报告项目定义.md#gabf53f1e2eae6d686aeb7d62cc46b22ad)
- [HID_USAGE_MAX8](../usb/P049_HID报告项目定义.md#gae7fc9684ef10f50d69df6f495cc09e91)
- [HID_USAGE_MIN16](../usb/P049_HID报告项目定义.md#ga0dbc847d11cf64676f7cfc51b54150fa)
- [HID_USAGE_MAX16](../usb/P049_HID报告项目定义.md#gadd11a09546bc275c82e7a992cb9441cc)
- [HID_UNIT_EXPONENT](../usb/P049_HID报告项目定义.md#ga2147820c08a9b4a18d3aa162460f3967)
- [HID_MOUSE_REPORT_DESC](../usb/P050_HID报告描述符构造宏.md#ga3696f0782268d504b0c8bb540236779f)
- [HID_KEYBOARD_REPORT_DESC](../usb/P050_HID报告描述符构造宏.md#gaea973ffbe1612187c90614133956cfd6)
- [USB_HID_VERSION](../usb/P048_HID通用定义.md#ga77f649cbc5ab446b2cfe3e68eb88ac91)
- [USB_DESC_HID](../usb/P048_HID通用定义.md#ga07e8028979ff1c3d30408b08778bfd3d)
- [USB_DESC_HID_REPORT](../usb/P048_HID通用定义.md#gaca594a2caf9cb5ebac863c6c2f233f31)
- [USB_DESC_HID_PHYSICAL](../usb/P048_HID通用定义.md#ga2d543337d798d1c85436d2fee1c5be3f)
- [USB_HID_GET_REPORT](../usb/P048_HID通用定义.md#ga3d4f67db0b3531f3493cde381110809d)
- [USB_HID_GET_IDLE](../usb/P048_HID通用定义.md#ga9d69e0dae00cf3c6c5dc5602f63b2f2f)
- [USB_HID_GET_PROTOCOL](../usb/P048_HID通用定义.md#ga09469e20036a4c3df8281a2575358747)
- [USB_HID_SET_REPORT](../usb/P048_HID通用定义.md#gaed6de2caf14f9caa049fab82902299cf)
- [USB_HID_SET_IDLE](../usb/P048_HID通用定义.md#ga1cbc5f99d9bd85fca7b9a624efb41078)
- [USB_HID_SET_PROTOCOL](../usb/P048_HID通用定义.md#ga2058ed723b6a4613b4dcb8040b739684)
- [HID_BOOT_IFACE_CODE_NONE](../usb/P048_HID通用定义.md#ga953074178d707cd3538da80f36a96ff6)
- [HID_BOOT_IFACE_CODE_KEYBOARD](../usb/P048_HID通用定义.md#ga6e6276ae88c414e10c602d5e041738ab)
- [HID_BOOT_IFACE_CODE_MOUSE](../usb/P048_HID通用定义.md#ga900873d4834ea511a08b08debe62bedf)
- [HID_PROTOCOL_BOOT](../usb/P048_HID通用定义.md#gafd24e87747c82293e689f58157f06128)
- [HID_PROTOCOL_REPORT](../usb/P048_HID通用定义.md#ga982c0da911cbda6e09bd48a5e4ab85f1)
- [HID_ITEM_TYPE_GLOBAL](../usb/P048_HID通用定义.md#ga8e56e8090f1af7aae473e8a8b6832fb8)
- [HID_ITEM_TYPE_LOCAL](../usb/P048_HID通用定义.md#ga0bfb0e326d9a01072c029cba788d6456)
- [HID_ITEM_TAG_INPUT](../usb/P048_HID通用定义.md#ga66e1c50fe814fd05d61dce12ce3888c1)
- [HID_ITEM_TAG_OUTPUT](../usb/P048_HID通用定义.md#ga70c32518a6b538831e821ad30022679b)
- [HID_ITEM_TAG_COLLECTION](../usb/P048_HID通用定义.md#ga2c06052593b060466f4c338a88319485)
- [HID_ITEM_TAG_FEATURE](../usb/P048_HID通用定义.md#gaeadcca849f0a0923d9a70605c44464a6)
- [HID_ITEM_TAG_USAGE_PAGE](../usb/P048_HID通用定义.md#ga73f58fa37c0bf6698463b9d31c8a511f)
- [HID_ITEM_TAG_LOGICAL_MIN](../usb/P048_HID通用定义.md#ga034033b1ae6f4677aef82d4243c6f712)
- [HID_ITEM_TAG_LOGICAL_MAX](../usb/P048_HID通用定义.md#gaab6aec72cca41670464605d6970ad553)
- [HID_ITEM_TAG_PHYSICAL_MIN](../usb/P048_HID通用定义.md#ga6dfdd60d0b985d683a58ad752d3ef3c3)
- [HID_ITEM_TAG_PHYSICAL_MAX](../usb/P048_HID通用定义.md#gaa68bd8a73cee33d810484f4aa3f30e92)
- [HID_ITEM_TAG_UNIT_EXPONENT](../usb/P048_HID通用定义.md#ga7c6d81ee211814ec9b5d17f95e57639b)
- [HID_ITEM_TAG_UNIT](../usb/P048_HID通用定义.md#ga98267b4ff28f435d67d2a7bf1055fc7c)
- [HID_ITEM_TAG_REPORT_SIZE](../usb/P048_HID通用定义.md#ga0e6d7a56593bd25a5e15683e9271bb19)
- [HID_ITEM_TAG_REPORT_ID](../usb/P048_HID通用定义.md#ga76cd3a266ae5d5e29292d93caceece72)
- [HID_ITEM_TAG_REPORT_COUNT](../usb/P048_HID通用定义.md#ga1847701703130ce8f57547811f28b2b4)
- [HID_ITEM_TAG_USAGE](../usb/P048_HID通用定义.md#gaefd616ecaa8fc8762e65ec9d7b01f0cd)
- [HID_ITEM_TAG_USAGE_MIN](../usb/P048_HID通用定义.md#ga4e6f4133f12276f4f9fa51ab06580676)
- [HID_ITEM_TAG_USAGE_MAX](../usb/P048_HID通用定义.md#gac2a0aff74caff6c03511fc0b6db6167b)
- [HID_COLLECTION_PHYSICAL](../usb/P048_HID通用定义.md#gaca1e227f9241c217b8b1aeae6c4bd672)
- [HID_COLLECTION_APPLICATION](../usb/P048_HID通用定义.md#ga2e5e5ad0919fbaea0e6f8e5d86f4c2fd)
- [HID_COLLECTION_LOGICAL](../usb/P048_HID通用定义.md#ga904a372a663bd7d9205402a3a014c04b)
- [HID_COLLECTION_REPORT](../usb/P048_HID通用定义.md#gac58ab4780c054754b7f94ff97a152694)
- [HID_COLLECTION_NAMED_ARRAY](../usb/P048_HID通用定义.md#ga8e1610365a1556adf7121cc3b1f83080)
- [HID_COLLECTION_USAGE_SWITCH](../usb/P048_HID通用定义.md#ga64af797e424ea1e2c02c745f30721e48)
- [HID_COLLECTION_MODIFIER](../usb/P048_HID通用定义.md#gaabc1c6bed23b88f4cdc89d5347595d4f)
- [HID_USAGE_GEN_DESKTOP](../usb/P048_HID通用定义.md#gacb3fc5b0f838dfa5eb95e9e1bf52b589)
- [HID_USAGE_GEN_KEYBOARD](../usb/P048_HID通用定义.md#ga1fdbfffd0b343cec1480e9f0347efa5d)
- [HID_USAGE_GEN_LEDS](../usb/P048_HID通用定义.md#gae632e9a37203506c051c3cacfdf0c2c7)
- [HID_USAGE_GEN_BUTTON](../usb/P048_HID通用定义.md#ga13401731a0ead5448a0823d0f6142404)
- [HID_USAGE_SENSORS](../usb/P048_HID通用定义.md#gab5d07369bed290a78a119d54240db567)
- [HID_USAGE_GEN_DESKTOP_UNDEFINED](../usb/P048_HID通用定义.md#ga1441517d7c57529dcf726a1dd8b09a07)
- [HID_USAGE_GEN_DESKTOP_POINTER](../usb/P048_HID通用定义.md#ga77a7162980a77efa1e2e7b21942bb7dd)
- [HID_USAGE_GEN_DESKTOP_MOUSE](../usb/P048_HID通用定义.md#ga983274dd50058de26e0e86d10d50e81a)
- [HID_USAGE_GEN_DESKTOP_JOYSTICK](../usb/P048_HID通用定义.md#gada59a9f3aeaeaefc6112c7d9902b2d6d)
- [HID_USAGE_GEN_DESKTOP_GAMEPAD](../usb/P048_HID通用定义.md#ga17404e33133204a538f976d321c84ff0)
- [HID_USAGE_GEN_DESKTOP_KEYBOARD](../usb/P048_HID通用定义.md#ga0bdaa3d23c79204a1064cb53b279bd77)
- [HID_USAGE_GEN_DESKTOP_KEYPAD](../usb/P048_HID通用定义.md#ga69f8e44306828b3f44d3a7704ff07807)
- [HID_USAGE_GEN_DESKTOP_X](../usb/P048_HID通用定义.md#gae283a3558ba536e163140a3b6cdbb273)
- [HID_USAGE_GEN_DESKTOP_Y](../usb/P048_HID通用定义.md#gad1ab1f8f9c8a4a80bfc8e3a327e3b2fb)
- [HID_USAGE_GEN_DESKTOP_WHEEL](../usb/P048_HID通用定义.md#gaa8c772d412ac1ac7a36739c52f04c0a9)
- [HID_USAGE_SENSOR_TYPE_COLLECTION](../usb/P048_HID通用定义.md#ga85a9547841ea4a2e4b56ba2a58e9d0ee)
- [HID_USAGE_SENSORS_TYPE_ENVIRONMENTAL_TEMPERATURE](../usb/P048_HID通用定义.md#ga00b6e4c7d3eb1576c9f3eb7bae076bab)
- [HID_USAGE_SENSORS_EVENT_SENSOR_STATE](../usb/P048_HID通用定义.md#ga062651fd2ce433819e1d61d0488e4b7f)
- [HID_USAGE_SENSORS_PROPERTY_FRIENDLY_NAME](../usb/P048_HID通用定义.md#gaf5d0cd096b1a0591002a6438a977710c)
- [HID_USAGE_SENSORS_DATA_ENVIRONMENTAL_TEMPERATURE](../usb/P048_HID通用定义.md#ga2108b2634377a0f8860b2f7de50f21e8)
- [HID_USAGE_SENSORS_PROPERTY_TIMESTAMP](../usb/P048_HID通用定义.md#ga0f907ba7b85ff784dde9a14b38ed6fbb)
- [HID_USAGE_SENSORS_SENSOR_STATE_UNDEFINED](../usb/P048_HID通用定义.md#gaa5a61c460035086e103a4fa97b89efb6)
- [HID_USAGE_SENSORS_SENSOR_STATE_READY](../usb/P048_HID通用定义.md#gae37e00681768e24a1995a6766bd5ba77)
- [HID_USAGE_SENSORS_SENSOR_STATE_NOT_AVAILABLE](../usb/P048_HID通用定义.md#ga5c897b459ec0f68d0825b6f454a49355)
- [HID_USAGE_SENSORS_SENSOR_STATE_NO_DATA](../usb/P048_HID通用定义.md#ga6948d4190e58386e184b0376b6c67584)
- [HID_USAGE_SENSORS_SENSOR_STATE_INITIALIZING](../usb/P048_HID通用定义.md#ga347b9f96fc87f3e7f6540961e240ef5e)
- [HID_USAGE_SENSORS_SENSOR_STATE_ACCESS_DENIED](../usb/P048_HID通用定义.md#gacd020e8f8e80bf1592b750542684d915)
- [HID_USAGE_SENSORS_SENSOR_STATE_ERROR](../usb/P048_HID通用定义.md#gaabb092d4a50f1f60298079d3e5a82242)
- [hid_kbd_code](../usb/P050_HID报告描述符构造宏.md#ga4f2bb15109c64695f852afd6bd99e3bf)
- [HID_KEY_A](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa5413afa6a28a21dd52f07db101f2d139)
- [HID_KEY_B](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfabb0b25fe8c201dc75b72c7b078f745d6)
- [HID_KEY_C](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa932c610512cc99157654c3997bc2b922)
- [HID_KEY_D](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfabc172093417a4c40a7443eee551e9700)
- [HID_KEY_E](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfaff7192b9ddd4228e02c44b6fb2d7bf85)
- [HID_KEY_F](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfacc002ca9f0f3bdc01b4de42d00e5560b)
- [HID_KEY_G](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa1eadd56346bbd64b1c33fa5393f65bda)
- [HID_KEY_H](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa4bfc341fccde664ec9267af6e705ba0c)
- [HID_KEY_I](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfafcd25dc5bba218f7097698f8f49fdc45)
- [HID_KEY_J](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa2a78196208c634941d63429cd1e1df7a)
- [HID_KEY_K](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa4ceddaaaa90d84f0afb3e1ee9a35a976)
- [HID_KEY_L](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfaf5de66adc9eb2aa183eab1e23f977894)
- [HID_KEY_M](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa4f8174feca1eb72901576c4e24c8f8a9)
- [HID_KEY_N](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfab4d202043e8b0b7a8c2d4c519fd1eb07)
- [HID_KEY_O](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfad8884ef7e77722099e6bd61265f6564c)
- [HID_KEY_P](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfaca0480331288d15eccec9f072f123817)
- [HID_KEY_Q](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa05fb920f8129f57dd350036f17fbe519)
- [HID_KEY_R](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa037de00c763ae6b270895b7a5f0f57a7)
- [HID_KEY_S](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfae6a84e8474b6c3e8f9f7d344408cfa0b)
- [HID_KEY_T](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa893799f48b30c438349335556a0e15b6)
- [HID_KEY_U](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfab3c7c9f3a73e83623c651cdfddddeb05)
- [HID_KEY_V](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa02f14e6303b4d2e4e46747324d649dda)
- [HID_KEY_W](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfadf81a88f3f92f15e2abec83911bf3732)
- [HID_KEY_X](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa9f3b8bb63f6628db9a1678b72ec12b6d)
- [HID_KEY_Y](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa4ca2ebe26c09f2400a8ebc0aa445ce89)
- [HID_KEY_Z](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfaa5cd01ad23ede98de1ae176920b8fc8f)
- [HID_KEY_1](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa039ced168420140b97e2d0676e1bb12a)
- [HID_KEY_2](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfae98dd71460def5e66fcf32e9783b96ea)
- [HID_KEY_3](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfaf58d848786f8d2dfac702f7fae178311)
- [HID_KEY_4](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa17019d72e84302486f72f7d8101baca5)
- [HID_KEY_5](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfaf32ab36da2e30066c9ed2816596011c8)
- [HID_KEY_6](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfae16b76c1bf9f7aa58a1b1c556a6b6022)
- [HID_KEY_7](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa5887a1854f7d0787121bd75034cdd726)
- [HID_KEY_8](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa1761228849d7dc2b84d0565d3337b2e2)
- [HID_KEY_9](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa758aec2540a6a2153702d6905c44ce52)
- [HID_KEY_0](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa856ca663233681e789ef4aa94c44ebaf)
- [HID_KEY_ENTER](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfaeeab6ddad27c449cbc44ca2458912a75)
- [HID_KEY_ESC](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa763b39fe76a92c4cc1fc32f47d2a760a)
- [HID_KEY_BACKSPACE](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfafd6cf6a44966d518b173df4ed57ae720)
- [HID_KEY_TAB](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa5a6c79e8ea85f6593c06d19098d69a03)
- [HID_KEY_SPACE](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfaf4fc3d7b4b86f9f095cec624d190ebec)
- [HID_KEY_MINUS](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfaa59864204064d3e8fac5271b69a7da23)
- [HID_KEY_EQUAL](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfac8d82858905175ba79c24b0be1b1b1a8)
- [HID_KEY_LEFTBRACE](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfac232473666b21ca772c84b68be6c1f3d)
- [HID_KEY_RIGHTBRACE](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfaef692bd882621d292255cb99d4697513)
- [HID_KEY_BACKSLASH](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa25ba5457bc128593b1624d95ec536182)
- [HID_KEY_HASH](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa0d57ce7c99d06ee9b15fef880af075eb)
- [HID_KEY_SEMICOLON](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa3743f920856a12e726e1be05932c7411)
- [HID_KEY_APOSTROPHE](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa7325a5bd52e9dc0cc38a85609b1c55ab)
- [HID_KEY_GRAVE](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa8b84c64da5b8c5f5d99b86c1cfe09ffc)
- [HID_KEY_COMMA](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfaa81aa5b3424f02fdf02295de47b11b19)
- [HID_KEY_DOT](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa403fe927ebb0014e2c1b3dc25e1d9779)
- [HID_KEY_SLASH](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa24c2c93a1c895745828311affc011dea)
- [HID_KEY_CAPSLOCK](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa4d40549a59fdcfdd0b2d592a6675bc89)
- [HID_KEY_F1](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa9642163abbbad8aa5c7088c8529aadd7)
- [HID_KEY_F2](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa9ce331f5f41ba3e3e05f485bc2d4138e)
- [HID_KEY_F3](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa76adde1d9295cf62e7efb35e27911a1e)
- [HID_KEY_F4](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfaa9956a2b95afe1a05fda65db5cc66467)
- [HID_KEY_F5](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bface9e8d409d981f193f69fc5b29f38ca7)
- [HID_KEY_F6](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfabc92147e725c8108c18f4e03005afbdc)
- [HID_KEY_F7](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa1e2eabf8b9fa6cbfea613696b2c4122a)
- [HID_KEY_F8](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa5092add2863231d273ba60cd583ebe33)
- [HID_KEY_F9](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa5a09deabde1a3a44378b7de44dad27b6)
- [HID_KEY_F10](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfac2c4a3aec85b4d8171de4429ccabbe19)
- [HID_KEY_F11](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa76bb35a0f71733b0a0f1bd7e3837064c)
- [HID_KEY_F12](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfab44ba4426c1574f4b296794b7bfe2172)
- [HID_KEY_SYSRQ](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfae5405b62cb20962cb5864ba6e90a4ab2)
- [HID_KEY_SCROLLLOCK](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfae16bd57629c7aba96a554d0446e83d98)
- [HID_KEY_PAUSE](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa1905733a0fe81f78e0752e3b0bb99c69)
- [HID_KEY_INSERT](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa1e1c320cea0644c3dc38da06c865837b)
- [HID_KEY_HOME](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa5fc1127fe9014018f4831cbf272c883b)
- [HID_KEY_PAGEUP](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa2468ac3b37d38b6158cd989ed54bcd8c)
- [HID_KEY_DELETE](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfae8f5051cb476c3e9253b008094c431fc)
- [HID_KEY_END](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa8f933f0f6e5a1a3c3cdc1819ffcdce63)
- [HID_KEY_PAGEDOWN](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfaf7615ff4f608d64ae20a61540d939065)
- [HID_KEY_RIGHT](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa4c203feb452e3212089e8246b8d75f6c)
- [HID_KEY_LEFT](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfaf7d3c678a8ac31916068a0c5aff54d4b)
- [HID_KEY_DOWN](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa9e2597c2a109abda1c63c8d5ca5376b3)
- [HID_KEY_UP](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfaf5fe431b55adf16d82604e0fc2239090)
- [HID_KEY_NUMLOCK](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfafec8c71efd5ee9decd156f0d33739fbe)
- [HID_KEY_KPSLASH](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa44e83040efab214dcfe462ac0d338e0c)
- [HID_KEY_KPASTERISK](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfaff47eb8157a7118183573e3aefb7df08)
- [HID_KEY_KPMINUS](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa6fb35c78b12ae434cb7a7280501886e9)
- [HID_KEY_KPPLUS](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa2cb7852467d2ebd785e2f7556383a883)
- [HID_KEY_KPENTER](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfab5b923992d0bdc176f716cd8ace3a66e)
- [HID_KEY_KP_1](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa7eea75b0eb4b4f0306daa3e6fccf09e4)
- [HID_KEY_KP_2](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa68db65e7002e7cc599394a7eea116e3c)
- [HID_KEY_KP_3](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa4210f9a5ae469c8b863b28b9b2d8189d)
- [HID_KEY_KP_4](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa48eefeeb48a942eaaa0726bd4a2df01d)
- [HID_KEY_KP_5](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa1b8d299d56a0289ae15cbf8c67e36a7c)
- [HID_KEY_KP_6](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa90f2c51ad42e335a474061c4d5e4e5a9)
- [HID_KEY_KP_7](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa1e191017084fadf830a7394de0e1cc05)
- [HID_KEY_KP_8](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfadd7c795e2c9c212a4adeaba904bda447)
- [HID_KEY_KP_9](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bface8d41615c6afd45724f4b6d16238c36)
- [HID_KEY_KP_0](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa4ae4af2b06f6f2585a598353bfef9af7)
- [HID_KEY_KPDOT](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa9f26dd9d2aaa5d328481715764dbb1b9)
- [HID_KEY_MENU](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa4b07b1bbe7695f2f67ce9df298c1d3c7)
- [hid_kbd_modifier](../usb/P050_HID报告描述符构造宏.md#ga12f11556b697518b00fa86eb040f9eb8)
- [HID_KBD_MODIFIER_NONE](../usb/P050_HID报告描述符构造宏.md#gga12f11556b697518b00fa86eb040f9eb8a79b0eb4f485bedb745180f1b8798c603)
- [HID_KBD_MODIFIER_LEFT_CTRL](../usb/P050_HID报告描述符构造宏.md#gga12f11556b697518b00fa86eb040f9eb8a4df663509a05599fd66657cfc90a37c7)
- [HID_KBD_MODIFIER_LEFT_SHIFT](../usb/P050_HID报告描述符构造宏.md#gga12f11556b697518b00fa86eb040f9eb8aba69ca183306d3d1427b66666803e57f)
- [HID_KBD_MODIFIER_LEFT_ALT](../usb/P050_HID报告描述符构造宏.md#gga12f11556b697518b00fa86eb040f9eb8a829d884291b546c0e276afa4ad92ac18)
- [HID_KBD_MODIFIER_LEFT_UI](../usb/P050_HID报告描述符构造宏.md#gga12f11556b697518b00fa86eb040f9eb8a718c92a2d0ca9dd6603825b97a99fc77)
- [HID_KBD_MODIFIER_RIGHT_CTRL](../usb/P050_HID报告描述符构造宏.md#gga12f11556b697518b00fa86eb040f9eb8a8e346c0e9c7d5b58e4b8748380423a92)
- [HID_KBD_MODIFIER_RIGHT_SHIFT](../usb/P050_HID报告描述符构造宏.md#gga12f11556b697518b00fa86eb040f9eb8affdba298e8860b000a0916be7495c2dc)
- [HID_KBD_MODIFIER_RIGHT_ALT](../usb/P050_HID报告描述符构造宏.md#gga12f11556b697518b00fa86eb040f9eb8a85ce29a6ab9feef68350deca92001db2)
- [HID_KBD_MODIFIER_RIGHT_UI](../usb/P050_HID报告描述符构造宏.md#gga12f11556b697518b00fa86eb040f9eb8a1b4b75cd0364824cbfc80dfc68e294dd)
- [hid_kbd_led](../usb/P050_HID报告描述符构造宏.md#ga8cef56ba216d0a01c6cc89f723d1740b)
- [HID_KBD_LED_NUM_LOCK](../usb/P050_HID报告描述符构造宏.md#gga8cef56ba216d0a01c6cc89f723d1740ba6cb2e1acb52cc5bab8dd3aa6ef6ac01b)
- [HID_KBD_LED_CAPS_LOCK](../usb/P050_HID报告描述符构造宏.md#gga8cef56ba216d0a01c6cc89f723d1740baa17e5130bd8c45eb21661d8783517266)
- [HID_KBD_LED_SCROLL_LOCK](../usb/P050_HID报告描述符构造宏.md#gga8cef56ba216d0a01c6cc89f723d1740ba6ea943f59b98680aefd0d5be4ef22e36)
- [HID_KBD_LED_COMPOSE](../usb/P050_HID报告描述符构造宏.md#gga8cef56ba216d0a01c6cc89f723d1740bad62692e71ae45351311c8bf2ce13e3c9)
- [HID_KBD_LED_KANA](../usb/P050_HID报告描述符构造宏.md#gga8cef56ba216d0a01c6cc89f723d1740bafd5d599c1955bdb1c62c7b17286b37f1)

<a id="header-details"></a>

---

[上一章](P012_zephyr__dt-bindings__gpio__st-zio-header.h_文件参考.md) · [返回大纲](大纲.md)
