---
id: learning.zephyr-docs.usb.api-36
title: USB设备控制器端点配置
kind: reference
status: maintained
domains: [zephyr, usb, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structudc__ep__config.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第36章\_USB设备控制器端点配置

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structudc__ep__config.html)。读取日期：2026-10-14；基线为保存的 `latest` 页面，HTML 摘要见[来源记录](../SOURCES.md)。

## 36.1\_阅读说明与来源

译注：本页属于[USB设备控制器API说明](P029_USB设备控制器API说明.md)的底层接口参考，供理解控制器驱动、端点管理和请求生命周期。声明和原注释按官方页面保留，补充解释明确标为源码译注。

[本册大纲](大纲.md)提供本组第29至39章的全部字段参考。

USB 设备控制器端点配置。

```c
#include <zephyr/drivers/usb/udc.h>
```

USB 设备控制器端点配置。

配置和管理端点必须使用此结构。它不向上层公开，仅由 UDC API 内部和驱动使用。

## 36.2\_数据成员（Data Fields）

<a id="r_aa62ff3f308771d51563df88439570918"></a>

```c
struct k_fifo fifo
```

端点请求的先进先出队列（First In, First Out，FIFO）。

相关声明：[k_fifo](../queue_reference/P004_内核FIFO结构.md)、[fifo](P036_USB设备控制器端点配置.md#aa62ff3f308771d51563df88439570918)。

<a id="r_a706987205ac971574d1b81bf72d03248"></a>

```c
struct udc_ep_caps caps
```

端点能力。

相关声明：[udc_ep_caps](P035_USB设备控制器端点能力.md)、[caps](P036_USB设备控制器端点配置.md#a706987205ac971574d1b81bf72d03248)。

<a id="r_ad42f77d1a9d65239cdb142209050e38e"></a>

```c
struct udc_ep_stat stat
```

端点状态。

相关声明：[udc_ep_stat](P037_USB设备控制器端点状态.md)、[stat](P036_USB设备控制器端点配置.md#ad42f77d1a9d65239cdb142209050e38e)。

<a id="r_ac795b839cbd426d233a1f91d10d5fc7e"></a>

```c
uint8_t addr
```

端点地址。

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[addr](P036_USB设备控制器端点配置.md#ac795b839cbd426d233a1f91d10d5fc7e)。

<a id="r_acbeab755d1b03da0c58f43aff5bd7d00"></a>

```c
uint8_t attributes
```

端点属性。

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[attributes](P036_USB设备控制器端点配置.md#acbeab755d1b03da0c58f43aff5bd7d00)。

<a id="r_ae4f75e52d1c822f5d873095a761c6b48"></a>

```c
uint16_t mps
```

最大包长。

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[mps](P036_USB设备控制器端点配置.md#ae4f75e52d1c822f5d873095a761c6b48)。

<a id="r_a1f2afc2d5e512229688764e1b7cd0171"></a>

```c
uint8_t interval
```

轮询间隔。

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[interval](P036_USB设备控制器端点配置.md#a1f2afc2d5e512229688764e1b7cd0171)。

## 36.3\_详细说明（Detailed Documentation）

<a id="ac795b839cbd426d233a1f91d10d5fc7e"></a>

### `addr`

```c
uint8_t udc_ep_config::addr
```

端点地址。

<a id="acbeab755d1b03da0c58f43aff5bd7d00"></a>

### `attributes`

```c
uint8_t udc_ep_config::attributes
```

端点属性。

<a id="a706987205ac971574d1b81bf72d03248"></a>

### `caps`

```c
struct udc_ep_caps udc_ep_config::caps
```

端点能力。

<a id="aa62ff3f308771d51563df88439570918"></a>

### `fifo`

```c
struct k_fifo udc_ep_config::fifo
```

端点请求的先进先出队列（First In, First Out，FIFO）。

<a id="a1f2afc2d5e512229688764e1b7cd0171"></a>

### `interval`

```c
uint8_t udc_ep_config::interval
```

轮询间隔。

<a id="ae4f75e52d1c822f5d873095a761c6b48"></a>

### `mps`

```c
uint16_t udc_ep_config::mps
```

最大包长。

<a id="ad42f77d1a9d65239cdb142209050e38e"></a>

### `stat`

```c
struct udc_ep_stat udc_ep_config::stat
```

端点状态。

## 36.4\_相关源码与使用边界

控制器接口与结构定义来自 `zephyr/drivers/usb/udc.h`，缓冲区宏来自 `zephyr/drivers/usb/usb_buf.h`。本仓库的[对应头文件](../../../include/zephyr/drivers/usb/udc.h)、[公共实现](../../../drivers/usb/udc/udc_common.c)、[内部辅助接口](../../../drivers/usb/udc/udc_common.h)和[驱动骨架](../../../drivers/usb/udc/udc_skeleton.c)可用于源码跟踪；版本可能与官方 latest 不同。译注依据保存的[官方头文件](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/include/zephyr/drivers/usb/udc.h)、[公共实现](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/drivers/usb/udc/udc_common.c)、[内部接口](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/drivers/usb/udc/udc_common.h)及[骨架实现](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/drivers/usb/udc/udc_skeleton.c)，摘要见[来源记录](../SOURCES.md)。本批没有编译、运行或操作USB设备。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>
<a id="details"></a>
<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

[上一章](P035_USB设备控制器端点能力.md) · [返回大纲](大纲.md) · [下一章](P037_USB设备控制器端点状态.md)
