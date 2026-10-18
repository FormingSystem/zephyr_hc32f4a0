---
id: learning.zephyr-docs.api-file-service-reference.page-59
title: zephyr__usb__class__usbd_uac2.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/usbd__uac2_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第59章\_zephyr\_\_usb\_\_class\_\_usbd\_uac2.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/usbd__uac2_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

USB音频类2（Audio Class 2）设备的公共头文件。

<a id="details"></a>

```c
#include <zephyr/device.h>
```

查看此文件的源码。

USB 音频类 2 设备公共头文件（USB Audio Class 2 Device Public Header）。本头文件仅描述类 API（Class API）与应用程序的交互。音频设备本身通过设备树 `zephyr,uac2` 兼容项（Compatible）建模。当前此 API 被视为实验性接口（Experimental API）。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 59.1\_数据结构（Data Structures）

<a id="r_uac2_5Fops"></a>

```c
struct uac2_ops
```

相关声明：[uac2_ops](../usb/P090_USB音频2回调接口.md)。

USB Audio 2的应用事件处理程序（Application Event Handlers）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 59.2\_宏定义（Macros）

<a id="r_gaa35265e83d894896806fcca28feb84a3"></a>

```c
#define UAC2_ENTITY_ID(node)
```

相关声明：[UAC2_ENTITY_ID](../usb/P089_USB音频2设备API.md#gaa35265e83d894896806fcca28feb84a3)。

获取实体标识（Entity ID）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 59.3\_函数（Functions）

<a id="r_ga802a727c1a201c26a3bd74f0e7f0900c"></a>

```c
void usbd_uac2_set_ops (const struct device *dev, const struct uac2_ops *ops, void *user_data)
```

相关声明：[usbd_uac2_set_ops](../usb/P089_USB音频2设备API.md#ga802a727c1a201c26a3bd74f0e7f0900c)、[device](../device_reference/P002_设备对象结构.md)、[uac2_ops](../usb/P090_USB音频2回调接口.md)。

注册 USB Audio 2 应用程序回调（Application Callbacks）。

<a id="r_gae899d75d786f5b1df86db48de88d1254"></a>

```c
int usbd_uac2_send (const struct device *dev, uint8_t terminal, void *data, uint16_t size)
```

相关声明：[usbd_uac2_send](../usb/P089_USB音频2设备API.md#gae899d75d786f5b1df86db48de88d1254)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

向输出终端（Output Terminal）发送音频数据（Audio Data）。


## 59.4\_原页交叉引用（Cross References）

- [zephyr/device.h](../device_reference/P008_设备模型头文件源码.md)
- [查看此文件的源码。](../api_source_reference/P897_usbd_uac2.h_源码浏览.md)
- [uac2_ops](../usb/P090_USB音频2回调接口.md)
- [UAC2_ENTITY_ID](../usb/P089_USB音频2设备API.md#gaa35265e83d894896806fcca28feb84a3)
- [usbd_uac2_set_ops](../usb/P089_USB音频2设备API.md#ga802a727c1a201c26a3bd74f0e7f0900c)
- [device](../device_reference/P002_设备对象结构.md)
- [usbd_uac2_send](../usb/P089_USB音频2设备API.md#gae899d75d786f5b1df86db48de88d1254)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)

<a id="header-details"></a>

---

[上一章](P058_zephyr__modem__ubx.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P060_zephyr__drivers__sensor__w1_sensor.h_文件参考.md)
