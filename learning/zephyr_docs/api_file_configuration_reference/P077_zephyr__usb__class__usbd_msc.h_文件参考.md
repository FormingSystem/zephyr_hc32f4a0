---
id: learning.zephyr-docs.api-file-configuration-reference.page-77
title: zephyr__usb__class__usbd_msc.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/usbd__msc_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第77章\_zephyr\_\_usb\_\_class\_\_usbd\_msc.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/usbd__msc_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

USB设备（USBD）大容量存储类（Mass Storage Class）的公共头文件。

<a id="details"></a>

```c
#include <zephyr/sys/iterable_sections.h>
```

查看此文件的源码。

USB 设备海量存储类公共头文件（USBD Mass Storage Class Public Header）。本头文件公开用于注册逻辑单元号（Logical Unit Numbers，LUNs）的 API。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 77.1\_数据结构（Data Structures）

<a id="r_usbd_5Fmsc_5Flun"></a>

```c
struct usbd_msc_lun
```

相关声明：[usbd_msc_lun](../usb/P059_USB大容量存储逻辑单元.md)。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 77.2\_宏定义（Macros）

<a id="r_ga7923a2f33e3dd8455f8f47cea08f1752"></a>

```c
#define USBD_DEFINE_MSC_LUN(id, disk_name, t10_vendor, t10_product, t10_revision)
```

相关声明：[USBD_DEFINE_MSC_LUN](../usb/P058_USB大容量存储API.md#ga7923a2f33e3dd8455f8f47cea08f1752)。

定义 USB 海量存储类逻辑单元（USB Mass Storage Class Logical Unit）。


## 77.3\_原页交叉引用（Cross References）

- [zephyr/sys/iterable_sections.h](../iterable_reference/P003_可遍历段辅助头文件源码.md)
- [查看此文件的源码。](../api_source_reference/P895_usbd_msc.h_源码浏览.md)
- [usbd_msc_lun](../usb/P059_USB大容量存储逻辑单元.md)
- [USBD_DEFINE_MSC_LUN](../usb/P058_USB大容量存储API.md#ga7923a2f33e3dd8455f8f47cea08f1752)

<a id="header-details"></a>

---

[上一章](P076_zephyr__drivers__uart_emul.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P078_zephyr__usb__usbd_msg.h_文件参考.md)
