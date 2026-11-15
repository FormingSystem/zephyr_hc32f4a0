---
id: learning.zephyr-docs.usb.api-38
title: USB设备控制器事件结构
kind: reference
status: maintained
domains: [zephyr, usb, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structudc__event.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第38章\_USB设备控制器事件结构

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structudc__event.html)。读取日期：2026-10-14；基线为保存的 `latest` 页面，HTML 摘要见[来源记录](../SOURCES.md)。

## 38.1\_阅读说明与来源

译注：本页属于[USB设备控制器API说明](P029_USB设备控制器API说明.md)的底层接口参考，供理解控制器驱动、端点管理和请求生命周期。声明和原注释按官方页面保留，补充解释明确标为源码译注。

[本册大纲](大纲.md)提供本组第29至39章的全部字段参考。

USB 设备控制器事件。

```c
#include <zephyr/drivers/usb/udc.h>
```

USB 设备控制器事件。

这是所有 UDC 驱动事件共用的结构。事件通过消息队列及上层在控制器初始化（udc_init）时提供的回调（udc_event_cb_t）传递给上层。

## 38.2\_数据成员（Data Fields）

<a id="r_a3acfe5d21d16f6edfa24e9964b636434"></a>

```c
enum udc_event_type type
```

事件类型。

相关声明：[udc_event_type](https://docs.zephyrproject.org/latest/doxygen/html/udc_8h.html#a03749f5acb64ff8cfddc3c0b6b81a040)、[type](P038_USB设备控制器事件结构.md#a3acfe5d21d16f6edfa24e9964b636434)。

```c
union {
```



<a id="r_a4528eb5ea96a1364c99c4433064ffdf9"></a>

```c
uint32_t value
```

事件值。

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[value](P038_USB设备控制器事件结构.md#ada24e0e920c39bc60a6c7fbbe54277f4)。

<a id="r_a01d34ccd58fc0a19a9c557f1a3bc6d19"></a>

```c
int status
```

事件状态值，如果存在。

相关声明：[status](P038_USB设备控制器事件结构.md#a0707d65716a4b1e6dd3132a0bb370770)。

<a id="r_a8d149ed523ded9d7731e1ee85734a31c"></a>

```c
struct net_buf * buf
```

指向请求的指针，仅用于 UDC_EVT_EP_REQUEST。

相关声明：[net_buf](https://docs.zephyrproject.org/latest/doxygen/html/structnet__buf.html)、[buf](P038_USB设备控制器事件结构.md#ac1ff3bc9d629eb9b6c55602e7861e945)。

<a id="r_afbb3dd119205d7f7aa5ef7f473746060"></a>

```c
};
```



<a id="r_a900404c46850d34cd7121eeedc2fce9d"></a>

```c
const struct device * dev
```

指向设备结构体的指针。

相关声明：[device](../device_reference/P002_设备对象结构.md)、[dev](P038_USB设备控制器事件结构.md#a900404c46850d34cd7121eeedc2fce9d)。

## 38.3\_详细说明（Detailed Documentation）

<a id="afbb3dd119205d7f7aa5ef7f473746060"></a>

### `[union]`

```c
union { ... } udc_event
```

> 译注（源码核对）：value、status 与 buf 位于同一匿名联合体，共用存储空间，须根据 type 选择有效成员。UDC_EVT_EP_REQUEST 使用 buf。

<a id="ac1ff3bc9d629eb9b6c55602e7861e945"></a>

### `buf`

```c
struct net_buf* udc_event::buf
```

指向请求的指针，仅用于 UDC_EVT_EP_REQUEST。

> 译注（源码核对）：当前公共提交函数在栈上构造 udc_event 并立即调用上层回调，因此回调要保存事件时应复制结构内容，不能长期保存事件指针。复制事件只复制 buf 指针，不会自动复制或增加请求缓冲区的引用。

<a id="a900404c46850d34cd7121eeedc2fce9d"></a>

### `dev`

```c
const struct device* udc_event::dev
```

指向设备结构体的指针。

<a id="a0707d65716a4b1e6dd3132a0bb370770"></a>

### `status`

```c
int udc_event::status
```

事件状态值，如果存在。

<a id="a3acfe5d21d16f6edfa24e9964b636434"></a>

### `type`

```c
enum udc_event_type udc_event::type
```

事件类型。

<a id="ada24e0e920c39bc60a6c7fbbe54277f4"></a>

### `value`

```c
uint32_t udc_event::value
```

事件值。

## 38.4\_相关源码与使用边界

控制器接口与结构定义来自 `zephyr/drivers/usb/udc.h`，缓冲区宏来自 `zephyr/drivers/usb/usb_buf.h`。本仓库的[对应头文件](../../../include/zephyr/drivers/usb/udc.h)、[公共实现](../../../drivers/usb/udc/udc_common.c)、[内部辅助接口](../../../drivers/usb/udc/udc_common.h)和[驱动骨架](../../../drivers/usb/udc/udc_skeleton.c)可用于源码跟踪；版本可能与官方 latest 不同。译注依据保存的[官方头文件](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/include/zephyr/drivers/usb/udc.h)、[公共实现](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/drivers/usb/udc/udc_common.c)、[内部接口](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/drivers/usb/udc/udc_common.h)及[骨架实现](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/drivers/usb/udc/udc_skeleton.c)，摘要见[来源记录](../SOURCES.md)。本批没有编译、运行或操作USB设备。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>
<a id="details"></a>
<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

[上一章](P037_USB设备控制器端点状态.md) · [返回大纲](大纲.md) · [下一章](P039_USB缓冲区宏与定义.md)
