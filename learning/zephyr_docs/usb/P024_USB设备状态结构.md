---
id: learning.zephyr-docs.usb.api-24
title: USB设备状态结构
kind: reference
status: maintained
domains: [zephyr, usb, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structusbd__status.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第24章\_USB设备状态结构

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structusbd__status.html)。读取日期：2026-10-14；基线为保存的 `latest` 页面，HTML 摘要见[来源记录](../SOURCES.md)。

## 24.1\_阅读说明与来源

译注：本页是[USB设备核心API](P015_USB设备核心API.md)的数据结构参考，说明描述符、配置、上下文与类实例的成员。字段声明和原注释按官方页面保留；内部类型或回调约定的补充明确标为源码译注。

[本册大纲](大纲.md)提供本组第18至28章的全部字段参考。

USB 设备支持状态。

```c
#include <zephyr/usb/usbd.h>
```

USB 设备支持状态。

## 24.2\_数据成员（Data Fields）

<a id="r_a78de12245d08ecc71e09d5519fe0e857"></a>

```c
unsigned int initialized: 1
```

USB 设备支持已初始化。

相关声明：[unsigned](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a4089fb16419d359081465355db05f846)、[initialized](P024_USB设备状态结构.md#a78de12245d08ecc71e09d5519fe0e857)。

<a id="r_a2382fcb655fe51e0bcf83f85aa182ba3"></a>

```c
unsigned int enabled: 1
```

USB 设备支持已启用。

相关声明：[unsigned](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a4089fb16419d359081465355db05f846)、[enabled](P024_USB设备状态结构.md#a2382fcb655fe51e0bcf83f85aa182ba3)。

<a id="r_afb67cfda187e40229f842c93aa09f0ba"></a>

```c
unsigned int suspended: 1
```

USB 设备已挂起（Suspended）。

相关声明：[unsigned](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a4089fb16419d359081465355db05f846)、[suspended](P024_USB设备状态结构.md#afb67cfda187e40229f842c93aa09f0ba)。

<a id="r_a113085892967cf7c9cb70131b320d61a"></a>

```c
unsigned int rwup: 1
```

USB 远程唤醒（Remote Wake-up）功能已启用。

相关声明：[unsigned](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a4089fb16419d359081465355db05f846)、[rwup](P024_USB设备状态结构.md#a113085892967cf7c9cb70131b320d61a)。

<a id="r_ae4107cb4f379cce8c0472a98483705b8"></a>

```c
unsigned int self_powered: 1
```

USB 设备采用自供电（Self-powered）。

相关声明：[unsigned](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a4089fb16419d359081465355db05f846)、[self_powered](P024_USB设备状态结构.md#ae4107cb4f379cce8c0472a98483705b8)。

<a id="r_a295009d25826732ba9eebd7735d93d23"></a>

```c
enum usbd_speed speed: 2
```

USB 设备速率。

相关声明：[usbd_speed](P015_USB设备核心API.md#ga2f2da3d634530f08cd59d408c811ad71)、[speed](P024_USB设备状态结构.md#a295009d25826732ba9eebd7735d93d23)。

## 24.3\_详细说明（Detailed Documentation）

<a id="a2382fcb655fe51e0bcf83f85aa182ba3"></a>

### `enabled`

```c
unsigned int usbd_status::enabled
```

USB 设备支持已启用。

<a id="a78de12245d08ecc71e09d5519fe0e857"></a>

### `initialized`

```c
unsigned int usbd_status::initialized
```

USB 设备支持已初始化。

> 译注（源码核对）：initialized 与 enabled 是独立状态：初始化不等于已对外启用，停用也不自动撤销初始化。生命周期和注册条件见核心API中的 usbd_init()、usbd_disable()、usbd_shutdown()。当前头文件中这些布尔状态各为1位位域，speed 为2位位域。

<a id="a113085892967cf7c9cb70131b320d61a"></a>

### `rwup`

```c
unsigned int usbd_status::rwup
```

USB 远程唤醒（Remote Wake-up）功能已启用。

<a id="ae4107cb4f379cce8c0472a98483705b8"></a>

### `self_powered`

```c
unsigned int usbd_status::self_powered
```

USB 设备采用自供电（Self-powered）。

<a id="a295009d25826732ba9eebd7735d93d23"></a>

### `speed`

```c
enum usbd_speed usbd_status::speed
```

USB 设备速率。

<a id="afb67cfda187e40229f842c93aa09f0ba"></a>

### `suspended`

```c
unsigned int usbd_status::suspended
```

USB 设备已挂起（Suspended）。

## 24.4\_相关源码与使用边界

本页结构定义来自 `zephyr/usb/usbd.h`；本仓库的[对应头文件](../../../include/zephyr/usb/usbd.h)、[类回调包装接口](../../../subsys/usb/device_next/usbd_class_api.h)、[第9章控制请求处理](../../../subsys/usb/device_next/usbd_ch9.c)及[初始化实现](../../../subsys/usb/device_next/usbd_init.c)可用于源码跟踪，版本可能与官网 latest 不同。译注依据保存的[官方头文件](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/include/zephyr/usb/usbd.h)、[回调接口](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/device_next/usbd_class_api.h)、[控制请求实现](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/device_next/usbd_ch9.c)、[描述符管理](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/device_next/usbd_desc.c)和[初始化实现](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/device_next/usbd_init.c)，摘要见[来源记录](../SOURCES.md)。本批没有编译、运行或操作USB设备。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>
<a id="details"></a>
<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

[上一章](P023_USB第9章运行时数据.md) · [返回大纲](大纲.md) · [下一章](P025_USB设备上下文结构.md)
