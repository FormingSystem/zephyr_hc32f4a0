---
id: learning.zephyr-docs.api-source-reference.page-896
title: usbd_msg.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/usbd__msg_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第896章\_usbd\_msg.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/usbd__msg_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/usbd__msg_8h.html)。

## 896.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00011"></a>
<a id="l00012"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00018"></a>
<a id="l00019"></a>
<a id="l00020"></a>
<a id="l00028"></a>
<a id="foldopen00034"></a>
<a id="l00034"></a>
<a id="l00036"></a>
<a id="l00038"></a>
<a id="l00040"></a>
<a id="l00042"></a>
<a id="l00044"></a>
<a id="l00046"></a>
<a id="l00048"></a>
<a id="l00050"></a>
<a id="l00052"></a>
<a id="l00054"></a>
<a id="l00056"></a>
<a id="l00058"></a>
<a id="l00060"></a>
<a id="l00061"></a>
<a id="l00062"></a>
<a id="l00066"></a>
<a id="l00067"></a>
<a id="l00068"></a>
<a id="l00069"></a>
<a id="l00070"></a>
<a id="l00071"></a>
<a id="l00072"></a>
<a id="l00073"></a>
<a id="l00074"></a>
<a id="l00075"></a>
<a id="l00076"></a>
<a id="l00077"></a>
<a id="l00078"></a>
<a id="l00079"></a>
<a id="l00080"></a>
<a id="l00081"></a>
<a id="l00082"></a>
<a id="l00084"></a>
<a id="foldopen00088"></a>
<a id="l00088"></a>
<a id="l00090"></a>
<a id="l00092"></a>
<a id="l00093"></a>
<a id="l00094"></a>
<a id="l00095"></a>
<a id="l00096"></a>
<a id="l00097"></a>
<a id="foldopen00105"></a>
<a id="l00105"></a>
<a id="l00106"></a>
<a id="l00107"></a>
<a id="l00108"></a>
<a id="l00109"></a>
<a id="l00110"></a>
<a id="l00111"></a>
<a id="l00112"></a>
<a id="l00113"></a>
<a id="l00117"></a>
<a id="l00118"></a>
<a id="l00119"></a>
<a id="l00120"></a>
<a id="l00121"></a>
<a id="l00122"></a>
<a id="agroup__sys-util_html_ga70c57aae3eb654e205459b4362c8089a"></a>
<a id="agroup__usbd__msg__api_html_ga6cf3d874b1516256187bd96cf73ddde4"></a>
<a id="agroup__usbd__msg__api_html_gaa9163408c0006825575a919322f25f56"></a>
<a id="agroup__usbd__msg__api_html_ggaa9163408c0006825575a919322f25f56a426138988ff9e9274bf03ae7c4650d32"></a>
<a id="agroup__usbd__msg__api_html_ggaa9163408c0006825575a919322f25f56a49cb7594f7394e1672bdcadeadfe73a3"></a>
<a id="agroup__usbd__msg__api_html_ggaa9163408c0006825575a919322f25f56a4b313687741459c964322c471eb3d61d"></a>
<a id="agroup__usbd__msg__api_html_ggaa9163408c0006825575a919322f25f56a790c82f770e7b4c34cf36c3dbf1375f6"></a>
<a id="agroup__usbd__msg__api_html_ggaa9163408c0006825575a919322f25f56a820f9547e0db4baea563dca9c211f9b1"></a>
<a id="agroup__usbd__msg__api_html_ggaa9163408c0006825575a919322f25f56a9ee9c7aad5d802e7368b2ba7c33ae071"></a>
<a id="agroup__usbd__msg__api_html_ggaa9163408c0006825575a919322f25f56ab680ec928192288ca6b4acf729cf7268"></a>
<a id="agroup__usbd__msg__api_html_ggaa9163408c0006825575a919322f25f56abab0429d965ce259077295173f5fcd5f"></a>
<a id="agroup__usbd__msg__api_html_ggaa9163408c0006825575a919322f25f56ac57b2327e425927e276bd632f090d156"></a>
<a id="agroup__usbd__msg__api_html_ggaa9163408c0006825575a919322f25f56acac7d18047e013a94507e4047030c641"></a>
<a id="agroup__usbd__msg__api_html_ggaa9163408c0006825575a919322f25f56adb21635528f4f87ccce7dceae67ef3af"></a>
<a id="agroup__usbd__msg__api_html_ggaa9163408c0006825575a919322f25f56af7d92f86d4953ae3160abc91b975c7ce"></a>
<a id="agroup__usbd__msg__api_html_ggaa9163408c0006825575a919322f25f56af80d93cdeb2ed8620f3fd4a5d0d0a2b1"></a>
<a id="astdint_8h_html"></a>
<a id="astructdevice_html"></a>
<a id="astructusbd__msg_html"></a>
<a id="astructusbd__msg_html_a37b6c815edc24c8aed291fac7c765abe"></a>
<a id="astructusbd__msg_html_ab75e8dfe889902f536367c0ef15410f8"></a>
<a id="astructusbd__msg_html_ad3cc8990c42917871981f2f810a2d7e7"></a>

```c
/*
 * Copyright (c) 2024 Nordic Semiconductor ASA
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_USBD_MSG_H_
#define ZEPHYR_INCLUDE_USBD_MSG_H_

#include <stdint.h>

#ifdef __cplusplus
extern "C" {
#endif


enum usbd_msg_type {
        USBD_MSG_VBUS_READY,
        USBD_MSG_VBUS_REMOVED,
        USBD_MSG_RESUME,
        USBD_MSG_SUSPEND,
        USBD_MSG_RESET,
        USBD_MSG_CONFIGURATION,
        USBD_MSG_UDC_ERROR,
        USBD_MSG_STACK_ERROR,
        USBD_MSG_CDC_ACM_LINE_CODING,
        USBD_MSG_CDC_ACM_CONTROL_LINE_STATE,
        USBD_MSG_DFU_APP_DETACH,
        USBD_MSG_DFU_DOWNLOAD_COMPLETED,
        USBD_MSG_MAX_NUMBER,
};

static const char *const usbd_msg_type_list[] = {
        "VBUS ready",
        "VBUS removed",
        "Device resumed",
        "Device suspended",
        "Bus reset",
        "New device configuration",
        "Controller error",
        "Stack error",
        "CDC ACM line coding",
        "CDC ACM control line state",
        "DFU detach request",
        "DFU download completed",
};

BUILD_ASSERT(ARRAY_SIZE(usbd_msg_type_list) == USBD_MSG_MAX_NUMBER,
             "Number of entries in usbd_msg_type_list is not equal to USBD_MSG_MAX_NUMBER");

struct usbd_msg {
        enum usbd_msg_type type;
        union {
                int status;
                const struct device *dev;
        };
};

static inline const char *usbd_msg_type_string(const enum usbd_msg_type type)
{
        if (type >= 0 && type < USBD_MSG_MAX_NUMBER) {
                return usbd_msg_type_list[type];
        }

        return "?";
}


#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_USBD_MSG_H_ */
```

## 896.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2024 Nordic Semiconductor ASA。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 122 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_USBD_MSG_H_`。

## 896.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/usbd__msg_8h.html)
- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html)
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
- [ARRAY_SIZE](../util_reference/P001_通用工具公共接口.md#ga70c57aae3eb654e205459b4362c8089a)
- [usbd_msg](../usb/P017_USB设备消息结构.md)
- [type](../usb/P017_USB设备消息结构.md#a37b6c815edc24c8aed291fac7c765abe)
- [status](../usb/P017_USB设备消息结构.md#ad3cc8990c42917871981f2f810a2d7e7)
- [device](../device_reference/P002_设备对象结构.md)
- [dev](../usb/P017_USB设备消息结构.md#ab75e8dfe889902f536367c0ef15410f8)
- [usbd_msg_type_string](../usb/P016_USB设备消息API.md#ga6cf3d874b1516256187bd96cf73ddde4)
- [usbd_msg::type](../usb/P017_USB设备消息结构.md#a37b6c815edc24c8aed291fac7c765abe)
- [usbd_msg::dev](../usb/P017_USB设备消息结构.md#ab75e8dfe889902f536367c0ef15410f8)
- [usbd_msg::status](../usb/P017_USB设备消息结构.md#ad3cc8990c42917871981f2f810a2d7e7)

---

[上一章](P895_usbd_msc.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P897_usbd_uac2.h_源码浏览.md)
