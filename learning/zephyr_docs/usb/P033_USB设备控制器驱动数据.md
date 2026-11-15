---
id: learning.zephyr-docs.usb.api-33
title: USB设备控制器驱动数据
kind: reference
status: maintained
domains: [zephyr, usb, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structudc__data.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第33章\_USB设备控制器驱动数据

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structudc__data.html)。读取日期：2026-10-14；基线为保存的 `latest` 页面，HTML 摘要见[来源记录](../SOURCES.md)。

## 33.1\_阅读说明与来源

译注：本页属于[USB设备控制器API说明](P029_USB设备控制器API说明.md)的底层接口参考，供理解控制器驱动、端点管理和请求生命周期。声明和原注释按官方页面保留，补充解释明确标为源码译注。

[本册大纲](大纲.md)提供本组第29至39章的全部字段参考。

公共 UDC 驱动数据结构。

```c
#include <zephyr/drivers/usb/udc.h>
```

公共 UDC 驱动数据结构。

每个 UDC 控制器驱动都必须具备此结构，应作为设备的私有数据（device->data）实现。

## 33.2\_数据成员（Data Fields）

<a id="r_acc471b34bb24453377b1ae54d33fa415"></a>

```c
struct udc_ep_config * ep_lut [32]
```

用于端点管理的查找表（Lookup Table，LUT）。

相关声明：[udc_ep_config](P036_USB设备控制器端点配置.md)、[ep_lut](P033_USB设备控制器驱动数据.md#acc471b34bb24453377b1ae54d33fa415)。

<a id="r_aae68bfba2e92894851c36dd40c33c0f0"></a>

```c
struct udc_device_caps caps
```

控制器能力。

相关声明：[udc_device_caps](P034_USB设备控制器设备能力.md)、[caps](P033_USB设备控制器驱动数据.md#aae68bfba2e92894851c36dd40c33c0f0)。

<a id="r_a1ba1b93af26bca4f4554a43a65ab3c2a"></a>

```c
struct k_mutex mutex
```

驱动访问互斥量（Mutex）。

相关声明：[k_mutex](../synchronization_reference/P007_内核互斥量结构.md)、[mutex](P033_USB设备控制器驱动数据.md#a1ba1b93af26bca4f4554a43a65ab3c2a)。

<a id="r_a9bb216d0c87b9ff4e2e99f0c3cfbb381"></a>

```c
udc_event_cb_t event_cb
```

向上层提交 UDC 事件的回调。

相关声明：[udc_event_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/udc_8h.html#aa3ff247fd5234f65d91f84ebc38e384a)、[event_cb](P033_USB设备控制器驱动数据.md#a9bb216d0c87b9ff4e2e99f0c3cfbb381)。

<a id="r_aaf98e53580a27635a7b02acbcf29ae14"></a>

```c
const void * event_ctx
```

用于保存上层上下文的不透明指针。

相关声明：[event_ctx](P033_USB设备控制器驱动数据.md#aaf98e53580a27635a7b02acbcf29ae14)。

<a id="r_a9c1ae6e5e204b5a0ed15e92f8b3b384f"></a>

```c
atomic_t status
```

USB 设备控制器状态。

相关声明：[atomic_t](../atomic_reference/P001_原子操作公共接口.md#ga124f07c3a788e53c3a40e4e1c06d8af8)、[status](P033_USB设备控制器驱动数据.md#a9c1ae6e5e204b5a0ed15e92f8b3b384f)。

<a id="r_ac58682fa2f37bf2034a69cc9b6b10dfb"></a>

```c
void * priv
```

驱动私有数据。

相关声明：[priv](P033_USB设备控制器驱动数据.md#ac58682fa2f37bf2034a69cc9b6b10dfb)。

<a id="r_ae301e1a80165ae90d7d09dbb6463c88c"></a>

```c
uint8_t setup [8]
```

最近缓存的设置数据，不一定是最近接收的设置数据。

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[setup](P033_USB设备控制器驱动数据.md#ae301e1a80165ae90d7d09dbb6463c88c)。

<a id="r_a849581d1e3692c6c585e9fb24e9bbb4f"></a>

```c
bool setup_pending
```

缓存的设置数据正在等待 USB 栈处理。

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[setup_pending](P033_USB设备控制器驱动数据.md#a849581d1e3692c6c585e9fb24e9bbb4f)。

<a id="r_a2222bd71ecbb8051dfab7b6134f9a2c9"></a>

```c
bool setup_valid
```

最近缓存的设置数据有效，即长度为 8 字节且循环冗余校验（Cyclic Redundancy Check，CRC）正确。

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[setup_valid](P033_USB设备控制器驱动数据.md#a2222bd71ecbb8051dfab7b6134f9a2c9)。

## 33.3\_详细说明（Detailed Documentation）

<a id="aae68bfba2e92894851c36dd40c33c0f0"></a>

### `caps`

```c
struct udc_device_caps udc_data::caps
```

控制器能力。

<a id="acc471b34bb24453377b1ae54d33fa415"></a>

### `ep_lut`

```c
struct udc_ep_config* udc_data::ep_lut[32]
```

用于端点管理的查找表（Lookup Table，LUT）。

> 译注（源码核对）：当前头文件的表长为32，为端点号与方向组合提供查找空间；表长不意味着具体控制器实现32个可用硬件端点，应结合各槽位配置及控制器能力判断。

<a id="a9bb216d0c87b9ff4e2e99f0c3cfbb381"></a>

### `event_cb`

```c
udc_event_cb_t udc_data::event_cb
```

向上层提交 UDC 事件的回调。

<a id="aaf98e53580a27635a7b02acbcf29ae14"></a>

### `event_ctx`

```c
const void* udc_data::event_ctx
```

用于保存上层上下文的不透明指针。

<a id="a1ba1b93af26bca4f4554a43a65ab3c2a"></a>

### `mutex`

```c
struct k_mutex udc_data::mutex
```

驱动访问互斥量（Mutex）。

<a id="ac58682fa2f37bf2034a69cc9b6b10dfb"></a>

### `priv`

```c
void* udc_data::priv
```

驱动私有数据。

<a id="ae301e1a80165ae90d7d09dbb6463c88c"></a>

### `setup`

```c
uint8_t udc_data::setup[8]
```

最近缓存的设置数据，不一定是最近接收的设置数据。

<a id="a849581d1e3692c6c585e9fb24e9bbb4f"></a>

### `setup_pending`

```c
bool udc_data::setup_pending
```

缓存的设置数据正在等待 USB 栈处理。

<a id="a2222bd71ecbb8051dfab7b6134f9a2c9"></a>

### `setup_valid`

```c
bool udc_data::setup_valid
```

最近缓存的设置数据有效，即长度为 8 字节且循环冗余校验（Cyclic Redundancy Check，CRC）正确。

<a id="a9c1ae6e5e204b5a0ed15e92f8b3b384f"></a>

### `status`

```c
atomic_t udc_data::status
```

USB 设备控制器状态。

## 33.4\_相关源码与使用边界

控制器接口与结构定义来自 `zephyr/drivers/usb/udc.h`，缓冲区宏来自 `zephyr/drivers/usb/usb_buf.h`。本仓库的[对应头文件](../../../include/zephyr/drivers/usb/udc.h)、[公共实现](../../../drivers/usb/udc/udc_common.c)、[内部辅助接口](../../../drivers/usb/udc/udc_common.h)和[驱动骨架](../../../drivers/usb/udc/udc_skeleton.c)可用于源码跟踪；版本可能与官方 latest 不同。译注依据保存的[官方头文件](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/include/zephyr/drivers/usb/udc.h)、[公共实现](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/drivers/usb/udc/udc_common.c)、[内部接口](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/drivers/usb/udc/udc_common.h)及[骨架实现](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/drivers/usb/udc/udc_skeleton.c)，摘要见[来源记录](../SOURCES.md)。本批没有编译、运行或操作USB设备。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>
<a id="details"></a>
<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

[上一章](P032_USB设备控制器缓冲区信息.md) · [返回大纲](大纲.md) · [下一章](P034_USB设备控制器设备能力.md)
