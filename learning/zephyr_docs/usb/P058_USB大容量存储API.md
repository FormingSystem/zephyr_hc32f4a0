---
id: learning.zephyr-docs.usb.api-58
title: USB大容量存储API
kind: reference
status: maintained
domains: [zephyr, usb, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__usbd__msc__device.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第58章\_USB大容量存储API

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__usbd__msc__device.html)。读取日期：2026-10-14；基线为保存的 `latest` 页面，HTML 摘要见[来源记录](../SOURCES.md)。

## 58.1\_阅读说明与来源

译注：本页说明USB大容量存储（MSC）或设备固件升级（DFU）的公开声明。官方只列声明的字段保持完整，源码补充明确标为译注；[本册大纲](大纲.md)列出对应说明、接口和示例。

USB大容量存储类（USB Mass Storage Class，MSC）设备API。

USB大容量存储类（USB Mass Storage Class，MSC）设备API。

引入版本（Since）：3.4。

接口版本（Version）：0.2.0。

## 58.2\_宏定义（Macros）

<a id="r_ga7923a2f33e3dd8455f8f47cea08f1752"></a>

```c
#define USBD_DEFINE_MSC_LUN(id, disk_name, t10_vendor, t10_product, t10_revision)
```

定义USB大容量存储类逻辑单元（Logical Unit）。

相关声明：[USBD_DEFINE_MSC_LUN](P058_USB大容量存储API.md#ga7923a2f33e3dd8455f8f47cea08f1752)。

## 58.3\_详细说明（Detailed Documentation）

<a id="ga7923a2f33e3dd8455f8f47cea08f1752"></a>

### 58.3.1\_`USBD\_DEFINE\_MSC\_LUN`

```c
#define USBD_DEFINE_MSC_LUN ( id, disk_name, t10_vendor, t10_product, t10_revision )
```

```c
#include <zephyr/usb/class/usbd_msc.h>
```

**宏展开值（Value）**

```c
static const STRUCT_SECTION_ITERABLE(usbd_msc_lun, usbd_msc_lun_##id) = {       \
        .disk = disk_name,                                                      \
        .vendor = t10_vendor,                                                   \
        .product = t10_product,                                                 \
        .revision = t10_revision,                                               \
}
```

定义USB大容量存储类逻辑单元（Logical Unit）。

使用此宏为选定磁盘创建USB MSC逻辑单元映射。每个USB MSC实例最多可以注册CONFIG_USBD_MSC_LUNS_PER_INSTANCE个磁盘。目前只支持一个USB MSC实例。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `id` | 链接器（Linker）据以对已注册逻辑单元号（Logical Unit Number，LUN）排序的标识符 |
| `disk_name` | 磁盘访问接口（Disk Access Interface）使用的磁盘名称 |
| `t10_vendor` | T10厂商标识（Vendor Identification） |
| `t10_product` | T10产品标识（Product Identification） |
| `t10_revision` | T10产品修订级别（Product Revision Level） |

> 译注（源码核对）：宏在可迭代段（Iterable Section）中定义静态常量映射；它不分配磁盘、不创建文件系统，也不格式化介质。id决定链接器排序，disk_name必须与磁盘访问接口的已注册名称对应。当前类初始化遍历这些映射建立LUN；超过配置上限时记录错误并返回-ENOMEM，类初始化失败。

## 58.4\_源码跟踪与使用边界

译注依据保存的[官方头文件](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/include/zephyr/usb/class/usbd_msc.h)和[官方实现](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/device_next/class/usbd_msc.c)，摘要见[来源记录](../SOURCES.md)。可沿本仓库的[头文件](../../../include/zephyr/usb/class/usbd_msc.h)和[类实现](../../../subsys/usb/device_next/class/usbd_msc.c)跟踪符号；仓库源码可能与网页版本不同。本批没有执行固件构建或硬件操作。

<a id="header-define-members"></a>
<a id="define-members"></a>
<a id="details"></a>
<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="agroup__iterable__section__apis_html_ga9104f42cbe4a67a931bed7f7cc8f600f"></a>
<a id="astructusbd__msc__lun_html"></a>

[上一章](P057_USB大容量存储API说明.md) · [返回大纲](大纲.md) · [下一章](P059_USB大容量存储逻辑单元.md)
