---
id: learning.zephyr-docs.usb.api-48
title: HID通用定义
kind: reference
status: maintained
domains: [zephyr, usb, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__usb__hid__definitions.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第48章\_HID通用定义

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__hid__definitions.html)。读取日期：2026-10-14；基线为保存的 `latest` 页面，HTML 摘要见[来源记录](../SOURCES.md)。

## 48.1\_阅读说明与来源

译注：本页属于[HID通用说明](P040_HID通用说明.md)及其设备接口参考，说明报告描述符、设备回调和报告传输。声明和原注释按官方页面保留，补充解释明确标为源码译注。

[本册大纲](大纲.md)提供本组第40至50章的全部字段参考。

hid.h API。

hid.h API。

引入版本（Since）：1.11。

接口版本（Version）：1.0.0。

## 48.2\_主题（Topics）

<a id="r_usb_5Fhid_5Fmk_5Freport_5Fdesc"></a>

鼠标与键盘报告描述符（Mouse and keyboard report descriptors）。



相关声明：[Mouse and keyboard report descriptors](P050_HID报告描述符构造宏.md)。

<a id="r_usb_5Fhid_5Fitems"></a>

USB HID项目辅助宏（USB HID Item helpers）。



相关声明：[USB HID Item helpers](P049_HID报告项目定义.md)。

## 48.3\_USB HID类型与值（USB HID Types and Values）

<a id="r_ga77f649cbc5ab446b2cfe3e68eb88ac91"></a>

```c
#define USB_HID_VERSION 0x0111
```

HID 规范发布版本 v1.11。

相关声明：[USB_HID_VERSION](P048_HID通用定义.md#ga77f649cbc5ab446b2cfe3e68eb88ac91)。

<a id="r_ga07e8028979ff1c3d30408b08778bfd3d"></a>

```c
#define USB_DESC_HID 0x21
```

USB HID 类的 HID 描述符类型。

相关声明：[USB_DESC_HID](P048_HID通用定义.md#ga07e8028979ff1c3d30408b08778bfd3d)。

<a id="r_gaca594a2caf9cb5ebac863c6c2f233f31"></a>

```c
#define USB_DESC_HID_REPORT 0x22
```

USB HID 类的报告描述符（Report Descriptor）类型。

相关声明：[USB_DESC_HID_REPORT](P048_HID通用定义.md#gaca594a2caf9cb5ebac863c6c2f233f31)。

<a id="r_ga2d543337d798d1c85436d2fee1c5be3f"></a>

```c
#define USB_DESC_HID_PHYSICAL 0x23
```

USB HID 类的物理描述符（Physical Descriptor）类型。

相关声明：[USB_DESC_HID_PHYSICAL](P048_HID通用定义.md#ga2d543337d798d1c85436d2fee1c5be3f)。

<a id="r_ga3d4f67db0b3531f3493cde381110809d"></a>

```c
#define USB_HID_GET_REPORT 0x01
```

USB HID 类 GetReport 的 bRequest 值。

相关声明：[USB_HID_GET_REPORT](P048_HID通用定义.md#ga3d4f67db0b3531f3493cde381110809d)。

<a id="r_ga9d69e0dae00cf3c6c5dc5602f63b2f2f"></a>

```c
#define USB_HID_GET_IDLE 0x02
```

USB HID 类 GetIdle 的 bRequest 值。

相关声明：[USB_HID_GET_IDLE](P048_HID通用定义.md#ga9d69e0dae00cf3c6c5dc5602f63b2f2f)。

<a id="r_ga09469e20036a4c3df8281a2575358747"></a>

```c
#define USB_HID_GET_PROTOCOL 0x03
```

USB HID 类 GetProtocol 的 bRequest 值。

相关声明：[USB_HID_GET_PROTOCOL](P048_HID通用定义.md#ga09469e20036a4c3df8281a2575358747)。

<a id="r_gaed6de2caf14f9caa049fab82902299cf"></a>

```c
#define USB_HID_SET_REPORT 0x09
```

USB HID 类 SetReport 的 bRequest 值。

相关声明：[USB_HID_SET_REPORT](P048_HID通用定义.md#gaed6de2caf14f9caa049fab82902299cf)。

<a id="r_ga1cbc5f99d9bd85fca7b9a624efb41078"></a>

```c
#define USB_HID_SET_IDLE 0x0A
```

USB HID 类 SetIdle 的 bRequest 值。

相关声明：[USB_HID_SET_IDLE](P048_HID通用定义.md#ga1cbc5f99d9bd85fca7b9a624efb41078)。

<a id="r_ga2058ed723b6a4613b4dcb8040b739684"></a>

```c
#define USB_HID_SET_PROTOCOL 0x0B
```

USB HID 类 SetProtocol 的 bRequest 值。

相关声明：[USB_HID_SET_PROTOCOL](P048_HID通用定义.md#ga2058ed723b6a4613b4dcb8040b739684)。

<a id="r_ga953074178d707cd3538da80f36a96ff6"></a>

```c
#define HID_BOOT_IFACE_CODE_NONE 0
```

USB HID 引导接口协议（bInterfaceProtocol）的 None 代码。

相关声明：[HID_BOOT_IFACE_CODE_NONE](P048_HID通用定义.md#ga953074178d707cd3538da80f36a96ff6)。

<a id="r_ga6e6276ae88c414e10c602d5e041738ab"></a>

```c
#define HID_BOOT_IFACE_CODE_KEYBOARD 1
```

USB HID 引导接口协议（bInterfaceProtocol）的 Keyboard 键盘代码。

相关声明：[HID_BOOT_IFACE_CODE_KEYBOARD](P048_HID通用定义.md#ga6e6276ae88c414e10c602d5e041738ab)。

<a id="r_ga900873d4834ea511a08b08debe62bedf"></a>

```c
#define HID_BOOT_IFACE_CODE_MOUSE 2
```

USB HID 引导接口协议（bInterfaceProtocol）的 Mouse 鼠标代码。

相关声明：[HID_BOOT_IFACE_CODE_MOUSE](P048_HID通用定义.md#ga900873d4834ea511a08b08debe62bedf)。

<a id="r_gafd24e87747c82293e689f58157f06128"></a>

```c
#define HID_PROTOCOL_BOOT 0
```

USB HID 类引导协议（Boot Protocol）代码。

相关声明：[HID_PROTOCOL_BOOT](P048_HID通用定义.md#gafd24e87747c82293e689f58157f06128)。

<a id="r_ga982c0da911cbda6e09bd48a5e4ab85f1"></a>

```c
#define HID_PROTOCOL_REPORT 1
```

USB HID 类报告协议（Report Protocol）代码。

相关声明：[HID_PROTOCOL_REPORT](P048_HID通用定义.md#ga982c0da911cbda6e09bd48a5e4ab85f1)。

<a id="r_ga9a71248c522943951b5af70ec9c14c02"></a>

```c
#define HID_ITEM_TYPE_MAIN 0x0
```

HID 主项目（Main Item）类型。

相关声明：[HID_ITEM_TYPE_MAIN](P048_HID通用定义.md#ga9a71248c522943951b5af70ec9c14c02)。

<a id="r_ga8e56e8090f1af7aae473e8a8b6832fb8"></a>

```c
#define HID_ITEM_TYPE_GLOBAL 0x1
```

HID 全局项目（Global Item）类型。

相关声明：[HID_ITEM_TYPE_GLOBAL](P048_HID通用定义.md#ga8e56e8090f1af7aae473e8a8b6832fb8)。

<a id="r_ga0bfb0e326d9a01072c029cba788d6456"></a>

```c
#define HID_ITEM_TYPE_LOCAL 0x2
```

HID 局部项目（Local Item）类型。

相关声明：[HID_ITEM_TYPE_LOCAL](P048_HID通用定义.md#ga0bfb0e326d9a01072c029cba788d6456)。

<a id="r_ga66e1c50fe814fd05d61dce12ce3888c1"></a>

```c
#define HID_ITEM_TAG_INPUT 0x8
```

HID 输入项目（Input Item）标签。

相关声明：[HID_ITEM_TAG_INPUT](P048_HID通用定义.md#ga66e1c50fe814fd05d61dce12ce3888c1)。

<a id="r_ga70c32518a6b538831e821ad30022679b"></a>

```c
#define HID_ITEM_TAG_OUTPUT 0x9
```

HID 输出项目（Output Item）标签。

相关声明：[HID_ITEM_TAG_OUTPUT](P048_HID通用定义.md#ga70c32518a6b538831e821ad30022679b)。

<a id="r_ga2c06052593b060466f4c338a88319485"></a>

```c
#define HID_ITEM_TAG_COLLECTION 0xA
```

HID 集合项目（Collection Item）标签。

相关声明：[HID_ITEM_TAG_COLLECTION](P048_HID通用定义.md#ga2c06052593b060466f4c338a88319485)。

<a id="r_gaeadcca849f0a0923d9a70605c44464a6"></a>

```c
#define HID_ITEM_TAG_FEATURE 0xB
```

HID 特性项目（Feature Item）标签。

相关声明：[HID_ITEM_TAG_FEATURE](P048_HID通用定义.md#gaeadcca849f0a0923d9a70605c44464a6)。

<a id="r_ga3f4fe1817887966f0d05aa597cd0ab79"></a>

```c
#define HID_ITEM_TAG_COLLECTION_END 0xC
```

HID 集合结束项目（End Collection Item）标签。

相关声明：[HID_ITEM_TAG_COLLECTION_END](P048_HID通用定义.md#ga3f4fe1817887966f0d05aa597cd0ab79)。

<a id="r_ga73f58fa37c0bf6698463b9d31c8a511f"></a>

```c
#define HID_ITEM_TAG_USAGE_PAGE 0x0
```

HID 用途页项目（Usage Page Item）标签。

相关声明：[HID_ITEM_TAG_USAGE_PAGE](P048_HID通用定义.md#ga73f58fa37c0bf6698463b9d31c8a511f)。

<a id="r_ga034033b1ae6f4677aef82d4243c6f712"></a>

```c
#define HID_ITEM_TAG_LOGICAL_MIN 0x1
```

HID 逻辑最小值项目（Logical Minimum Item）标签。

相关声明：[HID_ITEM_TAG_LOGICAL_MIN](P048_HID通用定义.md#ga034033b1ae6f4677aef82d4243c6f712)。

<a id="r_gaab6aec72cca41670464605d6970ad553"></a>

```c
#define HID_ITEM_TAG_LOGICAL_MAX 0x2
```

HID 逻辑最大值项目（Logical Maximum Item）标签。

相关声明：[HID_ITEM_TAG_LOGICAL_MAX](P048_HID通用定义.md#gaab6aec72cca41670464605d6970ad553)。

<a id="r_ga6dfdd60d0b985d683a58ad752d3ef3c3"></a>

```c
#define HID_ITEM_TAG_PHYSICAL_MIN 0x3
```

HID 物理最小值项目（Physical Minimum Item）标签。

相关声明：[HID_ITEM_TAG_PHYSICAL_MIN](P048_HID通用定义.md#ga6dfdd60d0b985d683a58ad752d3ef3c3)。

<a id="r_gaa68bd8a73cee33d810484f4aa3f30e92"></a>

```c
#define HID_ITEM_TAG_PHYSICAL_MAX 0x4
```

HID 物理最大值项目（Physical Maximum Item）标签。

相关声明：[HID_ITEM_TAG_PHYSICAL_MAX](P048_HID通用定义.md#gaa68bd8a73cee33d810484f4aa3f30e92)。

<a id="r_ga7c6d81ee211814ec9b5d17f95e57639b"></a>

```c
#define HID_ITEM_TAG_UNIT_EXPONENT 0x5
```

HID 单位指数项目（Unit Exponent Item）标签。

相关声明：[HID_ITEM_TAG_UNIT_EXPONENT](P048_HID通用定义.md#ga7c6d81ee211814ec9b5d17f95e57639b)。

<a id="r_ga98267b4ff28f435d67d2a7bf1055fc7c"></a>

```c
#define HID_ITEM_TAG_UNIT 0x6
```

HID 单位项目（Unit Item）标签。

相关声明：[HID_ITEM_TAG_UNIT](P048_HID通用定义.md#ga98267b4ff28f435d67d2a7bf1055fc7c)。

<a id="r_ga0e6d7a56593bd25a5e15683e9271bb19"></a>

```c
#define HID_ITEM_TAG_REPORT_SIZE 0x7
```

HID 报告字段大小项目（Report Size Item）标签。

相关声明：[HID_ITEM_TAG_REPORT_SIZE](P048_HID通用定义.md#ga0e6d7a56593bd25a5e15683e9271bb19)。

<a id="r_ga76cd3a266ae5d5e29292d93caceece72"></a>

```c
#define HID_ITEM_TAG_REPORT_ID 0x8
```

HID 报告 ID 项目（Report ID Item）标签。

相关声明：[HID_ITEM_TAG_REPORT_ID](P048_HID通用定义.md#ga76cd3a266ae5d5e29292d93caceece72)。

<a id="r_ga1847701703130ce8f57547811f28b2b4"></a>

```c
#define HID_ITEM_TAG_REPORT_COUNT 0x9
```

HID 报告字段数量项目（Report Count Item）标签。

相关声明：[HID_ITEM_TAG_REPORT_COUNT](P048_HID通用定义.md#ga1847701703130ce8f57547811f28b2b4)。

<a id="r_gaefd616ecaa8fc8762e65ec9d7b01f0cd"></a>

```c
#define HID_ITEM_TAG_USAGE 0x0
```

HID 用途项目（Usage Item）标签。

相关声明：[HID_ITEM_TAG_USAGE](P048_HID通用定义.md#gaefd616ecaa8fc8762e65ec9d7b01f0cd)。

<a id="r_ga4e6f4133f12276f4f9fa51ab06580676"></a>

```c
#define HID_ITEM_TAG_USAGE_MIN 0x1
```

HID 用途最小值项目（Usage Minimum Item）标签。

相关声明：[HID_ITEM_TAG_USAGE_MIN](P048_HID通用定义.md#ga4e6f4133f12276f4f9fa51ab06580676)。

<a id="r_gac2a0aff74caff6c03511fc0b6db6167b"></a>

```c
#define HID_ITEM_TAG_USAGE_MAX 0x2
```

HID 用途最大值项目（Usage Maximum Item）标签。

相关声明：[HID_ITEM_TAG_USAGE_MAX](P048_HID通用定义.md#gac2a0aff74caff6c03511fc0b6db6167b)。

<a id="r_gaca1e227f9241c217b8b1aeae6c4bd672"></a>

```c
#define HID_COLLECTION_PHYSICAL 0x00
```

物理集合（Physical Collection）类型。

相关声明：[HID_COLLECTION_PHYSICAL](P048_HID通用定义.md#gaca1e227f9241c217b8b1aeae6c4bd672)。

<a id="r_ga2e5e5ad0919fbaea0e6f8e5d86f4c2fd"></a>

```c
#define HID_COLLECTION_APPLICATION 0x01
```

应用集合（Application Collection）类型。

相关声明：[HID_COLLECTION_APPLICATION](P048_HID通用定义.md#ga2e5e5ad0919fbaea0e6f8e5d86f4c2fd)。

<a id="r_ga904a372a663bd7d9205402a3a014c04b"></a>

```c
#define HID_COLLECTION_LOGICAL 0x02
```

逻辑集合（Logical Collection）类型。

相关声明：[HID_COLLECTION_LOGICAL](P048_HID通用定义.md#ga904a372a663bd7d9205402a3a014c04b)。

<a id="r_gac58ab4780c054754b7f94ff97a152694"></a>

```c
#define HID_COLLECTION_REPORT 0x03
```

报告集合（Report Collection）类型。

相关声明：[HID_COLLECTION_REPORT](P048_HID通用定义.md#gac58ab4780c054754b7f94ff97a152694)。

<a id="r_ga8e1610365a1556adf7121cc3b1f83080"></a>

```c
#define HID_COLLECTION_NAMED_ARRAY 0x04
```

命名数组集合（Named Array Collection）类型。

相关声明：[HID_COLLECTION_NAMED_ARRAY](P048_HID通用定义.md#ga8e1610365a1556adf7121cc3b1f83080)。

<a id="r_ga64af797e424ea1e2c02c745f30721e48"></a>

```c
#define HID_COLLECTION_USAGE_SWITCH 0x05
```

用途切换集合（Usage Switch Collection）类型。

相关声明：[HID_COLLECTION_USAGE_SWITCH](P048_HID通用定义.md#ga64af797e424ea1e2c02c745f30721e48)。

<a id="r_gaabc1c6bed23b88f4cdc89d5347595d4f"></a>

```c
#define HID_COLLECTION_MODIFIER 0x06
```

修饰集合（Modifier Collection）类型。

相关声明：[HID_COLLECTION_MODIFIER](P048_HID通用定义.md#gaabc1c6bed23b88f4cdc89d5347595d4f)。

<a id="r_gacb3fc5b0f838dfa5eb95e9e1bf52b589"></a>

```c
#define HID_USAGE_GEN_DESKTOP 0x01
```

HID 通用桌面控件用途页（Generic Desktop Controls Usage Page）。

相关声明：[HID_USAGE_GEN_DESKTOP](P048_HID通用定义.md#gacb3fc5b0f838dfa5eb95e9e1bf52b589)。

<a id="r_ga1fdbfffd0b343cec1480e9f0347efa5d"></a>

```c
#define HID_USAGE_GEN_KEYBOARD 0x07
```

HID 键盘用途页（Keyboard Usage Page）。

相关声明：[HID_USAGE_GEN_KEYBOARD](P048_HID通用定义.md#ga1fdbfffd0b343cec1480e9f0347efa5d)。

<a id="r_gae632e9a37203506c051c3cacfdf0c2c7"></a>

```c
#define HID_USAGE_GEN_LEDS 0x08
```

HID LED 用途页（LEDs Usage Page）。

相关声明：[HID_USAGE_GEN_LEDS](P048_HID通用定义.md#gae632e9a37203506c051c3cacfdf0c2c7)。

<a id="r_ga13401731a0ead5448a0823d0f6142404"></a>

```c
#define HID_USAGE_GEN_BUTTON 0x09
```

HID 按钮用途页（Button Usage Page）。

相关声明：[HID_USAGE_GEN_BUTTON](P048_HID通用定义.md#ga13401731a0ead5448a0823d0f6142404)。

<a id="r_gab5d07369bed290a78a119d54240db567"></a>

```c
#define HID_USAGE_SENSORS 0x20
```

HID 传感器用途页（Sensors Usage Page）。

相关声明：[HID_USAGE_SENSORS](P048_HID通用定义.md#gab5d07369bed290a78a119d54240db567)。

<a id="r_ga1441517d7c57529dcf726a1dd8b09a07"></a>

```c
#define HID_USAGE_GEN_DESKTOP_UNDEFINED 0x00
```

HID 通用桌面的未定义用途 ID（Undefined Usage ID）。

相关声明：[HID_USAGE_GEN_DESKTOP_UNDEFINED](P048_HID通用定义.md#ga1441517d7c57529dcf726a1dd8b09a07)。

<a id="r_ga77a7162980a77efa1e2e7b21942bb7dd"></a>

```c
#define HID_USAGE_GEN_DESKTOP_POINTER 0x01
```

HID 通用桌面的指针用途 ID（Pointer Usage ID）。

相关声明：[HID_USAGE_GEN_DESKTOP_POINTER](P048_HID通用定义.md#ga77a7162980a77efa1e2e7b21942bb7dd)。

<a id="r_ga983274dd50058de26e0e86d10d50e81a"></a>

```c
#define HID_USAGE_GEN_DESKTOP_MOUSE 0x02
```

HID 通用桌面的鼠标用途 ID（Mouse Usage ID）。

相关声明：[HID_USAGE_GEN_DESKTOP_MOUSE](P048_HID通用定义.md#ga983274dd50058de26e0e86d10d50e81a)。

<a id="r_gada59a9f3aeaeaefc6112c7d9902b2d6d"></a>

```c
#define HID_USAGE_GEN_DESKTOP_JOYSTICK 0x04
```

HID 通用桌面的操纵杆用途 ID（Joystick Usage ID）。

相关声明：[HID_USAGE_GEN_DESKTOP_JOYSTICK](P048_HID通用定义.md#gada59a9f3aeaeaefc6112c7d9902b2d6d)。

<a id="r_ga17404e33133204a538f976d321c84ff0"></a>

```c
#define HID_USAGE_GEN_DESKTOP_GAMEPAD 0x05
```

HID 通用桌面的游戏手柄用途 ID（Gamepad Usage ID）。

相关声明：[HID_USAGE_GEN_DESKTOP_GAMEPAD](P048_HID通用定义.md#ga17404e33133204a538f976d321c84ff0)。

<a id="r_ga0bdaa3d23c79204a1064cb53b279bd77"></a>

```c
#define HID_USAGE_GEN_DESKTOP_KEYBOARD 0x06
```

HID 通用桌面的键盘用途 ID（Keyboard Usage ID）。

相关声明：[HID_USAGE_GEN_DESKTOP_KEYBOARD](P048_HID通用定义.md#ga0bdaa3d23c79204a1064cb53b279bd77)。

<a id="r_ga69f8e44306828b3f44d3a7704ff07807"></a>

```c
#define HID_USAGE_GEN_DESKTOP_KEYPAD 0x07
```

HID 通用桌面的小键盘用途 ID（Keypad Usage ID）。

相关声明：[HID_USAGE_GEN_DESKTOP_KEYPAD](P048_HID通用定义.md#ga69f8e44306828b3f44d3a7704ff07807)。

<a id="r_gae283a3558ba536e163140a3b6cdbb273"></a>

```c
#define HID_USAGE_GEN_DESKTOP_X 0x30
```

HID 通用桌面的 X 轴用途 ID（X Usage ID）。

相关声明：[HID_USAGE_GEN_DESKTOP_X](P048_HID通用定义.md#gae283a3558ba536e163140a3b6cdbb273)。

<a id="r_gad1ab1f8f9c8a4a80bfc8e3a327e3b2fb"></a>

```c
#define HID_USAGE_GEN_DESKTOP_Y 0x31
```

HID 通用桌面的 Y 轴用途 ID（Y Usage ID）。

相关声明：[HID_USAGE_GEN_DESKTOP_Y](P048_HID通用定义.md#gad1ab1f8f9c8a4a80bfc8e3a327e3b2fb)。

<a id="r_gaa8c772d412ac1ac7a36739c52f04c0a9"></a>

```c
#define HID_USAGE_GEN_DESKTOP_WHEEL 0x38
```

HID 通用桌面的滚轮用途 ID（Wheel Usage ID）。

相关声明：[HID_USAGE_GEN_DESKTOP_WHEEL](P048_HID通用定义.md#gaa8c772d412ac1ac7a36739c52f04c0a9)。

<a id="r_ga85a9547841ea4a2e4b56ba2a58e9d0ee"></a>

```c
#define HID_USAGE_SENSOR_TYPE_COLLECTION 0x001
```

HID 传感器集合用途 ID（Collection Usage ID）。

相关声明：[HID_USAGE_SENSOR_TYPE_COLLECTION](P048_HID通用定义.md#ga85a9547841ea4a2e4b56ba2a58e9d0ee)。

<a id="r_ga00b6e4c7d3eb1576c9f3eb7bae076bab"></a>

```c
#define HID_USAGE_SENSORS_TYPE_ENVIRONMENTAL_TEMPERATURE 0x033
```

HID 传感器的环境温度类型用途 ID（Environmental Temperature Type Usage ID）。

相关声明：[HID_USAGE_SENSORS_TYPE_ENVIRONMENTAL_TEMPERATURE](P048_HID通用定义.md#ga00b6e4c7d3eb1576c9f3eb7bae076bab)。

<a id="r_ga062651fd2ce433819e1d61d0488e4b7f"></a>

```c
#define HID_USAGE_SENSORS_EVENT_SENSOR_STATE 0x201
```

HID 传感器的传感器状态事件用途 ID（Event Sensor State Usage ID）。

相关声明：[HID_USAGE_SENSORS_EVENT_SENSOR_STATE](P048_HID通用定义.md#ga062651fd2ce433819e1d61d0488e4b7f)。

<a id="r_gaf5d0cd096b1a0591002a6438a977710c"></a>

```c
#define HID_USAGE_SENSORS_PROPERTY_FRIENDLY_NAME 0x301
```

HID 传感器的友好名称属性用途 ID（Friendly Name Property Usage ID）。

相关声明：[HID_USAGE_SENSORS_PROPERTY_FRIENDLY_NAME](P048_HID通用定义.md#gaf5d0cd096b1a0591002a6438a977710c)。

<a id="r_ga2108b2634377a0f8860b2f7de50f21e8"></a>

```c
#define HID_USAGE_SENSORS_DATA_ENVIRONMENTAL_TEMPERATURE 0x434
```

HID 传感器的环境温度数据用途 ID（Environmental Temperature Data Usage ID）。

相关声明：[HID_USAGE_SENSORS_DATA_ENVIRONMENTAL_TEMPERATURE](P048_HID通用定义.md#ga2108b2634377a0f8860b2f7de50f21e8)。

<a id="r_ga0f907ba7b85ff784dde9a14b38ed6fbb"></a>

```c
#define HID_USAGE_SENSORS_PROPERTY_TIMESTAMP 0x529
```

HID 传感器的时间戳属性用途 ID（Timestamp Property Usage ID）。

相关声明：[HID_USAGE_SENSORS_PROPERTY_TIMESTAMP](P048_HID通用定义.md#ga0f907ba7b85ff784dde9a14b38ed6fbb)。

<a id="r_gaa5a61c460035086e103a4fa97b89efb6"></a>

```c
#define HID_USAGE_SENSORS_SENSOR_STATE_UNDEFINED 0x800
```

HID 传感器的未定义状态用途 ID（Undefined Usage ID）。

相关声明：[HID_USAGE_SENSORS_SENSOR_STATE_UNDEFINED](P048_HID通用定义.md#gaa5a61c460035086e103a4fa97b89efb6)。

<a id="r_gae37e00681768e24a1995a6766bd5ba77"></a>

```c
#define HID_USAGE_SENSORS_SENSOR_STATE_READY 0x801
```

HID 传感器的就绪状态用途 ID（Ready Usage ID）。

相关声明：[HID_USAGE_SENSORS_SENSOR_STATE_READY](P048_HID通用定义.md#gae37e00681768e24a1995a6766bd5ba77)。

<a id="r_ga5c897b459ec0f68d0825b6f454a49355"></a>

```c
#define HID_USAGE_SENSORS_SENSOR_STATE_NOT_AVAILABLE 0x802
```

HID 传感器的不可用状态用途 ID（Not Available Usage ID）。

相关声明：[HID_USAGE_SENSORS_SENSOR_STATE_NOT_AVAILABLE](P048_HID通用定义.md#ga5c897b459ec0f68d0825b6f454a49355)。

<a id="r_ga6948d4190e58386e184b0376b6c67584"></a>

```c
#define HID_USAGE_SENSORS_SENSOR_STATE_NO_DATA 0x803
```

HID 传感器的无数据状态用途 ID（No Data Usage ID）。

相关声明：[HID_USAGE_SENSORS_SENSOR_STATE_NO_DATA](P048_HID通用定义.md#ga6948d4190e58386e184b0376b6c67584)。

<a id="r_ga347b9f96fc87f3e7f6540961e240ef5e"></a>

```c
#define HID_USAGE_SENSORS_SENSOR_STATE_INITIALIZING 0x804
```

HID 传感器的初始化中状态用途 ID（Initializing Usage ID）。

相关声明：[HID_USAGE_SENSORS_SENSOR_STATE_INITIALIZING](P048_HID通用定义.md#ga347b9f96fc87f3e7f6540961e240ef5e)。

<a id="r_gacd020e8f8e80bf1592b750542684d915"></a>

```c
#define HID_USAGE_SENSORS_SENSOR_STATE_ACCESS_DENIED 0x805
```

HID 传感器的拒绝访问状态用途 ID（Access Denied Usage ID）。

相关声明：[HID_USAGE_SENSORS_SENSOR_STATE_ACCESS_DENIED](P048_HID通用定义.md#gacd020e8f8e80bf1592b750542684d915)。

<a id="r_gaabb092d4a50f1f60298079d3e5a82242"></a>

```c
#define HID_USAGE_SENSORS_SENSOR_STATE_ERROR 0x806
```

HID 传感器的错误状态用途 ID（Error Usage ID）。

相关声明：[HID_USAGE_SENSORS_SENSOR_STATE_ERROR](P048_HID通用定义.md#gaabb092d4a50f1f60298079d3e5a82242)。

## 48.4\_详细说明（Detailed Documentation）

<a id="ga6e6276ae88c414e10c602d5e041738ab"></a>

### `HID_BOOT_IFACE_CODE_KEYBOARD`

```c
#define HID_BOOT_IFACE_CODE_KEYBOARD 1
```

```c
#include <zephyr/usb/class/hid.h>
```

USB HID 引导接口协议（bInterfaceProtocol）的 Keyboard 键盘代码。

<a id="ga900873d4834ea511a08b08debe62bedf"></a>

### `HID_BOOT_IFACE_CODE_MOUSE`

```c
#define HID_BOOT_IFACE_CODE_MOUSE 2
```

```c
#include <zephyr/usb/class/hid.h>
```

USB HID 引导接口协议（bInterfaceProtocol）的 Mouse 鼠标代码。

<a id="ga953074178d707cd3538da80f36a96ff6"></a>

### `HID_BOOT_IFACE_CODE_NONE`

```c
#define HID_BOOT_IFACE_CODE_NONE 0
```

```c
#include <zephyr/usb/class/hid.h>
```

USB HID 引导接口协议（bInterfaceProtocol）的 None 代码。

<a id="ga2e5e5ad0919fbaea0e6f8e5d86f4c2fd"></a>

### `HID_COLLECTION_APPLICATION`

```c
#define HID_COLLECTION_APPLICATION 0x01
```

```c
#include <zephyr/usb/class/hid.h>
```

应用集合（Application Collection）类型。

<a id="ga904a372a663bd7d9205402a3a014c04b"></a>

### `HID_COLLECTION_LOGICAL`

```c
#define HID_COLLECTION_LOGICAL 0x02
```

```c
#include <zephyr/usb/class/hid.h>
```

逻辑集合（Logical Collection）类型。

<a id="gaabc1c6bed23b88f4cdc89d5347595d4f"></a>

### `HID_COLLECTION_MODIFIER`

```c
#define HID_COLLECTION_MODIFIER 0x06
```

```c
#include <zephyr/usb/class/hid.h>
```

修饰集合（Modifier Collection）类型。

<a id="ga8e1610365a1556adf7121cc3b1f83080"></a>

### `HID_COLLECTION_NAMED_ARRAY`

```c
#define HID_COLLECTION_NAMED_ARRAY 0x04
```

```c
#include <zephyr/usb/class/hid.h>
```

命名数组集合（Named Array Collection）类型。

<a id="gaca1e227f9241c217b8b1aeae6c4bd672"></a>

### `HID_COLLECTION_PHYSICAL`

```c
#define HID_COLLECTION_PHYSICAL 0x00
```

```c
#include <zephyr/usb/class/hid.h>
```

物理集合（Physical Collection）类型。

<a id="gac58ab4780c054754b7f94ff97a152694"></a>

### `HID_COLLECTION_REPORT`

```c
#define HID_COLLECTION_REPORT 0x03
```

```c
#include <zephyr/usb/class/hid.h>
```

报告集合（Report Collection）类型。

<a id="ga64af797e424ea1e2c02c745f30721e48"></a>

### `HID_COLLECTION_USAGE_SWITCH`

```c
#define HID_COLLECTION_USAGE_SWITCH 0x05
```

```c
#include <zephyr/usb/class/hid.h>
```

用途切换集合（Usage Switch Collection）类型。

<a id="ga2c06052593b060466f4c338a88319485"></a>

### `HID_ITEM_TAG_COLLECTION`

```c
#define HID_ITEM_TAG_COLLECTION 0xA
```

```c
#include <zephyr/usb/class/hid.h>
```

HID 集合项目（Collection Item）标签。

<a id="ga3f4fe1817887966f0d05aa597cd0ab79"></a>

### `HID_ITEM_TAG_COLLECTION_END`

```c
#define HID_ITEM_TAG_COLLECTION_END 0xC
```

```c
#include <zephyr/usb/class/hid.h>
```

HID 集合结束项目（End Collection Item）标签。

<a id="gaeadcca849f0a0923d9a70605c44464a6"></a>

### `HID_ITEM_TAG_FEATURE`

```c
#define HID_ITEM_TAG_FEATURE 0xB
```

```c
#include <zephyr/usb/class/hid.h>
```

HID 特性项目（Feature Item）标签。

<a id="ga66e1c50fe814fd05d61dce12ce3888c1"></a>

### `HID_ITEM_TAG_INPUT`

```c
#define HID_ITEM_TAG_INPUT 0x8
```

```c
#include <zephyr/usb/class/hid.h>
```

HID 输入项目（Input Item）标签。

<a id="gaab6aec72cca41670464605d6970ad553"></a>

### `HID_ITEM_TAG_LOGICAL_MAX`

```c
#define HID_ITEM_TAG_LOGICAL_MAX 0x2
```

```c
#include <zephyr/usb/class/hid.h>
```

HID 逻辑最大值项目（Logical Maximum Item）标签。

<a id="ga034033b1ae6f4677aef82d4243c6f712"></a>

### `HID_ITEM_TAG_LOGICAL_MIN`

```c
#define HID_ITEM_TAG_LOGICAL_MIN 0x1
```

```c
#include <zephyr/usb/class/hid.h>
```

HID 逻辑最小值项目（Logical Minimum Item）标签。

<a id="ga70c32518a6b538831e821ad30022679b"></a>

### `HID_ITEM_TAG_OUTPUT`

```c
#define HID_ITEM_TAG_OUTPUT 0x9
```

```c
#include <zephyr/usb/class/hid.h>
```

HID 输出项目（Output Item）标签。

<a id="gaa68bd8a73cee33d810484f4aa3f30e92"></a>

### `HID_ITEM_TAG_PHYSICAL_MAX`

```c
#define HID_ITEM_TAG_PHYSICAL_MAX 0x4
```

```c
#include <zephyr/usb/class/hid.h>
```

HID 物理最大值项目（Physical Maximum Item）标签。

<a id="ga6dfdd60d0b985d683a58ad752d3ef3c3"></a>

### `HID_ITEM_TAG_PHYSICAL_MIN`

```c
#define HID_ITEM_TAG_PHYSICAL_MIN 0x3
```

```c
#include <zephyr/usb/class/hid.h>
```

HID 物理最小值项目（Physical Minimum Item）标签。

<a id="ga1847701703130ce8f57547811f28b2b4"></a>

### `HID_ITEM_TAG_REPORT_COUNT`

```c
#define HID_ITEM_TAG_REPORT_COUNT 0x9
```

```c
#include <zephyr/usb/class/hid.h>
```

HID 报告字段数量项目（Report Count Item）标签。

<a id="ga76cd3a266ae5d5e29292d93caceece72"></a>

### `HID_ITEM_TAG_REPORT_ID`

```c
#define HID_ITEM_TAG_REPORT_ID 0x8
```

```c
#include <zephyr/usb/class/hid.h>
```

HID 报告 ID 项目（Report ID Item）标签。

<a id="ga0e6d7a56593bd25a5e15683e9271bb19"></a>

### `HID_ITEM_TAG_REPORT_SIZE`

```c
#define HID_ITEM_TAG_REPORT_SIZE 0x7
```

```c
#include <zephyr/usb/class/hid.h>
```

HID 报告字段大小项目（Report Size Item）标签。

<a id="ga98267b4ff28f435d67d2a7bf1055fc7c"></a>

### `HID_ITEM_TAG_UNIT`

```c
#define HID_ITEM_TAG_UNIT 0x6
```

```c
#include <zephyr/usb/class/hid.h>
```

HID 单位项目（Unit Item）标签。

<a id="ga7c6d81ee211814ec9b5d17f95e57639b"></a>

### `HID_ITEM_TAG_UNIT_EXPONENT`

```c
#define HID_ITEM_TAG_UNIT_EXPONENT 0x5
```

```c
#include <zephyr/usb/class/hid.h>
```

HID 单位指数项目（Unit Exponent Item）标签。

<a id="gaefd616ecaa8fc8762e65ec9d7b01f0cd"></a>

### `HID_ITEM_TAG_USAGE`

```c
#define HID_ITEM_TAG_USAGE 0x0
```

```c
#include <zephyr/usb/class/hid.h>
```

HID 用途项目（Usage Item）标签。

<a id="gac2a0aff74caff6c03511fc0b6db6167b"></a>

### `HID_ITEM_TAG_USAGE_MAX`

```c
#define HID_ITEM_TAG_USAGE_MAX 0x2
```

```c
#include <zephyr/usb/class/hid.h>
```

HID 用途最大值项目（Usage Maximum Item）标签。

<a id="ga4e6f4133f12276f4f9fa51ab06580676"></a>

### `HID_ITEM_TAG_USAGE_MIN`

```c
#define HID_ITEM_TAG_USAGE_MIN 0x1
```

```c
#include <zephyr/usb/class/hid.h>
```

HID 用途最小值项目（Usage Minimum Item）标签。

<a id="ga73f58fa37c0bf6698463b9d31c8a511f"></a>

### `HID_ITEM_TAG_USAGE_PAGE`

```c
#define HID_ITEM_TAG_USAGE_PAGE 0x0
```

```c
#include <zephyr/usb/class/hid.h>
```

HID 用途页项目（Usage Page Item）标签。

<a id="ga8e56e8090f1af7aae473e8a8b6832fb8"></a>

### `HID_ITEM_TYPE_GLOBAL`

```c
#define HID_ITEM_TYPE_GLOBAL 0x1
```

```c
#include <zephyr/usb/class/hid.h>
```

HID 全局项目（Global Item）类型。

<a id="ga0bfb0e326d9a01072c029cba788d6456"></a>

### `HID_ITEM_TYPE_LOCAL`

```c
#define HID_ITEM_TYPE_LOCAL 0x2
```

```c
#include <zephyr/usb/class/hid.h>
```

HID 局部项目（Local Item）类型。

<a id="ga9a71248c522943951b5af70ec9c14c02"></a>

### `HID_ITEM_TYPE_MAIN`

```c
#define HID_ITEM_TYPE_MAIN 0x0
```

```c
#include <zephyr/usb/class/hid.h>
```

HID 主项目（Main Item）类型。

<a id="gafd24e87747c82293e689f58157f06128"></a>

### `HID_PROTOCOL_BOOT`

```c
#define HID_PROTOCOL_BOOT 0
```

```c
#include <zephyr/usb/class/hid.h>
```

USB HID 类引导协议（Boot Protocol）代码。

> 译注（源码核对）：Boot／Report协议选择值是0／1；HID_BOOT_IFACE_CODE_NONE／KEYBOARD／MOUSE则用于接口描述符的 bInterfaceProtocol。名字相近但用途不同，不应互换。

<a id="ga982c0da911cbda6e09bd48a5e4ab85f1"></a>

### `HID_PROTOCOL_REPORT`

```c
#define HID_PROTOCOL_REPORT 1
```

```c
#include <zephyr/usb/class/hid.h>
```

USB HID 类报告协议（Report Protocol）代码。

<a id="ga13401731a0ead5448a0823d0f6142404"></a>

### `HID_USAGE_GEN_BUTTON`

```c
#define HID_USAGE_GEN_BUTTON 0x09
```

```c
#include <zephyr/usb/class/hid.h>
```

HID 按钮用途页（Button Usage Page）。

<a id="gacb3fc5b0f838dfa5eb95e9e1bf52b589"></a>

### `HID_USAGE_GEN_DESKTOP`

```c
#define HID_USAGE_GEN_DESKTOP 0x01
```

```c
#include <zephyr/usb/class/hid.h>
```

HID 通用桌面控件用途页（Generic Desktop Controls Usage Page）。

<a id="ga17404e33133204a538f976d321c84ff0"></a>

### `HID_USAGE_GEN_DESKTOP_GAMEPAD`

```c
#define HID_USAGE_GEN_DESKTOP_GAMEPAD 0x05
```

```c
#include <zephyr/usb/class/hid.h>
```

HID 通用桌面的游戏手柄用途 ID（Gamepad Usage ID）。

<a id="gada59a9f3aeaeaefc6112c7d9902b2d6d"></a>

### `HID_USAGE_GEN_DESKTOP_JOYSTICK`

```c
#define HID_USAGE_GEN_DESKTOP_JOYSTICK 0x04
```

```c
#include <zephyr/usb/class/hid.h>
```

HID 通用桌面的操纵杆用途 ID（Joystick Usage ID）。

<a id="ga0bdaa3d23c79204a1064cb53b279bd77"></a>

### `HID_USAGE_GEN_DESKTOP_KEYBOARD`

```c
#define HID_USAGE_GEN_DESKTOP_KEYBOARD 0x06
```

```c
#include <zephyr/usb/class/hid.h>
```

HID 通用桌面的键盘用途 ID（Keyboard Usage ID）。

<a id="ga69f8e44306828b3f44d3a7704ff07807"></a>

### `HID_USAGE_GEN_DESKTOP_KEYPAD`

```c
#define HID_USAGE_GEN_DESKTOP_KEYPAD 0x07
```

```c
#include <zephyr/usb/class/hid.h>
```

HID 通用桌面的小键盘用途 ID（Keypad Usage ID）。

<a id="ga983274dd50058de26e0e86d10d50e81a"></a>

### `HID_USAGE_GEN_DESKTOP_MOUSE`

```c
#define HID_USAGE_GEN_DESKTOP_MOUSE 0x02
```

```c
#include <zephyr/usb/class/hid.h>
```

HID 通用桌面的鼠标用途 ID（Mouse Usage ID）。

<a id="ga77a7162980a77efa1e2e7b21942bb7dd"></a>

### `HID_USAGE_GEN_DESKTOP_POINTER`

```c
#define HID_USAGE_GEN_DESKTOP_POINTER 0x01
```

```c
#include <zephyr/usb/class/hid.h>
```

HID 通用桌面的指针用途 ID（Pointer Usage ID）。

<a id="ga1441517d7c57529dcf726a1dd8b09a07"></a>

### `HID_USAGE_GEN_DESKTOP_UNDEFINED`

```c
#define HID_USAGE_GEN_DESKTOP_UNDEFINED 0x00
```

```c
#include <zephyr/usb/class/hid.h>
```

HID 通用桌面的未定义用途 ID（Undefined Usage ID）。

<a id="gaa8c772d412ac1ac7a36739c52f04c0a9"></a>

### `HID_USAGE_GEN_DESKTOP_WHEEL`

```c
#define HID_USAGE_GEN_DESKTOP_WHEEL 0x38
```

```c
#include <zephyr/usb/class/hid.h>
```

HID 通用桌面的滚轮用途 ID（Wheel Usage ID）。

<a id="gae283a3558ba536e163140a3b6cdbb273"></a>

### `HID_USAGE_GEN_DESKTOP_X`

```c
#define HID_USAGE_GEN_DESKTOP_X 0x30
```

```c
#include <zephyr/usb/class/hid.h>
```

HID 通用桌面的 X 轴用途 ID（X Usage ID）。

<a id="gad1ab1f8f9c8a4a80bfc8e3a327e3b2fb"></a>

### `HID_USAGE_GEN_DESKTOP_Y`

```c
#define HID_USAGE_GEN_DESKTOP_Y 0x31
```

```c
#include <zephyr/usb/class/hid.h>
```

HID 通用桌面的 Y 轴用途 ID（Y Usage ID）。

<a id="ga1fdbfffd0b343cec1480e9f0347efa5d"></a>

### `HID_USAGE_GEN_KEYBOARD`

```c
#define HID_USAGE_GEN_KEYBOARD 0x07
```

```c
#include <zephyr/usb/class/hid.h>
```

HID 键盘用途页（Keyboard Usage Page）。

<a id="gae632e9a37203506c051c3cacfdf0c2c7"></a>

### `HID_USAGE_GEN_LEDS`

```c
#define HID_USAGE_GEN_LEDS 0x08
```

```c
#include <zephyr/usb/class/hid.h>
```

HID LED 用途页（LEDs Usage Page）。

<a id="ga85a9547841ea4a2e4b56ba2a58e9d0ee"></a>

### `HID_USAGE_SENSOR_TYPE_COLLECTION`

```c
#define HID_USAGE_SENSOR_TYPE_COLLECTION 0x001
```

```c
#include <zephyr/usb/class/hid.h>
```

HID 传感器集合用途 ID（Collection Usage ID）。

<a id="gab5d07369bed290a78a119d54240db567"></a>

### `HID_USAGE_SENSORS`

```c
#define HID_USAGE_SENSORS 0x20
```

```c
#include <zephyr/usb/class/hid.h>
```

HID 传感器用途页（Sensors Usage Page）。

<a id="ga2108b2634377a0f8860b2f7de50f21e8"></a>

### `HID_USAGE_SENSORS_DATA_ENVIRONMENTAL_TEMPERATURE`

```c
#define HID_USAGE_SENSORS_DATA_ENVIRONMENTAL_TEMPERATURE 0x434
```

```c
#include <zephyr/usb/class/hid.h>
```

HID 传感器的环境温度数据用途 ID（Environmental Temperature Data Usage ID）。

<a id="ga062651fd2ce433819e1d61d0488e4b7f"></a>

### `HID_USAGE_SENSORS_EVENT_SENSOR_STATE`

```c
#define HID_USAGE_SENSORS_EVENT_SENSOR_STATE 0x201
```

```c
#include <zephyr/usb/class/hid.h>
```

HID 传感器的传感器状态事件用途 ID（Event Sensor State Usage ID）。

<a id="gaf5d0cd096b1a0591002a6438a977710c"></a>

### `HID_USAGE_SENSORS_PROPERTY_FRIENDLY_NAME`

```c
#define HID_USAGE_SENSORS_PROPERTY_FRIENDLY_NAME 0x301
```

```c
#include <zephyr/usb/class/hid.h>
```

HID 传感器的友好名称属性用途 ID（Friendly Name Property Usage ID）。

<a id="ga0f907ba7b85ff784dde9a14b38ed6fbb"></a>

### `HID_USAGE_SENSORS_PROPERTY_TIMESTAMP`

```c
#define HID_USAGE_SENSORS_PROPERTY_TIMESTAMP 0x529
```

```c
#include <zephyr/usb/class/hid.h>
```

HID 传感器的时间戳属性用途 ID（Timestamp Property Usage ID）。

<a id="gacd020e8f8e80bf1592b750542684d915"></a>

### `HID_USAGE_SENSORS_SENSOR_STATE_ACCESS_DENIED`

```c
#define HID_USAGE_SENSORS_SENSOR_STATE_ACCESS_DENIED 0x805
```

```c
#include <zephyr/usb/class/hid.h>
```

HID 传感器的拒绝访问状态用途 ID（Access Denied Usage ID）。

<a id="gaabb092d4a50f1f60298079d3e5a82242"></a>

### `HID_USAGE_SENSORS_SENSOR_STATE_ERROR`

```c
#define HID_USAGE_SENSORS_SENSOR_STATE_ERROR 0x806
```

```c
#include <zephyr/usb/class/hid.h>
```

HID 传感器的错误状态用途 ID（Error Usage ID）。

<a id="ga347b9f96fc87f3e7f6540961e240ef5e"></a>

### `HID_USAGE_SENSORS_SENSOR_STATE_INITIALIZING`

```c
#define HID_USAGE_SENSORS_SENSOR_STATE_INITIALIZING 0x804
```

```c
#include <zephyr/usb/class/hid.h>
```

HID 传感器的初始化中状态用途 ID（Initializing Usage ID）。

<a id="ga6948d4190e58386e184b0376b6c67584"></a>

### `HID_USAGE_SENSORS_SENSOR_STATE_NO_DATA`

```c
#define HID_USAGE_SENSORS_SENSOR_STATE_NO_DATA 0x803
```

```c
#include <zephyr/usb/class/hid.h>
```

HID 传感器的无数据状态用途 ID（No Data Usage ID）。

<a id="ga5c897b459ec0f68d0825b6f454a49355"></a>

### `HID_USAGE_SENSORS_SENSOR_STATE_NOT_AVAILABLE`

```c
#define HID_USAGE_SENSORS_SENSOR_STATE_NOT_AVAILABLE 0x802
```

```c
#include <zephyr/usb/class/hid.h>
```

HID 传感器的不可用状态用途 ID（Not Available Usage ID）。

<a id="gae37e00681768e24a1995a6766bd5ba77"></a>

### `HID_USAGE_SENSORS_SENSOR_STATE_READY`

```c
#define HID_USAGE_SENSORS_SENSOR_STATE_READY 0x801
```

```c
#include <zephyr/usb/class/hid.h>
```

HID 传感器的就绪状态用途 ID（Ready Usage ID）。

<a id="gaa5a61c460035086e103a4fa97b89efb6"></a>

### `HID_USAGE_SENSORS_SENSOR_STATE_UNDEFINED`

```c
#define HID_USAGE_SENSORS_SENSOR_STATE_UNDEFINED 0x800
```

```c
#include <zephyr/usb/class/hid.h>
```

HID 传感器的未定义状态用途 ID（Undefined Usage ID）。

<a id="ga00b6e4c7d3eb1576c9f3eb7bae076bab"></a>

### `HID_USAGE_SENSORS_TYPE_ENVIRONMENTAL_TEMPERATURE`

```c
#define HID_USAGE_SENSORS_TYPE_ENVIRONMENTAL_TEMPERATURE 0x033
```

```c
#include <zephyr/usb/class/hid.h>
```

HID 传感器的环境温度类型用途 ID（Environmental Temperature Type Usage ID）。

<a id="ga07e8028979ff1c3d30408b08778bfd3d"></a>

### `USB_DESC_HID`

```c
#define USB_DESC_HID 0x21
```

```c
#include <zephyr/usb/class/hid.h>
```

USB HID 类的 HID 描述符类型。

<a id="ga2d543337d798d1c85436d2fee1c5be3f"></a>

### `USB_DESC_HID_PHYSICAL`

```c
#define USB_DESC_HID_PHYSICAL 0x23
```

```c
#include <zephyr/usb/class/hid.h>
```

USB HID 类的物理描述符（Physical Descriptor）类型。

<a id="gaca594a2caf9cb5ebac863c6c2f233f31"></a>

### `USB_DESC_HID_REPORT`

```c
#define USB_DESC_HID_REPORT 0x22
```

```c
#include <zephyr/usb/class/hid.h>
```

USB HID 类的报告描述符（Report Descriptor）类型。

<a id="ga9d69e0dae00cf3c6c5dc5602f63b2f2f"></a>

### `USB_HID_GET_IDLE`

```c
#define USB_HID_GET_IDLE 0x02
```

```c
#include <zephyr/usb/class/hid.h>
```

USB HID 类 GetIdle 的 bRequest 值。

<a id="ga09469e20036a4c3df8281a2575358747"></a>

### `USB_HID_GET_PROTOCOL`

```c
#define USB_HID_GET_PROTOCOL 0x03
```

```c
#include <zephyr/usb/class/hid.h>
```

USB HID 类 GetProtocol 的 bRequest 值。

<a id="ga3d4f67db0b3531f3493cde381110809d"></a>

### `USB_HID_GET_REPORT`

```c
#define USB_HID_GET_REPORT 0x01
```

```c
#include <zephyr/usb/class/hid.h>
```

USB HID 类 GetReport 的 bRequest 值。

<a id="ga1cbc5f99d9bd85fca7b9a624efb41078"></a>

### `USB_HID_SET_IDLE`

```c
#define USB_HID_SET_IDLE 0x0A
```

```c
#include <zephyr/usb/class/hid.h>
```

USB HID 类 SetIdle 的 bRequest 值。

<a id="ga2058ed723b6a4613b4dcb8040b739684"></a>

### `USB_HID_SET_PROTOCOL`

```c
#define USB_HID_SET_PROTOCOL 0x0B
```

```c
#include <zephyr/usb/class/hid.h>
```

USB HID 类 SetProtocol 的 bRequest 值。

<a id="gaed6de2caf14f9caa049fab82902299cf"></a>

### `USB_HID_SET_REPORT`

```c
#define USB_HID_SET_REPORT 0x09
```

```c
#include <zephyr/usb/class/hid.h>
```

USB HID 类 SetReport 的 bRequest 值。

<a id="ga77f649cbc5ab446b2cfe3e68eb88ac91"></a>

### `USB_HID_VERSION`

```c
#define USB_HID_VERSION 0x0111
```

```c
#include <zephyr/usb/class/hid.h>
```

HID 规范发布版本 v1.11。

## 48.5\_源码跟踪与使用边界

通用项目及描述符见[hid.h](../../../include/zephyr/usb/class/hid.h)，新版接口见[usbd_hid.h](../../../include/zephyr/usb/class/usbd_hid.h)和[新版实现](../../../subsys/usb/device_next/class/usbd_hid.c)，旧接口见[usb_hid.h](../../../include/zephyr/usb/class/usb_hid.h)、[旧版实现](../../../subsys/usb/device/class/hid/core.c)及[新版兼容包装](../../../subsys/usb/device_next/class/usbd_hid_api.c)。本仓库版本可能与官方 latest 不同；译注依据保存的[官方通用头文件](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/include/zephyr/usb/class/hid.h)、[新版头文件](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/include/zephyr/usb/class/usbd_hid.h)、[新版实现](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/device_next/class/usbd_hid.c)、[兼容包装](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/device_next/class/usbd_hid_api.c)和[旧版实现](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/device/class/hid/core.c)，摘要见[来源记录](../SOURCES.md)。本批未编译、运行或操作USB硬件。

<a id="header-groups"></a>
<a id="groups"></a>
<a id="header-member-group"></a>
<a id="member-group"></a>
<a id="details"></a>
<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

[上一章](P047_旧版HID回调接口.md) · [返回大纲](大纲.md) · [下一章](P049_HID报告项目定义.md)
