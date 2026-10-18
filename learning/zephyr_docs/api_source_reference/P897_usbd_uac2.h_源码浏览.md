---
id: learning.zephyr-docs.api-source-reference.page-897
title: usbd_uac2.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/usbd__uac2_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第897章\_usbd\_uac2.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/usbd__uac2_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/usbd__uac2_8h.html)。

## 897.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00018"></a>
<a id="l00019"></a>
<a id="l00020"></a>
<a id="l00021"></a>
<a id="l00030"></a>
<a id="foldopen00036"></a>
<a id="l00036"></a>
<a id="l00037"></a>
<a id="l00038"></a>
<a id="l00039"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="foldopen00045"></a>
<a id="l00045"></a>
<a id="l00055"></a>
<a id="l00068"></a>
<a id="l00069"></a>
<a id="l00070"></a>
<a id="l00085"></a>
<a id="l00086"></a>
<a id="l00100"></a>
<a id="l00101"></a>
<a id="l00114"></a>
<a id="l00115"></a>
<a id="l00134"></a>
<a id="l00135"></a>
<a id="l00150"></a>
<a id="l00151"></a>
<a id="l00167"></a>
<a id="l00168"></a>
<a id="l00169"></a>
<a id="l00170"></a>
<a id="l00178"></a>
<a id="l00179"></a>
<a id="l00180"></a>
<a id="l00197"></a>
<a id="l00198"></a>
<a id="l00199"></a>
<a id="l00203"></a>
<a id="l00204"></a>
<a id="adevice_8h_html"></a>
<a id="agroup__uac2__device_html_ga802a727c1a201c26a3bd74f0e7f0900c"></a>
<a id="agroup__uac2__device_html_gae899d75d786f5b1df86db48de88d1254"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astructdevice_html"></a>
<a id="astructdevice_html_a27573cbd10ee145f8bb1396242b27a3e"></a>
<a id="astructdevice_html_ab6d65f3402e67afb9810a8356b915071"></a>
<a id="astructuac2__ops_html"></a>
<a id="astructuac2__ops_html_a76e31b01dc6ce52793735b70301e8470"></a>
<a id="astructuac2__ops_html_aa934f5ecee8f8e67e2165735a6dd2bca"></a>
<a id="astructuac2__ops_html_ab658d1468ba300f882dfb61e3e73ed1b"></a>
<a id="astructuac2__ops_html_abb973db8018d09ba34f508c4e8aff573"></a>
<a id="astructuac2__ops_html_ad427ec3534c8c2b1fe097a7eb83a2e87"></a>
<a id="astructuac2__ops_html_ad8a5599b97edbecc653da41a970f378d"></a>
<a id="astructuac2__ops_html_ae938633dcf6eb6f120ca458bf8a2142f"></a>

```c
/*
 * Copyright (c) 2023-2024 Nordic Semiconductor ASA
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_USB_CLASS_USBD_UAC2_H_
#define ZEPHYR_INCLUDE_USB_CLASS_USBD_UAC2_H_

#include <zephyr/device.h>


#define UAC2_ENTITY_ID(node)                                                    \
        ({                                                                      \
                BUILD_ASSERT(DT_NODE_HAS_COMPAT(DT_PARENT(node), zephyr_uac2)); \
                UTIL_INC(DT_NODE_CHILD_IDX(node));                              \
        })

struct uac2_ops {
        void (*sof_cb)(const struct device *dev, void *user_data);
        void (*terminal_update_cb)(const struct device *dev, uint8_t terminal,
                                   bool enabled, bool microframes,
                                   void *user_data);
        void *(*get_recv_buf)(const struct device *dev, uint8_t terminal,
                              uint16_t size, void *user_data);
        void (*data_recv_cb)(const struct device *dev, uint8_t terminal,
                             void *buf, uint16_t size, void *user_data);
        void (*buf_release_cb)(const struct device *dev, uint8_t terminal,
                               void *buf, void *user_data);
        uint32_t (*feedback_cb)(const struct device *dev, uint8_t terminal,
                                void *user_data);
        uint32_t (*get_sample_rate)(const struct device *dev, uint8_t clock_id,
                                    void *user_data);
        int (*set_sample_rate)(const struct device *dev, uint8_t clock_id,
                               uint32_t rate, void *user_data);
};

void usbd_uac2_set_ops(const struct device *dev,
                       const struct uac2_ops *ops, void *user_data);

int usbd_uac2_send(const struct device *dev, uint8_t terminal,
                   void *data, uint16_t size);


#endif /* ZEPHYR_INCLUDE_USB_CLASS_USBD_UAC2_H_ */
```

## 897.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2023-2024 Nordic Semiconductor ASA。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 204 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_USB_CLASS_USBD_UAC2_H_`。

## 897.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/usbd__uac2_8h.html)
- [zephyr/device.h](../device_reference/P007_设备模型头文件参考.md)
- [uac2_ops](../usb/P090_USB音频2回调接口.md)
- [sof_cb](../usb/P090_USB音频2回调接口.md#a76e31b01dc6ce52793735b70301e8470)
- [device](../device_reference/P002_设备对象结构.md)
- [terminal_update_cb](../usb/P090_USB音频2回调接口.md#ae938633dcf6eb6f120ca458bf8a2142f)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [data_recv_cb](../usb/P090_USB音频2回调接口.md#abb973db8018d09ba34f508c4e8aff573)
- [buf_release_cb](../usb/P090_USB音频2回调接口.md#aa934f5ecee8f8e67e2165735a6dd2bca)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [feedback_cb](../usb/P090_USB音频2回调接口.md#ad427ec3534c8c2b1fe097a7eb83a2e87)
- [get_sample_rate](../usb/P090_USB音频2回调接口.md#ad8a5599b97edbecc653da41a970f378d)
- [set_sample_rate](../usb/P090_USB音频2回调接口.md#ab658d1468ba300f882dfb61e3e73ed1b)
- [usbd_uac2_set_ops](../usb/P089_USB音频2设备API.md#ga802a727c1a201c26a3bd74f0e7f0900c)
- [ops](../device_reference/P002_设备对象结构.md#ab6d65f3402e67afb9810a8356b915071)
- [usbd_uac2_send](../usb/P089_USB音频2设备API.md#gae899d75d786f5b1df86db48de88d1254)
- [data](../device_reference/P002_设备对象结构.md#a27573cbd10ee145f8bb1396242b27a3e)
- [device.h](../device_reference/P007_设备模型头文件参考.md)
- [device::data](../device_reference/P002_设备对象结构.md#a27573cbd10ee145f8bb1396242b27a3e)
- [device::ops](../device_reference/P002_设备对象结构.md#ab6d65f3402e67afb9810a8356b915071)
- [uac2_ops::sof_cb](../usb/P090_USB音频2回调接口.md#a76e31b01dc6ce52793735b70301e8470)
- [uac2_ops::buf_release_cb](../usb/P090_USB音频2回调接口.md#aa934f5ecee8f8e67e2165735a6dd2bca)
- [uac2_ops::set_sample_rate](../usb/P090_USB音频2回调接口.md#ab658d1468ba300f882dfb61e3e73ed1b)
- [uac2_ops::data_recv_cb](../usb/P090_USB音频2回调接口.md#abb973db8018d09ba34f508c4e8aff573)
- [uac2_ops::feedback_cb](../usb/P090_USB音频2回调接口.md#ad427ec3534c8c2b1fe097a7eb83a2e87)
- [uac2_ops::get_sample_rate](../usb/P090_USB音频2回调接口.md#ad8a5599b97edbecc653da41a970f378d)
- [uac2_ops::terminal_update_cb](../usb/P090_USB音频2回调接口.md#ae938633dcf6eb6f120ca458bf8a2142f)

---

[上一章](P896_usbd_msg.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P898_usbd_uvc.h_源码浏览.md)
