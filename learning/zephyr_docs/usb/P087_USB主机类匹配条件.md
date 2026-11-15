---
id: learning.zephyr-docs.usb.api-87
title: USB主机类匹配条件
kind: reference
status: maintained
domains: [zephyr, usb, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structusbh__class__filter.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第87章\_USB主机类匹配条件

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structusbh__class__filter.html)。读取日期：2026-10-14；基线为保存的 `latest` 页面，HTML 摘要见[来源记录](../SOURCES.md)。

## 87.1\_阅读说明与来源

译注：本页说明USB主机栈（USB Host Stack）的接口与数据对象。官方只列声明的字段保持完整，源码补充明确标为译注；[本册大纲](大纲.md)列出对应说明、接口和示例。

与匹配特定类有关的设备信息。

```c
#include <zephyr/usb/usbh.h>
```

与匹配特定类有关的设备信息。

## 87.2\_数据成员（Data Fields）

<a id="r_aad46cc5db6098c402098e4c2d0503f88"></a>

```c
uint16_t vid
```

厂商ID（Vendor ID，VID）。

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[vid](P087_USB主机类匹配条件.md#aad46cc5db6098c402098e4c2d0503f88)。

<a id="r_a07dbc7ed52af241a25bcb481438c3f2f"></a>

```c
uint16_t pid
```

产品ID（Product ID，PID）。

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[pid](P087_USB主机类匹配条件.md#a07dbc7ed52af241a25bcb481438c3f2f)。

<a id="r_a9e25adaebddae32c54905f1cb616ed7e"></a>

```c
uint8_t class
```

类代码（Class Code）。

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[class](P087_USB主机类匹配条件.md#a9e25adaebddae32c54905f1cb616ed7e)。

<a id="r_aa2b4eafefe108ecb978c21d00ad0561c"></a>

```c
uint8_t sub
```

子类代码（Subclass Code）。

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[sub](P087_USB主机类匹配条件.md#aa2b4eafefe108ecb978c21d00ad0561c)。

<a id="r_adeede762ef1ff70888f794b688de01c2"></a>

```c
uint8_t proto
```

协议代码（Protocol Code）。

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[proto](P087_USB主机类匹配条件.md#adeede762ef1ff70888f794b688de01c2)。

<a id="r_a202e2f9e25b49c790f979654575452ee"></a>

```c
uint8_t flags
```

指定参与匹配字段的标志（Flags）。

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[flags](P087_USB主机类匹配条件.md#a202e2f9e25b49c790f979654575452ee)。

## 87.3\_详细说明（Detailed Documentation）

<a id="a9e25adaebddae32c54905f1cb616ed7e"></a>

### 87.3.1\_`class`

```c
uint8_t usbh_class_filter::class
```

类代码（Class Code）。

> 译注（源码核对）：设备级匹配取bDeviceClass；功能级匹配取IAD的bFunctionClass或接口的bInterfaceClass。三种来源的语义相关但字段位置不同。

<a id="a202e2f9e25b49c790f979654575452ee"></a>

### 87.3.2\_`flags`

```c
uint8_t usbh_class_filter::flags
```

指定参与匹配字段的标志（Flags）。

> 译注（源码核对）：当前内部规则提供USBH_CLASS_MATCH_VID_PID（BIT(1)）和USBH_CLASS_MATCH_CODE_TRIPLE（BIT(2)）。前者同时比较VID和PID，后者同时比较类／子类／协议；同一条规则的已选条件都须满足，数组中任意一条完整匹配即可。flags=0是终止项，首项即0的非NULL数组不匹配任何对象。

<a id="a07dbc7ed52af241a25bcb481438c3f2f"></a>

### 87.3.3\_`pid`

```c
uint16_t usbh_class_filter::pid
```

产品ID（Product ID，PID）。

> 译注（源码核对）：来自设备描述符idProduct，须与同一条规则的VID一起解释，不是接口号。

<a id="adeede762ef1ff70888f794b688de01c2"></a>

### 87.3.4\_`proto`

```c
uint8_t usbh_class_filter::proto
```

协议代码（Protocol Code）。

<a id="aa2b4eafefe108ecb978c21d00ad0561c"></a>

### 87.3.5\_`sub`

```c
uint8_t usbh_class_filter::sub
```

子类代码（Subclass Code）。

<a id="aad46cc5db6098c402098e4c2d0503f88"></a>

### 87.3.6\_`vid`

```c
uint16_t usbh_class_filter::vid
```

厂商ID（Vendor ID，VID）。

> 译注（源码核对）：来自设备描述符idVendor。当前规则没有单独只比较VID的标志，VID/PID作为一组比较。

## 87.4\_源码跟踪与使用边界

译注依据保存的[官方主机头文件](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/include/zephyr/usb/usbh.h)、[UHC头文件](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/include/zephyr/drivers/usb/uhc.h)、[生命周期实现](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/host/usbh_api.c)、[类匹配实现](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/host/usbh_class.c)、[类回调包装](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/host/usbh_class_api.h)、[设备管理](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/host/usbh_device.c)及[事件处理](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/host/usbh_core.c)，摘要见[来源记录](../SOURCES.md)。本仓库的[主机头文件](../../../include/zephyr/usb/usbh.h)、[UHC头文件](../../../include/zephyr/drivers/usb/uhc.h)与[主机栈目录](../../../subsys/usb/host)可用于源码跟踪，版本可能与网页不同。本批未构建、运行或操作USB硬件。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>
<a id="details"></a>
<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

[上一章](P086_USB主机类驱动数据.md) · [返回大纲](大纲.md) · [下一章](P088_USB音频2设备API说明.md)
