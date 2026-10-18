---
id: learning.zephyr-docs.api-file-network-pcie-reference.page-12
title: zephyr__usb__class__usb_hub.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/usb__hub_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第12章\_zephyr\_\_usb\_\_class\_\_usb\_hub.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/usb__hub_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

USB集线器类（Hub Class）的公共头文件。

查看此文件的源码。

<a id="details"></a>

USB集线器类（Hub Class）的公共头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 12.1\_数据结构（Data Structures）

<a id="r_usb_5Fhub_5Fdescriptor"></a>

```c
struct usb_hub_descriptor
```

相关声明：[usb_hub_descriptor](../device_power_control_model_reference/P097_usb_hub_descriptor_结构体.md)。

USB集线器描述符（Hub Descriptor）。

<a id="r_usb_5Fhub_5Fstatus"></a>

```c
struct usb_hub_status
```

相关声明：[usb_hub_status](../device_power_control_model_reference/P099_usb_hub_status_结构体.md)。

USB集线器状态（Hub Status）。

<a id="r_usb_5Fhub_5Fport_5Fstatus"></a>

```c
struct usb_hub_port_status
```

相关声明：[usb_hub_port_status](../device_power_control_model_reference/P098_usb_hub_port_status_结构体.md)。

USB集线器端口状态（Hub Port Status）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 12.2\_宏定义（Macros）

<a id="r_a046305cfa6801f9df1f180b06f8c7330"></a>

```c
#define USB_HUB_DESC_BUF_SIZE 71
```

相关声明：[USB_HUB_DESC_BUF_SIZE](#a046305cfa6801f9df1f180b06f8c7330)。

集线器描述符最大大小（Maximum Hub Descriptor Size）。

<a id="r_a058a9526a6cc90ca98ceee729d489911"></a>

```c
#define USB_HUB_GET_THINK_TIME(wHubCharacteristics)
```

相关声明：[USB_HUB_GET_THINK_TIME](#a058a9526a6cc90ca98ceee729d489911)。

从 `wHubCharacteristics` 字段获取思考时间值（Think Time）。

<a id="define-members-0"></a>

### USB 集线器类代码（USB Hub Class Codes）

<a id="r_aebe338a3fb6193dcbfac244ca8042ad1"></a>

```c
#define USB_HUB_CLASS_CODE 0x09
```

相关声明：[USB_HUB_CLASS_CODE](#aebe338a3fb6193dcbfac244ca8042ad1)。

集线器类代码（Hub Class Code）。

<a id="r_a5633c828019ace8d57e864b575406709"></a>

```c
#define USB_HUB_SUBCLASS_CODE 0x00
```

相关声明：[USB_HUB_SUBCLASS_CODE](#a5633c828019ace8d57e864b575406709)。

集线器子类代码（Hub Subclass Code）。

<a id="r_a7fde1fdcc7ac52b8f54a461b60dd5f37"></a>

```c
#define USB_HUB_PROTOCOL_FS 0x00
```

相关声明：[USB_HUB_PROTOCOL_FS](#a7fde1fdcc7ac52b8f54a461b60dd5f37)。

集线器协议代码（Hub Protocol Codes），参见 USB 2.0 规范表 11-17。

<a id="r_a89deb4aa95ba6c2f7f774a8b0a1f726b"></a>

```c
#define USB_HUB_PROTOCOL_HS_SINGLE_TT 0x01
```

相关声明：[USB_HUB_PROTOCOL_HS_SINGLE_TT](#a89deb4aa95ba6c2f7f774a8b0a1f726b)。

具有单个事务转换器（TT）的高速集线器（High-speed Hub）。

<a id="r_af7c6620f35c78adc1ed9b8d7190d4790"></a>

```c
#define USB_HUB_PROTOCOL_HS_MULTI_TT 0x02
```

相关声明：[USB_HUB_PROTOCOL_HS_MULTI_TT](#af7c6620f35c78adc1ed9b8d7190d4790)。

具有多个事务转换器（TT）的高速集线器（High-speed Hub）。

<a id="r_afa18145aa35c0148f9f962eca59ef11b"></a>

```c
#define USB_HUB_PROTOCOL_CODE USB_HUB_PROTOCOL_HS_SINGLE_TT
```

相关声明：[USB_HUB_PROTOCOL_CODE](#afa18145aa35c0148f9f962eca59ef11b)、[USB_HUB_PROTOCOL_HS_SINGLE_TT](#a89deb4aa95ba6c2f7f774a8b0a1f726b)。

旧别名（Legacy Alias），与 `USB_HUB_PROTOCOL_HS_SINGLE_TT` 相同。

<a id="define-members-1"></a>

### USB 集线器描述符类型（USB Hub Descriptor Types）

<a id="r_aaff00aa691a20b1768001da087304588"></a>

```c
#define USB_HUB_DESCRIPTOR_TYPE 0x29
```

相关声明：[USB_HUB_DESCRIPTOR_TYPE](#aaff00aa691a20b1768001da087304588)。

集线器描述符类型（Hub Descriptor Type）。

<a id="define-members-2"></a>

### USB 集线器类请求代码（USB Hub Class Request Codes）

参见规范（Specification）的表 11-16。

<a id="r_a91ad2acf2c5316d20738f4d65d68ee14"></a>

```c
#define USB_HCREQ_GET_STATUS 0x00
```

相关声明：[USB_HCREQ_GET_STATUS](#a91ad2acf2c5316d20738f4d65d68ee14)。

获取状态请求（Get Status Request）。

<a id="r_a3fc30c26205b41f2ca3abeef815917fa"></a>

```c
#define USB_HCREQ_CLEAR_FEATURE 0x01
```

相关声明：[USB_HCREQ_CLEAR_FEATURE](#a3fc30c26205b41f2ca3abeef815917fa)。

清除特性请求（Clear Feature Request）。

<a id="r_a7b4f58864afb11d881929e81aa4843bd"></a>

```c
#define USB_HCREQ_SET_FEATURE 0x03
```

相关声明：[USB_HCREQ_SET_FEATURE](#a7b4f58864afb11d881929e81aa4843bd)。

设置特性请求（Set Feature Request）。

<a id="r_a5c13eb60a311c0bf7c1f5e9fa1f66f2b"></a>

```c
#define USB_HCREQ_GET_DESCRIPTOR 0x06
```

相关声明：[USB_HCREQ_GET_DESCRIPTOR](#a5c13eb60a311c0bf7c1f5e9fa1f66f2b)。

获取描述符请求（Get Descriptor Request）。

<a id="r_af632ce62b30de5103c799171d08b0f08"></a>

```c
#define USB_HCREQ_SET_DESCRIPTOR 0x07
```

相关声明：[USB_HCREQ_SET_DESCRIPTOR](#af632ce62b30de5103c799171d08b0f08)。

设置描述符请求（Set Descriptor Request）。

<a id="r_a479c4d6fe6691d3cda5d4ba6f868cb2f"></a>

```c
#define USB_HCREQ_CLEAR_TT_BUFFER 0x08
```

相关声明：[USB_HCREQ_CLEAR_TT_BUFFER](#a479c4d6fe6691d3cda5d4ba6f868cb2f)。

清除事务转换器缓冲区请求（Clear TT Buffer Request）。

<a id="r_a09990d8d948aef82115489f60a83250b"></a>

```c
#define USB_HCREQ_RESET_TT 0x09
```

相关声明：[USB_HCREQ_RESET_TT](#a09990d8d948aef82115489f60a83250b)。

复位事务转换器请求（Reset TT Request）。

<a id="r_a4cafe5c744f8e73e1477791c1b64d650"></a>

```c
#define USB_HCREQ_GET_TT_STATE 0x0A
```

相关声明：[USB_HCREQ_GET_TT_STATE](#a4cafe5c744f8e73e1477791c1b64d650)。

获取事务转换器状态请求（Get TT State Request）。

<a id="r_aacc155cfc273b57e73d2893d1693bfd1"></a>

```c
#define USB_HCREQ_STOP_TT 0x0B
```

相关声明：[USB_HCREQ_STOP_TT](#aacc155cfc273b57e73d2893d1693bfd1)。

停止事务转换器请求（Stop TT Request）。

<a id="define-members-3"></a>

### USB 集线器类特性选择器（USB Hub Class Feature Selectors）

参见规范（Specification）的表 11-17。

<a id="r_a997b8615c74e9aa88f8e273b6a3a61fc"></a>

```c
#define USB_HCFS_C_HUB_LOCAL_POWER 0x00
```

相关声明：[USB_HCFS_C_HUB_LOCAL_POWER](#a997b8615c74e9aa88f8e273b6a3a61fc)。

集线器本地电源变化特性选择器（Hub Local Power Change Feature Selector）。

<a id="r_a0b1a392fe6a9e5932158c1cdca43f4bf"></a>

```c
#define USB_HCFS_C_HUB_OVER_CURRENT 0x01
```

相关声明：[USB_HCFS_C_HUB_OVER_CURRENT](#a0b1a392fe6a9e5932158c1cdca43f4bf)。

集线器过流变化特性选择器（Hub Over-current Change Feature Selector）。

<a id="r_ad2d66d4f6f517ea0d3dd76da62742552"></a>

```c
#define USB_HCFS_PORT_CONNECTION 0x00
```

相关声明：[USB_HCFS_PORT_CONNECTION](#ad2d66d4f6f517ea0d3dd76da62742552)。

端口连接特性选择器（Port Connection Feature Selector）。

<a id="r_a5c8ba71161b59bae12afb5dde7728808"></a>

```c
#define USB_HCFS_PORT_ENABLE 0x01
```

相关声明：[USB_HCFS_PORT_ENABLE](#a5c8ba71161b59bae12afb5dde7728808)。

端口使能特性选择器（Port Enable Feature Selector）。

<a id="r_a8cd0227e68d424b758e13f470d838868"></a>

```c
#define USB_HCFS_PORT_SUSPEND 0x02
```

相关声明：[USB_HCFS_PORT_SUSPEND](#a8cd0227e68d424b758e13f470d838868)。

端口挂起特性选择器（Port Suspend Feature Selector）。

<a id="r_ae1c71c8da58b67ed5f12f640827b9d77"></a>

```c
#define USB_HCFS_PORT_OVER_CURRENT 0x03
```

相关声明：[USB_HCFS_PORT_OVER_CURRENT](#ae1c71c8da58b67ed5f12f640827b9d77)。

端口过流特性选择器（Port Over-current Feature Selector）。

<a id="r_ae4fd5c849765661c61b4212f0bfe495e"></a>

```c
#define USB_HCFS_PORT_RESET 0x04
```

相关声明：[USB_HCFS_PORT_RESET](#ae4fd5c849765661c61b4212f0bfe495e)。

端口复位特性选择器（Port Reset Feature Selector）。

<a id="r_a1fe915a2e5569480f4fc24e69f24228c"></a>

```c
#define USB_HCFS_PORT_POWER 0x08
```

相关声明：[USB_HCFS_PORT_POWER](#a1fe915a2e5569480f4fc24e69f24228c)。

端口电源特性选择器（Port Power Feature Selector）。

<a id="r_ab3dc8ec69e15379c606e7e58980617ca"></a>

```c
#define USB_HCFS_PORT_LOW_SPEED 0x09
```

相关声明：[USB_HCFS_PORT_LOW_SPEED](#ab3dc8ec69e15379c606e7e58980617ca)。

端口低速特性选择器（Port Low Speed Feature Selector）。

<a id="r_a75e8cf42cfd77add9f306a20fe6bb14f"></a>

```c
#define USB_HCFS_C_PORT_CONNECTION 0x10
```

相关声明：[USB_HCFS_C_PORT_CONNECTION](#a75e8cf42cfd77add9f306a20fe6bb14f)。

端口连接变化特性选择器（Port Connection Change Feature Selector）。

<a id="r_a71f79a0dbf15b792ffd93305145de316"></a>

```c
#define USB_HCFS_C_PORT_ENABLE 0x11
```

相关声明：[USB_HCFS_C_PORT_ENABLE](#a71f79a0dbf15b792ffd93305145de316)。

端口使能变化特性选择器（Port Enable Change Feature Selector）。

<a id="r_a84c40b25ec588b86131300a4dbc765bd"></a>

```c
#define USB_HCFS_C_PORT_SUSPEND 0x12
```

相关声明：[USB_HCFS_C_PORT_SUSPEND](#a84c40b25ec588b86131300a4dbc765bd)。

端口挂起变化特性选择器（Port Suspend Change Feature Selector）。

<a id="r_aa3273e27d90c343899c4cb1f722c2878"></a>

```c
#define USB_HCFS_C_PORT_OVER_CURRENT 0x13
```

相关声明：[USB_HCFS_C_PORT_OVER_CURRENT](#aa3273e27d90c343899c4cb1f722c2878)。

端口过流变化特性选择器（Port Over-current Change Feature Selector）。

<a id="r_ad53ce209e4472d86b6643c7d391b7f24"></a>

```c
#define USB_HCFS_C_PORT_RESET 0x14
```

相关声明：[USB_HCFS_C_PORT_RESET](#ad53ce209e4472d86b6643c7d391b7f24)。

端口复位变化特性选择器（Port Reset Change Feature Selector）。

<a id="r_a94a24ef58ab59d399a0dfa0f0903dfb0"></a>

```c
#define USB_HCFS_PORT_TEST 0x15
```

相关声明：[USB_HCFS_PORT_TEST](#a94a24ef58ab59d399a0dfa0f0903dfb0)。

端口测试特性选择器（Port Test Feature Selector）。

<a id="r_a2e049932c995b1fe489c38ed0cf09049"></a>

```c
#define USB_HCFS_PORT_INDICATOR 0x16
```

相关声明：[USB_HCFS_PORT_INDICATOR](#a2e049932c995b1fe489c38ed0cf09049)。

端口指示器特性选择器（Port Indicator Feature Selector）。

<a id="define-members-4"></a>

### USB 集线器状态字段 wHubStatus（USB Hub Status Field, wHubStatus）

参见规范（Specification）的表 11-19。

<a id="r_a2f559cd1caba075d19148ace2546a0be"></a>

```c
#define USB_HUB_STATUS_LOCAL_POWER BIT(0)
```

相关声明：[USB_HUB_STATUS_LOCAL_POWER](#a2f559cd1caba075d19148ace2546a0be)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

集线器本地电源状态位（Hub Local Power Status Bit）。

<a id="r_a62fa1aec4dead020fbf0e7c0a49da742"></a>

```c
#define USB_HUB_STATUS_OVER_CURRENT BIT(1)
```

相关声明：[USB_HUB_STATUS_OVER_CURRENT](#a62fa1aec4dead020fbf0e7c0a49da742)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

集线器过流状态位（Hub Over-current Status Bit）。

<a id="define-members-5"></a>

### USB 集线器变化字段 wHubChange（USB Hub Change Field, wHubChange）

参见规范（Specification）的表 11-20。

<a id="r_a2052b94473b3b3ad4d5d3736e53df25a"></a>

```c
#define USB_HUB_CHANGE_LOCAL_POWER BIT(0)
```

相关声明：[USB_HUB_CHANGE_LOCAL_POWER](#a2052b94473b3b3ad4d5d3736e53df25a)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

集线器本地电源变化位（Hub Local Power Change Bit）。

<a id="r_abdba72e7b9e7a8c030f6144ac1e10567"></a>

```c
#define USB_HUB_CHANGE_OVER_CURRENT BIT(1)
```

相关声明：[USB_HUB_CHANGE_OVER_CURRENT](#abdba72e7b9e7a8c030f6144ac1e10567)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

集线器过流变化位（Hub Over-current Change Bit）。

<a id="define-members-6"></a>

### USB 集线器端口状态字段 wPortStatus（USB Hub Port Status Field, wPortStatus）

参见规范（Specification）的表 11-21。

<a id="r_a23ea83195b2ad16144646e270347ff2b"></a>

```c
#define USB_HUB_PORT_STATUS_CONNECTION BIT(0)
```

相关声明：[USB_HUB_PORT_STATUS_CONNECTION](#a23ea83195b2ad16144646e270347ff2b)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

端口连接状态位（Port Connection Status Bit）。

<a id="r_aadfac36490dfb9ada85349fef4ce0662"></a>

```c
#define USB_HUB_PORT_STATUS_ENABLE BIT(1)
```

相关声明：[USB_HUB_PORT_STATUS_ENABLE](#aadfac36490dfb9ada85349fef4ce0662)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

端口使能状态位（Port Enable Status Bit）。

<a id="r_a228040b24ce38bc50264f320fc2699a3"></a>

```c
#define USB_HUB_PORT_STATUS_SUSPEND BIT(2)
```

相关声明：[USB_HUB_PORT_STATUS_SUSPEND](#a228040b24ce38bc50264f320fc2699a3)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

端口挂起状态位（Port Suspend Status Bit）。

<a id="r_a3807e908a10bea029439ed7116dec34a"></a>

```c
#define USB_HUB_PORT_STATUS_OVER_CURRENT BIT(3)
```

相关声明：[USB_HUB_PORT_STATUS_OVER_CURRENT](#a3807e908a10bea029439ed7116dec34a)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

端口过流状态位（Port Over-current Status Bit）。

<a id="r_a4ac5745ed2c116f2d4f4dc7a6ff3aac5"></a>

```c
#define USB_HUB_PORT_STATUS_RESET BIT(4)
```

相关声明：[USB_HUB_PORT_STATUS_RESET](#a4ac5745ed2c116f2d4f4dc7a6ff3aac5)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

端口复位状态位（Port Reset Status Bit）。

<a id="r_a074b9b78954ad2ed8ed9382fbd984362"></a>

```c
#define USB_HUB_PORT_STATUS_POWER BIT(8)
```

相关声明：[USB_HUB_PORT_STATUS_POWER](#a074b9b78954ad2ed8ed9382fbd984362)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

端口电源状态位（Port Power Status Bit）。

<a id="r_a1f36fdd6b73b415f797853b47eb3bcec"></a>

```c
#define USB_HUB_PORT_STATUS_LOW_SPEED BIT(9)
```

相关声明：[USB_HUB_PORT_STATUS_LOW_SPEED](#a1f36fdd6b73b415f797853b47eb3bcec)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

端口低速设备接入位（Port Low Speed Device Attached Bit）。

<a id="r_a91b6bfed358f730d9ca74a290b38ccd1"></a>

```c
#define USB_HUB_PORT_STATUS_HIGH_SPEED BIT(10)
```

相关声明：[USB_HUB_PORT_STATUS_HIGH_SPEED](#a91b6bfed358f730d9ca74a290b38ccd1)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

端口高速设备接入位（Port High Speed Device Attached Bit）。

<a id="r_a34e5c01049adbe7e4534ca2a36b49cbd"></a>

```c
#define USB_HUB_PORT_STATUS_TEST BIT(11)
```

相关声明：[USB_HUB_PORT_STATUS_TEST](#a34e5c01049adbe7e4534ca2a36b49cbd)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

端口测试模式位（Port Test Mode Bit）。

<a id="r_ab6cc05708a4b88fbdd12c0191a3a9d4d"></a>

```c
#define USB_HUB_PORT_STATUS_INDICATOR BIT(12)
```

相关声明：[USB_HUB_PORT_STATUS_INDICATOR](#ab6cc05708a4b88fbdd12c0191a3a9d4d)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

端口指示器控制位（Port Indicator Control Bit）。

<a id="define-members-7"></a>

### USB 集线器端口变化字段 wPortChange（USB Hub Port Change Field, wPortChange）

参见规范（Specification）的表 11-22。

<a id="r_a95ce530cddf8e7808d9f5f9be8388f19"></a>

```c
#define USB_HUB_PORT_CHANGE_CONNECTION BIT(0)
```

相关声明：[USB_HUB_PORT_CHANGE_CONNECTION](#a95ce530cddf8e7808d9f5f9be8388f19)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

端口连接变化位（Port Connection Change Bit）。

<a id="r_a5d339543733053a1f7b6f7fe8af4bc04"></a>

```c
#define USB_HUB_PORT_CHANGE_ENABLE BIT(1)
```

相关声明：[USB_HUB_PORT_CHANGE_ENABLE](#a5d339543733053a1f7b6f7fe8af4bc04)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

端口使能变化位（Port Enable Change Bit）。

<a id="r_a1cb940fa53d43cc6c024e49f5ea14707"></a>

```c
#define USB_HUB_PORT_CHANGE_SUSPEND BIT(2)
```

相关声明：[USB_HUB_PORT_CHANGE_SUSPEND](#a1cb940fa53d43cc6c024e49f5ea14707)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

端口挂起变化位（Port Suspend Change Bit）。

<a id="r_ac18151fde3c4d8120dbdb94fbd9cbbb8"></a>

```c
#define USB_HUB_PORT_CHANGE_OVER_CURRENT BIT(3)
```

相关声明：[USB_HUB_PORT_CHANGE_OVER_CURRENT](#ac18151fde3c4d8120dbdb94fbd9cbbb8)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

端口过流变化位（Port Over-current Change Bit）。

<a id="r_a78315909ff1ca72eaedfb3d038e71afb"></a>

```c
#define USB_HUB_PORT_CHANGE_RESET BIT(4)
```

相关声明：[USB_HUB_PORT_CHANGE_RESET](#a78315909ff1ca72eaedfb3d038e71afb)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

端口复位变化位（Port Reset Change Bit）。

## 12.3\_详细说明（Detailed Documentation）

<a id="a997b8615c74e9aa88f8e273b6a3a61fc"></a>

### `USB_HCFS_C_HUB_LOCAL_POWER`

```c
#define USB_HCFS_C_HUB_LOCAL_POWER 0x00
```

集线器本地电源变化特性选择器（Hub Local Power Change Feature Selector）。

<a id="a0b1a392fe6a9e5932158c1cdca43f4bf"></a>

### `USB_HCFS_C_HUB_OVER_CURRENT`

```c
#define USB_HCFS_C_HUB_OVER_CURRENT 0x01
```

集线器过流变化特性选择器（Hub Over-current Change Feature Selector）。

<a id="a75e8cf42cfd77add9f306a20fe6bb14f"></a>

### `USB_HCFS_C_PORT_CONNECTION`

```c
#define USB_HCFS_C_PORT_CONNECTION 0x10
```

端口连接变化特性选择器（Port Connection Change Feature Selector）。

<a id="a71f79a0dbf15b792ffd93305145de316"></a>

### `USB_HCFS_C_PORT_ENABLE`

```c
#define USB_HCFS_C_PORT_ENABLE 0x11
```

端口使能变化特性选择器（Port Enable Change Feature Selector）。

<a id="aa3273e27d90c343899c4cb1f722c2878"></a>

### `USB_HCFS_C_PORT_OVER_CURRENT`

```c
#define USB_HCFS_C_PORT_OVER_CURRENT 0x13
```

端口过流变化特性选择器（Port Over-current Change Feature Selector）。

<a id="ad53ce209e4472d86b6643c7d391b7f24"></a>

### `USB_HCFS_C_PORT_RESET`

```c
#define USB_HCFS_C_PORT_RESET 0x14
```

端口复位变化特性选择器（Port Reset Change Feature Selector）。

<a id="a84c40b25ec588b86131300a4dbc765bd"></a>

### `USB_HCFS_C_PORT_SUSPEND`

```c
#define USB_HCFS_C_PORT_SUSPEND 0x12
```

端口挂起变化特性选择器（Port Suspend Change Feature Selector）。

<a id="ad2d66d4f6f517ea0d3dd76da62742552"></a>

### `USB_HCFS_PORT_CONNECTION`

```c
#define USB_HCFS_PORT_CONNECTION 0x00
```

端口连接特性选择器（Port Connection Feature Selector）。

<a id="a5c8ba71161b59bae12afb5dde7728808"></a>

### `USB_HCFS_PORT_ENABLE`

```c
#define USB_HCFS_PORT_ENABLE 0x01
```

端口使能特性选择器（Port Enable Feature Selector）。

<a id="a2e049932c995b1fe489c38ed0cf09049"></a>

### `USB_HCFS_PORT_INDICATOR`

```c
#define USB_HCFS_PORT_INDICATOR 0x16
```

端口指示器特性选择器（Port Indicator Feature Selector）。

<a id="ab3dc8ec69e15379c606e7e58980617ca"></a>

### `USB_HCFS_PORT_LOW_SPEED`

```c
#define USB_HCFS_PORT_LOW_SPEED 0x09
```

端口低速特性选择器（Port Low Speed Feature Selector）。

<a id="ae1c71c8da58b67ed5f12f640827b9d77"></a>

### `USB_HCFS_PORT_OVER_CURRENT`

```c
#define USB_HCFS_PORT_OVER_CURRENT 0x03
```

端口过流特性选择器（Port Over-current Feature Selector）。

<a id="a1fe915a2e5569480f4fc24e69f24228c"></a>

### `USB_HCFS_PORT_POWER`

```c
#define USB_HCFS_PORT_POWER 0x08
```

端口电源特性选择器（Port Power Feature Selector）。

<a id="ae4fd5c849765661c61b4212f0bfe495e"></a>

### `USB_HCFS_PORT_RESET`

```c
#define USB_HCFS_PORT_RESET 0x04
```

端口复位特性选择器（Port Reset Feature Selector）。

<a id="a8cd0227e68d424b758e13f470d838868"></a>

### `USB_HCFS_PORT_SUSPEND`

```c
#define USB_HCFS_PORT_SUSPEND 0x02
```

端口挂起特性选择器（Port Suspend Feature Selector）。

<a id="a94a24ef58ab59d399a0dfa0f0903dfb0"></a>

### `USB_HCFS_PORT_TEST`

```c
#define USB_HCFS_PORT_TEST 0x15
```

端口测试特性选择器（Port Test Feature Selector）。

<a id="a3fc30c26205b41f2ca3abeef815917fa"></a>

### `USB_HCREQ_CLEAR_FEATURE`

```c
#define USB_HCREQ_CLEAR_FEATURE 0x01
```

清除特性请求（Clear Feature Request）。

<a id="a479c4d6fe6691d3cda5d4ba6f868cb2f"></a>

### `USB_HCREQ_CLEAR_TT_BUFFER`

```c
#define USB_HCREQ_CLEAR_TT_BUFFER 0x08
```

清除事务转换器缓冲区请求（Clear TT Buffer Request）。

<a id="a5c13eb60a311c0bf7c1f5e9fa1f66f2b"></a>

### `USB_HCREQ_GET_DESCRIPTOR`

```c
#define USB_HCREQ_GET_DESCRIPTOR 0x06
```

获取描述符请求（Get Descriptor Request）。

<a id="a91ad2acf2c5316d20738f4d65d68ee14"></a>

### `USB_HCREQ_GET_STATUS`

```c
#define USB_HCREQ_GET_STATUS 0x00
```

获取状态请求（Get Status Request）。

<a id="a4cafe5c744f8e73e1477791c1b64d650"></a>

### `USB_HCREQ_GET_TT_STATE`

```c
#define USB_HCREQ_GET_TT_STATE 0x0A
```

获取事务转换器状态请求（Get TT State Request）。

<a id="a09990d8d948aef82115489f60a83250b"></a>

### `USB_HCREQ_RESET_TT`

```c
#define USB_HCREQ_RESET_TT 0x09
```

复位事务转换器请求（Reset TT Request）。

<a id="af632ce62b30de5103c799171d08b0f08"></a>

### `USB_HCREQ_SET_DESCRIPTOR`

```c
#define USB_HCREQ_SET_DESCRIPTOR 0x07
```

设置描述符请求（Set Descriptor Request）。

<a id="a7b4f58864afb11d881929e81aa4843bd"></a>

### `USB_HCREQ_SET_FEATURE`

```c
#define USB_HCREQ_SET_FEATURE 0x03
```

设置特性请求（Set Feature Request）。

<a id="aacc155cfc273b57e73d2893d1693bfd1"></a>

### `USB_HCREQ_STOP_TT`

```c
#define USB_HCREQ_STOP_TT 0x0B
```

停止事务转换器请求（Stop TT Request）。

<a id="a2052b94473b3b3ad4d5d3736e53df25a"></a>

### `USB_HUB_CHANGE_LOCAL_POWER`

```c
#define USB_HUB_CHANGE_LOCAL_POWER BIT(0)
```

集线器本地电源变化位（Hub Local Power Change Bit）。

<a id="abdba72e7b9e7a8c030f6144ac1e10567"></a>

### `USB_HUB_CHANGE_OVER_CURRENT`

```c
#define USB_HUB_CHANGE_OVER_CURRENT BIT(1)
```

集线器过流变化位（Hub Over-current Change Bit）。

<a id="aebe338a3fb6193dcbfac244ca8042ad1"></a>

### `USB_HUB_CLASS_CODE`

```c
#define USB_HUB_CLASS_CODE 0x09
```

集线器类代码（Hub Class Code）。

<a id="a046305cfa6801f9df1f180b06f8c7330"></a>

### `USB_HUB_DESC_BUF_SIZE`

```c
#define USB_HUB_DESC_BUF_SIZE 71
```

集线器描述符最大大小（Maximum Hub Descriptor Size）。

固定部分 7 字节，加上最多 32 字节的 `DeviceRemovable`，再加上最多 32 字节的 `PortPwrCtrlMask`。

<a id="aaff00aa691a20b1768001da087304588"></a>

### `USB_HUB_DESCRIPTOR_TYPE`

```c
#define USB_HUB_DESCRIPTOR_TYPE 0x29
```

集线器描述符类型（Hub Descriptor Type）。

<a id="a058a9526a6cc90ca98ceee729d489911"></a>

### `USB_HUB_GET_THINK_TIME`

```c
#define USB_HUB_GET_THINK_TIME ( wHubCharacteristics)
```

展开值（Value）：

```c
(((((wHubCharacteristics) & 0x0060U) >> 5) + 1) << 3)
```

从 `wHubCharacteristics` 字段获取思考时间值（Think Time）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `wHubCharacteristics` | 集线器描述符字段（Hub Descriptor Field）`wHubCharacteristics`。 |

**返回（Returns）**：返回值（Returns）：思考时间（Think Time），以全速位时间（Full-speed Bit Time）为单位，取值为 8、16、24 或 32。

<a id="a95ce530cddf8e7808d9f5f9be8388f19"></a>

### `USB_HUB_PORT_CHANGE_CONNECTION`

```c
#define USB_HUB_PORT_CHANGE_CONNECTION BIT(0)
```

端口连接变化位（Port Connection Change Bit）。

<a id="a5d339543733053a1f7b6f7fe8af4bc04"></a>

### `USB_HUB_PORT_CHANGE_ENABLE`

```c
#define USB_HUB_PORT_CHANGE_ENABLE BIT(1)
```

端口使能变化位（Port Enable Change Bit）。

<a id="ac18151fde3c4d8120dbdb94fbd9cbbb8"></a>

### `USB_HUB_PORT_CHANGE_OVER_CURRENT`

```c
#define USB_HUB_PORT_CHANGE_OVER_CURRENT BIT(3)
```

端口过流变化位（Port Over-current Change Bit）。

<a id="a78315909ff1ca72eaedfb3d038e71afb"></a>

### `USB_HUB_PORT_CHANGE_RESET`

```c
#define USB_HUB_PORT_CHANGE_RESET BIT(4)
```

端口复位变化位（Port Reset Change Bit）。

<a id="a1cb940fa53d43cc6c024e49f5ea14707"></a>

### `USB_HUB_PORT_CHANGE_SUSPEND`

```c
#define USB_HUB_PORT_CHANGE_SUSPEND BIT(2)
```

端口挂起变化位（Port Suspend Change Bit）。

<a id="a23ea83195b2ad16144646e270347ff2b"></a>

### `USB_HUB_PORT_STATUS_CONNECTION`

```c
#define USB_HUB_PORT_STATUS_CONNECTION BIT(0)
```

端口连接状态位（Port Connection Status Bit）。

<a id="aadfac36490dfb9ada85349fef4ce0662"></a>

### `USB_HUB_PORT_STATUS_ENABLE`

```c
#define USB_HUB_PORT_STATUS_ENABLE BIT(1)
```

端口使能状态位（Port Enable Status Bit）。

<a id="a91b6bfed358f730d9ca74a290b38ccd1"></a>

### `USB_HUB_PORT_STATUS_HIGH_SPEED`

```c
#define USB_HUB_PORT_STATUS_HIGH_SPEED BIT(10)
```

端口高速设备接入位（Port High Speed Device Attached Bit）。

<a id="ab6cc05708a4b88fbdd12c0191a3a9d4d"></a>

### `USB_HUB_PORT_STATUS_INDICATOR`

```c
#define USB_HUB_PORT_STATUS_INDICATOR BIT(12)
```

端口指示器控制位（Port Indicator Control Bit）。

<a id="a1f36fdd6b73b415f797853b47eb3bcec"></a>

### `USB_HUB_PORT_STATUS_LOW_SPEED`

```c
#define USB_HUB_PORT_STATUS_LOW_SPEED BIT(9)
```

端口低速设备接入位（Port Low Speed Device Attached Bit）。

<a id="a3807e908a10bea029439ed7116dec34a"></a>

### `USB_HUB_PORT_STATUS_OVER_CURRENT`

```c
#define USB_HUB_PORT_STATUS_OVER_CURRENT BIT(3)
```

端口过流状态位（Port Over-current Status Bit）。

<a id="a074b9b78954ad2ed8ed9382fbd984362"></a>

### `USB_HUB_PORT_STATUS_POWER`

```c
#define USB_HUB_PORT_STATUS_POWER BIT(8)
```

端口电源状态位（Port Power Status Bit）。

<a id="a4ac5745ed2c116f2d4f4dc7a6ff3aac5"></a>

### `USB_HUB_PORT_STATUS_RESET`

```c
#define USB_HUB_PORT_STATUS_RESET BIT(4)
```

端口复位状态位（Port Reset Status Bit）。

<a id="a228040b24ce38bc50264f320fc2699a3"></a>

### `USB_HUB_PORT_STATUS_SUSPEND`

```c
#define USB_HUB_PORT_STATUS_SUSPEND BIT(2)
```

端口挂起状态位（Port Suspend Status Bit）。

<a id="a34e5c01049adbe7e4534ca2a36b49cbd"></a>

### `USB_HUB_PORT_STATUS_TEST`

```c
#define USB_HUB_PORT_STATUS_TEST BIT(11)
```

端口测试模式位（Port Test Mode Bit）。

<a id="afa18145aa35c0148f9f962eca59ef11b"></a>

### `USB_HUB_PROTOCOL_CODE`

```c
#define USB_HUB_PROTOCOL_CODE USB_HUB_PROTOCOL_HS_SINGLE_TT
```

旧别名（Legacy Alias），与 `USB_HUB_PROTOCOL_HS_SINGLE_TT` 相同。

<a id="a7fde1fdcc7ac52b8f54a461b60dd5f37"></a>

### `USB_HUB_PROTOCOL_FS`

```c
#define USB_HUB_PROTOCOL_FS 0x00
```

集线器协议代码（Hub Protocol Codes），参见 USB 2.0 规范表 11-17。

全速／低速集线器（Full/Low-speed Hub），没有事务转换器（TT）。

<a id="af7c6620f35c78adc1ed9b8d7190d4790"></a>

### `USB_HUB_PROTOCOL_HS_MULTI_TT`

```c
#define USB_HUB_PROTOCOL_HS_MULTI_TT 0x02
```

具有多个事务转换器（TT）的高速集线器（High-speed Hub）。

<a id="a89deb4aa95ba6c2f7f774a8b0a1f726b"></a>

### `USB_HUB_PROTOCOL_HS_SINGLE_TT`

```c
#define USB_HUB_PROTOCOL_HS_SINGLE_TT 0x01
```

具有单个事务转换器（TT）的高速集线器（High-speed Hub）。

<a id="a2f559cd1caba075d19148ace2546a0be"></a>

### `USB_HUB_STATUS_LOCAL_POWER`

```c
#define USB_HUB_STATUS_LOCAL_POWER BIT(0)
```

集线器本地电源状态位（Hub Local Power Status Bit）。

<a id="a62fa1aec4dead020fbf0e7c0a49da742"></a>

### `USB_HUB_STATUS_OVER_CURRENT`

```c
#define USB_HUB_STATUS_OVER_CURRENT BIT(1)
```

集线器过流状态位（Hub Over-current Status Bit）。

<a id="a5633c828019ace8d57e864b575406709"></a>

### `USB_HUB_SUBCLASS_CODE`

```c
#define USB_HUB_SUBCLASS_CODE 0x00
```

集线器子类代码（Hub Subclass Code）。


## 12.4\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_reference/P888_usb_hub.h_源码浏览.md)
- [usb_hub_descriptor](../device_power_control_model_reference/P097_usb_hub_descriptor_结构体.md)
- [usb_hub_status](../device_power_control_model_reference/P099_usb_hub_status_结构体.md)
- [usb_hub_port_status](../device_power_control_model_reference/P098_usb_hub_port_status_结构体.md)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P011_zephyr__drivers__misc__renesas_rx_dtc__renesas_rx_dtc.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P013_zephyr__drivers__usb_c__usbc_pd.h_文件参考.md)
