---
id: learning.zephyr-docs.api-file-configuration-reference.page-78
title: zephyr__usb__usbd_msg.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/usbd__msg_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第78章\_zephyr\_\_usb\_\_usbd\_msg.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/usbd__msg_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

USB支持消息（Support Message）的类型和结构。

<a id="details"></a>

```c
#include <stdint.h>
```

查看此文件的源码。

USB支持消息（Support Message）的类型和结构。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 78.1\_数据结构（Data Structures）

<a id="r_usbd_5Fmsg"></a>

```c
struct usbd_msg
```

相关声明：[usbd_msg](../usb/P017_USB设备消息结构.md)。

USB设备消息（Device Message）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 78.2\_枚举（Enumerations）

<a id="r_gaa9163408c0006825575a919322f25f56"></a>

```c
enum usbd_msg_type { USBD_MSG_VBUS_READY , USBD_MSG_VBUS_REMOVED , USBD_MSG_RESUME , USBD_MSG_SUSPEND , USBD_MSG_RESET , USBD_MSG_CONFIGURATION , USBD_MSG_UDC_ERROR , USBD_MSG_STACK_ERROR , USBD_MSG_CDC_ACM_LINE_CODING , USBD_MSG_CDC_ACM_CONTROL_LINE_STATE , USBD_MSG_DFU_APP_DETACH , USBD_MSG_DFU_DOWNLOAD_COMPLETED , USBD_MSG_MAX_NUMBER }
```

相关声明：[usbd_msg_type](../usb/P016_USB设备消息API.md#gaa9163408c0006825575a919322f25f56)、[USBD_MSG_VBUS_READY](../usb/P016_USB设备消息API.md#ggaa9163408c0006825575a919322f25f56a4b313687741459c964322c471eb3d61d)、[USBD_MSG_VBUS_REMOVED](../usb/P016_USB设备消息API.md#ggaa9163408c0006825575a919322f25f56ab680ec928192288ca6b4acf729cf7268)、[USBD_MSG_RESUME](../usb/P016_USB设备消息API.md#ggaa9163408c0006825575a919322f25f56a426138988ff9e9274bf03ae7c4650d32)、[USBD_MSG_SUSPEND](../usb/P016_USB设备消息API.md#ggaa9163408c0006825575a919322f25f56a790c82f770e7b4c34cf36c3dbf1375f6)、[USBD_MSG_RESET](../usb/P016_USB设备消息API.md#ggaa9163408c0006825575a919322f25f56ac57b2327e425927e276bd632f090d156)、[USBD_MSG_CONFIGURATION](../usb/P016_USB设备消息API.md#ggaa9163408c0006825575a919322f25f56af7d92f86d4953ae3160abc91b975c7ce)、[USBD_MSG_UDC_ERROR](../usb/P016_USB设备消息API.md#ggaa9163408c0006825575a919322f25f56a49cb7594f7394e1672bdcadeadfe73a3)、[USBD_MSG_STACK_ERROR](../usb/P016_USB设备消息API.md#ggaa9163408c0006825575a919322f25f56acac7d18047e013a94507e4047030c641)、[USBD_MSG_CDC_ACM_LINE_CODING](../usb/P016_USB设备消息API.md#ggaa9163408c0006825575a919322f25f56a820f9547e0db4baea563dca9c211f9b1)、[USBD_MSG_CDC_ACM_CONTROL_LINE_STATE](../usb/P016_USB设备消息API.md#ggaa9163408c0006825575a919322f25f56abab0429d965ce259077295173f5fcd5f)、[USBD_MSG_DFU_APP_DETACH](../usb/P016_USB设备消息API.md#ggaa9163408c0006825575a919322f25f56af80d93cdeb2ed8620f3fd4a5d0d0a2b1)、[USBD_MSG_DFU_DOWNLOAD_COMPLETED](../usb/P016_USB设备消息API.md#ggaa9163408c0006825575a919322f25f56a9ee9c7aad5d802e7368b2ba7c33ae071)、[USBD_MSG_MAX_NUMBER](../usb/P016_USB设备消息API.md#ggaa9163408c0006825575a919322f25f56adb21635528f4f87ccce7dceae67ef3af)。

USB 设备支持消息类型（USB Device Support Message Types）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 78.3\_函数（Functions）

<a id="r_ga6cf3d874b1516256187bd96cf73ddde4"></a>

```c
static const char * usbd_msg_type_string (const enum usbd_msg_type type)
```

相关声明：[usbd_msg_type_string](../usb/P016_USB设备消息API.md#ga6cf3d874b1516256187bd96cf73ddde4)、[usbd_msg_type](../usb/P016_USB设备消息API.md#gaa9163408c0006825575a919322f25f56)。

以常量字符串（Constant String）形式返回消息类型（Message Type）。


## 78.4\_原页交叉引用（Cross References）

- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h_source.html)
- [查看此文件的源码。](../api_source_reference/P896_usbd_msg.h_源码浏览.md)
- [usbd_msg](../usb/P017_USB设备消息结构.md)
- [usbd_msg_type](../usb/P016_USB设备消息API.md#gaa9163408c0006825575a919322f25f56)
- [USBD_MSG_VBUS_READY](../usb/P016_USB设备消息API.md#ggaa9163408c0006825575a919322f25f56a4b313687741459c964322c471eb3d61d)
- [USBD_MSG_VBUS_REMOVED](../usb/P016_USB设备消息API.md#ggaa9163408c0006825575a919322f25f56ab680ec928192288ca6b4acf729cf7268)
- [USBD_MSG_RESUME](../usb/P016_USB设备消息API.md#ggaa9163408c0006825575a919322f25f56a426138988ff9e9274bf03ae7c4650d32)
- [USBD_MSG_SUSPEND](../usb/P016_USB设备消息API.md#ggaa9163408c0006825575a919322f25f56a790c82f770e7b4c34cf36c3dbf1375f6)
- [USBD_MSG_RESET](../usb/P016_USB设备消息API.md#ggaa9163408c0006825575a919322f25f56ac57b2327e425927e276bd632f090d156)
- [USBD_MSG_CONFIGURATION](../usb/P016_USB设备消息API.md#ggaa9163408c0006825575a919322f25f56af7d92f86d4953ae3160abc91b975c7ce)
- [USBD_MSG_UDC_ERROR](../usb/P016_USB设备消息API.md#ggaa9163408c0006825575a919322f25f56a49cb7594f7394e1672bdcadeadfe73a3)
- [USBD_MSG_STACK_ERROR](../usb/P016_USB设备消息API.md#ggaa9163408c0006825575a919322f25f56acac7d18047e013a94507e4047030c641)
- [USBD_MSG_CDC_ACM_LINE_CODING](../usb/P016_USB设备消息API.md#ggaa9163408c0006825575a919322f25f56a820f9547e0db4baea563dca9c211f9b1)
- [USBD_MSG_CDC_ACM_CONTROL_LINE_STATE](../usb/P016_USB设备消息API.md#ggaa9163408c0006825575a919322f25f56abab0429d965ce259077295173f5fcd5f)
- [USBD_MSG_DFU_APP_DETACH](../usb/P016_USB设备消息API.md#ggaa9163408c0006825575a919322f25f56af80d93cdeb2ed8620f3fd4a5d0d0a2b1)
- [USBD_MSG_DFU_DOWNLOAD_COMPLETED](../usb/P016_USB设备消息API.md#ggaa9163408c0006825575a919322f25f56a9ee9c7aad5d802e7368b2ba7c33ae071)
- [USBD_MSG_MAX_NUMBER](../usb/P016_USB设备消息API.md#ggaa9163408c0006825575a919322f25f56adb21635528f4f87ccce7dceae67ef3af)
- [usbd_msg_type_string](../usb/P016_USB设备消息API.md#ga6cf3d874b1516256187bd96cf73ddde4)

<a id="header-details"></a>

---

[上一章](P077_zephyr__usb__class__usbd_msc.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P079_zephyr__xen__version.h_文件参考.md)
