---
id: learning.zephyr-docs.usb.api-172
title: USB标准请求与描述符常量
kind: reference
status: maintained
domains: [zephyr, usb, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/usb__ch9_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- Copyright (c) 2020 PHYTEC Messtechnik GmbH -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第172章\_USB标准请求与描述符常量

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/usb__ch9_8h.html)。读取日期：2026-10-14；基线为保存的 `latest` 页面，HTML 摘要见[来源记录](../SOURCES.md)。

## 172.1\_阅读说明与来源

译注：本页属于 USB 第 9 章（Chapter 9）控制请求与描述符参考。这些结构把设备、配置、接口和端点的协议字段表示为 C 声明，便于对照枚举过程及设备栈实现。原字段说明完整保留，补充的源码解释明确标为译注；[本册大纲](大纲.md)提供相关接口和示例。

USB 第 9 章（Chapter 9）的结构与定义。

```c
#include <zephyr/version.h>
```

```c
#include <zephyr/sys/util.h>
```

```c
#include <zephyr/math/ilog2.h>
```

```c
#include <zephyr/usb/class/usb_hub.h>
```

USB 第 9 章（Chapter 9）的结构与定义。

本文件包含 USB 第 9 章的结构定义，除少数例外外遵循 USB 2.0 规范。

## 172.2\_数据结构（Data Structures）

<a id="r_usb_5Freq_5Ftype_5Ffield"></a>

```c
struct usb_req_type_field
```

bmRequestType 位域（Bit Field）的表示。

相关声明：[usb_req_type_field](P170_USB请求类型位域.md)。

<a id="r_usb_5Fsetup_5Fpacket"></a>

```c
struct usb_setup_packet
```

USB 设置数据包（Setup Data Packet）。

相关声明：[usb_setup_packet](P160_USB控制请求包.md)。

<a id="r_usb_5Fdesc_5Fheader"></a>

```c
struct usb_desc_header
```

USB 描述符头（Descriptor Header）。

相关声明：[usb_desc_header](P161_USB通用描述符头.md)。

<a id="r_usb_5Fcs_5Fdesc_5Fheader"></a>

```c
struct usb_cs_desc_header
```

USB 类专用描述符头（Class-specific Descriptor Header）。

相关声明：[usb_cs_desc_header](P162_USB类专用描述符头.md)。

<a id="r_usb_5Fdevice_5Fdescriptor"></a>

```c
struct usb_device_descriptor
```

USB 标准设备描述符（Standard Device Descriptor）。

相关声明：[usb_device_descriptor](P163_USB设备描述符.md)。

<a id="r_usb_5Fdevice_5Fqualifier_5Fdescriptor"></a>

```c
struct usb_device_qualifier_descriptor
```

USB 设备限定描述符（Device Qualifier Descriptor）。

相关声明：[usb_device_qualifier_descriptor](P169_USB设备限定描述符.md)。

<a id="r_usb_5Fcfg_5Fdescriptor"></a>

```c
struct usb_cfg_descriptor
```

USB 标准配置描述符（Standard Configuration Descriptor）。

相关声明：[usb_cfg_descriptor](P164_USB配置描述符.md)。

<a id="r_usb_5Fif_5Fdescriptor"></a>

```c
struct usb_if_descriptor
```

USB 标准接口描述符（Standard Interface Descriptor）。

相关声明：[usb_if_descriptor](P165_USB接口描述符.md)。

<a id="r_usb_5Fep_5Fdesc_5Fbmattr"></a>

```c
struct usb_ep_desc_bmattr
```

端点属性位域（Endpoint Attribute Bit Fields）。

相关声明：[usb_ep_desc_bmattr](P171_USB端点属性位域.md)。

<a id="r_usb_5Fep_5Fdescriptor"></a>

```c
struct usb_ep_descriptor
```

USB 标准端点描述符（Standard Endpoint Descriptor）。

相关声明：[usb_ep_descriptor](P166_USB端点描述符.md)。

<a id="r_usb_5Fstring_5Fdescriptor"></a>

```c
struct usb_string_descriptor
```

USB Unicode 字符串描述符（String Descriptor），采用 UTF-16 小端编码（UTF-16LE）。

相关声明：[usb_string_descriptor](P168_USB字符串描述符.md)。

<a id="r_usb_5Fassociation_5Fdescriptor"></a>

```c
struct usb_association_descriptor
```

USB 3 规范中定义的 USB 关联描述符（Association Descriptor）。

相关声明：[usb_association_descriptor](P167_USB接口关联描述符.md)。

## 172.3\_宏定义（Macros）

<a id="r_ab9c7b95bb1467f3d116432ac9194e92d"></a>

```c
#define USB_REQTYPE_GET_DIR(bmRequestType)
```

从 bmRequestType 获取数据传输方向。

相关声明：[USB_REQTYPE_GET_DIR](P172_USB标准请求与描述符常量.md#ab9c7b95bb1467f3d116432ac9194e92d)。

<a id="r_a18dd1450e8fe287b2de1f8871274a3b9"></a>

```c
#define USB_REQTYPE_GET_TYPE(bmRequestType)
```

从 bmRequestType 获取请求类型。

相关声明：[USB_REQTYPE_GET_TYPE](P172_USB标准请求与描述符常量.md#a18dd1450e8fe287b2de1f8871274a3b9)。

<a id="r_a933742b41b1da36545639df1a08c0db5"></a>

```c
#define USB_REQTYPE_GET_RECIPIENT(bmRequestType)
```

从 bmRequestType 获取请求接收方。

相关声明：[USB_REQTYPE_GET_RECIPIENT](P172_USB标准请求与描述符常量.md#a933742b41b1da36545639df1a08c0db5)。

<a id="r_aa021c46e7c0e127c513adbac04bc77ba"></a>

```c
#define USB_DEC_TO_BCD(dec)
```

将十进制值转换为二进制编码的十进制表示（Binary-coded Decimal，BCD）。

相关声明：[USB_DEC_TO_BCD](P172_USB标准请求与描述符常量.md#aa021c46e7c0e127c513adbac04bc77ba)。

<a id="r_a2f6e90e87d7a1d53418ce084a293e6fc"></a>

```c
#define USB_BCD_DRN
```

USB 设备版本号（Device Release Number，对应描述符的 bcdDevice 字段）。

相关声明：[USB_BCD_DRN](P172_USB标准请求与描述符常量.md#a2f6e90e87d7a1d53418ce084a293e6fc)。

<a id="r_a2916665797ca49936ed0572fb3b39a81"></a>

```c
#define USB_GET_DESCRIPTOR_TYPE(wValue)
```

从 USB_SREQ_GET_DESCRIPTOR 请求值获取描述符类型。

相关声明：[USB_GET_DESCRIPTOR_TYPE](P172_USB标准请求与描述符常量.md#a2916665797ca49936ed0572fb3b39a81)。

<a id="r_a653a141a5084536362396149e81b6b9a"></a>

```c
#define USB_GET_DESCRIPTOR_INDEX(wValue)
```

从 USB_SREQ_GET_DESCRIPTOR 请求值获取描述符索引。

相关声明：[USB_GET_DESCRIPTOR_INDEX](P172_USB标准请求与描述符常量.md#a653a141a5084536362396149e81b6b9a)。

<a id="r_a8c4dd61ae766f50c9398c9753b4156b5"></a>

```c
#define USB_CONTROL_EP_MPS 64U
```

USB 控制端点的最大包长（Maximum Packet Size，MPS）。

相关声明：[USB_CONTROL_EP_MPS](P172_USB标准请求与描述符常量.md#a8c4dd61ae766f50c9398c9753b4156b5)。

<a id="r_afb744cb324e47124f93424a47d874b2a"></a>

```c
#define USB_EP_DIR_MASK (uint8_t)BIT(7)
```

USB 端点方向掩码（Endpoint Direction Mask）。

相关声明：[USB_EP_DIR_MASK](P172_USB标准请求与描述符常量.md#afb744cb324e47124f93424a47d874b2a)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_aae8411e95f26738326bc25a0161dde99"></a>

```c
#define USB_EP_DIR_IN (uint8_t)BIT(7)
```

USB 输入端点方向（IN，设备到主机）。

相关声明：[USB_EP_DIR_IN](P172_USB标准请求与描述符常量.md#aae8411e95f26738326bc25a0161dde99)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_a0510b0a04d9cef144e4d9793310abccf"></a>

```c
#define USB_EP_DIR_OUT 0U
```

USB 输出端点方向（OUT，主机到设备）。

相关声明：[USB_EP_DIR_OUT](P172_USB标准请求与描述符常量.md#a0510b0a04d9cef144e4d9793310abccf)。

<a id="r_a4fd2505dba51e8f198276a032d3f0523"></a>

```c
#define USB_EP_GET_IDX(ep)
```

从端点地址获取端点索引（编号）。

相关声明：[USB_EP_GET_IDX](P172_USB标准请求与描述符常量.md#a4fd2505dba51e8f198276a032d3f0523)。

<a id="r_aa974862712344d5d806d521a87549284"></a>

```c
#define USB_EP_GET_DIR(ep)
```

根据端点地址获取方向。

相关声明：[USB_EP_GET_DIR](P172_USB标准请求与描述符常量.md#aa974862712344d5d806d521a87549284)。

<a id="r_aa5963d81b4b5bee364fb0078229c71cf"></a>

```c
#define USB_EP_GET_ADDR(idx, dir)
```

根据端点索引和方向获取端点地址。

相关声明：[USB_EP_GET_ADDR](P172_USB标准请求与描述符常量.md#aa5963d81b4b5bee364fb0078229c71cf)。

<a id="r_a495d790dfb00609ce029631f40d0a422"></a>

```c
#define USB_EP_DIR_IS_IN(ep)
```

判断端点地址是否指向 IN 端点。

相关声明：[USB_EP_DIR_IS_IN](P172_USB标准请求与描述符常量.md#a495d790dfb00609ce029631f40d0a422)。

<a id="r_a1734aa980e0f135ddc7873bb1a60c1a1"></a>

```c
#define USB_EP_DIR_IS_OUT(ep)
```

判断端点地址是否指向 OUT 端点。

相关声明：[USB_EP_DIR_IS_OUT](P172_USB标准请求与描述符常量.md#a1734aa980e0f135ddc7873bb1a60c1a1)。

<a id="r_a9af36e318a50a982ebf826ef1d9e384e"></a>

```c
#define USB_CONTROL_EP_OUT (USB_EP_DIR_OUT | 0U)
```

USB 控制端点的 OUT 地址。

相关声明：[USB_CONTROL_EP_OUT](P172_USB标准请求与描述符常量.md#a9af36e318a50a982ebf826ef1d9e384e)、[USB_EP_DIR_OUT](P172_USB标准请求与描述符常量.md#a0510b0a04d9cef144e4d9793310abccf)。

<a id="r_ad907649f48bf773b010ce8fa36639b99"></a>

```c
#define USB_CONTROL_EP_IN (USB_EP_DIR_IN | 0U)
```

USB 控制端点的 IN 地址。

相关声明：[USB_CONTROL_EP_IN](P172_USB标准请求与描述符常量.md#ad907649f48bf773b010ce8fa36639b99)、[USB_EP_DIR_IN](P172_USB标准请求与描述符常量.md#aae8411e95f26738326bc25a0161dde99)。

<a id="r_a3530fe35c97b660a43bcbd573015a14a"></a>

```c
#define USB_FS_INT_EP_INTERVAL(us)
```

由以微秒为单位的数值计算全速（Full Speed，FS）中断端点的 bInterval。

相关声明：[USB_FS_INT_EP_INTERVAL](P172_USB标准请求与描述符常量.md#a3530fe35c97b660a43bcbd573015a14a)。

<a id="r_aac29193abaef01df1c81566a9029c92f"></a>

```c
#define USB_HS_INT_EP_INTERVAL(us)
```

由微秒值计算高速（High Speed，HS）中断端点的 bInterval。

相关声明：[USB_HS_INT_EP_INTERVAL](P172_USB标准请求与描述符常量.md#aac29193abaef01df1c81566a9029c92f)。

<a id="r_a00508417f5da453f39a8aac96cbba673"></a>

```c
#define USB_FS_ISO_EP_INTERVAL(us)
```

由微秒值计算全速等时（Isochronous）端点的 bInterval。

相关声明：[USB_FS_ISO_EP_INTERVAL](P172_USB标准请求与描述符常量.md#a00508417f5da453f39a8aac96cbba673)。

<a id="r_ae4facc67e3acfcc97d6e9529968ea7ca"></a>

```c
#define USB_HS_ISO_EP_INTERVAL(us)
```

由微秒值计算高速等时端点的 bInterval。

相关声明：[USB_HS_ISO_EP_INTERVAL](P172_USB标准请求与描述符常量.md#ae4facc67e3acfcc97d6e9529968ea7ca)。

<a id="r_ae028a023a157a29a0e83dee304c6267a"></a>

```c
#define USB_MPS_EP_SIZE(mps)
```

从最大包长值获取端点大小字段（Endpoint Size Field）。

相关声明：[USB_MPS_EP_SIZE](P172_USB标准请求与描述符常量.md#ae028a023a157a29a0e83dee304c6267a)。

<a id="r_ad82d2bcde8045078531a607ddf5231b2"></a>

```c
#define USB_MPS_ADDITIONAL_TRANSACTIONS(mps)
```

从 MPS 获取每个微帧（Microframe）的额外事务（Additional Transactions）数量。

相关声明：[USB_MPS_ADDITIONAL_TRANSACTIONS](P172_USB标准请求与描述符常量.md#ad82d2bcde8045078531a607ddf5231b2)。

<a id="r_a10ea5b5c35aff863958c83ee1e4c9de5"></a>

```c
#define USB_MPS_TO_TPL(mps)
```

由最大包长值计算总有效载荷长度（Total Payload Length，TPL）。

相关声明：[USB_MPS_TO_TPL](P172_USB标准请求与描述符常量.md#a10ea5b5c35aff863958c83ee1e4c9de5)。

<a id="r_a4aa386328cee14a25e8e9b4183ca1353"></a>

```c
#define USB_TPL_TO_MPS(tpl)
```

由总有效载荷长度计算最大包长值。

相关声明：[USB_TPL_TO_MPS](P172_USB标准请求与描述符常量.md#a4aa386328cee14a25e8e9b4183ca1353)。

<a id="r_af0d975aa6569cdd395e0d08d6c866a02"></a>

```c
#define USB_TPL_ROUND_UP(tpl)
```

将总有效载荷长度向上舍入为下一个有效值。

相关声明：[USB_TPL_ROUND_UP](P172_USB标准请求与描述符常量.md#af0d975aa6569cdd395e0d08d6c866a02)。

<a id="r_a9a9dc75d25540bbf34543df09a9ecd4e"></a>

```c
#define USB_TPL_IS_VALID(tpl)
```

判断总有效载荷长度值是否符合 USB 2.0 的有效性要求。

相关声明：[USB_TPL_IS_VALID](P172_USB标准请求与描述符常量.md#a9a9dc75d25540bbf34543df09a9ecd4e)。

<a id="define-members-0"></a>

**USB 设置包 RequestType 的方向值（Direction Values）。参见规范表 9-2。**

<a id="r_a3e431a6f30304833b6aa45a454c8bdbd"></a>

```c
#define USB_REQTYPE_DIR_TO_DEVICE 0
```

主机到设备的数据方向（Host-to-device）。

相关声明：[USB_REQTYPE_DIR_TO_DEVICE](P172_USB标准请求与描述符常量.md#a3e431a6f30304833b6aa45a454c8bdbd)。

<a id="r_aa080957f00a9459f9f7c533da893b31f"></a>

```c
#define USB_REQTYPE_DIR_TO_HOST 1
```

设备到主机的数据方向（Device-to-host）。

相关声明：[USB_REQTYPE_DIR_TO_HOST](P172_USB标准请求与描述符常量.md#aa080957f00a9459f9f7c533da893b31f)。

<a id="define-members-1"></a>

**USB 设置包 RequestType 的类型值（Type Values）。参见规范表 9-2。**

<a id="r_a9529fae2802d82fd37d4ad58ab9d6f67"></a>

```c
#define USB_REQTYPE_TYPE_STANDARD 0
```

标准 USB 请求（Standard USB Request）。

相关声明：[USB_REQTYPE_TYPE_STANDARD](P172_USB标准请求与描述符常量.md#a9529fae2802d82fd37d4ad58ab9d6f67)。

<a id="r_abaeb448434207462bcb312973a013f3d"></a>

```c
#define USB_REQTYPE_TYPE_CLASS 1
```

类专用请求（Class-specific Request）。

相关声明：[USB_REQTYPE_TYPE_CLASS](P172_USB标准请求与描述符常量.md#abaeb448434207462bcb312973a013f3d)。

<a id="r_ad06cc151ffddfeba7bc99b819101d11d"></a>

```c
#define USB_REQTYPE_TYPE_VENDOR 2
```

厂商专用请求（Vendor-specific Request）。

相关声明：[USB_REQTYPE_TYPE_VENDOR](P172_USB标准请求与描述符常量.md#ad06cc151ffddfeba7bc99b819101d11d)。

<a id="r_ab43bb12a355f38ea09a1dee177619b78"></a>

```c
#define USB_REQTYPE_TYPE_RESERVED 3
```

保留的请求类型（Reserved Request Type）。

相关声明：[USB_REQTYPE_TYPE_RESERVED](P172_USB标准请求与描述符常量.md#ab43bb12a355f38ea09a1dee177619b78)。

<a id="define-members-2"></a>

**USB 设置包 RequestType 的接收方值（Recipient Values）。参见规范表 9-2。**

<a id="r_ab71be1695c56514626b15d3790e3d934"></a>

```c
#define USB_REQTYPE_RECIPIENT_DEVICE 0
```

接收方为设备（Device）。

相关声明：[USB_REQTYPE_RECIPIENT_DEVICE](P172_USB标准请求与描述符常量.md#ab71be1695c56514626b15d3790e3d934)。

<a id="r_a8c2c0646290270444df73b1319232ea7"></a>

```c
#define USB_REQTYPE_RECIPIENT_INTERFACE 1
```

接收方为接口（Interface）。

相关声明：[USB_REQTYPE_RECIPIENT_INTERFACE](P172_USB标准请求与描述符常量.md#a8c2c0646290270444df73b1319232ea7)。

<a id="r_a32154b80a8d73dfb4e261d31a8d351fa"></a>

```c
#define USB_REQTYPE_RECIPIENT_ENDPOINT 2
```

接收方为端点（Endpoint）。

相关声明：[USB_REQTYPE_RECIPIENT_ENDPOINT](P172_USB标准请求与描述符常量.md#a32154b80a8d73dfb4e261d31a8d351fa)。

<a id="r_a2e07a8841cf9d67dc0c60badc00761b0"></a>

```c
#define USB_REQTYPE_RECIPIENT_OTHER 3
```

其他接收方（Other）。

相关声明：[USB_REQTYPE_RECIPIENT_OTHER](P172_USB标准请求与描述符常量.md#a2e07a8841cf9d67dc0c60badc00761b0)。

<a id="define-members-3"></a>

**USB 标准请求代码（Standard Request Codes）。参见规范表 9-4。**

<a id="r_afffb7748ffdb525572e407024df9a201"></a>

```c
#define USB_SREQ_GET_STATUS 0x00
```

获取状态请求（Get Status）。

相关声明：[USB_SREQ_GET_STATUS](P172_USB标准请求与描述符常量.md#afffb7748ffdb525572e407024df9a201)。

<a id="r_a16d58595c13caa66989d63343de6bccb"></a>

```c
#define USB_SREQ_CLEAR_FEATURE 0x01
```

清除特性请求（Clear Feature）。

相关声明：[USB_SREQ_CLEAR_FEATURE](P172_USB标准请求与描述符常量.md#a16d58595c13caa66989d63343de6bccb)。

<a id="r_ac1ef5c9fe1f3107f1a55560f81b6e25a"></a>

```c
#define USB_SREQ_SET_FEATURE 0x03
```

设置特性请求（Set Feature）。

相关声明：[USB_SREQ_SET_FEATURE](P172_USB标准请求与描述符常量.md#ac1ef5c9fe1f3107f1a55560f81b6e25a)。

<a id="r_ac20c25ea20acac5d0f4484e3d9a5c759"></a>

```c
#define USB_SREQ_SET_ADDRESS 0x05
```

设置地址请求（Set Address）。

相关声明：[USB_SREQ_SET_ADDRESS](P172_USB标准请求与描述符常量.md#ac20c25ea20acac5d0f4484e3d9a5c759)。

<a id="r_ab3b49f2eb21dcd597ca73ea62bfa5523"></a>

```c
#define USB_SREQ_GET_DESCRIPTOR 0x06
```

获取描述符请求（Get Descriptor）。

相关声明：[USB_SREQ_GET_DESCRIPTOR](P172_USB标准请求与描述符常量.md#ab3b49f2eb21dcd597ca73ea62bfa5523)。

<a id="r_ac95699668d43a49f1dd17ee86220984c"></a>

```c
#define USB_SREQ_SET_DESCRIPTOR 0x07
```

设置描述符请求（Set Descriptor）。

相关声明：[USB_SREQ_SET_DESCRIPTOR](P172_USB标准请求与描述符常量.md#ac95699668d43a49f1dd17ee86220984c)。

<a id="r_a505c325ea65c44f9df6df87bef30f5ee"></a>

```c
#define USB_SREQ_GET_CONFIGURATION 0x08
```

获取配置请求（Get Configuration）。

相关声明：[USB_SREQ_GET_CONFIGURATION](P172_USB标准请求与描述符常量.md#a505c325ea65c44f9df6df87bef30f5ee)。

<a id="r_a0f87cedfecf77bba9c52514684a13bf3"></a>

```c
#define USB_SREQ_SET_CONFIGURATION 0x09
```

设置配置请求（Set Configuration）。

相关声明：[USB_SREQ_SET_CONFIGURATION](P172_USB标准请求与描述符常量.md#a0f87cedfecf77bba9c52514684a13bf3)。

<a id="r_a26034252f1f8ddc5d7793e1ff3974764"></a>

```c
#define USB_SREQ_GET_INTERFACE 0x0A
```

获取接口请求（Get Interface）。

相关声明：[USB_SREQ_GET_INTERFACE](P172_USB标准请求与描述符常量.md#a26034252f1f8ddc5d7793e1ff3974764)。

<a id="r_acf5ea7c90528a4d9d86c279318a6cb52"></a>

```c
#define USB_SREQ_SET_INTERFACE 0x0B
```

设置接口请求（Set Interface）。

相关声明：[USB_SREQ_SET_INTERFACE](P172_USB标准请求与描述符常量.md#acf5ea7c90528a4d9d86c279318a6cb52)。

<a id="r_a390ddf7167cc081fd3d3f24f09967d06"></a>

```c
#define USB_SREQ_SYNCH_FRAME 0x0C
```

同步帧请求（Synch Frame）。

相关声明：[USB_SREQ_SYNCH_FRAME](P172_USB标准请求与描述符常量.md#a390ddf7167cc081fd3d3f24f09967d06)。

<a id="define-members-4"></a>

**描述符类型（Descriptor Types）。参见规范表 9-5。**

<a id="r_aefeff68c3a236749d1105d94ed9bad68"></a>

```c
#define USB_DESC_DEVICE 1
```

设备描述符类型（Device Descriptor Type）。

相关声明：[USB_DESC_DEVICE](P172_USB标准请求与描述符常量.md#aefeff68c3a236749d1105d94ed9bad68)。

<a id="r_a7764131f2e59070eb032bd9d68d32620"></a>

```c
#define USB_DESC_CONFIGURATION 2
```

配置描述符类型（Configuration Descriptor Type）。

相关声明：[USB_DESC_CONFIGURATION](P172_USB标准请求与描述符常量.md#a7764131f2e59070eb032bd9d68d32620)。

<a id="r_a6a5678b964f3a9b4ba2f52e9a51bebf5"></a>

```c
#define USB_DESC_STRING 3
```

字符串描述符类型（String Descriptor Type）。

相关声明：[USB_DESC_STRING](P172_USB标准请求与描述符常量.md#a6a5678b964f3a9b4ba2f52e9a51bebf5)。

<a id="r_ab98b6a1b7ec1dc4adcbd188c3a38f69f"></a>

```c
#define USB_DESC_INTERFACE 4
```

接口描述符类型（Interface Descriptor Type）。

相关声明：[USB_DESC_INTERFACE](P172_USB标准请求与描述符常量.md#ab98b6a1b7ec1dc4adcbd188c3a38f69f)。

<a id="r_a1428ae675c4b17d84b91eda705fe0498"></a>

```c
#define USB_DESC_ENDPOINT 5
```

端点描述符类型（Endpoint Descriptor Type）。

相关声明：[USB_DESC_ENDPOINT](P172_USB标准请求与描述符常量.md#a1428ae675c4b17d84b91eda705fe0498)。

<a id="r_aae4580f7a31247f2bce47af2f27b3a64"></a>

```c
#define USB_DESC_DEVICE_QUALIFIER 6
```

设备限定描述符类型（Device Qualifier Descriptor Type）。

相关声明：[USB_DESC_DEVICE_QUALIFIER](P172_USB标准请求与描述符常量.md#aae4580f7a31247f2bce47af2f27b3a64)。

<a id="r_a3a8acce20fbea73ab685bb55a4a6356d"></a>

```c
#define USB_DESC_OTHER_SPEED 7
```

其他速率配置描述符类型（Other Speed Configuration Descriptor Type）。

相关声明：[USB_DESC_OTHER_SPEED](P172_USB标准请求与描述符常量.md#a3a8acce20fbea73ab685bb55a4a6356d)。

<a id="r_a075dd47d721cfd6cdf804f3cdf0feae1"></a>

```c
#define USB_DESC_INTERFACE_POWER 8
```

接口电源描述符类型（Interface Power Descriptor Type）。

相关声明：[USB_DESC_INTERFACE_POWER](P172_USB标准请求与描述符常量.md#a075dd47d721cfd6cdf804f3cdf0feae1)。

<a id="define-members-5"></a>

**附加描述符类型（Additional Descriptor Types）。参见规范表 9-5。**

<a id="r_a162988e9c51e1094635a553999f52d51"></a>

```c
#define USB_DESC_OTG 9
```

OTG 描述符类型（On-The-Go Descriptor Type）。

相关声明：[USB_DESC_OTG](P172_USB标准请求与描述符常量.md#a162988e9c51e1094635a553999f52d51)。

<a id="r_a0a7ab16adb76e6b9af587a82d5a7fbb3"></a>

```c
#define USB_DESC_DEBUG 10
```

调试描述符类型（Debug Descriptor Type）。

相关声明：[USB_DESC_DEBUG](P172_USB标准请求与描述符常量.md#a0a7ab16adb76e6b9af587a82d5a7fbb3)。

<a id="r_ac84354aa0bfec12d3e21e72d29caf48b"></a>

```c
#define USB_DESC_INTERFACE_ASSOC 11
```

接口关联描述符类型（Interface Association Descriptor Type）。

相关声明：[USB_DESC_INTERFACE_ASSOC](P172_USB标准请求与描述符常量.md#ac84354aa0bfec12d3e21e72d29caf48b)。

<a id="r_a9f6e306632b56036d4dd7cc2430bcec9"></a>

```c
#define USB_DESC_BOS 15
```

二进制对象存储描述符类型（Binary Object Store Descriptor Type，BOS）。

相关声明：[USB_DESC_BOS](P172_USB标准请求与描述符常量.md#a9f6e306632b56036d4dd7cc2430bcec9)。

<a id="r_a8ff1997b326965664d90926658af7e98"></a>

```c
#define USB_DESC_DEVICE_CAPABILITY 16
```

设备能力描述符类型（Device Capability Descriptor Type）。

相关声明：[USB_DESC_DEVICE_CAPABILITY](P172_USB标准请求与描述符常量.md#a8ff1997b326965664d90926658af7e98)。

<a id="define-members-6"></a>

**USB 通用类规范（USB Common Class Specification）定义的类专用描述符类型（Class-Specific Descriptor Types）。**

<a id="r_a4ee3b5be16342ce919483c66cc701cb4"></a>

```c
#define USB_DESC_CS_DEVICE 0x21
```

类专用设备描述符类型（Class-specific Device Descriptor Type）。

相关声明：[USB_DESC_CS_DEVICE](P172_USB标准请求与描述符常量.md#a4ee3b5be16342ce919483c66cc701cb4)。

<a id="r_a7221e0186e4e17a624b739d1807c161d"></a>

```c
#define USB_DESC_CS_CONFIGURATION 0x22
```

类专用配置描述符类型（Class-specific Configuration Descriptor Type）。

相关声明：[USB_DESC_CS_CONFIGURATION](P172_USB标准请求与描述符常量.md#a7221e0186e4e17a624b739d1807c161d)。

<a id="r_a0a89e53a56fcadd9f7b9e08e4d9ef5f8"></a>

```c
#define USB_DESC_CS_STRING 0x23
```

类专用字符串描述符类型（Class-specific String Descriptor Type）。

相关声明：[USB_DESC_CS_STRING](P172_USB标准请求与描述符常量.md#a0a89e53a56fcadd9f7b9e08e4d9ef5f8)。

<a id="r_ae47a98df81bbd33336e11c3742418217"></a>

```c
#define USB_DESC_CS_INTERFACE 0x24
```

类专用接口描述符类型（Class-specific Interface Descriptor Type）。

相关声明：[USB_DESC_CS_INTERFACE](P172_USB标准请求与描述符常量.md#ae47a98df81bbd33336e11c3742418217)。

<a id="r_a3222223114b6d7ecea051a862fb685e2"></a>

```c
#define USB_DESC_CS_ENDPOINT 0x25
```

类专用端点描述符类型（Class-specific Endpoint Descriptor Type）。

相关声明：[USB_DESC_CS_ENDPOINT](P172_USB标准请求与描述符常量.md#a3222223114b6d7ecea051a862fb685e2)。

<a id="define-members-7"></a>

**USB 标准特性选择器（Standard Feature Selectors）。参见规范表 9-6。**

<a id="r_a78ee83859d881216f702a349e9c5133b"></a>

```c
#define USB_SFS_ENDPOINT_HALT 0x00
```

端点停滞特性选择器（Endpoint Halt Feature Selector）。

相关声明：[USB_SFS_ENDPOINT_HALT](P172_USB标准请求与描述符常量.md#a78ee83859d881216f702a349e9c5133b)。

<a id="r_a954bd576fddb8178e15bb3081733e49c"></a>

```c
#define USB_SFS_REMOTE_WAKEUP 0x01
```

远程唤醒特性选择器（Remote Wakeup Feature Selector）。

相关声明：[USB_SFS_REMOTE_WAKEUP](P172_USB标准请求与描述符常量.md#a954bd576fddb8178e15bb3081733e49c)。

<a id="r_ae2a2cf879eace08bf86d330b39578792"></a>

```c
#define USB_SFS_TEST_MODE 0x02
```

测试模式特性选择器（Test Mode Feature Selector）。

相关声明：[USB_SFS_TEST_MODE](P172_USB标准请求与描述符常量.md#ae2a2cf879eace08bf86d330b39578792)。

<a id="define-members-8"></a>

**USB 测试模式选择器（Test Mode Selectors）。参见规范表 9-7。**

<a id="r_a48567c219ecb9e0b3c0d7a1685d68cec"></a>

```c
#define USB_SFS_TEST_MODE_J 0x01
```

Test_J 测试模式（Test Mode）。

相关声明：[USB_SFS_TEST_MODE_J](P172_USB标准请求与描述符常量.md#a48567c219ecb9e0b3c0d7a1685d68cec)。

<a id="r_a2693cbe71751c0990568c01c5137f34e"></a>

```c
#define USB_SFS_TEST_MODE_K 0x02
```

Test_K 测试模式。

相关声明：[USB_SFS_TEST_MODE_K](P172_USB标准请求与描述符常量.md#a2693cbe71751c0990568c01c5137f34e)。

<a id="r_a2e36154ec5720097fda6e8fb67ab8c5f"></a>

```c
#define USB_SFS_TEST_MODE_SE0_NAK 0x03
```

Test_SE0_NAK 测试模式。

相关声明：[USB_SFS_TEST_MODE_SE0_NAK](P172_USB标准请求与描述符常量.md#a2e36154ec5720097fda6e8fb67ab8c5f)。

<a id="r_a400245449e029997eab958d1963e27fa"></a>

```c
#define USB_SFS_TEST_MODE_PACKET 0x04
```

Test_Packet 测试模式。

相关声明：[USB_SFS_TEST_MODE_PACKET](P172_USB标准请求与描述符常量.md#a400245449e029997eab958d1963e27fa)。

<a id="r_a5b4e7459b82b9d22da12e9b5dd8b5ba0"></a>

```c
#define USB_SFS_TEST_MODE_FORCE_ENABLE 0x05
```

Test_Force_Enable 测试模式。

相关声明：[USB_SFS_TEST_MODE_FORCE_ENABLE](P172_USB标准请求与描述符常量.md#a5b4e7459b82b9d22da12e9b5dd8b5ba0)。

<a id="define-members-9"></a>

**GetStatus 响应使用的位（Response Bits）。参见图 9-4。**

<a id="r_a9dd608d5ce8d45fdd76bad3df4fdf34d"></a>

```c
#define USB_GET_STATUS_SELF_POWERED BIT(0)
```

自供电状态位（Self-powered Status Bit）。

相关声明：[USB_GET_STATUS_SELF_POWERED](P172_USB标准请求与描述符常量.md#a9dd608d5ce8d45fdd76bad3df4fdf34d)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_a6d896f4f58e13f87f8e74af6909fada9"></a>

```c
#define USB_GET_STATUS_REMOTE_WAKEUP BIT(1)
```

远程唤醒状态位（Remote Wakeup Status Bit）。

相关声明：[USB_GET_STATUS_REMOTE_WAKEUP](P172_USB标准请求与描述符常量.md#a6d896f4f58e13f87f8e74af6909fada9)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="define-members-10"></a>

**USB 标准配置描述符特性（Standard Configuration Descriptor Characteristics）。参见规范表 9-10。**

<a id="r_a2a8b7c42705cd1e0fd0aecb0028cb2ba"></a>

```c
#define USB_SCD_RESERVED BIT(7)
```

保留的配置位（Reserved Configuration Bit）。

相关声明：[USB_SCD_RESERVED](P172_USB标准请求与描述符常量.md#a2a8b7c42705cd1e0fd0aecb0028cb2ba)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_a0122c49a39e67e2443e491132aa0ecfd"></a>

```c
#define USB_SCD_SELF_POWERED BIT(6)
```

自供电配置位（Self-powered Configuration Bit）。

相关声明：[USB_SCD_SELF_POWERED](P172_USB标准请求与描述符常量.md#a0122c49a39e67e2443e491132aa0ecfd)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_aa1fa7548e67cc2755d91b68fd1545088"></a>

```c
#define USB_SCD_REMOTE_WAKEUP BIT(5)
```

远程唤醒配置位（Remote Wakeup Configuration Bit）。

相关声明：[USB_SCD_REMOTE_WAKEUP](P172_USB标准请求与描述符常量.md#aa1fa7548e67cc2755d91b68fd1545088)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="define-members-11"></a>

**USB 定义的基类代码（Base Class Codes）。**

<a id="r_ae7de426be60abc372396692f11a0d087"></a>

```c
#define USB_BCC_AUDIO 0x01
```

音频设备类（Audio Device Class）。

相关声明：[USB_BCC_AUDIO](P172_USB标准请求与描述符常量.md#ae7de426be60abc372396692f11a0d087)。

<a id="r_a1d41de530a4da0ac75ff9bb875fe037e"></a>

```c
#define USB_BCC_CDC_CONTROL 0x02
```

通信设备类控制设备（Communications Device Class，CDC Control）。

相关声明：[USB_BCC_CDC_CONTROL](P172_USB标准请求与描述符常量.md#a1d41de530a4da0ac75ff9bb875fe037e)。

<a id="r_ad5904a6d6835614adc9ab914778da4a4"></a>

```c
#define USB_BCC_HID 0x03
```

人机接口设备类（Human Interface Device，HID）。

相关声明：[USB_BCC_HID](P172_USB标准请求与描述符常量.md#ad5904a6d6835614adc9ab914778da4a4)。

<a id="r_ab0c954d8432828c1a8baa63514053cf3"></a>

```c
#define USB_BCC_MASS_STORAGE 0x08
```

大容量存储设备类（Mass Storage Device Class）。

相关声明：[USB_BCC_MASS_STORAGE](P172_USB标准请求与描述符常量.md#ab0c954d8432828c1a8baa63514053cf3)。

<a id="r_a83fa62678f36459d11f9cec677990d44"></a>

```c
#define USB_BCC_CDC_DATA 0x0A
```

CDC 数据设备类（CDC Data Device Class）。

相关声明：[USB_BCC_CDC_DATA](P172_USB标准请求与描述符常量.md#a83fa62678f36459d11f9cec677990d44)。

<a id="r_a96a42b56555daa525605e124d50ecac6"></a>

```c
#define USB_BCC_VIDEO 0x0E
```

视频设备类（Video Device Class）。

相关声明：[USB_BCC_VIDEO](P172_USB标准请求与描述符常量.md#a96a42b56555daa525605e124d50ecac6)。

<a id="r_a8c2d16e36c8522008c15b8a9dc5fc32c"></a>

```c
#define USB_BCC_MCTP 0x14
```

管理组件传输协议设备类（Management Component Transport Protocol，MCTP）。

相关声明：[USB_BCC_MCTP](P172_USB标准请求与描述符常量.md#a8c2d16e36c8522008c15b8a9dc5fc32c)。

<a id="r_a960d92dd43d279b6def9a0cca3d88dc2"></a>

```c
#define USB_BCC_WIRELESS_CONTROLLER 0xE0
```

无线控制器设备类（Wireless Controller Device Class）。

相关声明：[USB_BCC_WIRELESS_CONTROLLER](P172_USB标准请求与描述符常量.md#a960d92dd43d279b6def9a0cca3d88dc2)。

<a id="r_a62bf5e94c7c36c9d1d94438d7a12a482"></a>

```c
#define USB_BCC_MISCELLANEOUS 0xEF
```

杂项设备类（Miscellaneous Device Class）。

相关声明：[USB_BCC_MISCELLANEOUS](P172_USB标准请求与描述符常量.md#a62bf5e94c7c36c9d1d94438d7a12a482)。

<a id="r_a732af05b87cb1c53dbc7496a0da6434e"></a>

```c
#define USB_BCC_APPLICATION 0xFE
```

应用专用设备类（Application-specific Device Class）。

相关声明：[USB_BCC_APPLICATION](P172_USB标准请求与描述符常量.md#a732af05b87cb1c53dbc7496a0da6434e)。

<a id="r_ac016944fd71362ce3924ec92cbd8f35b"></a>

```c
#define USB_BCC_VENDOR 0xFF
```

厂商专用设备类（Vendor-specific Device Class）。

相关声明：[USB_BCC_VENDOR](P172_USB标准请求与描述符常量.md#ac016944fd71362ce3924ec92cbd8f35b)。

<a id="define-members-12"></a>

**USB 规范版本号（Specification Release Numbers，对应描述符的 bcdUSB 字段）。**

<a id="r_a0aadee41a18ac57c3ff4cd8af79c954c"></a>

```c
#define USB_SRN_1_1 0x0110
```

USB 1.1 规范版本号（Specification Release Number）。

相关声明：[USB_SRN_1_1](P172_USB标准请求与描述符常量.md#a0aadee41a18ac57c3ff4cd8af79c954c)。

<a id="r_a14527f51ba0e1634b3b477c80e7ae31f"></a>

```c
#define USB_SRN_2_0 0x0200
```

USB 2.0 规范版本号。

相关声明：[USB_SRN_2_0](P172_USB标准请求与描述符常量.md#a14527f51ba0e1634b3b477c80e7ae31f)。

<a id="r_a08c992901c6007e9a2e0e4a493358653"></a>

```c
#define USB_SRN_2_0_1 0x0201
```

USB 2.0.1 规范版本号。

相关声明：[USB_SRN_2_0_1](P172_USB标准请求与描述符常量.md#a08c992901c6007e9a2e0e4a493358653)。

<a id="r_aa39f04e0a9ad954389f19ba55ca16954"></a>

```c
#define USB_SRN_2_1 0x0210
```

USB 2.1 规范版本号。

相关声明：[USB_SRN_2_1](P172_USB标准请求与描述符常量.md#aa39f04e0a9ad954389f19ba55ca16954)。

<a id="define-members-13"></a>

**USB 端点传输类型（Endpoint Transfer Types）。**

<a id="r_a619c400cb86d083c38d59366bf18ee0c"></a>

```c
#define USB_EP_TRANSFER_TYPE_MASK 0x3U
```

端点传输类型掩码（Endpoint Transfer Type Mask）。

相关声明：[USB_EP_TRANSFER_TYPE_MASK](P172_USB标准请求与描述符常量.md#a619c400cb86d083c38d59366bf18ee0c)。

<a id="r_a1cecaf205acbc73308396af4f540c012"></a>

```c
#define USB_EP_TYPE_CONTROL 0U
```

控制传输端点（Control Transfer Endpoint）。

相关声明：[USB_EP_TYPE_CONTROL](P172_USB标准请求与描述符常量.md#a1cecaf205acbc73308396af4f540c012)。

<a id="r_ad128f0d04114e8a5d40a943bb58eb7d2"></a>

```c
#define USB_EP_TYPE_ISO 1U
```

等时传输端点（Isochronous Transfer Endpoint）。

相关声明：[USB_EP_TYPE_ISO](P172_USB标准请求与描述符常量.md#ad128f0d04114e8a5d40a943bb58eb7d2)。

<a id="r_a89eb27133e7e106c3637039f6f49d187"></a>

```c
#define USB_EP_TYPE_BULK 2U
```

批量传输端点（Bulk Transfer Endpoint）。

相关声明：[USB_EP_TYPE_BULK](P172_USB标准请求与描述符常量.md#a89eb27133e7e106c3637039f6f49d187)。

<a id="r_a904b4eef8e7bcab363757e19832617ee"></a>

```c
#define USB_EP_TYPE_INTERRUPT 3U
```

中断传输端点（Interrupt Transfer Endpoint）。

相关声明：[USB_EP_TYPE_INTERRUPT](P172_USB标准请求与描述符常量.md#a904b4eef8e7bcab363757e19832617ee)。

## 172.4\_函数（Functions）

<a id="r_a88dd2eb9cd06e825eb5de6a8ad38c97c"></a>

```c
static bool usb_reqtype_is_to_host (const struct usb_setup_packet *setup)
```

检查请求的传输方向是否为发往主机。

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[usb_reqtype_is_to_host](P172_USB标准请求与描述符常量.md#a88dd2eb9cd06e825eb5de6a8ad38c97c)、[usb_setup_packet](P160_USB控制请求包.md)。

<a id="r_a7542609be1ae1730be4e14d4242d9696"></a>

```c
static bool usb_reqtype_is_to_device (const struct usb_setup_packet *setup)
```

检查请求的传输方向是否为发往设备。

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[usb_reqtype_is_to_device](P172_USB标准请求与描述符常量.md#a7542609be1ae1730be4e14d4242d9696)、[usb_setup_packet](P160_USB控制请求包.md)。

## 172.5\_详细说明（Detailed Documentation）

<a id="a732af05b87cb1c53dbc7496a0da6434e"></a>

### 172.5.1\_`USB_BCC_APPLICATION`

```c
#define USB_BCC_APPLICATION 0xFE
```

应用专用设备类（Application-specific Device Class）。

<a id="ae7de426be60abc372396692f11a0d087"></a>

### 172.5.2\_`USB_BCC_AUDIO`

```c
#define USB_BCC_AUDIO 0x01
```

音频设备类（Audio Device Class）。

<a id="a1d41de530a4da0ac75ff9bb875fe037e"></a>

### 172.5.3\_`USB_BCC_CDC_CONTROL`

```c
#define USB_BCC_CDC_CONTROL 0x02
```

通信设备类控制设备（Communications Device Class，CDC Control）。

<a id="a83fa62678f36459d11f9cec677990d44"></a>

### 172.5.4\_`USB_BCC_CDC_DATA`

```c
#define USB_BCC_CDC_DATA 0x0A
```

CDC 数据设备类（CDC Data Device Class）。

<a id="ad5904a6d6835614adc9ab914778da4a4"></a>

### 172.5.5\_`USB_BCC_HID`

```c
#define USB_BCC_HID 0x03
```

人机接口设备类（Human Interface Device，HID）。

<a id="ab0c954d8432828c1a8baa63514053cf3"></a>

### 172.5.6\_`USB_BCC_MASS_STORAGE`

```c
#define USB_BCC_MASS_STORAGE 0x08
```

大容量存储设备类（Mass Storage Device Class）。

<a id="a8c2d16e36c8522008c15b8a9dc5fc32c"></a>

### 172.5.7\_`USB_BCC_MCTP`

```c
#define USB_BCC_MCTP 0x14
```

管理组件传输协议设备类（Management Component Transport Protocol，MCTP）。

<a id="a62bf5e94c7c36c9d1d94438d7a12a482"></a>

### 172.5.8\_`USB_BCC_MISCELLANEOUS`

```c
#define USB_BCC_MISCELLANEOUS 0xEF
```

杂项设备类（Miscellaneous Device Class）。

<a id="ac016944fd71362ce3924ec92cbd8f35b"></a>

### 172.5.9\_`USB_BCC_VENDOR`

```c
#define USB_BCC_VENDOR 0xFF
```

厂商专用设备类（Vendor-specific Device Class）。

<a id="a96a42b56555daa525605e124d50ecac6"></a>

### 172.5.10\_`USB_BCC_VIDEO`

```c
#define USB_BCC_VIDEO 0x0E
```

视频设备类（Video Device Class）。

<a id="a960d92dd43d279b6def9a0cca3d88dc2"></a>

### 172.5.11\_`USB_BCC_WIRELESS_CONTROLLER`

```c
#define USB_BCC_WIRELESS_CONTROLLER 0xE0
```

无线控制器设备类（Wireless Controller Device Class）。

<a id="a2f6e90e87d7a1d53418ce084a293e6fc"></a>

### 172.5.12\_`USB_BCD_DRN`

```c
#define USB_BCD_DRN
```

**宏展开值（Value）**

```c
(USB_DEC_TO_BCD(KERNEL_VERSION_MAJOR) << 8 | \
USB_DEC_TO_BCD(KERNEL_VERSION_MINOR))
```

USB 设备版本号（Device Release Number，对应描述符的 bcdDevice 字段）。

> 译注（源码核对）：这个辅助宏的默认实现确实用 Zephyr 的 `KERNEL_VERSION_MAJOR` 和 `KERNEL_VERSION_MINOR` 生成设备版本字段。它提供默认编码方式，不意味着协议中的 `bcdDevice` 与 USB 规范版本 `bcdUSB` 是同一含义；产品如何定义设备版本需结合实际描述符配置。

<a id="ad907649f48bf773b010ce8fa36639b99"></a>

### 172.5.13\_`USB_CONTROL_EP_IN`

```c
#define USB_CONTROL_EP_IN (USB_EP_DIR_IN | 0U)
```

USB 控制端点的 IN 地址。

<a id="a8c4dd61ae766f50c9398c9753b4156b5"></a>

### 172.5.14\_`USB_CONTROL_EP_MPS`

```c
#define USB_CONTROL_EP_MPS 64U
```

USB 控制端点的最大包长（Maximum Packet Size，MPS）。

对于运行在高速以外速率的设备，此值可能不正确。

<a id="a9af36e318a50a982ebf826ef1d9e384e"></a>

### 172.5.15\_`USB_CONTROL_EP_OUT`

```c
#define USB_CONTROL_EP_OUT (USB_EP_DIR_OUT | 0U)
```

USB 控制端点的 OUT 地址。

<a id="aa021c46e7c0e127c513adbac04bc77ba"></a>

### 172.5.16\_`USB_DEC_TO_BCD`

```c
#define USB_DEC_TO_BCD ( dec)
```

**宏展开值（Value）**

```c
((((dec) / 10) << 4) | ((dec) % 10))
```

将十进制值转换为二进制编码的十进制表示（Binary-coded Decimal，BCD）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dec` | 十进制值（Decimal Value）。 |

**返回（Returns）**：采用 BCD 编码的值。

> 译注（源码核对）：展开式分别取十位与个位，没有输入范围校验。它不是任意位数十进制数的通用 BCD 编码器，不能把含副作用的表达式当作参数，因为参数可能被多次求值。

<a id="a9f6e306632b56036d4dd7cc2430bcec9"></a>

### 172.5.17\_`USB_DESC_BOS`

```c
#define USB_DESC_BOS 15
```

二进制对象存储描述符类型（Binary Object Store Descriptor Type，BOS）。

<a id="a7764131f2e59070eb032bd9d68d32620"></a>

### 172.5.18\_`USB_DESC_CONFIGURATION`

```c
#define USB_DESC_CONFIGURATION 2
```

配置描述符类型（Configuration Descriptor Type）。

<a id="a7221e0186e4e17a624b739d1807c161d"></a>

### 172.5.19\_`USB_DESC_CS_CONFIGURATION`

```c
#define USB_DESC_CS_CONFIGURATION 0x22
```

类专用配置描述符类型（Class-specific Configuration Descriptor Type）。

<a id="a4ee3b5be16342ce919483c66cc701cb4"></a>

### 172.5.20\_`USB_DESC_CS_DEVICE`

```c
#define USB_DESC_CS_DEVICE 0x21
```

类专用设备描述符类型（Class-specific Device Descriptor Type）。

<a id="a3222223114b6d7ecea051a862fb685e2"></a>

### 172.5.21\_`USB_DESC_CS_ENDPOINT`

```c
#define USB_DESC_CS_ENDPOINT 0x25
```

类专用端点描述符类型（Class-specific Endpoint Descriptor Type）。

<a id="ae47a98df81bbd33336e11c3742418217"></a>

### 172.5.22\_`USB_DESC_CS_INTERFACE`

```c
#define USB_DESC_CS_INTERFACE 0x24
```

类专用接口描述符类型（Class-specific Interface Descriptor Type）。

<a id="a0a89e53a56fcadd9f7b9e08e4d9ef5f8"></a>

### 172.5.23\_`USB_DESC_CS_STRING`

```c
#define USB_DESC_CS_STRING 0x23
```

类专用字符串描述符类型（Class-specific String Descriptor Type）。

<a id="a0a7ab16adb76e6b9af587a82d5a7fbb3"></a>

### 172.5.24\_`USB_DESC_DEBUG`

```c
#define USB_DESC_DEBUG 10
```

调试描述符类型（Debug Descriptor Type）。

<a id="aefeff68c3a236749d1105d94ed9bad68"></a>

### 172.5.25\_`USB_DESC_DEVICE`

```c
#define USB_DESC_DEVICE 1
```

设备描述符类型（Device Descriptor Type）。

<a id="a8ff1997b326965664d90926658af7e98"></a>

### 172.5.26\_`USB_DESC_DEVICE_CAPABILITY`

```c
#define USB_DESC_DEVICE_CAPABILITY 16
```

设备能力描述符类型（Device Capability Descriptor Type）。

<a id="aae4580f7a31247f2bce47af2f27b3a64"></a>

### 172.5.27\_`USB_DESC_DEVICE_QUALIFIER`

```c
#define USB_DESC_DEVICE_QUALIFIER 6
```

设备限定描述符类型（Device Qualifier Descriptor Type）。

<a id="a1428ae675c4b17d84b91eda705fe0498"></a>

### 172.5.28\_`USB_DESC_ENDPOINT`

```c
#define USB_DESC_ENDPOINT 5
```

端点描述符类型（Endpoint Descriptor Type）。

<a id="ab98b6a1b7ec1dc4adcbd188c3a38f69f"></a>

### 172.5.29\_`USB_DESC_INTERFACE`

```c
#define USB_DESC_INTERFACE 4
```

接口描述符类型（Interface Descriptor Type）。

<a id="ac84354aa0bfec12d3e21e72d29caf48b"></a>

### 172.5.30\_`USB_DESC_INTERFACE_ASSOC`

```c
#define USB_DESC_INTERFACE_ASSOC 11
```

接口关联描述符类型（Interface Association Descriptor Type）。

<a id="a075dd47d721cfd6cdf804f3cdf0feae1"></a>

### 172.5.31\_`USB_DESC_INTERFACE_POWER`

```c
#define USB_DESC_INTERFACE_POWER 8
```

接口电源描述符类型（Interface Power Descriptor Type）。

<a id="a162988e9c51e1094635a553999f52d51"></a>

### 172.5.32\_`USB_DESC_OTG`

```c
#define USB_DESC_OTG 9
```

OTG 描述符类型（On-The-Go Descriptor Type）。

<a id="a3a8acce20fbea73ab685bb55a4a6356d"></a>

### 172.5.33\_`USB_DESC_OTHER_SPEED`

```c
#define USB_DESC_OTHER_SPEED 7
```

其他速率配置描述符类型（Other Speed Configuration Descriptor Type）。

<a id="a6a5678b964f3a9b4ba2f52e9a51bebf5"></a>

### 172.5.34\_`USB_DESC_STRING`

```c
#define USB_DESC_STRING 3
```

字符串描述符类型（String Descriptor Type）。

<a id="aae8411e95f26738326bc25a0161dde99"></a>

### 172.5.35\_`USB_EP_DIR_IN`

```c
#define USB_EP_DIR_IN (uint8_t)BIT(7)
```

USB 输入端点方向（IN，设备到主机）。

<a id="a495d790dfb00609ce029631f40d0a422"></a>

### 172.5.36\_`USB_EP_DIR_IS_IN`

```c
#define USB_EP_DIR_IS_IN ( ep)
```

**宏展开值（Value）**

```c
(USB_EP_GET_DIR(ep) == USB_EP_DIR_IN)
```

判断端点地址是否指向 IN 端点。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ep` | 端点地址（Endpoint Address）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `true` | 端点是 IN 端点。 |
| `false` | 端点是 OUT 端点。 |

<a id="a1734aa980e0f135ddc7873bb1a60c1a1"></a>

### 172.5.37\_`USB_EP_DIR_IS_OUT`

```c
#define USB_EP_DIR_IS_OUT ( ep)
```

**宏展开值（Value）**

```c
(USB_EP_GET_DIR(ep) == USB_EP_DIR_OUT)
```

判断端点地址是否指向 OUT 端点。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ep` | 端点地址（Endpoint Address）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `true` | 端点是 OUT 端点。 |
| `false` | 端点是 IN 端点。 |

<a id="afb744cb324e47124f93424a47d874b2a"></a>

### 172.5.38\_`USB_EP_DIR_MASK`

```c
#define USB_EP_DIR_MASK (uint8_t)BIT(7)
```

USB 端点方向掩码（Endpoint Direction Mask）。

<a id="a0510b0a04d9cef144e4d9793310abccf"></a>

### 172.5.39\_`USB_EP_DIR_OUT`

```c
#define USB_EP_DIR_OUT 0U
```

USB 输出端点方向（OUT，主机到设备）。

<a id="aa5963d81b4b5bee364fb0078229c71cf"></a>

### 172.5.40\_`USB_EP_GET_ADDR`

```c
#define USB_EP_GET_ADDR ( idx, dir )
```

**宏展开值（Value）**

```c
((idx) | ((dir) & USB_EP_DIR_MASK))
```

根据端点索引和方向获取端点地址。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `idx` | 端点索引（Endpoint Index）。 |
| `dir` | 端点方向（USB_EP_DIR_IN 或 USB_EP_DIR_OUT）。 |

**返回（Returns）**：编码后的端点地址。

> 译注（源码核对）：此宏仅对 `dir` 施加方向掩码，`idx` 直接参与按位或；它不负责校验端点索引范围，也不会替调用者清除索引中的保留位。

<a id="aa974862712344d5d806d521a87549284"></a>

### 172.5.41\_`USB_EP_GET_DIR`

```c
#define USB_EP_GET_DIR ( ep)
```

**宏展开值（Value）**

```c
((ep) & USB_EP_DIR_MASK)
```

根据端点地址获取方向。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ep` | 端点地址（Endpoint Address）。 |

**返回（Returns）**：方向掩码。

<a id="a4fd2505dba51e8f198276a032d3f0523"></a>

### 172.5.42\_`USB_EP_GET_IDX`

```c
#define USB_EP_GET_IDX ( ep)
```

**宏展开值（Value）**

```c
((ep) & ~USB_EP_DIR_MASK)
```

从端点地址获取端点索引（编号）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ep` | 端点地址（Endpoint Address）。 |

**返回（Returns）**：端点编号。

> 译注（源码核对）：原始源码的 REVISE 注释说明：理论上应采用 `(ep) & 0x0F`，当前只清除方向位，是为避免既有设备支持中的多处回归。这里保留实际宏展开，不能把它描述成同时清除了所有保留位。

<a id="a619c400cb86d083c38d59366bf18ee0c"></a>

### 172.5.43\_`USB_EP_TRANSFER_TYPE_MASK`

```c
#define USB_EP_TRANSFER_TYPE_MASK 0x3U
```

端点传输类型掩码（Endpoint Transfer Type Mask）。

<a id="a89eb27133e7e106c3637039f6f49d187"></a>

### 172.5.44\_`USB_EP_TYPE_BULK`

```c
#define USB_EP_TYPE_BULK 2U
```

批量传输端点（Bulk Transfer Endpoint）。

<a id="a1cecaf205acbc73308396af4f540c012"></a>

### 172.5.45\_`USB_EP_TYPE_CONTROL`

```c
#define USB_EP_TYPE_CONTROL 0U
```

控制传输端点（Control Transfer Endpoint）。

<a id="a904b4eef8e7bcab363757e19832617ee"></a>

### 172.5.46\_`USB_EP_TYPE_INTERRUPT`

```c
#define USB_EP_TYPE_INTERRUPT 3U
```

中断传输端点（Interrupt Transfer Endpoint）。

<a id="ad128f0d04114e8a5d40a943bb58eb7d2"></a>

### 172.5.47\_`USB_EP_TYPE_ISO`

```c
#define USB_EP_TYPE_ISO 1U
```

等时传输端点（Isochronous Transfer Endpoint）。

<a id="a3530fe35c97b660a43bcbd573015a14a"></a>

### 172.5.48\_`USB_FS_INT_EP_INTERVAL`

```c
#define USB_FS_INT_EP_INTERVAL ( us)
```

**宏展开值（Value）**

```c
CLAMP(((us) / 1000U), 1U, 255U)
```

由以微秒为单位的数值计算全速（Full Speed，FS）中断端点的 bInterval。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `us` | 轮询间隔（Polling Interval），单位为微秒。 |

**返回（Returns）**：编码后的 bInterval 值。

> 译注（源码核对）：实现先按整数除法将微秒换成毫秒，再限制到 1～255。输入不能整除 1000 时会截断；例如 1500 微秒得到字段值 1，不能把它读成精确保留了 1.5 毫秒。

<a id="a00508417f5da453f39a8aac96cbba673"></a>

### 172.5.49\_`USB_FS_ISO_EP_INTERVAL`

```c
#define USB_FS_ISO_EP_INTERVAL ( us)
```

**宏展开值（Value）**

```c
CLAMP((ilog2((us) / 1000U) + 1U), 1U, 16U)
```

由微秒值计算全速等时（Isochronous）端点的 bInterval。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `us` | 轮询间隔（Polling Interval），单位为微秒。 |

**返回（Returns）**：编码后的 bInterval 值。

> 译注（源码核对）：全速等时端点采用先除以 1000、再取整数 log2 加 1 的编码，与全速中断端点的线性换算不同。输入应按协议和实际端点条件选择。

<a id="a653a141a5084536362396149e81b6b9a"></a>

### 172.5.50\_`USB_GET_DESCRIPTOR_INDEX`

```c
#define USB_GET_DESCRIPTOR_INDEX ( wValue)
```

**宏展开值（Value）**

```c
((uint8_t)(wValue))
```

从 USB_SREQ_GET_DESCRIPTOR 请求值获取描述符索引。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `wValue` | GET_DESCRIPTOR 请求的 wValue 字段。 |

**返回（Returns）**：编码在 wValue 中的描述符索引。

<a id="a2916665797ca49936ed0572fb3b39a81"></a>

### 172.5.51\_`USB_GET_DESCRIPTOR_TYPE`

```c
#define USB_GET_DESCRIPTOR_TYPE ( wValue)
```

**宏展开值（Value）**

```c
((uint8_t)((wValue) >> 8))
```

从 USB_SREQ_GET_DESCRIPTOR 请求值获取描述符类型。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `wValue` | GET_DESCRIPTOR 请求的 wValue 字段。 |

**返回（Returns）**：编码在 wValue 中的描述符类型。

<a id="a6d896f4f58e13f87f8e74af6909fada9"></a>

### 172.5.52\_`USB_GET_STATUS_REMOTE_WAKEUP`

```c
#define USB_GET_STATUS_REMOTE_WAKEUP BIT(1)
```

远程唤醒状态位（Remote Wakeup Status Bit）。

<a id="a9dd608d5ce8d45fdd76bad3df4fdf34d"></a>

### 172.5.53\_`USB_GET_STATUS_SELF_POWERED`

```c
#define USB_GET_STATUS_SELF_POWERED BIT(0)
```

自供电状态位（Self-powered Status Bit）。

<a id="aac29193abaef01df1c81566a9029c92f"></a>

### 172.5.54\_`USB_HS_INT_EP_INTERVAL`

```c
#define USB_HS_INT_EP_INTERVAL ( us)
```

**宏展开值（Value）**

```c
CLAMP((ilog2((us) / 125U) + 1U), 1U, 16U)
```

由微秒值计算高速（High Speed，HS）中断端点的 bInterval。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `us` | 轮询间隔（Polling Interval），单位为微秒。 |

**返回（Returns）**：编码后的 bInterval 值。

> 译注（源码核对）：此宏先除以 125 微秒，再计算整数 log2 并加 1，最后限制为 1～16。整数 log2 对正数向下取整，例如 1000 微秒得到 4。这里的字段是编码值，不是微秒数；不应依靠末尾 CLAMP 为无效输入兜底。

<a id="ae4facc67e3acfcc97d6e9529968ea7ca"></a>

### 172.5.55\_`USB_HS_ISO_EP_INTERVAL`

```c
#define USB_HS_ISO_EP_INTERVAL ( us)
```

**宏展开值（Value）**

```c
CLAMP((ilog2((us) / 125U) + 1U), 1U, 16U)
```

由微秒值计算高速等时端点的 bInterval。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `us` | 轮询间隔（Polling Interval），单位为微秒。 |

**返回（Returns）**：编码后的 bInterval 值。

> 译注（源码核对）：当前展开式与高速中断端点宏相同，时间基准均为 125 微秒；这不表示中断传输与等时传输具有相同的传输语义。

<a id="ad82d2bcde8045078531a607ddf5231b2"></a>

### 172.5.56\_`USB_MPS_ADDITIONAL_TRANSACTIONS`

```c
#define USB_MPS_ADDITIONAL_TRANSACTIONS ( mps)
```

**宏展开值（Value）**

```c
(((mps) & 0x1800) >> 11)
```

从 MPS 获取每个微帧（Microframe）的额外事务（Additional Transactions）数量。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `mps` | 编码后的最大包长（Encoded Max Packet Size）。 |

**返回（Returns）**：每个微帧的额外事务数量。

<a id="ae028a023a157a29a0e83dee304c6267a"></a>

### 172.5.57\_`USB_MPS_EP_SIZE`

```c
#define USB_MPS_EP_SIZE ( mps)
```

**宏展开值（Value）**

```c
((mps) & BIT_MASK(11))
```

从最大包长值获取端点大小字段（Endpoint Size Field）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `mps` | 编码后的最大包长（Encoded Max Packet Size）。 |

**返回（Returns）**：端点大小字段。

<a id="a10ea5b5c35aff863958c83ee1e4c9de5"></a>

### 172.5.58\_`USB_MPS_TO_TPL`

```c
#define USB_MPS_TO_TPL ( mps)
```

**宏展开值（Value）**

```c
((1 + USB_MPS_ADDITIONAL_TRANSACTIONS(mps)) * USB_MPS_EP_SIZE(mps))
```

由最大包长值计算总有效载荷长度（Total Payload Length，TPL）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `mps` | 编码后的最大包长（Encoded Max Packet Size）。 |

**返回（Returns）**：总有效载荷长度，单位为字节。

> 译注（源码核对）：该式把低 11 位的单次事务字节数乘以“1 + 额外事务数”。它解释的是编码后的最大包长字段，不是简单返回原始数值，也不检查编码中的保留值。

<a id="a3e431a6f30304833b6aa45a454c8bdbd"></a>

### 172.5.59\_`USB_REQTYPE_DIR_TO_DEVICE`

```c
#define USB_REQTYPE_DIR_TO_DEVICE 0
```

主机到设备的数据方向（Host-to-device）。

<a id="aa080957f00a9459f9f7c533da893b31f"></a>

### 172.5.60\_`USB_REQTYPE_DIR_TO_HOST`

```c
#define USB_REQTYPE_DIR_TO_HOST 1
```

设备到主机的数据方向（Device-to-host）。

<a id="ab9c7b95bb1467f3d116432ac9194e92d"></a>

### 172.5.61\_`USB_REQTYPE_GET_DIR`

```c
#define USB_REQTYPE_GET_DIR ( bmRequestType)
```

**宏展开值（Value）**

```c
(((bmRequestType) >> 7) & 0x01U)
```

从 bmRequestType 获取数据传输方向。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `bmRequestType` | 编码后的请求类型。 |

**返回（Returns）**：主机到设备为 0，设备到主机为 1（参见 usb_reqtype_dir）。

<a id="a933742b41b1da36545639df1a08c0db5"></a>

### 172.5.62\_`USB_REQTYPE_GET_RECIPIENT`

```c
#define USB_REQTYPE_GET_RECIPIENT ( bmRequestType)
```

**宏展开值（Value）**

```c
((bmRequestType) & 0x1FU)
```

从 bmRequestType 获取请求接收方。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `bmRequestType` | 编码后的请求类型。 |

**返回（Returns）**：编码后的接收方值（参见 usb_reqtype_recipient）。

<a id="a18dd1450e8fe287b2de1f8871274a3b9"></a>

### 172.5.63\_`USB_REQTYPE_GET_TYPE`

```c
#define USB_REQTYPE_GET_TYPE ( bmRequestType)
```

**宏展开值（Value）**

```c
(((bmRequestType) >> 5) & 0x03U)
```

从 bmRequestType 获取请求类型。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `bmRequestType` | 编码后的请求类型。 |

**返回（Returns）**：编码后的请求类型值（参见 usb_reqtype_type）。

<a id="ab71be1695c56514626b15d3790e3d934"></a>

### 172.5.64\_`USB_REQTYPE_RECIPIENT_DEVICE`

```c
#define USB_REQTYPE_RECIPIENT_DEVICE 0
```

接收方为设备（Device）。

<a id="a32154b80a8d73dfb4e261d31a8d351fa"></a>

### 172.5.65\_`USB_REQTYPE_RECIPIENT_ENDPOINT`

```c
#define USB_REQTYPE_RECIPIENT_ENDPOINT 2
```

接收方为端点（Endpoint）。

<a id="a8c2c0646290270444df73b1319232ea7"></a>

### 172.5.66\_`USB_REQTYPE_RECIPIENT_INTERFACE`

```c
#define USB_REQTYPE_RECIPIENT_INTERFACE 1
```

接收方为接口（Interface）。

<a id="a2e07a8841cf9d67dc0c60badc00761b0"></a>

### 172.5.67\_`USB_REQTYPE_RECIPIENT_OTHER`

```c
#define USB_REQTYPE_RECIPIENT_OTHER 3
```

其他接收方（Other）。

<a id="abaeb448434207462bcb312973a013f3d"></a>

### 172.5.68\_`USB_REQTYPE_TYPE_CLASS`

```c
#define USB_REQTYPE_TYPE_CLASS 1
```

类专用请求（Class-specific Request）。

<a id="ab43bb12a355f38ea09a1dee177619b78"></a>

### 172.5.69\_`USB_REQTYPE_TYPE_RESERVED`

```c
#define USB_REQTYPE_TYPE_RESERVED 3
```

保留的请求类型（Reserved Request Type）。

<a id="a9529fae2802d82fd37d4ad58ab9d6f67"></a>

### 172.5.70\_`USB_REQTYPE_TYPE_STANDARD`

```c
#define USB_REQTYPE_TYPE_STANDARD 0
```

标准 USB 请求（Standard USB Request）。

<a id="ad06cc151ffddfeba7bc99b819101d11d"></a>

### 172.5.71\_`USB_REQTYPE_TYPE_VENDOR`

```c
#define USB_REQTYPE_TYPE_VENDOR 2
```

厂商专用请求（Vendor-specific Request）。

<a id="aa1fa7548e67cc2755d91b68fd1545088"></a>

### 172.5.72\_`USB_SCD_REMOTE_WAKEUP`

```c
#define USB_SCD_REMOTE_WAKEUP BIT(5)
```

远程唤醒配置位（Remote Wakeup Configuration Bit）。

<a id="a2a8b7c42705cd1e0fd0aecb0028cb2ba"></a>

### 172.5.73\_`USB_SCD_RESERVED`

```c
#define USB_SCD_RESERVED BIT(7)
```

保留的配置位（Reserved Configuration Bit）。

<a id="a0122c49a39e67e2443e491132aa0ecfd"></a>

### 172.5.74\_`USB_SCD_SELF_POWERED`

```c
#define USB_SCD_SELF_POWERED BIT(6)
```

自供电配置位（Self-powered Configuration Bit）。

<a id="a78ee83859d881216f702a349e9c5133b"></a>

### 172.5.75\_`USB_SFS_ENDPOINT_HALT`

```c
#define USB_SFS_ENDPOINT_HALT 0x00
```

端点停滞特性选择器（Endpoint Halt Feature Selector）。

<a id="a954bd576fddb8178e15bb3081733e49c"></a>

### 172.5.76\_`USB_SFS_REMOTE_WAKEUP`

```c
#define USB_SFS_REMOTE_WAKEUP 0x01
```

远程唤醒特性选择器（Remote Wakeup Feature Selector）。

<a id="ae2a2cf879eace08bf86d330b39578792"></a>

### 172.5.77\_`USB_SFS_TEST_MODE`

```c
#define USB_SFS_TEST_MODE 0x02
```

测试模式特性选择器（Test Mode Feature Selector）。

<a id="a5b4e7459b82b9d22da12e9b5dd8b5ba0"></a>

### 172.5.78\_`USB_SFS_TEST_MODE_FORCE_ENABLE`

```c
#define USB_SFS_TEST_MODE_FORCE_ENABLE 0x05
```

Test_Force_Enable 测试模式。

<a id="a48567c219ecb9e0b3c0d7a1685d68cec"></a>

### 172.5.79\_`USB_SFS_TEST_MODE_J`

```c
#define USB_SFS_TEST_MODE_J 0x01
```

Test_J 测试模式（Test Mode）。

<a id="a2693cbe71751c0990568c01c5137f34e"></a>

### 172.5.80\_`USB_SFS_TEST_MODE_K`

```c
#define USB_SFS_TEST_MODE_K 0x02
```

Test_K 测试模式。

<a id="a400245449e029997eab958d1963e27fa"></a>

### 172.5.81\_`USB_SFS_TEST_MODE_PACKET`

```c
#define USB_SFS_TEST_MODE_PACKET 0x04
```

Test_Packet 测试模式。

<a id="a2e36154ec5720097fda6e8fb67ab8c5f"></a>

### 172.5.82\_`USB_SFS_TEST_MODE_SE0_NAK`

```c
#define USB_SFS_TEST_MODE_SE0_NAK 0x03
```

Test_SE0_NAK 测试模式。

<a id="a16d58595c13caa66989d63343de6bccb"></a>

### 172.5.83\_`USB_SREQ_CLEAR_FEATURE`

```c
#define USB_SREQ_CLEAR_FEATURE 0x01
```

清除特性请求（Clear Feature）。

<a id="a505c325ea65c44f9df6df87bef30f5ee"></a>

### 172.5.84\_`USB_SREQ_GET_CONFIGURATION`

```c
#define USB_SREQ_GET_CONFIGURATION 0x08
```

获取配置请求（Get Configuration）。

<a id="ab3b49f2eb21dcd597ca73ea62bfa5523"></a>

### 172.5.85\_`USB_SREQ_GET_DESCRIPTOR`

```c
#define USB_SREQ_GET_DESCRIPTOR 0x06
```

获取描述符请求（Get Descriptor）。

<a id="a26034252f1f8ddc5d7793e1ff3974764"></a>

### 172.5.86\_`USB_SREQ_GET_INTERFACE`

```c
#define USB_SREQ_GET_INTERFACE 0x0A
```

获取接口请求（Get Interface）。

<a id="afffb7748ffdb525572e407024df9a201"></a>

### 172.5.87\_`USB_SREQ_GET_STATUS`

```c
#define USB_SREQ_GET_STATUS 0x00
```

获取状态请求（Get Status）。

<a id="ac20c25ea20acac5d0f4484e3d9a5c759"></a>

### 172.5.88\_`USB_SREQ_SET_ADDRESS`

```c
#define USB_SREQ_SET_ADDRESS 0x05
```

设置地址请求（Set Address）。

<a id="a0f87cedfecf77bba9c52514684a13bf3"></a>

### 172.5.89\_`USB_SREQ_SET_CONFIGURATION`

```c
#define USB_SREQ_SET_CONFIGURATION 0x09
```

设置配置请求（Set Configuration）。

<a id="ac95699668d43a49f1dd17ee86220984c"></a>

### 172.5.90\_`USB_SREQ_SET_DESCRIPTOR`

```c
#define USB_SREQ_SET_DESCRIPTOR 0x07
```

设置描述符请求（Set Descriptor）。

<a id="ac1ef5c9fe1f3107f1a55560f81b6e25a"></a>

### 172.5.91\_`USB_SREQ_SET_FEATURE`

```c
#define USB_SREQ_SET_FEATURE 0x03
```

设置特性请求（Set Feature）。

<a id="acf5ea7c90528a4d9d86c279318a6cb52"></a>

### 172.5.92\_`USB_SREQ_SET_INTERFACE`

```c
#define USB_SREQ_SET_INTERFACE 0x0B
```

设置接口请求（Set Interface）。

<a id="a390ddf7167cc081fd3d3f24f09967d06"></a>

### 172.5.93\_`USB_SREQ_SYNCH_FRAME`

```c
#define USB_SREQ_SYNCH_FRAME 0x0C
```

同步帧请求（Synch Frame）。

<a id="a0aadee41a18ac57c3ff4cd8af79c954c"></a>

### 172.5.94\_`USB_SRN_1_1`

```c
#define USB_SRN_1_1 0x0110
```

USB 1.1 规范版本号（Specification Release Number）。

<a id="a14527f51ba0e1634b3b477c80e7ae31f"></a>

### 172.5.95\_`USB_SRN_2_0`

```c
#define USB_SRN_2_0 0x0200
```

USB 2.0 规范版本号。

<a id="a08c992901c6007e9a2e0e4a493358653"></a>

### 172.5.96\_`USB_SRN_2_0_1`

```c
#define USB_SRN_2_0_1 0x0201
```

USB 2.0.1 规范版本号。

<a id="aa39f04e0a9ad954389f19ba55ca16954"></a>

### 172.5.97\_`USB_SRN_2_1`

```c
#define USB_SRN_2_1 0x0210
```

USB 2.1 规范版本号。

<a id="a9a9dc75d25540bbf34543df09a9ecd4e"></a>

### 172.5.98\_`USB_TPL_IS_VALID`

```c
#define USB_TPL_IS_VALID ( tpl)
```

**宏展开值（Value）**

```c
(((tpl) > 3072) ? false :                       \
 ((tpl) > 2048) ? ((tpl) % 3 == 0) :            \
 ((tpl) > 1024) ? ((tpl) % 2 == 0) :            \
 ((tpl) >= 0))
```

判断总有效载荷长度值是否符合 USB 2.0 的有效性要求。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `tpl` | 总有效载荷长度，单位为字节。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `true` | 有效载荷长度有效。 |
| `false` | 有效载荷长度无效。 |

> 译注（源码核对）：本宏只按数值上限 3072，以及大于 1024 时的 2 倍数、大于 2048 时的 3 倍数规则判断，0 也返回 true。它不接收速率、端点类型或控制器能力参数，因此不能代替完整的端点配置合法性检查。

<a id="af0d975aa6569cdd395e0d08d6c866a02"></a>

### 172.5.99\_`USB_TPL_ROUND_UP`

```c
#define USB_TPL_ROUND_UP ( tpl)
```

**宏展开值（Value）**

```c
(((tpl) > 2048) ? ROUND_UP(tpl, 3) :            \
 ((tpl) > 1024) ? ROUND_UP(tpl, 2) :            \
 (tpl))
```

将总有效载荷长度向上舍入为下一个有效值。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `tpl` | 总有效载荷长度，单位为字节。 |

**返回（Returns）**：舍入后的有效载荷长度。

> 译注（源码核对）：该宏只按当前区间向上对齐，不执行 3072 的上限限制；超范围输入舍入后仍可能无效。与 `USB_TPL_TO_MPS` 配合时，先确保有效载荷长度满足应用所需的协议约束。

<a id="a4aa386328cee14a25e8e9b4183ca1353"></a>

### 172.5.100\_`USB_TPL_TO_MPS`

```c
#define USB_TPL_TO_MPS ( tpl)
```

**宏展开值（Value）**

```c
(((tpl) > 2048) ? ((2 << 11) | ((tpl) / 3)) :   \
 ((tpl) > 1024) ? ((1 << 11) | ((tpl) / 2)) :   \
 (tpl))
```

由总有效载荷长度计算最大包长值。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `tpl` | 总有效载荷长度，单位为字节。 |

**返回（Returns）**：编码后的最大包长值。

> 译注（源码核对）：宏直接根据区间除以 2 或 3 并设置额外事务位，不会先替调用者向上对齐。对不满足整除条件的输入会发生整数截断；不要把它当作自动修正任意长度的转换。

<a id="a7542609be1ae1730be4e14d4242d9696"></a>

### 172.5.101\_`usb_reqtype_is_to_device()`

```c
static inline bool usb_reqtype_is_to_device ( const struct usb_setup_packet * setup)
```

检查请求的传输方向是否为发往设备。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `setup` | 指向 USB 设置包（Setup Packet）的指针。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `true` | 传输方向是主机到设备。 |
| `false` | 传输方向是设备到主机。 |

<a id="a88dd2eb9cd06e825eb5de6a8ad38c97c"></a>

### 172.5.102\_`usb_reqtype_is_to_host()`

```c
static inline bool usb_reqtype_is_to_host ( const struct usb_setup_packet * setup)
```

检查请求的传输方向是否为发往主机。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `setup` | 指向 USB 设置包（Setup Packet）的指针。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `true` | 传输方向是设备到主机。 |
| `false` | 传输方向是主机到设备。 |

> 译注（源码核对）：此公开辅助函数只检查 `RequestType.direction`，不检查 `wLength`。设备栈 usbd_ch9.c 中另有名称相近的内部 `reqtype_is_to_host()`，同时要求 `wLength` 非零；源码跟踪时应区分二者。

## 172.6\_源码跟踪与使用边界

译注依据保存的[官方 USB 第 9 章头文件](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/include/zephyr/usb/usb_ch9.h)与[新版设备栈标准请求处理](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/device_next/usbd_ch9.c)，原始头文件署名为 Copyright (c) 2020 PHYTEC Messtechnik GmbH，许可证为 `Apache-2.0`。文件摘要见[来源记录](../SOURCES.md)。本仓库的[同名头文件](../../../include/zephyr/usb/usb_ch9.h)和[请求处理源码](../../../subsys/usb/device_next/usbd_ch9.c)供相对路径跟踪，版本可能与官网不同。轮询间隔换算还核对保存的[官方整数 log2 头文件](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/include/zephyr/math/ilog2.h)。标准字段的具体编码仍应结合原页所引用的规范及目标速率理解；本页不以字段名称替代协议约束。本批未构建固件或连接设备进行枚举测试。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>
<a id="header-define-members"></a>
<a id="define-members"></a>
<a id="usb_reqtype_dir"></a>
<a id="usb_reqtype_type"></a>
<a id="usb_reqtype_recipient"></a>
<a id="header-func-members"></a>
<a id="func-members"></a>
<a id="details"></a>
<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="ausb__ch9_8h_html_aa021c46e7c0e127c513adbac04bc77ba"></a>
<a id="ausb__ch9_8h_html_aa974862712344d5d806d521a87549284"></a>
<a id="ausb__ch9_8h_html_aae8411e95f26738326bc25a0161dde99"></a>
<a id="ausb__ch9_8h_html_a0510b0a04d9cef144e4d9793310abccf"></a>
<a id="ausb__ch9_8h_html_afb744cb324e47124f93424a47d874b2a"></a>
<a id="agroup__sys-util_html_gad6e7d4f6ba5a77f9ee3c04026f1c2b67"></a>
<a id="agroup__math__ilog2_html_ga2696c6303d4c53b65a3a7f7ff771d5eb"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="agroup__sys-util_html_ga3c12c6d36ad0aa481a3436923d21f4f8"></a>
<a id="ausb__ch9_8h_html_ad82d2bcde8045078531a607ddf5231b2"></a>
<a id="ausb__ch9_8h_html_ae028a023a157a29a0e83dee304c6267a"></a>
<a id="astdbool_8h_html_a65e9886d74aaee76545e83dd09011727"></a>
<a id="agroup__sys-util_html_gaada5610108b15d85c65d863b0c646ef3"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

[上一章](P171_USB端点属性位域.md) · [返回大纲](大纲.md) · [下一章](P173_USB第9章头文件源码.md)
