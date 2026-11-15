---
id: learning.zephyr-docs.usb.api-35
title: USB设备控制器端点能力
kind: reference
status: maintained
domains: [zephyr, usb, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structudc__ep__caps.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第35章\_USB设备控制器端点能力

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structudc__ep__caps.html)。读取日期：2026-10-14；基线为保存的 `latest` 页面，HTML 摘要见[来源记录](../SOURCES.md)。

## 35.1\_阅读说明与来源

译注：本页属于[USB设备控制器API说明](P029_USB设备控制器API说明.md)的底层接口参考，供理解控制器驱动、端点管理和请求生命周期。声明和原注释按官方页面保留，补充解释明确标为源码译注。

[本册大纲](大纲.md)提供本组第29至39章的全部字段参考。

USB 设备控制器端点能力。

```c
#include <zephyr/drivers/usb/udc.h>
```

USB 设备控制器端点能力。

## 35.2\_数据成员（Data Fields）

<a id="r_a5e90d1362855dd77a1f7ef9e0cd82ef8"></a>

```c
uint32_t mps: 16
```

端点缓冲区的最大包长。

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[mps](P035_USB设备控制器端点能力.md#a5e90d1362855dd77a1f7ef9e0cd82ef8)。

<a id="r_a98afb85c03ff01ba82d55884cea0ea31"></a>

```c
uint32_t control: 1
```

端点支持控制传输（Control Transfer），为完整性而列出。

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[control](P035_USB设备控制器端点能力.md#a98afb85c03ff01ba82d55884cea0ea31)。

<a id="r_a73f06f9e2af5770cab84d2adb76d42de"></a>

```c
uint32_t interrupt: 1
```

端点支持中断传输（Interrupt Transfer）。

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[interrupt](P035_USB设备控制器端点能力.md#a73f06f9e2af5770cab84d2adb76d42de)。

<a id="r_a73ec7e7c7fd043065a7c59c89c6cc36e"></a>

```c
uint32_t bulk: 1
```

端点支持批量传输（Bulk Transfer）。

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[bulk](P035_USB设备控制器端点能力.md#a73ec7e7c7fd043065a7c59c89c6cc36e)。

<a id="r_a15ce10028e09b3af021a83dc36eba99a"></a>

```c
uint32_t iso: 1
```

端点支持等时传输（Isochronous Transfer，ISO）。

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[iso](P035_USB设备控制器端点能力.md#a15ce10028e09b3af021a83dc36eba99a)。

<a id="r_ad556a4c17a01bb6b8355fb6b5ea9d418"></a>

```c
uint32_t high_bandwidth: 1
```

端点支持高带宽（High-Bandwidth）中断或等时传输。

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[high_bandwidth](P035_USB设备控制器端点能力.md#ad556a4c17a01bb6b8355fb6b5ea9d418)。

<a id="r_a3a944cda429c916b60cff3a332b970a7"></a>

```c
uint32_t in: 1
```

端点支持 IN 传输。

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[in](P035_USB设备控制器端点能力.md#a3a944cda429c916b60cff3a332b970a7)。

<a id="r_afc424ee2bb31c19451facc0b79bb73c7"></a>

```c
uint32_t out: 1
```

端点支持 OUT 传输。

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[out](P035_USB设备控制器端点能力.md#afc424ee2bb31c19451facc0b79bb73c7)。

## 35.3\_详细说明（Detailed Documentation）

<a id="a73ec7e7c7fd043065a7c59c89c6cc36e"></a>

### `bulk`

```c
uint32_t udc_ep_caps::bulk
```

端点支持批量传输（Bulk Transfer）。

<a id="a98afb85c03ff01ba82d55884cea0ea31"></a>

### `control`

```c
uint32_t udc_ep_caps::control
```

端点支持控制传输（Control Transfer），为完整性而列出。

<a id="ad556a4c17a01bb6b8355fb6b5ea9d418"></a>

### `high_bandwidth`

```c
uint32_t udc_ep_caps::high_bandwidth
```

端点支持高带宽（High-Bandwidth）中断或等时传输。

<a id="a3a944cda429c916b60cff3a332b970a7"></a>

### `in`

```c
uint32_t udc_ep_caps::in
```

端点支持 IN 传输。

<a id="a73f06f9e2af5770cab84d2adb76d42de"></a>

### `interrupt`

```c
uint32_t udc_ep_caps::interrupt
```

端点支持中断传输（Interrupt Transfer）。

<a id="a15ce10028e09b3af021a83dc36eba99a"></a>

### `iso`

```c
uint32_t udc_ep_caps::iso
```

端点支持等时传输（Isochronous Transfer，ISO）。

<a id="a5e90d1362855dd77a1f7ef9e0cd82ef8"></a>

### `mps`

```c
uint32_t udc_ep_caps::mps
```

端点缓冲区的最大包长。

> 译注（源码核对）：当前头文件中 mps 是16位位域，其余能力开关各为1位。能力记录支持上限；端点当前采用的 mps 位于 udc_ep_config 中，二者不可混作同一状态。

<a id="afc424ee2bb31c19451facc0b79bb73c7"></a>

### `out`

```c
uint32_t udc_ep_caps::out
```

端点支持 OUT 传输。

## 35.4\_相关源码与使用边界

控制器接口与结构定义来自 `zephyr/drivers/usb/udc.h`，缓冲区宏来自 `zephyr/drivers/usb/usb_buf.h`。本仓库的[对应头文件](../../../include/zephyr/drivers/usb/udc.h)、[公共实现](../../../drivers/usb/udc/udc_common.c)、[内部辅助接口](../../../drivers/usb/udc/udc_common.h)和[驱动骨架](../../../drivers/usb/udc/udc_skeleton.c)可用于源码跟踪；版本可能与官方 latest 不同。译注依据保存的[官方头文件](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/include/zephyr/drivers/usb/udc.h)、[公共实现](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/drivers/usb/udc/udc_common.c)、[内部接口](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/drivers/usb/udc/udc_common.h)及[骨架实现](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/drivers/usb/udc/udc_skeleton.c)，摘要见[来源记录](../SOURCES.md)。本批没有编译、运行或操作USB设备。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>
<a id="details"></a>
<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

[上一章](P034_USB设备控制器设备能力.md) · [返回大纲](大纲.md) · [下一章](P036_USB设备控制器端点配置.md)
