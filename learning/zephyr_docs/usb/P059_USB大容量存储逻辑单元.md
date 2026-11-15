---
id: learning.zephyr-docs.usb.api-59
title: USB大容量存储逻辑单元
kind: reference
status: maintained
domains: [zephyr, usb, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structusbd__msc__lun.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第59章\_USB大容量存储逻辑单元

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structusbd__msc__lun.html)。读取日期：2026-10-14；基线为保存的 `latest` 页面，HTML 摘要见[来源记录](../SOURCES.md)。

## 59.1\_阅读说明与来源

译注：本页说明USB大容量存储（MSC）或设备固件升级（DFU）的公开声明。官方只列声明的字段保持完整，源码补充明确标为译注；[本册大纲](大纲.md)列出对应说明、接口和示例。

```c
#include <zephyr/usb/class/usbd_msc.h>
```

## 59.2\_数据成员（Data Fields）

<a id="r_a20c6b15b6ac9c09e1aa4369dd477ebba"></a>

```c
const char * disk
```



相关声明：[disk](P059_USB大容量存储逻辑单元.md#a20c6b15b6ac9c09e1aa4369dd477ebba)。

<a id="r_a13325438f09bff0d3070e5614b736bed"></a>

```c
const char * vendor
```



相关声明：[vendor](P059_USB大容量存储逻辑单元.md#a13325438f09bff0d3070e5614b736bed)。

<a id="r_a9cb7ba0f92f36944585eac23ed283ab6"></a>

```c
const char * product
```



相关声明：[product](P059_USB大容量存储逻辑单元.md#a9cb7ba0f92f36944585eac23ed283ab6)。

<a id="r_a94eb2dc151b476e733aea388255e198d"></a>

```c
const char * revision
```



相关声明：[revision](P059_USB大容量存储逻辑单元.md#a94eb2dc151b476e733aea388255e198d)。

## 59.3\_详细说明（Detailed Documentation）

<a id="a20c6b15b6ac9c09e1aa4369dd477ebba"></a>

### 59.3.1\_`disk`

```c
const char* usbd_msc_lun::disk
```

> 译注（源码核对）：磁盘访问接口的名称，与USB显示的产品字符串不同。字段含义由usbd_msc.h及类初始化时传给scsi_init()的参数核对；官方页面只列出了声明。

<a id="a9cb7ba0f92f36944585eac23ed283ab6"></a>

### 59.3.2\_`product`

```c
const char* usbd_msc_lun::product
```

> 译注（源码核对）：作为T10产品识别字符串传给SCSI层，不是USB设备描述符中的16位idProduct。

<a id="a94eb2dc151b476e733aea388255e198d"></a>

### 59.3.3\_`revision`

```c
const char* usbd_msc_lun::revision
```

> 译注（源码核对）：T10产品修订字符串，与固件镜像版本或USB规范版本没有自动对应关系。

<a id="a13325438f09bff0d3070e5614b736bed"></a>

### 59.3.4\_`vendor`

```c
const char* usbd_msc_lun::vendor
```

> 译注（源码核对）：作为T10厂商识别字符串传给SCSI层，不是USB设备描述符中的16位idVendor。

## 59.4\_源码跟踪与使用边界

译注依据保存的[官方头文件](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/include/zephyr/usb/class/usbd_msc.h)和[官方实现](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/device_next/class/usbd_msc.c)，摘要见[来源记录](../SOURCES.md)。可沿本仓库的[头文件](../../../include/zephyr/usb/class/usbd_msc.h)和[类实现](../../../subsys/usb/device_next/class/usbd_msc.c)跟踪符号；仓库源码可能与网页版本不同。本批没有执行固件构建或硬件操作。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

[上一章](P058_USB大容量存储API.md) · [返回大纲](大纲.md) · [下一章](P060_USB大容量存储示例.md)
