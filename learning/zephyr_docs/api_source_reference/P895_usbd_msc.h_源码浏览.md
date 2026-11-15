---
id: learning.zephyr-docs.api-source-reference.page-895
title: usbd_msc.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/usbd__msc_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第895章\_usbd\_msc.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/usbd__msc_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/usbd__msc_8h.html)。

## 895.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00018"></a>
<a id="foldopen00019"></a>
<a id="l00019"></a>
<a id="l00020"></a>
<a id="l00021"></a>
<a id="l00022"></a>
<a id="l00023"></a>
<a id="l00024"></a>
<a id="l00025"></a>
<a id="l00034"></a>
<a id="foldopen00048"></a>
<a id="l00048"></a>
<a id="l00049"></a>
<a id="l00050"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="l00054"></a>
<a id="l00055"></a>
<a id="l00059"></a>
<a id="l00060"></a>
<a id="astructusbd__msc__lun_html"></a>
<a id="astructusbd__msc__lun_html_a13325438f09bff0d3070e5614b736bed"></a>
<a id="astructusbd__msc__lun_html_a20c6b15b6ac9c09e1aa4369dd477ebba"></a>
<a id="astructusbd__msc__lun_html_a94eb2dc151b476e733aea388255e198d"></a>
<a id="astructusbd__msc__lun_html_a9cb7ba0f92f36944585eac23ed283ab6"></a>
<a id="asys_2iterable__sections_8h_html"></a>

```c
/*
 * Copyright (c) 2023 Nordic Semiconductor ASA
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#include <zephyr/sys/iterable_sections.h>

#ifndef ZEPHYR_INCLUDE_USB_CLASS_USBD_MSC_H_
#define ZEPHYR_INCLUDE_USB_CLASS_USBD_MSC_H_

struct usbd_msc_lun {
        const char *disk;
        const char *vendor;
        const char *product;
        const char *revision;
};


#define USBD_DEFINE_MSC_LUN(id, disk_name, t10_vendor, t10_product, t10_revision)       \
        static const STRUCT_SECTION_ITERABLE(usbd_msc_lun, usbd_msc_lun_##id) = {       \
                .disk = disk_name,                                                      \
                .vendor = t10_vendor,                                                   \
                .product = t10_product,                                                 \
                .revision = t10_revision,                                               \
        }


#endif /* ZEPHYR_INCLUDE_USB_CLASS_USBD_MSC_H_ */
```

## 895.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2023 Nordic Semiconductor ASA。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 60 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_USB_CLASS_USBD_MSC_H_`。

## 895.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/usbd__msc_8h.html)
- [zephyr/sys/iterable_sections.h](../iterable_reference/P002_可遍历段辅助头文件参考.md)
- [usbd_msc_lun](../usb/P059_USB大容量存储逻辑单元.md)
- [disk](../usb/P059_USB大容量存储逻辑单元.md#a20c6b15b6ac9c09e1aa4369dd477ebba)
- [vendor](../usb/P059_USB大容量存储逻辑单元.md#a13325438f09bff0d3070e5614b736bed)
- [product](../usb/P059_USB大容量存储逻辑单元.md#a9cb7ba0f92f36944585eac23ed283ab6)
- [revision](../usb/P059_USB大容量存储逻辑单元.md#a94eb2dc151b476e733aea388255e198d)
- [usbd_msc_lun::vendor](../usb/P059_USB大容量存储逻辑单元.md#a13325438f09bff0d3070e5614b736bed)
- [usbd_msc_lun::disk](../usb/P059_USB大容量存储逻辑单元.md#a20c6b15b6ac9c09e1aa4369dd477ebba)
- [usbd_msc_lun::revision](../usb/P059_USB大容量存储逻辑单元.md#a94eb2dc151b476e733aea388255e198d)
- [usbd_msc_lun::product](../usb/P059_USB大容量存储逻辑单元.md#a9cb7ba0f92f36944585eac23ed283ab6)
- [iterable_sections.h](../iterable_reference/P002_可遍历段辅助头文件参考.md)

---

[上一章](P894_usbd_midi2.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P896_usbd_msg.h_源码浏览.md)
