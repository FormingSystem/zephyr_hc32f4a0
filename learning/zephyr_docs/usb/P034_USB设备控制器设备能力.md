---
id: learning.zephyr-docs.usb.api-34
title: USB设备控制器设备能力
kind: reference
status: maintained
domains: [zephyr, usb, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structudc__device__caps.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第34章\_USB设备控制器设备能力

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structudc__device__caps.html)。读取日期：2026-10-14；基线为保存的 `latest` 页面，HTML 摘要见[来源记录](../SOURCES.md)。

## 34.1\_阅读说明与来源

译注：本页属于[USB设备控制器API说明](P029_USB设备控制器API说明.md)的底层接口参考，供理解控制器驱动、端点管理和请求生命周期。声明和原注释按官方页面保留，补充解释明确标为源码译注。

[本册大纲](大纲.md)提供本组第29至39章的全部字段参考。

USB 设备控制器能力。

```c
#include <zephyr/drivers/usb/udc.h>
```

USB 设备控制器能力。

此结构主要面向 USB 设备栈。

## 34.2\_数据成员（Data Fields）

<a id="r_aea376ff4a0c5a27c3b8f7d4416e17b5b"></a>

```c
uint32_t hs: 1
```

控制器具备 USB 高速能力。

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[hs](P034_USB设备控制器设备能力.md#aea376ff4a0c5a27c3b8f7d4416e17b5b)。

<a id="r_aab85e74e40876040c3d2f961c36b9780"></a>

```c
uint32_t rwup: 1
```

控制器支持 USB 远程唤醒（Remote Wakeup）。

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[rwup](P034_USB设备控制器设备能力.md#aab85e74e40876040c3d2f961c36b9780)。

<a id="r_a0adada5003bccfbd6df8329198639dc0"></a>

```c
uint32_t out_ack: 1
```

控制器在 Data IN 之后自动执行 Status OUT 阶段。

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[out_ack](P034_USB设备控制器设备能力.md#a0adada5003bccfbd6df8329198639dc0)。

<a id="r_aefef262532e3eab3baa90eb8e79f9dc8"></a>

```c
uint32_t addr_before_status: 1
```

控制器要求在状态阶段之前设置设备地址。

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[addr_before_status](P034_USB设备控制器设备能力.md#aefef262532e3eab3baa90eb8e79f9dc8)。

<a id="r_a7aaf6ecac2904acb5560f2f90cfef8d1"></a>

```c
uint32_t can_detect_vbus: 1
```

控制器能检测 USB 供电 VBUS 的状态变化。

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[can_detect_vbus](P034_USB设备控制器设备能力.md#a7aaf6ecac2904acb5560f2f90cfef8d1)。

<a id="r_a63affa3fe08cbaec8351297ad9d26911"></a>

```c
enum udc_mps0 mps0: 2
```

控制端点的最大包长。

相关声明：[udc_mps0](https://docs.zephyrproject.org/latest/doxygen/html/udc_8h.html#ac254f8a970f890d14e35c43474c915fd)、[mps0](P034_USB设备控制器设备能力.md#a63affa3fe08cbaec8351297ad9d26911)。

## 34.3\_详细说明（Detailed Documentation）

<a id="aefef262532e3eab3baa90eb8e79f9dc8"></a>

### `addr_before_status`

```c
uint32_t udc_device_caps::addr_before_status
```

控制器要求在状态阶段之前设置设备地址。

<a id="a7aaf6ecac2904acb5560f2f90cfef8d1"></a>

### `can_detect_vbus`

```c
uint32_t udc_device_caps::can_detect_vbus
```

控制器能检测 USB 供电 VBUS 的状态变化。

<a id="aea376ff4a0c5a27c3b8f7d4416e17b5b"></a>

### `hs`

```c
uint32_t udc_device_caps::hs
```

控制器具备 USB 高速能力。

<a id="a63affa3fe08cbaec8351297ad9d26911"></a>

### `mps0`

```c
enum udc_mps0 udc_device_caps::mps0
```

控制端点的最大包长。

> 译注（源码核对）：该字段是2位枚举位域，存储 UDC_MPS0_8、UDC_MPS0_16、UDC_MPS0_32 或 UDC_MPS0_64；枚举值并不直接等于8、16、32、64这些字节数。其他能力开关各为1位位域。

<a id="a0adada5003bccfbd6df8329198639dc0"></a>

### `out_ack`

```c
uint32_t udc_device_caps::out_ack
```

控制器在 Data IN 之后自动执行 Status OUT 阶段。

设置此标志后，USB 栈不会将 Status OUT 缓冲区加入队列。

<a id="aab85e74e40876040c3d2f961c36b9780"></a>

### `rwup`

```c
uint32_t udc_device_caps::rwup
```

控制器支持 USB 远程唤醒（Remote Wakeup）。

## 34.4\_相关源码与使用边界

控制器接口与结构定义来自 `zephyr/drivers/usb/udc.h`，缓冲区宏来自 `zephyr/drivers/usb/usb_buf.h`。本仓库的[对应头文件](../../../include/zephyr/drivers/usb/udc.h)、[公共实现](../../../drivers/usb/udc/udc_common.c)、[内部辅助接口](../../../drivers/usb/udc/udc_common.h)和[驱动骨架](../../../drivers/usb/udc/udc_skeleton.c)可用于源码跟踪；版本可能与官方 latest 不同。译注依据保存的[官方头文件](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/include/zephyr/drivers/usb/udc.h)、[公共实现](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/drivers/usb/udc/udc_common.c)、[内部接口](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/drivers/usb/udc/udc_common.h)及[骨架实现](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/drivers/usb/udc/udc_skeleton.c)，摘要见[来源记录](../SOURCES.md)。本批没有编译、运行或操作USB设备。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>
<a id="details"></a>
<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

[上一章](P033_USB设备控制器驱动数据.md) · [返回大纲](大纲.md) · [下一章](P035_USB设备控制器端点能力.md)
