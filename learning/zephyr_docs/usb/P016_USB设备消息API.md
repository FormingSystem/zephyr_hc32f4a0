---
id: learning.zephyr-docs.usb.api-16
title: USB设备消息API
kind: reference
status: maintained
domains: [zephyr, usb, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__usbd__msg__api.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第16章\_USB设备消息API

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__usbd__msg__api.html)。读取日期：2026-10-14；基线为保存的 `latest` 页面，HTML 摘要见[来源记录](../SOURCES.md)。

## 16.1\_阅读说明与来源

译注：配合[USB设备支持](P002_USB设备支持.md)与[设备栈API说明](P014_USB设备栈API说明.md)阅读。这里翻译新版设备栈核心接口、通知消息及其数据结构；旧版 usb_enable() 接口另见旧版指南。函数参数、返回值和原始宏定义按保存的官方页面保留，源码差异明确标为译注。

本组：[USB设备核心API](P015_USB设备核心API.md) · [USB设备消息API](P016_USB设备消息API.md) · [USB设备消息结构](P017_USB设备消息结构.md)。

自 Zephyr 3.7 引入；接口版本为 0.2.0。

## 16.2\_数据结构（Data Structures）

<a id="r_usbd_5Fmsg"></a>

```c
struct usbd_msg
```

USB 设备消息（Message）。

相关声明：[usbd_msg](P017_USB设备消息结构.md)。

## 16.3\_枚举（Enumerations）

<a id="r_gaa9163408c0006825575a919322f25f56"></a>

```c
enum usbd_msg_type { USBD_MSG_VBUS_READY , USBD_MSG_VBUS_REMOVED , USBD_MSG_RESUME , USBD_MSG_SUSPEND , USBD_MSG_RESET , USBD_MSG_CONFIGURATION , USBD_MSG_UDC_ERROR , USBD_MSG_STACK_ERROR , USBD_MSG_CDC_ACM_LINE_CODING , USBD_MSG_CDC_ACM_CONTROL_LINE_STATE , USBD_MSG_DFU_APP_DETACH , USBD_MSG_DFU_DOWNLOAD_COMPLETED , USBD_MSG_MAX_NUMBER }
```

USB 设备支持的消息类型。

相关声明：[usbd_msg_type](P016_USB设备消息API.md#gaa9163408c0006825575a919322f25f56)、[USBD_MSG_VBUS_READY](P016_USB设备消息API.md#ggaa9163408c0006825575a919322f25f56a4b313687741459c964322c471eb3d61d)、[USBD_MSG_VBUS_REMOVED](P016_USB设备消息API.md#ggaa9163408c0006825575a919322f25f56ab680ec928192288ca6b4acf729cf7268)、[USBD_MSG_RESUME](P016_USB设备消息API.md#ggaa9163408c0006825575a919322f25f56a426138988ff9e9274bf03ae7c4650d32)、[USBD_MSG_SUSPEND](P016_USB设备消息API.md#ggaa9163408c0006825575a919322f25f56a790c82f770e7b4c34cf36c3dbf1375f6)、[USBD_MSG_RESET](P016_USB设备消息API.md#ggaa9163408c0006825575a919322f25f56ac57b2327e425927e276bd632f090d156)、[USBD_MSG_CONFIGURATION](P016_USB设备消息API.md#ggaa9163408c0006825575a919322f25f56af7d92f86d4953ae3160abc91b975c7ce)、[USBD_MSG_UDC_ERROR](P016_USB设备消息API.md#ggaa9163408c0006825575a919322f25f56a49cb7594f7394e1672bdcadeadfe73a3)、[USBD_MSG_STACK_ERROR](P016_USB设备消息API.md#ggaa9163408c0006825575a919322f25f56acac7d18047e013a94507e4047030c641)、[USBD_MSG_CDC_ACM_LINE_CODING](P016_USB设备消息API.md#ggaa9163408c0006825575a919322f25f56a820f9547e0db4baea563dca9c211f9b1)、[USBD_MSG_CDC_ACM_CONTROL_LINE_STATE](P016_USB设备消息API.md#ggaa9163408c0006825575a919322f25f56abab0429d965ce259077295173f5fcd5f)、[USBD_MSG_DFU_APP_DETACH](P016_USB设备消息API.md#ggaa9163408c0006825575a919322f25f56af80d93cdeb2ed8620f3fd4a5d0d0a2b1)、[USBD_MSG_DFU_DOWNLOAD_COMPLETED](P016_USB设备消息API.md#ggaa9163408c0006825575a919322f25f56a9ee9c7aad5d802e7368b2ba7c33ae071)、[USBD_MSG_MAX_NUMBER](P016_USB设备消息API.md#ggaa9163408c0006825575a919322f25f56adb21635528f4f87ccce7dceae67ef3af)。

## 16.4\_函数（Functions）

<a id="r_ga6cf3d874b1516256187bd96cf73ddde4"></a>

```c
static const char * usbd_msg_type_string (const enum usbd_msg_type type)
```

以常量字符串返回消息类型。

相关声明：[usbd_msg_type_string](P016_USB设备消息API.md#ga6cf3d874b1516256187bd96cf73ddde4)、[usbd_msg_type](P016_USB设备消息API.md#gaa9163408c0006825575a919322f25f56)。

## 16.5\_详细说明（Detailed Documentation）

<a id="gaa9163408c0006825575a919322f25f56"></a>

### `usbd_msg_type`

```c
enum usbd_msg_type
```

```c
#include <zephyr/usb/usbd_msg.h>
```

USB 设备支持的消息类型。

第一组消息类型对应 UDC 驱动 API 的事件类型。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `USBD_MSG_VBUS_READY` | VBUS 就绪消息，可选。 |
| `USBD_MSG_VBUS_REMOVED` | VBUS 移除消息，可选。 |
| `USBD_MSG_RESUME` | 设备恢复（Resume）消息。 |
| `USBD_MSG_SUSPEND` | 设备挂起消息。 |
| `USBD_MSG_RESET` | 检测到总线复位。 |
| `USBD_MSG_CONFIGURATION` | 设备配置发生变化。 |
| `USBD_MSG_UDC_ERROR` | 不可纠正的 UDC 错误消息。 |
| `USBD_MSG_STACK_ERROR` | 不可恢复的设备栈错误消息。 |
| `USBD_MSG_CDC_ACM_LINE_CODING` | CDC ACM 线路编码（Line Coding）更新。 |
| `USBD_MSG_CDC_ACM_CONTROL_LINE_STATE` | CDC ACM 线路状态（Line State）更新。 |
| `USBD_MSG_DFU_APP_DETACH` | USB 设备固件升级（Device Firmware Upgrade，DFU）类的分离请求。 |
| `USBD_MSG_DFU_DOWNLOAD_COMPLETED` | USB DFU 类下载完成。 |
| `USBD_MSG_MAX_NUMBER` | 消息类型的最大数量。 |

<a id="ga6cf3d874b1516256187bd96cf73ddde4"></a>

### `usbd_msg_type_string()`

```c
const char * usbd_msg_type_string ( const enum usbd_msg_type type) inlinestatic
```

```c
#include <zephyr/usb/usbd_msg.h>
```

以常量字符串返回消息类型。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] type` | USBD 消息类型。 |

**返回（Returns）**：表示消息类型的常量字符串。

> 译注（源码核对）：当前实现对合法枚举返回对应常量字符串，超出 0 到 USBD_MSG_MAX_NUMBER-1 的范围时返回 "?"。USBD_MSG_MAX_NUMBER 是计数边界，不是一个可投递事件。

## 16.6\_相关源码与使用边界

本仓库的[核心头文件](../../../include/zephyr/usb/usbd.h)、[消息头文件](../../../include/zephyr/usb/usbd_msg.h)、[类注册实现](../../../subsys/usb/device_next/usbd_class.c)、[设备生命周期实现](../../../subsys/usb/device_next/usbd_device.c)与[消息投递实现](../../../subsys/usb/device_next/usbd_msg.c)可用于源码跟踪，版本可能与官网 latest 不同。译注核对依据为保存的[官方核心头文件](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/include/zephyr/usb/usbd.h)、[消息定义](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/include/zephyr/usb/usbd_msg.h)、[类实现](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/device_next/usbd_class.c)、[设备实现](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/device_next/usbd_device.c)、[配置实现](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/device_next/usbd_config.c)与[消息实现](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/device_next/usbd_msg.c)，摘要见[来源记录](../SOURCES.md)。本批没有构建或运行USB固件，也未进行实板验证。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>
<a id="header-enum-members"></a>
<a id="enum-members"></a>
<a id="header-func-members"></a>
<a id="func-members"></a>
<a id="details"></a>
<a id="header-details"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="ggaa9163408c0006825575a919322f25f56a4b313687741459c964322c471eb3d61d"></a>
<a id="ggaa9163408c0006825575a919322f25f56ab680ec928192288ca6b4acf729cf7268"></a>
<a id="ggaa9163408c0006825575a919322f25f56a426138988ff9e9274bf03ae7c4650d32"></a>
<a id="ggaa9163408c0006825575a919322f25f56a790c82f770e7b4c34cf36c3dbf1375f6"></a>
<a id="ggaa9163408c0006825575a919322f25f56ac57b2327e425927e276bd632f090d156"></a>
<a id="ggaa9163408c0006825575a919322f25f56af7d92f86d4953ae3160abc91b975c7ce"></a>
<a id="ggaa9163408c0006825575a919322f25f56a49cb7594f7394e1672bdcadeadfe73a3"></a>
<a id="ggaa9163408c0006825575a919322f25f56acac7d18047e013a94507e4047030c641"></a>
<a id="ggaa9163408c0006825575a919322f25f56a820f9547e0db4baea563dca9c211f9b1"></a>
<a id="ggaa9163408c0006825575a919322f25f56abab0429d965ce259077295173f5fcd5f"></a>
<a id="ggaa9163408c0006825575a919322f25f56af80d93cdeb2ed8620f3fd4a5d0d0a2b1"></a>
<a id="ggaa9163408c0006825575a919322f25f56a9ee9c7aad5d802e7368b2ba7c33ae071"></a>
<a id="ggaa9163408c0006825575a919322f25f56adb21635528f4f87ccce7dceae67ef3af"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

[上一章](P015_USB设备核心API.md) · [返回大纲](大纲.md) · [下一章](P017_USB设备消息结构.md)
